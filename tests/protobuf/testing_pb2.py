# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/protobuf/testing.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tests/protobuf/testing.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1ctests/protobuf/testing.proto\"\x1e\n\rSavoysRequest\x12\r\n\x05kyler\x18\x01 \x01(\t\"\x1d\n\x0bSavoysReply\x12\x0e\n\x06\x62\x65nito\x18\x01 \x01(\t2:\n\rBombedService\x12)\n\x07Plaster\x12\x0e.SavoysRequest\x1a\x0c.SavoysReply\"\x00\x62\x06proto3')
)




_SAVOYSREQUEST = _descriptor.Descriptor(
  name='SavoysRequest',
  full_name='SavoysRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kyler', full_name='SavoysRequest.kyler', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=62,
)


_SAVOYSREPLY = _descriptor.Descriptor(
  name='SavoysReply',
  full_name='SavoysReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='benito', full_name='SavoysReply.benito', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['SavoysRequest'] = _SAVOYSREQUEST
DESCRIPTOR.message_types_by_name['SavoysReply'] = _SAVOYSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SavoysRequest = _reflection.GeneratedProtocolMessageType('SavoysRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVOYSREQUEST,
  __module__ = 'tests.protobuf.testing_pb2'
  # @@protoc_insertion_point(class_scope:SavoysRequest)
  ))
_sym_db.RegisterMessage(SavoysRequest)

SavoysReply = _reflection.GeneratedProtocolMessageType('SavoysReply', (_message.Message,), dict(
  DESCRIPTOR = _SAVOYSREPLY,
  __module__ = 'tests.protobuf.testing_pb2'
  # @@protoc_insertion_point(class_scope:SavoysReply)
  ))
_sym_db.RegisterMessage(SavoysReply)


# @@protoc_insertion_point(module_scope)
