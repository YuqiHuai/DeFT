"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/planning/proto/pad_msg.proto\x12\x0fapollo.planning\x1a!modules/common/proto/header.proto"c\n\nPadMessage\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12.\n\x06action\x18\x02 \x01(\x0e2\x1e.apollo.planning.DrivingAction*t\n\rDrivingAction\x12\x08\n\x04NONE\x10d\x12\n\n\x06FOLLOW\x10\x00\x12\x0f\n\x0bCHANGE_LEFT\x10\x01\x12\x10\n\x0cCHANGE_RIGHT\x10\x02\x12\r\n\tPULL_OVER\x10\x03\x12\x08\n\x04STOP\x10\x04\x12\x11\n\rRESUME_CRUISE\x10\x05')
_DRIVINGACTION = DESCRIPTOR.enum_types_by_name['DrivingAction']
DrivingAction = enum_type_wrapper.EnumTypeWrapper(_DRIVINGACTION)
NONE = 100
FOLLOW = 0
CHANGE_LEFT = 1
CHANGE_RIGHT = 2
PULL_OVER = 3
STOP = 4
RESUME_CRUISE = 5
_PADMESSAGE = DESCRIPTOR.message_types_by_name['PadMessage']
PadMessage = _reflection.GeneratedProtocolMessageType('PadMessage', (_message.Message,), {'DESCRIPTOR': _PADMESSAGE, '__module__': 'modules.planning.proto.pad_msg_pb2'})
_sym_db.RegisterMessage(PadMessage)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DRIVINGACTION._serialized_start = 193
    _DRIVINGACTION._serialized_end = 309
    _PADMESSAGE._serialized_start = 92
    _PADMESSAGE._serialized_end = 191