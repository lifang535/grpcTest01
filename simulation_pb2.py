# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simulation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10simulation.proto\x12\nsimulation\")\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\nstart_time\x18\x02 \x01(\x03\")\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tend_times\x18\x02 \x03(\x03\x32\x46\n\x08\x46rontend\x12:\n\x0bSendRequest\x12\x13.simulation.Request\x1a\x14.simulation.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simulation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=32
  _REQUEST._serialized_end=73
  _RESPONSE._serialized_start=75
  _RESPONSE._serialized_end=116
  _FRONTEND._serialized_start=118
  _FRONTEND._serialized_end=188
# @@protoc_insertion_point(module_scope)