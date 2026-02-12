"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/control/proto/pad_msg.proto\x12\x0eapollo.control\x1a!modules/common/proto/header.proto\x1a"modules/canbus/proto/chassis.proto"\x9c\x01\n\nPadMessage\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x128\n\x0cdriving_mode\x18\x02 \x01(\x0e2".apollo.canbus.Chassis.DrivingMode\x12-\n\x06action\x18\x03 \x01(\x0e2\x1d.apollo.control.DrivingAction*/\n\rDrivingAction\x12\x08\n\x04STOP\x10\x00\x12\t\n\x05START\x10\x01\x12\t\n\x05RESET\x10\x02')
_DRIVINGACTION = DESCRIPTOR.enum_types_by_name['DrivingAction']
DrivingAction = enum_type_wrapper.EnumTypeWrapper(_DRIVINGACTION)
STOP = 0
START = 1
RESET = 2
_PADMESSAGE = DESCRIPTOR.message_types_by_name['PadMessage']
PadMessage = _reflection.GeneratedProtocolMessageType('PadMessage', (_message.Message,), {'DESCRIPTOR': _PADMESSAGE, '__module__': 'modules.control.proto.pad_msg_pb2'})
_sym_db.RegisterMessage(PadMessage)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DRIVINGACTION._serialized_start = 285
    _DRIVINGACTION._serialized_end = 332
    _PADMESSAGE._serialized_start = 127
    _PADMESSAGE._serialized_end = 283