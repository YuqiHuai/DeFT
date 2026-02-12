"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!modules/canbus/proto/devkit.proto\x12\rapollo.canbus"\x88\x02\n\x14Throttle_command_100\x12\x14\n\x0cthrottle_acc\x18\x01 \x01(\x01\x12\x14\n\x0cchecksum_100\x18\x02 \x01(\x05\x12\x1d\n\x15throttle_pedal_target\x18\x03 \x01(\x01\x12R\n\x10throttle_en_ctrl\x18\x04 \x01(\x0e28.apollo.canbus.Throttle_command_100.Throttle_en_ctrlType"Q\n\x14Throttle_en_ctrlType\x12\x1c\n\x18THROTTLE_EN_CTRL_DISABLE\x10\x00\x12\x1b\n\x17THROTTLE_EN_CTRL_ENABLE\x10\x01"\x80\x03\n\x11Brake_command_101\x12\x11\n\tbrake_dec\x18\x01 \x01(\x01\x12\x14\n\x0cchecksum_101\x18\x02 \x01(\x05\x12\x1a\n\x12brake_pedal_target\x18\x03 \x01(\x01\x12I\n\rbrake_en_ctrl\x18\x04 \x01(\x0e22.apollo.canbus.Brake_command_101.Brake_en_ctrlType\x12E\n\x0baeb_en_ctrl\x18\x05 \x01(\x0e20.apollo.canbus.Brake_command_101.Aeb_en_ctrlType"J\n\x0fAeb_en_ctrlType\x12\x1b\n\x17AEB_EN_CTRL_DISABLE_AEB\x10\x00\x12\x1a\n\x16AEB_EN_CTRL_ENABLE_AEB\x10\x01"H\n\x11Brake_en_ctrlType\x12\x19\n\x15BRAKE_EN_CTRL_DISABLE\x10\x00\x12\x18\n\x14BRAKE_EN_CTRL_ENABLE\x10\x01"\xf9\x01\n\x14Steering_command_102\x12L\n\rsteer_en_ctrl\x18\x01 \x01(\x0e25.apollo.canbus.Steering_command_102.Steer_en_ctrlType\x12\x1a\n\x12steer_angle_target\x18\x02 \x01(\x05\x12\x17\n\x0fsteer_angle_spd\x18\x03 \x01(\x05\x12\x14\n\x0cchecksum_102\x18\x04 \x01(\x05"H\n\x11Steer_en_ctrlType\x12\x19\n\x15STEER_EN_CTRL_DISABLE\x10\x00\x12\x18\n\x14STEER_EN_CTRL_ENABLE\x10\x01"\x89\x03\n\x10Gear_command_103\x12D\n\x0bgear_target\x18\x01 \x01(\x0e2/.apollo.canbus.Gear_command_103.Gear_targetType\x12F\n\x0cgear_en_ctrl\x18\x02 \x01(\x0e20.apollo.canbus.Gear_command_103.Gear_en_ctrlType\x12\x14\n\x0cchecksum_103\x18\x03 \x01(\x05"\x89\x01\n\x0fGear_targetType\x12\x17\n\x13GEAR_TARGET_INVALID\x10\x00\x12\x14\n\x10GEAR_TARGET_PARK\x10\x01\x12\x17\n\x13GEAR_TARGET_REVERSE\x10\x02\x12\x17\n\x13GEAR_TARGET_NEUTRAL\x10\x03\x12\x15\n\x11GEAR_TARGET_DRIVE\x10\x04"E\n\x10Gear_en_ctrlType\x12\x18\n\x14GEAR_EN_CTRL_DISABLE\x10\x00\x12\x17\n\x13GEAR_EN_CTRL_ENABLE\x10\x01"\xca\x02\n\x10Park_command_104\x12\x14\n\x0cchecksum_104\x18\x01 \x01(\x05\x12D\n\x0bpark_target\x18\x02 \x01(\x0e2/.apollo.canbus.Park_command_104.Park_targetType\x12F\n\x0cpark_en_ctrl\x18\x03 \x01(\x0e20.apollo.canbus.Park_command_104.Park_en_ctrlType"K\n\x0fPark_targetType\x12\x17\n\x13PARK_TARGET_RELEASE\x10\x00\x12\x1f\n\x1bPARK_TARGET_PARKING_TRIGGER\x10\x01"E\n\x10Park_en_ctrlType\x12\x18\n\x14PARK_EN_CTRL_DISABLE\x10\x00\x12\x17\n\x13PARK_EN_CTRL_ENABLE\x10\x01"\xfa\x04\n\x13Throttle_report_500\x12\x1d\n\x15throttle_pedal_actual\x18\x01 \x01(\x01\x12K\n\rthrottle_flt2\x18\x02 \x01(\x0e24.apollo.canbus.Throttle_report_500.Throttle_flt2Type\x12K\n\rthrottle_flt1\x18\x03 \x01(\x0e24.apollo.canbus.Throttle_report_500.Throttle_flt1Type\x12S\n\x11throttle_en_state\x18\x04 \x01(\x0e28.apollo.canbus.Throttle_report_500.Throttle_en_stateType"b\n\x11Throttle_flt2Type\x12\x1a\n\x16THROTTLE_FLT2_NO_FAULT\x10\x00\x121\n-THROTTLE_FLT2_DRIVE_SYSTEM_COMUNICATION_FAULT\x10\x01"^\n\x11Throttle_flt1Type\x12\x1a\n\x16THROTTLE_FLT1_NO_FAULT\x10\x00\x12-\n)THROTTLE_FLT1_DRIVE_SYSTEM_HARDWARE_FAULT\x10\x01"\x90\x01\n\x15Throttle_en_stateType\x12\x1c\n\x18THROTTLE_EN_STATE_MANUAL\x10\x00\x12\x1a\n\x16THROTTLE_EN_STATE_AUTO\x10\x01\x12\x1e\n\x1aTHROTTLE_EN_STATE_TAKEOVER\x10\x02\x12\x1d\n\x19THROTTLE_EN_STATE_STANDBY\x10\x03"\xb8\x04\n\x10Brake_report_501\x12\x1a\n\x12brake_pedal_actual\x18\x01 \x01(\x01\x12B\n\nbrake_flt2\x18\x02 \x01(\x0e2..apollo.canbus.Brake_report_501.Brake_flt2Type\x12B\n\nbrake_flt1\x18\x03 \x01(\x0e2..apollo.canbus.Brake_report_501.Brake_flt1Type\x12J\n\x0ebrake_en_state\x18\x04 \x01(\x0e22.apollo.canbus.Brake_report_501.Brake_en_stateType"Y\n\x0eBrake_flt2Type\x12\x17\n\x13BRAKE_FLT2_NO_FAULT\x10\x00\x12.\n*BRAKE_FLT2_BRAKE_SYSTEM_COMUNICATION_FAULT\x10\x01"U\n\x0eBrake_flt1Type\x12\x17\n\x13BRAKE_FLT1_NO_FAULT\x10\x00\x12*\n&BRAKE_FLT1_BRAKE_SYSTEM_HARDWARE_FAULT\x10\x01"\x81\x01\n\x12Brake_en_stateType\x12\x19\n\x15BRAKE_EN_STATE_MANUAL\x10\x00\x12\x17\n\x13BRAKE_EN_STATE_AUTO\x10\x01\x12\x1b\n\x17BRAKE_EN_STATE_TAKEOVER\x10\x02\x12\x1a\n\x16BRAKE_EN_STATE_STANDBY\x10\x03"\xe4\x04\n\x13Steering_report_502\x12\x1e\n\x16steer_angle_spd_actual\x18\x01 \x01(\x05\x12E\n\nsteer_flt2\x18\x02 \x01(\x0e21.apollo.canbus.Steering_report_502.Steer_flt2Type\x12E\n\nsteer_flt1\x18\x03 \x01(\x0e21.apollo.canbus.Steering_report_502.Steer_flt1Type\x12M\n\x0esteer_en_state\x18\x04 \x01(\x0e25.apollo.canbus.Steering_report_502.Steer_en_stateType\x12\x1a\n\x12steer_angle_actual\x18\x05 \x01(\x05"Y\n\x0eSteer_flt2Type\x12\x17\n\x13STEER_FLT2_NO_FAULT\x10\x00\x12.\n*STEER_FLT2_STEER_SYSTEM_COMUNICATION_FAULT\x10\x01"U\n\x0eSteer_flt1Type\x12\x17\n\x13STEER_FLT1_NO_FAULT\x10\x00\x12*\n&STEER_FLT1_STEER_SYSTEM_HARDWARE_FAULT\x10\x01"\x81\x01\n\x12Steer_en_stateType\x12\x19\n\x15STEER_EN_STATE_MANUAL\x10\x00\x12\x17\n\x13STEER_EN_STATE_AUTO\x10\x01\x12\x1b\n\x17STEER_EN_STATE_TAKEOVER\x10\x02\x12\x1a\n\x16STEER_EN_STATE_STANDBY\x10\x03"\xdc\x02\n\x0fGear_report_503\x12=\n\x08gear_flt\x18\x01 \x01(\x0e2+.apollo.canbus.Gear_report_503.Gear_fltType\x12C\n\x0bgear_actual\x18\x02 \x01(\x0e2..apollo.canbus.Gear_report_503.Gear_actualType"9\n\x0cGear_fltType\x12\x15\n\x11GEAR_FLT_NO_FAULT\x10\x00\x12\x12\n\x0eGEAR_FLT_FAULT\x10\x01"\x89\x01\n\x0fGear_actualType\x12\x17\n\x13GEAR_ACTUAL_INVALID\x10\x00\x12\x14\n\x10GEAR_ACTUAL_PARK\x10\x01\x12\x17\n\x13GEAR_ACTUAL_REVERSE\x10\x02\x12\x17\n\x13GEAR_ACTUAL_NEUTRAL\x10\x03\x12\x15\n\x11GEAR_ACTUAL_DRIVE\x10\x04"\xac\x02\n\x0fPark_report_504\x12I\n\x0eparking_actual\x18\x01 \x01(\x0e21.apollo.canbus.Park_report_504.Parking_actualType\x12=\n\x08park_flt\x18\x02 \x01(\x0e2+.apollo.canbus.Park_report_504.Park_fltType"T\n\x12Parking_actualType\x12\x1a\n\x16PARKING_ACTUAL_RELEASE\x10\x00\x12"\n\x1ePARKING_ACTUAL_PARKING_TRIGGER\x10\x01"9\n\x0cPark_fltType\x12\x15\n\x11PARK_FLT_NO_FAULT\x10\x00\x12\x12\n\x0ePARK_FLT_FAULT\x10\x01"\xfa\x05\n\x0eVcu_report_505\x12P\n\x12vehicle_mode_state\x18\x01 \x01(\x0e24.apollo.canbus.Vcu_report_505.Vehicle_mode_stateType\x12L\n\x10frontcrash_state\x18\x02 \x01(\x0e22.apollo.canbus.Vcu_report_505.Frontcrash_stateType\x12J\n\x0fbackcrash_state\x18\x03 \x01(\x0e21.apollo.canbus.Vcu_report_505.Backcrash_stateType\x12>\n\taeb_state\x18\x04 \x01(\x0e2+.apollo.canbus.Vcu_report_505.Aeb_stateType\x12\x0b\n\x03acc\x18\x05 \x01(\x01\x12\r\n\x05speed\x18\x06 \x01(\x01"\xb1\x01\n\x16Vehicle_mode_stateType\x12)\n%VEHICLE_MODE_STATE_MANUAL_REMOTE_MODE\x10\x00\x12 \n\x1cVEHICLE_MODE_STATE_AUTO_MODE\x10\x01\x12%\n!VEHICLE_MODE_STATE_EMERGENCY_MODE\x10\x02\x12#\n\x1fVEHICLE_MODE_STATE_STANDBY_MODE\x10\x03"W\n\x14Frontcrash_stateType\x12\x1d\n\x19FRONTCRASH_STATE_NO_EVENT\x10\x00\x12 \n\x1cFRONTCRASH_STATE_CRASH_EVENT\x10\x01"T\n\x13Backcrash_stateType\x12\x1c\n\x18BACKCRASH_STATE_NO_EVENT\x10\x00\x12\x1f\n\x1bBACKCRASH_STATE_CRASH_EVENT\x10\x01"=\n\rAeb_stateType\x12\x16\n\x12AEB_STATE_INACTIVE\x10\x00\x12\x14\n\x10AEB_STATE_ACTIVE\x10\x01"G\n\x15Wheelspeed_report_506\x12\n\n\x02rr\x18\x01 \x01(\x01\x12\n\n\x02rl\x18\x02 \x01(\x01\x12\n\n\x02fr\x18\x03 \x01(\x01\x12\n\n\x02fl\x18\x04 \x01(\x01"\x81\x01\n\x11Ultr_sensor_1_507\x12\x19\n\x11uiuss9_tof_direct\x18\x01 \x01(\x01\x12\x19\n\x11uiuss8_tof_direct\x18\x02 \x01(\x01\x12\x1a\n\x12uiuss11_tof_direct\x18\x03 \x01(\x01\x12\x1a\n\x12uiuss10_tof_direct\x18\x04 \x01(\x01"\x89\x01\n\x11Ultr_sensor_2_508\x12\x1b\n\x13uiuss9_tof_indirect\x18\x01 \x01(\x01\x12\x1b\n\x13uiuss8_tof_indirect\x18\x02 \x01(\x01\x12\x1c\n\x14uiuss11_tof_indirect\x18\x03 \x01(\x01\x12\x1c\n\x14uiuss10_tof_indirect\x18\x04 \x01(\x01"\x7f\n\x11Ultr_sensor_3_509\x12\x19\n\x11uiuss5_tof_direct\x18\x01 \x01(\x01\x12\x19\n\x11uiuss4_tof_direct\x18\x02 \x01(\x01\x12\x19\n\x11uiuss3_tof_direct\x18\x03 \x01(\x01\x12\x19\n\x11uiuss2_tof_direct\x18\x04 \x01(\x01"\x87\x01\n\x11Ultr_sensor_4_510\x12\x1b\n\x13uiuss5_tof_indirect\x18\x01 \x01(\x01\x12\x1b\n\x13uiuss4_tof_indirect\x18\x02 \x01(\x01\x12\x1b\n\x13uiuss3_tof_indirect\x18\x03 \x01(\x01\x12\x1b\n\x13uiuss2_tof_indirect\x18\x04 \x01(\x01"\x7f\n\x11Ultr_sensor_5_511\x12\x19\n\x11uiuss7_tof_direct\x18\x01 \x01(\x01\x12\x19\n\x11uiuss6_tof_direct\x18\x02 \x01(\x01\x12\x19\n\x11uiuss1_tof_direct\x18\x03 \x01(\x01\x12\x19\n\x11uiuss0_tof_direct\x18\x04 \x01(\x01"W\n\x0eBms_report_512\x12\x17\n\x0fbattery_current\x18\x01 \x01(\x01\x12\x17\n\x0fbattery_voltage\x18\x02 \x01(\x01\x12\x13\n\x0bbattery_soc\x18\x03 \x01(\x05"\xd4\x08\n\x06Devkit\x12A\n\x14throttle_command_100\x18\x01 \x01(\x0b2#.apollo.canbus.Throttle_command_100\x12;\n\x11brake_command_101\x18\x02 \x01(\x0b2 .apollo.canbus.Brake_command_101\x12A\n\x14steering_command_102\x18\x03 \x01(\x0b2#.apollo.canbus.Steering_command_102\x129\n\x10gear_command_103\x18\x04 \x01(\x0b2\x1f.apollo.canbus.Gear_command_103\x129\n\x10park_command_104\x18\x05 \x01(\x0b2\x1f.apollo.canbus.Park_command_104\x12?\n\x13throttle_report_500\x18\x06 \x01(\x0b2".apollo.canbus.Throttle_report_500\x129\n\x10brake_report_501\x18\x07 \x01(\x0b2\x1f.apollo.canbus.Brake_report_501\x12?\n\x13steering_report_502\x18\x08 \x01(\x0b2".apollo.canbus.Steering_report_502\x127\n\x0fgear_report_503\x18\t \x01(\x0b2\x1e.apollo.canbus.Gear_report_503\x127\n\x0fpark_report_504\x18\n \x01(\x0b2\x1e.apollo.canbus.Park_report_504\x125\n\x0evcu_report_505\x18\x0b \x01(\x0b2\x1d.apollo.canbus.Vcu_report_505\x12C\n\x15wheelspeed_report_506\x18\x0c \x01(\x0b2$.apollo.canbus.Wheelspeed_report_506\x12;\n\x11ultr_sensor_1_507\x18\r \x01(\x0b2 .apollo.canbus.Ultr_sensor_1_507\x12;\n\x11ultr_sensor_2_508\x18\x0e \x01(\x0b2 .apollo.canbus.Ultr_sensor_2_508\x12;\n\x11ultr_sensor_3_509\x18\x0f \x01(\x0b2 .apollo.canbus.Ultr_sensor_3_509\x12;\n\x11ultr_sensor_4_510\x18\x10 \x01(\x0b2 .apollo.canbus.Ultr_sensor_4_510\x12;\n\x11ultr_sensor_5_511\x18\x11 \x01(\x0b2 .apollo.canbus.Ultr_sensor_5_511\x125\n\x0ebms_report_512\x18\x12 \x01(\x0b2\x1d.apollo.canbus.Bms_report_512')
_THROTTLE_COMMAND_100 = DESCRIPTOR.message_types_by_name['Throttle_command_100']
_BRAKE_COMMAND_101 = DESCRIPTOR.message_types_by_name['Brake_command_101']
_STEERING_COMMAND_102 = DESCRIPTOR.message_types_by_name['Steering_command_102']
_GEAR_COMMAND_103 = DESCRIPTOR.message_types_by_name['Gear_command_103']
_PARK_COMMAND_104 = DESCRIPTOR.message_types_by_name['Park_command_104']
_THROTTLE_REPORT_500 = DESCRIPTOR.message_types_by_name['Throttle_report_500']
_BRAKE_REPORT_501 = DESCRIPTOR.message_types_by_name['Brake_report_501']
_STEERING_REPORT_502 = DESCRIPTOR.message_types_by_name['Steering_report_502']
_GEAR_REPORT_503 = DESCRIPTOR.message_types_by_name['Gear_report_503']
_PARK_REPORT_504 = DESCRIPTOR.message_types_by_name['Park_report_504']
_VCU_REPORT_505 = DESCRIPTOR.message_types_by_name['Vcu_report_505']
_WHEELSPEED_REPORT_506 = DESCRIPTOR.message_types_by_name['Wheelspeed_report_506']
_ULTR_SENSOR_1_507 = DESCRIPTOR.message_types_by_name['Ultr_sensor_1_507']
_ULTR_SENSOR_2_508 = DESCRIPTOR.message_types_by_name['Ultr_sensor_2_508']
_ULTR_SENSOR_3_509 = DESCRIPTOR.message_types_by_name['Ultr_sensor_3_509']
_ULTR_SENSOR_4_510 = DESCRIPTOR.message_types_by_name['Ultr_sensor_4_510']
_ULTR_SENSOR_5_511 = DESCRIPTOR.message_types_by_name['Ultr_sensor_5_511']
_BMS_REPORT_512 = DESCRIPTOR.message_types_by_name['Bms_report_512']
_DEVKIT = DESCRIPTOR.message_types_by_name['Devkit']
_THROTTLE_COMMAND_100_THROTTLE_EN_CTRLTYPE = _THROTTLE_COMMAND_100.enum_types_by_name['Throttle_en_ctrlType']
_BRAKE_COMMAND_101_AEB_EN_CTRLTYPE = _BRAKE_COMMAND_101.enum_types_by_name['Aeb_en_ctrlType']
_BRAKE_COMMAND_101_BRAKE_EN_CTRLTYPE = _BRAKE_COMMAND_101.enum_types_by_name['Brake_en_ctrlType']
_STEERING_COMMAND_102_STEER_EN_CTRLTYPE = _STEERING_COMMAND_102.enum_types_by_name['Steer_en_ctrlType']
_GEAR_COMMAND_103_GEAR_TARGETTYPE = _GEAR_COMMAND_103.enum_types_by_name['Gear_targetType']
_GEAR_COMMAND_103_GEAR_EN_CTRLTYPE = _GEAR_COMMAND_103.enum_types_by_name['Gear_en_ctrlType']
_PARK_COMMAND_104_PARK_TARGETTYPE = _PARK_COMMAND_104.enum_types_by_name['Park_targetType']
_PARK_COMMAND_104_PARK_EN_CTRLTYPE = _PARK_COMMAND_104.enum_types_by_name['Park_en_ctrlType']
_THROTTLE_REPORT_500_THROTTLE_FLT2TYPE = _THROTTLE_REPORT_500.enum_types_by_name['Throttle_flt2Type']
_THROTTLE_REPORT_500_THROTTLE_FLT1TYPE = _THROTTLE_REPORT_500.enum_types_by_name['Throttle_flt1Type']
_THROTTLE_REPORT_500_THROTTLE_EN_STATETYPE = _THROTTLE_REPORT_500.enum_types_by_name['Throttle_en_stateType']
_BRAKE_REPORT_501_BRAKE_FLT2TYPE = _BRAKE_REPORT_501.enum_types_by_name['Brake_flt2Type']
_BRAKE_REPORT_501_BRAKE_FLT1TYPE = _BRAKE_REPORT_501.enum_types_by_name['Brake_flt1Type']
_BRAKE_REPORT_501_BRAKE_EN_STATETYPE = _BRAKE_REPORT_501.enum_types_by_name['Brake_en_stateType']
_STEERING_REPORT_502_STEER_FLT2TYPE = _STEERING_REPORT_502.enum_types_by_name['Steer_flt2Type']
_STEERING_REPORT_502_STEER_FLT1TYPE = _STEERING_REPORT_502.enum_types_by_name['Steer_flt1Type']
_STEERING_REPORT_502_STEER_EN_STATETYPE = _STEERING_REPORT_502.enum_types_by_name['Steer_en_stateType']
_GEAR_REPORT_503_GEAR_FLTTYPE = _GEAR_REPORT_503.enum_types_by_name['Gear_fltType']
_GEAR_REPORT_503_GEAR_ACTUALTYPE = _GEAR_REPORT_503.enum_types_by_name['Gear_actualType']
_PARK_REPORT_504_PARKING_ACTUALTYPE = _PARK_REPORT_504.enum_types_by_name['Parking_actualType']
_PARK_REPORT_504_PARK_FLTTYPE = _PARK_REPORT_504.enum_types_by_name['Park_fltType']
_VCU_REPORT_505_VEHICLE_MODE_STATETYPE = _VCU_REPORT_505.enum_types_by_name['Vehicle_mode_stateType']
_VCU_REPORT_505_FRONTCRASH_STATETYPE = _VCU_REPORT_505.enum_types_by_name['Frontcrash_stateType']
_VCU_REPORT_505_BACKCRASH_STATETYPE = _VCU_REPORT_505.enum_types_by_name['Backcrash_stateType']
_VCU_REPORT_505_AEB_STATETYPE = _VCU_REPORT_505.enum_types_by_name['Aeb_stateType']
Throttle_command_100 = _reflection.GeneratedProtocolMessageType('Throttle_command_100', (_message.Message,), {'DESCRIPTOR': _THROTTLE_COMMAND_100, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Throttle_command_100)
Brake_command_101 = _reflection.GeneratedProtocolMessageType('Brake_command_101', (_message.Message,), {'DESCRIPTOR': _BRAKE_COMMAND_101, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Brake_command_101)
Steering_command_102 = _reflection.GeneratedProtocolMessageType('Steering_command_102', (_message.Message,), {'DESCRIPTOR': _STEERING_COMMAND_102, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Steering_command_102)
Gear_command_103 = _reflection.GeneratedProtocolMessageType('Gear_command_103', (_message.Message,), {'DESCRIPTOR': _GEAR_COMMAND_103, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Gear_command_103)
Park_command_104 = _reflection.GeneratedProtocolMessageType('Park_command_104', (_message.Message,), {'DESCRIPTOR': _PARK_COMMAND_104, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Park_command_104)
Throttle_report_500 = _reflection.GeneratedProtocolMessageType('Throttle_report_500', (_message.Message,), {'DESCRIPTOR': _THROTTLE_REPORT_500, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Throttle_report_500)
Brake_report_501 = _reflection.GeneratedProtocolMessageType('Brake_report_501', (_message.Message,), {'DESCRIPTOR': _BRAKE_REPORT_501, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Brake_report_501)
Steering_report_502 = _reflection.GeneratedProtocolMessageType('Steering_report_502', (_message.Message,), {'DESCRIPTOR': _STEERING_REPORT_502, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Steering_report_502)
Gear_report_503 = _reflection.GeneratedProtocolMessageType('Gear_report_503', (_message.Message,), {'DESCRIPTOR': _GEAR_REPORT_503, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Gear_report_503)
Park_report_504 = _reflection.GeneratedProtocolMessageType('Park_report_504', (_message.Message,), {'DESCRIPTOR': _PARK_REPORT_504, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Park_report_504)
Vcu_report_505 = _reflection.GeneratedProtocolMessageType('Vcu_report_505', (_message.Message,), {'DESCRIPTOR': _VCU_REPORT_505, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Vcu_report_505)
Wheelspeed_report_506 = _reflection.GeneratedProtocolMessageType('Wheelspeed_report_506', (_message.Message,), {'DESCRIPTOR': _WHEELSPEED_REPORT_506, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Wheelspeed_report_506)
Ultr_sensor_1_507 = _reflection.GeneratedProtocolMessageType('Ultr_sensor_1_507', (_message.Message,), {'DESCRIPTOR': _ULTR_SENSOR_1_507, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Ultr_sensor_1_507)
Ultr_sensor_2_508 = _reflection.GeneratedProtocolMessageType('Ultr_sensor_2_508', (_message.Message,), {'DESCRIPTOR': _ULTR_SENSOR_2_508, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Ultr_sensor_2_508)
Ultr_sensor_3_509 = _reflection.GeneratedProtocolMessageType('Ultr_sensor_3_509', (_message.Message,), {'DESCRIPTOR': _ULTR_SENSOR_3_509, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Ultr_sensor_3_509)
Ultr_sensor_4_510 = _reflection.GeneratedProtocolMessageType('Ultr_sensor_4_510', (_message.Message,), {'DESCRIPTOR': _ULTR_SENSOR_4_510, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Ultr_sensor_4_510)
Ultr_sensor_5_511 = _reflection.GeneratedProtocolMessageType('Ultr_sensor_5_511', (_message.Message,), {'DESCRIPTOR': _ULTR_SENSOR_5_511, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Ultr_sensor_5_511)
Bms_report_512 = _reflection.GeneratedProtocolMessageType('Bms_report_512', (_message.Message,), {'DESCRIPTOR': _BMS_REPORT_512, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Bms_report_512)
Devkit = _reflection.GeneratedProtocolMessageType('Devkit', (_message.Message,), {'DESCRIPTOR': _DEVKIT, '__module__': 'modules.canbus.proto.devkit_pb2'})
_sym_db.RegisterMessage(Devkit)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _THROTTLE_COMMAND_100._serialized_start = 53
    _THROTTLE_COMMAND_100._serialized_end = 317
    _THROTTLE_COMMAND_100_THROTTLE_EN_CTRLTYPE._serialized_start = 236
    _THROTTLE_COMMAND_100_THROTTLE_EN_CTRLTYPE._serialized_end = 317
    _BRAKE_COMMAND_101._serialized_start = 320
    _BRAKE_COMMAND_101._serialized_end = 704
    _BRAKE_COMMAND_101_AEB_EN_CTRLTYPE._serialized_start = 556
    _BRAKE_COMMAND_101_AEB_EN_CTRLTYPE._serialized_end = 630
    _BRAKE_COMMAND_101_BRAKE_EN_CTRLTYPE._serialized_start = 632
    _BRAKE_COMMAND_101_BRAKE_EN_CTRLTYPE._serialized_end = 704
    _STEERING_COMMAND_102._serialized_start = 707
    _STEERING_COMMAND_102._serialized_end = 956
    _STEERING_COMMAND_102_STEER_EN_CTRLTYPE._serialized_start = 884
    _STEERING_COMMAND_102_STEER_EN_CTRLTYPE._serialized_end = 956
    _GEAR_COMMAND_103._serialized_start = 959
    _GEAR_COMMAND_103._serialized_end = 1352
    _GEAR_COMMAND_103_GEAR_TARGETTYPE._serialized_start = 1144
    _GEAR_COMMAND_103_GEAR_TARGETTYPE._serialized_end = 1281
    _GEAR_COMMAND_103_GEAR_EN_CTRLTYPE._serialized_start = 1283
    _GEAR_COMMAND_103_GEAR_EN_CTRLTYPE._serialized_end = 1352
    _PARK_COMMAND_104._serialized_start = 1355
    _PARK_COMMAND_104._serialized_end = 1685
    _PARK_COMMAND_104_PARK_TARGETTYPE._serialized_start = 1539
    _PARK_COMMAND_104_PARK_TARGETTYPE._serialized_end = 1614
    _PARK_COMMAND_104_PARK_EN_CTRLTYPE._serialized_start = 1616
    _PARK_COMMAND_104_PARK_EN_CTRLTYPE._serialized_end = 1685
    _THROTTLE_REPORT_500._serialized_start = 1688
    _THROTTLE_REPORT_500._serialized_end = 2322
    _THROTTLE_REPORT_500_THROTTLE_FLT2TYPE._serialized_start = 1981
    _THROTTLE_REPORT_500_THROTTLE_FLT2TYPE._serialized_end = 2079
    _THROTTLE_REPORT_500_THROTTLE_FLT1TYPE._serialized_start = 2081
    _THROTTLE_REPORT_500_THROTTLE_FLT1TYPE._serialized_end = 2175
    _THROTTLE_REPORT_500_THROTTLE_EN_STATETYPE._serialized_start = 2178
    _THROTTLE_REPORT_500_THROTTLE_EN_STATETYPE._serialized_end = 2322
    _BRAKE_REPORT_501._serialized_start = 2325
    _BRAKE_REPORT_501._serialized_end = 2893
    _BRAKE_REPORT_501_BRAKE_FLT2TYPE._serialized_start = 2585
    _BRAKE_REPORT_501_BRAKE_FLT2TYPE._serialized_end = 2674
    _BRAKE_REPORT_501_BRAKE_FLT1TYPE._serialized_start = 2676
    _BRAKE_REPORT_501_BRAKE_FLT1TYPE._serialized_end = 2761
    _BRAKE_REPORT_501_BRAKE_EN_STATETYPE._serialized_start = 2764
    _BRAKE_REPORT_501_BRAKE_EN_STATETYPE._serialized_end = 2893
    _STEERING_REPORT_502._serialized_start = 2896
    _STEERING_REPORT_502._serialized_end = 3508
    _STEERING_REPORT_502_STEER_FLT2TYPE._serialized_start = 3200
    _STEERING_REPORT_502_STEER_FLT2TYPE._serialized_end = 3289
    _STEERING_REPORT_502_STEER_FLT1TYPE._serialized_start = 3291
    _STEERING_REPORT_502_STEER_FLT1TYPE._serialized_end = 3376
    _STEERING_REPORT_502_STEER_EN_STATETYPE._serialized_start = 3379
    _STEERING_REPORT_502_STEER_EN_STATETYPE._serialized_end = 3508
    _GEAR_REPORT_503._serialized_start = 3511
    _GEAR_REPORT_503._serialized_end = 3859
    _GEAR_REPORT_503_GEAR_FLTTYPE._serialized_start = 3662
    _GEAR_REPORT_503_GEAR_FLTTYPE._serialized_end = 3719
    _GEAR_REPORT_503_GEAR_ACTUALTYPE._serialized_start = 3722
    _GEAR_REPORT_503_GEAR_ACTUALTYPE._serialized_end = 3859
    _PARK_REPORT_504._serialized_start = 3862
    _PARK_REPORT_504._serialized_end = 4162
    _PARK_REPORT_504_PARKING_ACTUALTYPE._serialized_start = 4019
    _PARK_REPORT_504_PARKING_ACTUALTYPE._serialized_end = 4103
    _PARK_REPORT_504_PARK_FLTTYPE._serialized_start = 4105
    _PARK_REPORT_504_PARK_FLTTYPE._serialized_end = 4162
    _VCU_REPORT_505._serialized_start = 4165
    _VCU_REPORT_505._serialized_end = 4927
    _VCU_REPORT_505_VEHICLE_MODE_STATETYPE._serialized_start = 4512
    _VCU_REPORT_505_VEHICLE_MODE_STATETYPE._serialized_end = 4689
    _VCU_REPORT_505_FRONTCRASH_STATETYPE._serialized_start = 4691
    _VCU_REPORT_505_FRONTCRASH_STATETYPE._serialized_end = 4778
    _VCU_REPORT_505_BACKCRASH_STATETYPE._serialized_start = 4780
    _VCU_REPORT_505_BACKCRASH_STATETYPE._serialized_end = 4864
    _VCU_REPORT_505_AEB_STATETYPE._serialized_start = 4866
    _VCU_REPORT_505_AEB_STATETYPE._serialized_end = 4927
    _WHEELSPEED_REPORT_506._serialized_start = 4929
    _WHEELSPEED_REPORT_506._serialized_end = 5000
    _ULTR_SENSOR_1_507._serialized_start = 5003
    _ULTR_SENSOR_1_507._serialized_end = 5132
    _ULTR_SENSOR_2_508._serialized_start = 5135
    _ULTR_SENSOR_2_508._serialized_end = 5272
    _ULTR_SENSOR_3_509._serialized_start = 5274
    _ULTR_SENSOR_3_509._serialized_end = 5401
    _ULTR_SENSOR_4_510._serialized_start = 5404
    _ULTR_SENSOR_4_510._serialized_end = 5539
    _ULTR_SENSOR_5_511._serialized_start = 5541
    _ULTR_SENSOR_5_511._serialized_end = 5668
    _BMS_REPORT_512._serialized_start = 5670
    _BMS_REPORT_512._serialized_end = 5757
    _DEVKIT._serialized_start = 5760
    _DEVKIT._serialized_end = 6868