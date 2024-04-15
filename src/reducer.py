import time
import grpc
from concurrent import futures
from reducer_pb2_grpc import add_ReducerServicer_to_server
from reducer_pb2 import ReduceData

class ReducerServicer:
    def __init__(self):
        self.data = {}

    def ReceiveData(self, request, context):
        if request.key not in self.data:
            self.data[request.key] = []
        self.data[request.key].append(request.value)
        return Empty()  # Assuming an Empty response type is defined in your proto

    def process_data(self):
        # Sort and process the data
        for key in sorted(self.data.keys()):
            aggregated_value = self.aggregate(self.data[key])
            print(f"Processed key {key} with value {aggregated_value}")

    def Shuffle_and_Sort(self, request, context):

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ReducerServicer_to_server(ReducerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

def main():
    serve()

if __name__ == "__main__":
    main()