"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import vehicle_signal_pb2 as modules_dot_common_dot_proto_dot_vehicle__signal__pb2
from ....modules.common.proto import drive_state_pb2 as modules_dot_common_dot_proto_dot_drive__state__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.configs.proto import vehicle_config_pb2 as modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"modules/canbus/proto/chassis.proto\x12\rapollo.canbus\x1a!modules/common/proto/header.proto\x1a)modules/common/proto/vehicle_signal.proto\x1a&modules/common/proto/drive_state.proto\x1a#modules/common/proto/geometry.proto\x1a1modules/common/configs/proto/vehicle_config.proto"\xec\x0c\n\x07Chassis\x12\x16\n\x0eengine_started\x18\x03 \x01(\x08\x12\x17\n\nengine_rpm\x18\x04 \x01(\x02:\x03nan\x12\x16\n\tspeed_mps\x18\x05 \x01(\x02:\x03nan\x12\x17\n\nodometer_m\x18\x06 \x01(\x02:\x03nan\x12\x14\n\x0cfuel_range_m\x18\x07 \x01(\x05\x12 \n\x13throttle_percentage\x18\x08 \x01(\x02:\x03nan\x12\x1d\n\x10brake_percentage\x18\t \x01(\x02:\x03nan\x12 \n\x13steering_percentage\x18\x0b \x01(\x02:\x03nan\x12\x1f\n\x12steering_torque_nm\x18\x0c \x01(\x02:\x03nan\x12\x15\n\rparking_brake\x18\r \x01(\x08\x12\x1c\n\x10high_beam_signal\x18\x0e \x01(\x08B\x02\x18\x01\x12\x1b\n\x0flow_beam_signal\x18\x0f \x01(\x08B\x02\x18\x01\x12\x1c\n\x10left_turn_signal\x18\x10 \x01(\x08B\x02\x18\x01\x12\x1d\n\x11right_turn_signal\x18\x11 \x01(\x08B\x02\x18\x01\x12\x10\n\x04horn\x18\x12 \x01(\x08B\x02\x18\x01\x12\r\n\x05wiper\x18\x13 \x01(\x08\x12\x1c\n\x10disengage_status\x18\x14 \x01(\x08B\x02\x18\x01\x12I\n\x0cdriving_mode\x18\x15 \x01(\x0e2".apollo.canbus.Chassis.DrivingMode:\x0fCOMPLETE_MANUAL\x12>\n\nerror_code\x18\x16 \x01(\x0e2 .apollo.canbus.Chassis.ErrorCode:\x08NO_ERROR\x12:\n\rgear_location\x18\x17 \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x12\x1a\n\x12steering_timestamp\x18\x18 \x01(\x01\x12%\n\x06header\x18\x19 \x01(\x0b2\x15.apollo.common.Header\x12\x1d\n\x12chassis_error_mask\x18\x1a \x01(\x05:\x010\x12,\n\x06signal\x18\x1b \x01(\x0b2\x1c.apollo.common.VehicleSignal\x12.\n\x0bchassis_gps\x18\x1c \x01(\x0b2\x19.apollo.canbus.ChassisGPS\x122\n\rengage_advice\x18\x1d \x01(\x0b2\x1b.apollo.common.EngageAdvice\x12.\n\x0bwheel_speed\x18\x1e \x01(\x0b2\x19.apollo.canbus.WheelSpeed\x12)\n\x08surround\x18\x1f \x01(\x0b2\x17.apollo.canbus.Surround\x12+\n\x07license\x18  \x01(\x0b2\x16.apollo.canbus.LicenseB\x02\x18\x01\x12,\n\nvehicle_id\x18! \x01(\x0b2\x18.apollo.common.VehicleID\x12"\n\x16battery_soc_percentage\x18" \x01(\x05:\x02-1"y\n\x0bDrivingMode\x12\x13\n\x0fCOMPLETE_MANUAL\x10\x00\x12\x17\n\x13COMPLETE_AUTO_DRIVE\x10\x01\x12\x13\n\x0fAUTO_STEER_ONLY\x10\x02\x12\x13\n\x0fAUTO_SPEED_ONLY\x10\x03\x12\x12\n\x0eEMERGENCY_MODE\x10\x04"\x80\x02\n\tErrorCode\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x15\n\x11CMD_NOT_IN_PERIOD\x10\x01\x12\x11\n\rCHASSIS_ERROR\x10\x02\x12\x1a\n\x16CHASSIS_ERROR_ON_STEER\x10\x06\x12\x1a\n\x16CHASSIS_ERROR_ON_BRAKE\x10\x07\x12\x1d\n\x19CHASSIS_ERROR_ON_THROTTLE\x10\x08\x12\x19\n\x15CHASSIS_ERROR_ON_GEAR\x10\t\x12\x17\n\x13MANUAL_INTERVENTION\x10\x03\x12\x1d\n\x19CHASSIS_CAN_NOT_IN_PERIOD\x10\x04\x12\x11\n\rUNKNOWN_ERROR\x10\x05"\x83\x01\n\x0cGearPosition\x12\x10\n\x0cGEAR_NEUTRAL\x10\x00\x12\x0e\n\nGEAR_DRIVE\x10\x01\x12\x10\n\x0cGEAR_REVERSE\x10\x02\x12\x10\n\x0cGEAR_PARKING\x10\x03\x12\x0c\n\x08GEAR_LOW\x10\x04\x12\x10\n\x0cGEAR_INVALID\x10\x05\x12\r\n\tGEAR_NONE\x10\x06"\x89\x03\n\nChassisGPS\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x11\n\tgps_valid\x18\x03 \x01(\x08\x12\x0c\n\x04year\x18\x04 \x01(\x05\x12\r\n\x05month\x18\x05 \x01(\x05\x12\x0b\n\x03day\x18\x06 \x01(\x05\x12\r\n\x05hours\x18\x07 \x01(\x05\x12\x0f\n\x07minutes\x18\x08 \x01(\x05\x12\x0f\n\x07seconds\x18\t \x01(\x05\x12\x19\n\x11compass_direction\x18\n \x01(\x01\x12\x0c\n\x04pdop\x18\x0b \x01(\x01\x12\x14\n\x0cis_gps_fault\x18\x0c \x01(\x08\x12\x13\n\x0bis_inferred\x18\r \x01(\x08\x12\x10\n\x08altitude\x18\x0e \x01(\x01\x12\x0f\n\x07heading\x18\x0f \x01(\x01\x12\x0c\n\x04hdop\x18\x10 \x01(\x01\x12\x0c\n\x04vdop\x18\x11 \x01(\x01\x12*\n\x07quality\x18\x12 \x01(\x0e2\x19.apollo.canbus.GpsQuality\x12\x16\n\x0enum_satellites\x18\x13 \x01(\x05\x12\x11\n\tgps_speed\x18\x14 \x01(\x01"\x8e\x05\n\nWheelSpeed\x12$\n\x15is_wheel_spd_rr_valid\x18\x01 \x01(\x08:\x05false\x12M\n\x12wheel_direction_rr\x18\x02 \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType:\x07INVALID\x12\x17\n\x0cwheel_spd_rr\x18\x03 \x01(\x01:\x010\x12$\n\x15is_wheel_spd_rl_valid\x18\x04 \x01(\x08:\x05false\x12M\n\x12wheel_direction_rl\x18\x05 \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType:\x07INVALID\x12\x17\n\x0cwheel_spd_rl\x18\x06 \x01(\x01:\x010\x12$\n\x15is_wheel_spd_fr_valid\x18\x07 \x01(\x08:\x05false\x12M\n\x12wheel_direction_fr\x18\x08 \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType:\x07INVALID\x12\x17\n\x0cwheel_spd_fr\x18\t \x01(\x01:\x010\x12$\n\x15is_wheel_spd_fl_valid\x18\n \x01(\x08:\x05false\x12M\n\x12wheel_direction_fl\x18\x0b \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType:\x07INVALID\x12\x17\n\x0cwheel_spd_fl\x18\x0c \x01(\x01:\x010"H\n\x0eWheelSpeedType\x12\x0b\n\x07FORWARD\x10\x00\x12\x0c\n\x08BACKWARD\x10\x01\x12\x0e\n\nSTANDSTILL\x10\x02\x12\x0b\n\x07INVALID\x10\x03"p\n\x05Sonar\x12\r\n\x05range\x18\x01 \x01(\x01\x12+\n\x0btranslation\x18\x02 \x01(\x0b2\x16.apollo.common.Point3D\x12+\n\x08rotation\x18\x03 \x01(\x0b2\x19.apollo.common.Quaternion"\xe4\x04\n\x08Surround\x12 \n\x18cross_traffic_alert_left\x18\x01 \x01(\x08\x12(\n cross_traffic_alert_left_enabled\x18\x02 \x01(\x08\x12\x1d\n\x15blind_spot_left_alert\x18\x03 \x01(\x08\x12%\n\x1dblind_spot_left_alert_enabled\x18\x04 \x01(\x08\x12!\n\x19cross_traffic_alert_right\x18\x05 \x01(\x08\x12)\n!cross_traffic_alert_right_enabled\x18\x06 \x01(\x08\x12\x1e\n\x16blind_spot_right_alert\x18\x07 \x01(\x08\x12&\n\x1eblind_spot_right_alert_enabled\x18\x08 \x01(\x08\x12\x0f\n\x07sonar00\x18\t \x01(\x01\x12\x0f\n\x07sonar01\x18\n \x01(\x01\x12\x0f\n\x07sonar02\x18\x0b \x01(\x01\x12\x0f\n\x07sonar03\x18\x0c \x01(\x01\x12\x0f\n\x07sonar04\x18\r \x01(\x01\x12\x0f\n\x07sonar05\x18\x0e \x01(\x01\x12\x0f\n\x07sonar06\x18\x0f \x01(\x01\x12\x0f\n\x07sonar07\x18\x10 \x01(\x01\x12\x0f\n\x07sonar08\x18\x11 \x01(\x01\x12\x0f\n\x07sonar09\x18\x12 \x01(\x01\x12\x0f\n\x07sonar10\x18\x13 \x01(\x01\x12\x0f\n\x07sonar11\x18\x14 \x01(\x01\x12\x15\n\rsonar_enabled\x18\x15 \x01(\x08\x12\x13\n\x0bsonar_fault\x18\x16 \x01(\x08\x12\x13\n\x0bsonar_range\x18\x17 \x03(\x01\x12#\n\x05sonar\x18\x18 \x03(\x0b2\x14.apollo.canbus.Sonar"\x1a\n\x07License\x12\x0f\n\x03vin\x18\x01 \x01(\tB\x02\x18\x01*A\n\nGpsQuality\x12\n\n\x06FIX_NO\x10\x00\x12\n\n\x06FIX_2D\x10\x01\x12\n\n\x06FIX_3D\x10\x02\x12\x0f\n\x0bFIX_INVALID\x10\x03')
_GPSQUALITY = DESCRIPTOR.enum_types_by_name['GpsQuality']
GpsQuality = enum_type_wrapper.EnumTypeWrapper(_GPSQUALITY)
FIX_NO = 0
FIX_2D = 1
FIX_3D = 2
FIX_INVALID = 3
_CHASSIS = DESCRIPTOR.message_types_by_name['Chassis']
_CHASSISGPS = DESCRIPTOR.message_types_by_name['ChassisGPS']
_WHEELSPEED = DESCRIPTOR.message_types_by_name['WheelSpeed']
_SONAR = DESCRIPTOR.message_types_by_name['Sonar']
_SURROUND = DESCRIPTOR.message_types_by_name['Surround']
_LICENSE = DESCRIPTOR.message_types_by_name['License']
_CHASSIS_DRIVINGMODE = _CHASSIS.enum_types_by_name['DrivingMode']
_CHASSIS_ERRORCODE = _CHASSIS.enum_types_by_name['ErrorCode']
_CHASSIS_GEARPOSITION = _CHASSIS.enum_types_by_name['GearPosition']
_WHEELSPEED_WHEELSPEEDTYPE = _WHEELSPEED.enum_types_by_name['WheelSpeedType']
Chassis = _reflection.GeneratedProtocolMessageType('Chassis', (_message.Message,), {'DESCRIPTOR': _CHASSIS, '__module__': 'modules.canbus.proto.chassis_pb2'})
_sym_db.RegisterMessage(Chassis)
ChassisGPS = _reflection.GeneratedProtocolMessageType('ChassisGPS', (_message.Message,), {'DESCRIPTOR': _CHASSISGPS, '__module__': 'modules.canbus.proto.chassis_pb2'})
_sym_db.RegisterMessage(ChassisGPS)
WheelSpeed = _reflection.GeneratedProtocolMessageType('WheelSpeed', (_message.Message,), {'DESCRIPTOR': _WHEELSPEED, '__module__': 'modules.canbus.proto.chassis_pb2'})
_sym_db.RegisterMessage(WheelSpeed)
Sonar = _reflection.GeneratedProtocolMessageType('Sonar', (_message.Message,), {'DESCRIPTOR': _SONAR, '__module__': 'modules.canbus.proto.chassis_pb2'})
_sym_db.RegisterMessage(Sonar)
Surround = _reflection.GeneratedProtocolMessageType('Surround', (_message.Message,), {'DESCRIPTOR': _SURROUND, '__module__': 'modules.canbus.proto.chassis_pb2'})
_sym_db.RegisterMessage(Surround)
License = _reflection.GeneratedProtocolMessageType('License', (_message.Message,), {'DESCRIPTOR': _LICENSE, '__module__': 'modules.canbus.proto.chassis_pb2'})
_sym_db.RegisterMessage(License)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CHASSIS.fields_by_name['high_beam_signal']._options = None
    _CHASSIS.fields_by_name['high_beam_signal']._serialized_options = b'\x18\x01'
    _CHASSIS.fields_by_name['low_beam_signal']._options = None
    _CHASSIS.fields_by_name['low_beam_signal']._serialized_options = b'\x18\x01'
    _CHASSIS.fields_by_name['left_turn_signal']._options = None
    _CHASSIS.fields_by_name['left_turn_signal']._serialized_options = b'\x18\x01'
    _CHASSIS.fields_by_name['right_turn_signal']._options = None
    _CHASSIS.fields_by_name['right_turn_signal']._serialized_options = b'\x18\x01'
    _CHASSIS.fields_by_name['horn']._options = None
    _CHASSIS.fields_by_name['horn']._serialized_options = b'\x18\x01'
    _CHASSIS.fields_by_name['disengage_status']._options = None
    _CHASSIS.fields_by_name['disengage_status']._serialized_options = b'\x18\x01'
    _CHASSIS.fields_by_name['license']._options = None
    _CHASSIS.fields_by_name['license']._serialized_options = b'\x18\x01'
    _LICENSE.fields_by_name['vin']._options = None
    _LICENSE.fields_by_name['vin']._serialized_options = b'\x18\x01'
    _GPSQUALITY._serialized_start = 3716
    _GPSQUALITY._serialized_end = 3781
    _CHASSIS._serialized_start = 260
    _CHASSIS._serialized_end = 1904
    _CHASSIS_DRIVINGMODE._serialized_start = 1390
    _CHASSIS_DRIVINGMODE._serialized_end = 1511
    _CHASSIS_ERRORCODE._serialized_start = 1514
    _CHASSIS_ERRORCODE._serialized_end = 1770
    _CHASSIS_GEARPOSITION._serialized_start = 1773
    _CHASSIS_GEARPOSITION._serialized_end = 1904
    _CHASSISGPS._serialized_start = 1907
    _CHASSISGPS._serialized_end = 2300
    _WHEELSPEED._serialized_start = 2303
    _WHEELSPEED._serialized_end = 2957
    _WHEELSPEED_WHEELSPEEDTYPE._serialized_start = 2885
    _WHEELSPEED_WHEELSPEEDTYPE._serialized_end = 2957
    _SONAR._serialized_start = 2959
    _SONAR._serialized_end = 3071
    _SURROUND._serialized_start = 3074
    _SURROUND._serialized_end = 3686
    _LICENSE._serialized_start = 3688
    _LICENSE._serialized_end = 3714