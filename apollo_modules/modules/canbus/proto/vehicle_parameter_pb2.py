"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from ....modules.common.configs.proto import vehicle_config_pb2 as modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/canbus/proto/vehicle_parameter.proto\x12\rapollo.canbus\x1a"modules/canbus/proto/chassis.proto\x1a1modules/common/configs/proto/vehicle_config.proto"\xb3\x01\n\x10VehicleParameter\x12*\n\x05brand\x18\x01 \x01(\x0e2\x1b.apollo.common.VehicleBrand\x12\x18\n\x10max_engine_pedal\x18\x02 \x01(\x01\x12\x1f\n\x17max_enable_fail_attempt\x18\x03 \x01(\x05\x128\n\x0cdriving_mode\x18\x04 \x01(\x0e2".apollo.canbus.Chassis.DrivingMode')
_VEHICLEPARAMETER = DESCRIPTOR.message_types_by_name['VehicleParameter']
VehicleParameter = _reflection.GeneratedProtocolMessageType('VehicleParameter', (_message.Message,), {'DESCRIPTOR': _VEHICLEPARAMETER, '__module__': 'modules.canbus.proto.vehicle_parameter_pb2'})
_sym_db.RegisterMessage(VehicleParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VEHICLEPARAMETER._serialized_start = 151
    _VEHICLEPARAMETER._serialized_end = 330