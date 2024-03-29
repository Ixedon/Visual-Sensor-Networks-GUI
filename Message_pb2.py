# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto

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
  name='Message.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rMessage.proto\"w\n\tImageInfo\x12\x10\n\x08\x63\x61meraID\x18\x01 \x01(\x05\x12\r\n\x05image\x18\x02 \x01(\x0c\x12\x0b\n\x03\x62\x62X\x18\x03 \x01(\x05\x12\x0b\n\x03\x62\x62Y\x18\x04 \x01(\x05\x12\x0f\n\x07\x62\x62Width\x18\x05 \x01(\x05\x12\x10\n\x08\x62\x62Height\x18\x06 \x01(\x05\x12\x0c\n\x04\x63onf\x18\x07 \x01(\x01\"6\n\x11\x41\x64\x64itionalControl\x12\x10\n\x08\x63\x61meraID\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\"A\n\nPrediction\x12\x10\n\x08\x63\x61meraID\x18\x01 \x01(\x05\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x12\r\n\x05shape\x18\x03 \x01(\tb\x06proto3')
)




_IMAGEINFO = _descriptor.Descriptor(
  name='ImageInfo',
  full_name='ImageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cameraID', full_name='ImageInfo.cameraID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='ImageInfo.image', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbX', full_name='ImageInfo.bbX', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbY', full_name='ImageInfo.bbY', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbWidth', full_name='ImageInfo.bbWidth', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbHeight', full_name='ImageInfo.bbHeight', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='ImageInfo.conf', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=17,
  serialized_end=136,
)


_ADDITIONALCONTROL = _descriptor.Descriptor(
  name='AdditionalControl',
  full_name='AdditionalControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cameraID', full_name='AdditionalControl.cameraID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='AdditionalControl.command', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=138,
  serialized_end=192,
)


_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cameraID', full_name='Prediction.cameraID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Prediction.confidence', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='Prediction.shape', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=194,
  serialized_end=259,
)

DESCRIPTOR.message_types_by_name['ImageInfo'] = _IMAGEINFO
DESCRIPTOR.message_types_by_name['AdditionalControl'] = _ADDITIONALCONTROL
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageInfo = _reflection.GeneratedProtocolMessageType('ImageInfo', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEINFO,
  __module__ = 'Message_pb2'
  # @@protoc_insertion_point(class_scope:ImageInfo)
  ))
_sym_db.RegisterMessage(ImageInfo)

AdditionalControl = _reflection.GeneratedProtocolMessageType('AdditionalControl', (_message.Message,), dict(
  DESCRIPTOR = _ADDITIONALCONTROL,
  __module__ = 'Message_pb2'
  # @@protoc_insertion_point(class_scope:AdditionalControl)
  ))
_sym_db.RegisterMessage(AdditionalControl)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTION,
  __module__ = 'Message_pb2'
  # @@protoc_insertion_point(class_scope:Prediction)
  ))
_sym_db.RegisterMessage(Prediction)


# @@protoc_insertion_point(module_scope)
