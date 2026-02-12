"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/v2x/proto/v2x_obu_rsi.proto\x12\x0eapollo.v2x.obu\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\xec\x01\n\x06ObuRsi\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x0e\n\x06rsu_id\x18\x02 \x01(\x0c\x12\x0e\n\x06rsi_id\x18\x03 \x01(\x05\x12\x12\n\nalter_type\x18\x04 \x01(\x05\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12)\n\tref_point\x18\x06 \x01(\x0b2\x16.apollo.common.Point2D\x12&\n\x06points\x18\x07 \x03(\x0b2\x16.apollo.common.Point2D\x12\x0e\n\x06radius\x18\x08 \x01(\x05\x12\x0f\n\x07msg_cnt\x18\t \x01(\x05')
_OBURSI = DESCRIPTOR.message_types_by_name['ObuRsi']
ObuRsi = _reflection.GeneratedProtocolMessageType('ObuRsi', (_message.Message,), {'DESCRIPTOR': _OBURSI, '__module__': 'modules.v2x.proto.v2x_obu_rsi_pb2'})
_sym_db.RegisterMessage(ObuRsi)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OBURSI._serialized_start = 128
    _OBURSI._serialized_end = 364