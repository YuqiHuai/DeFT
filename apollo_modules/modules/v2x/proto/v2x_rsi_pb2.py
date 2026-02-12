"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmodules/v2x/proto/v2x_rsi.proto\x12\napollo.v2x\x1a!modules/common/proto/header.proto" \n\x08RsiPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01"\xd4\x01\n\x06RsiMsg\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12$\n\x06points\x18\x02 \x03(\x0b2\x14.apollo.v2x.RsiPoint\x12\r\n\x05speed\x18\x03 \x01(\x01\x12\x11\n\tlow_speed\x18\x04 \x01(\x01\x12\x12\n\nhigh_speed\x18\x05 \x01(\x01\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x10\n\x08rsi_type\x18\x07 \x01(\x05\x12\x0e\n\x06radius\x18\x08 \x01(\x01\x12\x10\n\x08priority\x18\t \x01(\x05')
_RSIPOINT = DESCRIPTOR.message_types_by_name['RsiPoint']
_RSIMSG = DESCRIPTOR.message_types_by_name['RsiMsg']
RsiPoint = _reflection.GeneratedProtocolMessageType('RsiPoint', (_message.Message,), {'DESCRIPTOR': _RSIPOINT, '__module__': 'modules.v2x.proto.v2x_rsi_pb2'})
_sym_db.RegisterMessage(RsiPoint)
RsiMsg = _reflection.GeneratedProtocolMessageType('RsiMsg', (_message.Message,), {'DESCRIPTOR': _RSIMSG, '__module__': 'modules.v2x.proto.v2x_rsi_pb2'})
_sym_db.RegisterMessage(RsiMsg)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _RSIPOINT._serialized_start = 82
    _RSIPOINT._serialized_end = 114
    _RSIMSG._serialized_start = 117
    _RSIMSG._serialized_end = 329