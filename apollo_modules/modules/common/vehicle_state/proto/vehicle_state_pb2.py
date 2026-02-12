"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from .....modules.localization.proto import pose_pb2 as modules_dot_localization_dot_proto_dot_pose__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/common/vehicle_state/proto/vehicle_state.proto\x12\rapollo.common\x1a"modules/canbus/proto/chassis.proto\x1a%modules/localization/proto/pose.proto"\xb3\x03\n\x0cVehicleState\x12\x0c\n\x01x\x18\x01 \x01(\x01:\x010\x12\x0c\n\x01y\x18\x02 \x01(\x01:\x010\x12\x0c\n\x01z\x18\x03 \x01(\x01:\x010\x12\x14\n\ttimestamp\x18\x04 \x01(\x01:\x010\x12\x0f\n\x04roll\x18\x05 \x01(\x01:\x010\x12\x10\n\x05pitch\x18\x06 \x01(\x01:\x010\x12\x0e\n\x03yaw\x18\x07 \x01(\x01:\x010\x12\x12\n\x07heading\x18\x08 \x01(\x01:\x010\x12\x10\n\x05kappa\x18\t \x01(\x01:\x010\x12\x1a\n\x0flinear_velocity\x18\n \x01(\x01:\x010\x12\x1b\n\x10angular_velocity\x18\x0b \x01(\x01:\x010\x12\x1e\n\x13linear_acceleration\x18\x0c \x01(\x01:\x010\x121\n\x04gear\x18\r \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x128\n\x0cdriving_mode\x18\x0e \x01(\x0e2".apollo.canbus.Chassis.DrivingMode\x12\'\n\x04pose\x18\x0f \x01(\x0b2\x19.apollo.localization.Pose\x12\x1b\n\x13steering_percentage\x18\x10 \x01(\x01')
_VEHICLESTATE = DESCRIPTOR.message_types_by_name['VehicleState']
VehicleState = _reflection.GeneratedProtocolMessageType('VehicleState', (_message.Message,), {'DESCRIPTOR': _VEHICLESTATE, '__module__': 'modules.common.vehicle_state.proto.vehicle_state_pb2'})
_sym_db.RegisterMessage(VehicleState)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VEHICLESTATE._serialized_start = 149
    _VEHICLESTATE._serialized_end = 584