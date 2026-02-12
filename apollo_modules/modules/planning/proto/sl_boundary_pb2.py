"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/planning/proto/sl_boundary.proto\x12\x0fapollo.planning\x1a$modules/common/proto/pnc_point.proto"|\n\nSLBoundary\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05end_s\x18\x02 \x01(\x01\x12\x0f\n\x07start_l\x18\x03 \x01(\x01\x12\r\n\x05end_l\x18\x04 \x01(\x01\x12.\n\x0eboundary_point\x18\x05 \x03(\x0b2\x16.apollo.common.SLPoint')
_SLBOUNDARY = DESCRIPTOR.message_types_by_name['SLBoundary']
SLBoundary = _reflection.GeneratedProtocolMessageType('SLBoundary', (_message.Message,), {'DESCRIPTOR': _SLBOUNDARY, '__module__': 'modules.planning.proto.sl_boundary_pb2'})
_sym_db.RegisterMessage(SLBoundary)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SLBOUNDARY._serialized_start = 99
    _SLBOUNDARY._serialized_end = 223