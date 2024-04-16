# import cmd
import subprocess
import argparse
import os
import grpc
from mapper_pb2 import ShardData, Centroid
from mapper_pb2_grpc import MapperStub
from reducer_pb2_grpc import ReducerStub
from google.protobuf.empty_pb2 import Empty
import sys
import signal
import random

def create_shards(num_mappers):
    # read input file(s)
    num_input_files = len(os.listdir("data/input/"))
    
    shard_map = {}
    
    if num_input_files == 0:
        print("No input files found")
        return
    
    if num_input_files == 1:
        input_file = os.listdir("data/input/")[0]
        num_lines = sum(1 for line in open(f"data/input/{input_file}"))
        for i in range(num_mappers):
            start = i * num_lines // num_mappers
            end = (i + 1) * num_lines // num_mappers
            if i == num_mappers - 1:
                end = num_lines
            shard_map[i] = (input_file, start, end)
            
    else:
        # in case of multiple files, you cannot use the indices approach. You will have to distribute one file per mapper.
        input_files = os.listdir("data/input/")
        for i in range(num_mappers):
            num_lines = len(open(os.path.join("data", "input", input_files[i])).read().splitlines())
            shard_map[i] = (input_files[i], 0, num_lines)

    return shard_map

def start_map_phase(shard_map, centroids, num_reducers):
    #can distribute work in parallel
    for mapper_id, (shard_file, start, end) in shard_map.items():
        print(f"Master send to mapper {mapper_id}")
        with grpc.insecure_channel(f'localhost:{6000 + mapper_id}') as channel:
            stub = MapperStub(channel)
            response = stub.MapData(ShardData(mapper_id = mapper_id, shard_file=shard_file, start=start, end=end, centroids = centroids, R = num_reducers))
            print(f"Mapper {mapper_id} response: {response.result}")

def start_reduce_phase(num_reducers):
    print("Starting reduce phase.")
    for i in range(num_reducers):
        with grpc.insecure_channel(f'localhost:{7000 + i}') as channel:
            stub = ReducerStub(channel)
            response = stub.StartReduce(Empty())  # assuming an Empty message signals reducer to start processing
            print(f"Reducer {i} started reduce phase: {response.result}")


def main(num_mappers, num_reducers, num_centroids):
    p = []
    centroids = []
    for i in range(num_centroids):
        centroids.append(Centroid(centroid_id = i+1, x = random.random()*10, y = random.random()*10))
    print("centroids_main", centroids)
    for i in range(num_mappers):
        # s = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True)
        # s = subprocess.Popen(["python3", "mapper.py", f"localhost:{6000 + i}"], stdout=subprocess.PIPE, shell=True)
        s = subprocess.Popen(["python3", "mapper.py", f"localhost:{6000 + i}"])
        p.append(s)
        print(f"Mapper {i} started with PID {s.pid}")
    for i in range(num_reducers):
        # s = subprocess.Popen(["python3", "reducer.py", f"localhost:{7000 + i}"], stdout=subprocess.PIPE, shell=True)
        s = subprocess.Popen(["python3", "reducer.py", f"localhost:{7000 + i}"])
        p.append(s)
        print(f"Reducer {i} started with PID {s.pid}")

    shutdown = False    
        
    while not shutdown:
        shard_map = create_shards(num_mappers)
        print(shard_map)
        start_map_phase(shard_map, centroids, num_reducers)
        start_reduce_phase(num_reducers)

        while True:
            try:
                pass
            except KeyboardInterrupt:
                for process in p:
                    print("terminating")
                    process.kill()
                sys.exit(0)
        
        shutdown = True

if __name__ == "__main__":
    main(num_mappers = 4, num_reducers = 6, num_centroids = 3)