# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reducer.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rreducer.proto\x12\x07reducer\x1a\x1bgoogle/protobuf/empty.proto\"(\n\nReduceData\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"!\n\x0fReducerResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\x8b\x01\n\x07Reducer\x12?\n\x0bStartReduce\x12\x16.google.protobuf.Empty\x1a\x18.reducer.ReducerResponse\x12?\n\x0eSendReduceData\x12\x13.reducer.ReduceData\x1a\x18.reducer.ReducerResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reducer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REDUCEDATA']._serialized_start=55
  _globals['_REDUCEDATA']._serialized_end=95
  _globals['_REDUCERRESPONSE']._serialized_start=97
  _globals['_REDUCERRESPONSE']._serialized_end=130
  _globals['_REDUCER']._serialized_start=133
  _globals['_REDUCER']._serialized_end=272
# @@protoc_insertion_point(module_scope)