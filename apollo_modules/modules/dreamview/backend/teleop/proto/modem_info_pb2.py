"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7modules/dreamview/backend/teleop/proto/modem_info.proto\x12\x14modules.teleop.modem\x1a!modules/common/proto/header.proto"\xde\x02\n\tModemInfo\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08provider\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x10\n\x08ip_count\x18\x04 \x01(\x05\x12\x0f\n\x07gateway\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\t\x12\x0b\n\x03dev\x18\x07 \x01(\t\x12\n\n\x02tx\x18\x08 \x01(\x04\x12\n\n\x02rx\x18\t \x01(\x04\x12\x0c\n\x04ping\x18\n \x01(\t\x12\r\n\x05smoni\x18\x0b \x01(\t\x12\x12\n\ntechnology\x18\x0c \x01(\t\x12\x12\n\nconnection\x18\r \x01(\t\x12\x0e\n\x06signal\x18\x0e \x01(\x05\x12\x0f\n\x07quality\x18\x0f \x01(\x05\x12\x14\n\x0cbandwidth_ul\x18\x10 \x01(\x05\x12\x14\n\x0cbandwidth_dl\x18\x11 \x01(\x05\x12\x16\n\x0eca_aggregation\x18\x12 \x01(\x08\x12\x0c\n\x04rank\x18\x13 \x01(\x05')
_MODEMINFO = DESCRIPTOR.message_types_by_name['ModemInfo']
ModemInfo = _reflection.GeneratedProtocolMessageType('ModemInfo', (_message.Message,), {'DESCRIPTOR': _MODEMINFO, '__module__': 'modules.dreamview.backend.teleop.proto.modem_info_pb2'})
_sym_db.RegisterMessage(ModemInfo)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MODEMINFO._serialized_start = 117
    _MODEMINFO._serialized_end = 467