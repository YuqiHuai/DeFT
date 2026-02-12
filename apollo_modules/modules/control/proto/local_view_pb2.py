"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.control.proto import pad_msg_pb2 as modules_dot_control_dot_proto_dot_pad__msg__pb2
from ....modules.localization.proto import localization_pb2 as modules_dot_localization_dot_proto_dot_localization__pb2
from ....modules.planning.proto import planning_pb2 as modules_dot_planning_dot_proto_dot_planning__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/control/proto/local_view.proto\x12\x0eapollo.control\x1a"modules/canbus/proto/chassis.proto\x1a!modules/common/proto/header.proto\x1a#modules/control/proto/pad_msg.proto\x1a-modules/localization/proto/localization.proto\x1a%modules/planning/proto/planning.proto"\xfd\x01\n\tLocalView\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\'\n\x07chassis\x18\x02 \x01(\x0b2\x16.apollo.canbus.Chassis\x122\n\ntrajectory\x18\x03 \x01(\x0b2\x1e.apollo.planning.ADCTrajectory\x12?\n\x0clocalization\x18\x04 \x01(\x0b2).apollo.localization.LocalizationEstimate\x12+\n\x07pad_msg\x18\x05 \x01(\x0b2\x1a.apollo.control.PadMessage')
_LOCALVIEW = DESCRIPTOR.message_types_by_name['LocalView']
LocalView = _reflection.GeneratedProtocolMessageType('LocalView', (_message.Message,), {'DESCRIPTOR': _LOCALVIEW, '__module__': 'modules.control.proto.local_view_pb2'})
_sym_db.RegisterMessage(LocalView)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LOCALVIEW._serialized_start = 253
    _LOCALVIEW._serialized_end = 506