# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comment.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcomment.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8a\x01\n\x07\x43omment\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x1c\n\x05state\x18\x04 \x01(\x0e\x32\r.CommentState\x12\x34\n\x10publication_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*6\n\x0c\x43ommentState\x12\x12\n\x0e\x43OMMENT_NORMAL\x10\x00\x12\x12\n\x0e\x43OMMENT_HIDDEN\x10\x01\x32\x11\n\x0f\x43ommentServicerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'comment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COMMENTSTATE']._serialized_start=191
  _globals['_COMMENTSTATE']._serialized_end=245
  _globals['_COMMENT']._serialized_start=51
  _globals['_COMMENT']._serialized_end=189
  _globals['_COMMENTSERVICER']._serialized_start=247
  _globals['_COMMENTSERVICER']._serialized_end=264
# @@protoc_insertion_point(module_scope)
