"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/common/configs/proto/vehicle_config.proto\x12\rapollo.common\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\x91\x01\n\tTransform\x12\x14\n\x0csource_frame\x18\x01 \x01(\x0c\x12\x14\n\x0ctarget_frame\x18\x02 \x01(\x0c\x12+\n\x0btranslation\x18\x03 \x01(\x0b2\x16.apollo.common.Point3D\x12+\n\x08rotation\x18\x04 \x01(\x0b2\x19.apollo.common.Quaternion"9\n\nExtrinsics\x12+\n\ttansforms\x18\x01 \x03(\x0b2\x18.apollo.common.Transform"@\n\tVehicleID\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\r\n\x05plate\x18\x02 \x01(\t\x12\x17\n\x0fother_unique_id\x18\x03 \x01(\t"^\n\x0cLatencyParam\x12\x11\n\tdead_time\x18\x01 \x01(\x01\x12\x11\n\trise_time\x18\x02 \x01(\x01\x12\x11\n\tpeak_time\x18\x03 \x01(\x01\x12\x15\n\rsettling_time\x18\x04 \x01(\x01"\xe0\x06\n\x0cVehicleParam\x12*\n\x05brand\x18\x01 \x01(\x0e2\x1b.apollo.common.VehicleBrand\x12,\n\nvehicle_id\x18\x02 \x01(\x0b2\x18.apollo.common.VehicleID\x12!\n\x14front_edge_to_center\x18\x03 \x01(\x01:\x03nan\x12 \n\x13back_edge_to_center\x18\x04 \x01(\x01:\x03nan\x12 \n\x13left_edge_to_center\x18\x05 \x01(\x01:\x03nan\x12!\n\x14right_edge_to_center\x18\x06 \x01(\x01:\x03nan\x12\x13\n\x06length\x18\x07 \x01(\x01:\x03nan\x12\x12\n\x05width\x18\x08 \x01(\x01:\x03nan\x12\x13\n\x06height\x18\t \x01(\x01:\x03nan\x12\x1c\n\x0fmin_turn_radius\x18\n \x01(\x01:\x03nan\x12\x1d\n\x10max_acceleration\x18\x0b \x01(\x01:\x03nan\x12\x1d\n\x10max_deceleration\x18\x0c \x01(\x01:\x03nan\x12\x1c\n\x0fmax_steer_angle\x18\r \x01(\x01:\x03nan\x12!\n\x14max_steer_angle_rate\x18\x0e \x01(\x01:\x03nan\x12!\n\x14min_steer_angle_rate\x18\x0f \x01(\x01:\x03nan\x12\x18\n\x0bsteer_ratio\x18\x10 \x01(\x01:\x03nan\x12\x17\n\nwheel_base\x18\x11 \x01(\x01:\x03nan\x12!\n\x14wheel_rolling_radius\x18\x12 \x01(\x01:\x03nan\x12\'\n\x1amax_abs_speed_when_stopped\x18\x13 \x01(\x02:\x03nan\x12\x1b\n\x0ebrake_deadzone\x18\x14 \x01(\x01:\x03nan\x12\x1e\n\x11throttle_deadzone\x18\x15 \x01(\x01:\x03nan\x12;\n\x16steering_latency_param\x18\x16 \x01(\x0b2\x1b.apollo.common.LatencyParam\x12;\n\x16throttle_latency_param\x18\x17 \x01(\x0b2\x1b.apollo.common.LatencyParam\x128\n\x13brake_latency_param\x18\x18 \x01(\x0b2\x1b.apollo.common.LatencyParam"\x99\x01\n\rVehicleConfig\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x122\n\rvehicle_param\x18\x02 \x01(\x0b2\x1b.apollo.common.VehicleParam\x12-\n\nextrinsics\x18\x03 \x01(\x0b2\x19.apollo.common.Extrinsics*~\n\x0cVehicleBrand\x12\x0f\n\x0bLINCOLN_MKZ\x10\x00\x12\x07\n\x03GEM\x10\x01\x12\t\n\x05LEXUS\x10\x02\x12\x0b\n\x07TRANSIT\x10\x03\x12\x07\n\x03GE3\x10\x04\x12\x07\n\x03WEY\x10\x05\x12\x0c\n\x08ZHONGYUN\x10\x06\x12\x06\n\x02CH\x10\x07\x12\x08\n\x04DKIT\x10\x08\x12\n\n\x06NEOLIX\x10\t')
_VEHICLEBRAND = DESCRIPTOR.enum_types_by_name['VehicleBrand']
VehicleBrand = enum_type_wrapper.EnumTypeWrapper(_VEHICLEBRAND)
LINCOLN_MKZ = 0
GEM = 1
LEXUS = 2
TRANSIT = 3
GE3 = 4
WEY = 5
ZHONGYUN = 6
CH = 7
DKIT = 8
NEOLIX = 9
_TRANSFORM = DESCRIPTOR.message_types_by_name['Transform']
_EXTRINSICS = DESCRIPTOR.message_types_by_name['Extrinsics']
_VEHICLEID = DESCRIPTOR.message_types_by_name['VehicleID']
_LATENCYPARAM = DESCRIPTOR.message_types_by_name['LatencyParam']
_VEHICLEPARAM = DESCRIPTOR.message_types_by_name['VehicleParam']
_VEHICLECONFIG = DESCRIPTOR.message_types_by_name['VehicleConfig']
Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {'DESCRIPTOR': _TRANSFORM, '__module__': 'modules.common.configs.proto.vehicle_config_pb2'})
_sym_db.RegisterMessage(Transform)
Extrinsics = _reflection.GeneratedProtocolMessageType('Extrinsics', (_message.Message,), {'DESCRIPTOR': _EXTRINSICS, '__module__': 'modules.common.configs.proto.vehicle_config_pb2'})
_sym_db.RegisterMessage(Extrinsics)
VehicleID = _reflection.GeneratedProtocolMessageType('VehicleID', (_message.Message,), {'DESCRIPTOR': _VEHICLEID, '__module__': 'modules.common.configs.proto.vehicle_config_pb2'})
_sym_db.RegisterMessage(VehicleID)
LatencyParam = _reflection.GeneratedProtocolMessageType('LatencyParam', (_message.Message,), {'DESCRIPTOR': _LATENCYPARAM, '__module__': 'modules.common.configs.proto.vehicle_config_pb2'})
_sym_db.RegisterMessage(LatencyParam)
VehicleParam = _reflection.GeneratedProtocolMessageType('VehicleParam', (_message.Message,), {'DESCRIPTOR': _VEHICLEPARAM, '__module__': 'modules.common.configs.proto.vehicle_config_pb2'})
_sym_db.RegisterMessage(VehicleParam)
VehicleConfig = _reflection.GeneratedProtocolMessageType('VehicleConfig', (_message.Message,), {'DESCRIPTOR': _VEHICLECONFIG, '__module__': 'modules.common.configs.proto.vehicle_config_pb2'})
_sym_db.RegisterMessage(VehicleConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VEHICLEBRAND._serialized_start = 1532
    _VEHICLEBRAND._serialized_end = 1658
    _TRANSFORM._serialized_start = 141
    _TRANSFORM._serialized_end = 286
    _EXTRINSICS._serialized_start = 288
    _EXTRINSICS._serialized_end = 345
    _VEHICLEID._serialized_start = 347
    _VEHICLEID._serialized_end = 411
    _LATENCYPARAM._serialized_start = 413
    _LATENCYPARAM._serialized_end = 507
    _VEHICLEPARAM._serialized_start = 510
    _VEHICLEPARAM._serialized_end = 1374
    _VEHICLECONFIG._serialized_start = 1377
    _VEHICLECONFIG._serialized_end = 1530