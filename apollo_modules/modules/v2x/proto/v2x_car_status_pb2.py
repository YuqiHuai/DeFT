"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.localization.proto import localization_pb2 as modules_dot_localization_dot_proto_dot_localization__pb2
from ....modules.canbus.proto import chassis_detail_pb2 as modules_dot_canbus_dot_proto_dot_chassis__detail__pb2
from ....modules.v2x.proto import v2x_junction_pb2 as modules_dot_v2x_dot_proto_dot_v2x__junction__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/v2x/proto/v2x_car_status.proto\x12\napollo.v2x\x1a-modules/localization/proto/localization.proto\x1a)modules/canbus/proto/chassis_detail.proto\x1a$modules/v2x/proto/v2x_junction.proto"\xca\x01\n\tCarStatus\x12?\n\x0clocalization\x18\x01 \x01(\x0b2).apollo.localization.LocalizationEstimate\x124\n\x0echassis_detail\x18\x02 \x01(\x0b2\x1c.apollo.canbus.ChassisDetail\x12&\n\x08junction\x18\x03 \x01(\x0b2\x14.apollo.v2x.Junction\x12\x1e\n\x06rsu_id\x18\x04 \x01(\x0b2\x0e.apollo.v2x.Id')
_CARSTATUS = DESCRIPTOR.message_types_by_name['CarStatus']
CarStatus = _reflection.GeneratedProtocolMessageType('CarStatus', (_message.Message,), {'DESCRIPTOR': _CARSTATUS, '__module__': 'modules.v2x.proto.v2x_car_status_pb2'})
_sym_db.RegisterMessage(CarStatus)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CARSTATUS._serialized_start = 183
    _CARSTATUS._serialized_end = 385