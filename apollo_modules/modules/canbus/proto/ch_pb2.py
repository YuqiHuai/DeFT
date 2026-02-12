"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmodules/canbus/proto/ch.proto\x12\rapollo.canbus"\xf7\x01\n\x14Throttle_command_110\x12^\n\x16throttle_pedal_en_ctrl\x18\x01 \x01(\x0e2>.apollo.canbus.Throttle_command_110.Throttle_pedal_en_ctrlType\x12\x1a\n\x12throttle_pedal_cmd\x18\x02 \x01(\x05"c\n\x1aThrottle_pedal_en_ctrlType\x12"\n\x1eTHROTTLE_PEDAL_EN_CTRL_DISABLE\x10\x00\x12!\n\x1dTHROTTLE_PEDAL_EN_CTRL_ENABLE\x10\x01"\xdf\x01\n\x11Brake_command_111\x12U\n\x13brake_pedal_en_ctrl\x18\x01 \x01(\x0e28.apollo.canbus.Brake_command_111.Brake_pedal_en_ctrlType\x12\x17\n\x0fbrake_pedal_cmd\x18\x02 \x01(\x05"Z\n\x17Brake_pedal_en_ctrlType\x12\x1f\n\x1bBRAKE_PEDAL_EN_CTRL_DISABLE\x10\x00\x12\x1e\n\x1aBRAKE_PEDAL_EN_CTRL_ENABLE\x10\x01"\xdf\x01\n\x11Steer_command_112\x12U\n\x13steer_angle_en_ctrl\x18\x01 \x01(\x0e28.apollo.canbus.Steer_command_112.Steer_angle_en_ctrlType\x12\x17\n\x0fsteer_angle_cmd\x18\x02 \x01(\x01"Z\n\x17Steer_angle_en_ctrlType\x12\x1f\n\x1bSTEER_ANGLE_EN_CTRL_DISABLE\x10\x00\x12\x1e\n\x1aSTEER_ANGLE_EN_CTRL_ENABLE\x10\x01"\xd2\x01\n\x16Turnsignal_command_113\x12R\n\x0fturn_signal_cmd\x18\x01 \x01(\x0e29.apollo.canbus.Turnsignal_command_113.Turn_signal_cmdType"d\n\x13Turn_signal_cmdType\x12\x18\n\x14TURN_SIGNAL_CMD_NONE\x10\x00\x12\x18\n\x14TURN_SIGNAL_CMD_LEFT\x10\x01\x12\x19\n\x15TURN_SIGNAL_CMD_RIGHT\x10\x02"\xb5\x01\n\x10Gear_command_114\x12>\n\x08gear_cmd\x18\x01 \x01(\x0e2,.apollo.canbus.Gear_command_114.Gear_cmdType"a\n\x0cGear_cmdType\x12\x11\n\rGEAR_CMD_PARK\x10\x01\x12\x14\n\x10GEAR_CMD_REVERSE\x10\x02\x12\x14\n\x10GEAR_CMD_NEUTRAL\x10\x03\x12\x12\n\x0eGEAR_CMD_DRIVE\x10\x04"\xa1\x01\n\x13Control_command_115\x12A\n\x08ctrl_cmd\x18\x01 \x01(\x0e2/.apollo.canbus.Control_command_115.Ctrl_cmdType"G\n\x0cCtrl_cmdType\x12\x1b\n\x17CTRL_CMD_OUT_OF_CONTROL\x10\x00\x12\x1a\n\x16CTRL_CMD_UNDER_CONTROL\x10\x01"\xe3\x04\n\x14Throttle_status__510\x12\\\n\x15throttle_pedal_en_sts\x18\x01 \x01(\x0e2=.apollo.canbus.Throttle_status__510.Throttle_pedal_en_stsType\x12\x1a\n\x12throttle_pedal_sts\x18\x02 \x01(\x05\x12P\n\x0fdrive_motor_err\x18\x03 \x01(\x0e27.apollo.canbus.Throttle_status__510.Drive_motor_errType\x12P\n\x0fbattery_bms_err\x18\x04 \x01(\x0e27.apollo.canbus.Throttle_status__510.Battery_bms_errType"\x84\x01\n\x19Throttle_pedal_en_stsType\x12!\n\x1dTHROTTLE_PEDAL_EN_STS_DISABLE\x10\x00\x12 \n\x1cTHROTTLE_PEDAL_EN_STS_ENABLE\x10\x01\x12"\n\x1eTHROTTLE_PEDAL_EN_STS_TAKEOVER\x10\x02"S\n\x13Drive_motor_errType\x12\x19\n\x15DRIVE_MOTOR_ERR_NOERR\x10\x00\x12!\n\x1dDRIVE_MOTOR_ERR_DRV_MOTOR_ERR\x10\x01"Q\n\x13Battery_bms_errType\x12\x19\n\x15BATTERY_BMS_ERR_NOERR\x10\x00\x12\x1f\n\x1bBATTERY_BMS_ERR_BATTERY_ERR\x10\x01"\x87\x08\n\x11Brake_status__511\x12S\n\x12brake_pedal_en_sts\x18\x01 \x01(\x0e27.apollo.canbus.Brake_status__511.Brake_pedal_en_stsType\x12\x17\n\x0fbrake_pedal_sts\x18\x02 \x01(\x05\x12A\n\tbrake_err\x18\x03 \x01(\x0e2..apollo.canbus.Brake_status__511.Brake_errType\x12Q\n\x11emergency_btn_env\x18\x04 \x01(\x0e26.apollo.canbus.Brake_status__511.Emergency_btn_envType\x12K\n\x0efront_bump_env\x18\x05 \x01(\x0e23.apollo.canbus.Brake_status__511.Front_bump_envType\x12I\n\rback_bump_env\x18\x06 \x01(\x0e22.apollo.canbus.Brake_status__511.Back_bump_envType\x12E\n\x0boverspd_env\x18\x07 \x01(\x0e20.apollo.canbus.Brake_status__511.Overspd_envType"x\n\x16Brake_pedal_en_stsType\x12\x1e\n\x1aBRAKE_PEDAL_EN_STS_DISABLE\x10\x00\x12\x1d\n\x19BRAKE_PEDAL_EN_STS_ENABLE\x10\x01\x12\x1f\n\x1bBRAKE_PEDAL_EN_STS_TAKEOVER\x10\x02"D\n\rBrake_errType\x12\x13\n\x0fBRAKE_ERR_NOERR\x10\x00\x12\x1e\n\x1aBRAKE_ERR_BRAKE_SYSTEM_ERR\x10\x01"`\n\x15Emergency_btn_envType\x12\x1b\n\x17EMERGENCY_BTN_ENV_NOENV\x10\x00\x12*\n&EMERGENCY_BTN_ENV_EMERGENCY_BUTTON_ENV\x10\x01"S\n\x12Front_bump_envType\x12\x18\n\x14FRONT_BUMP_ENV_NOENV\x10\x00\x12#\n\x1fFRONT_BUMP_ENV_FRONT_BUMPER_ENV\x10\x01"O\n\x11Back_bump_envType\x12\x17\n\x13BACK_BUMP_ENV_NOENV\x10\x00\x12!\n\x1dBACK_BUMP_ENV_BACK_BUMPER_ENV\x10\x01"G\n\x0fOverspd_envType\x12\x15\n\x11OVERSPD_ENV_NOENV\x10\x00\x12\x1d\n\x19OVERSPD_ENV_OVERSPEED_ENV\x10\x01"\x91\x04\n\x11Steer_status__512\x12S\n\x12steer_angle_en_sts\x18\x01 \x01(\x0e27.apollo.canbus.Steer_status__512.Steer_angle_en_stsType\x12\x17\n\x0fsteer_angle_sts\x18\x02 \x01(\x01\x12A\n\tsteer_err\x18\x03 \x01(\x0e2..apollo.canbus.Steer_status__512.Steer_errType\x12C\n\nsensor_err\x18\x04 \x01(\x0e2/.apollo.canbus.Steer_status__512.Sensor_errType"x\n\x16Steer_angle_en_stsType\x12\x1e\n\x1aSTEER_ANGLE_EN_STS_DISABLE\x10\x00\x12\x1d\n\x19STEER_ANGLE_EN_STS_ENABLE\x10\x01\x12\x1f\n\x1bSTEER_ANGLE_EN_STS_TAKEOVER\x10\x02"C\n\rSteer_errType\x12\x13\n\x0fSTEER_ERR_NOERR\x10\x00\x12\x1d\n\x19STEER_ERR_STEER_MOTOR_ERR\x10\x01"G\n\x0eSensor_errType\x12\x14\n\x10SENSOR_ERR_NOERR\x10\x00\x12\x1f\n\x1bSENSOR_ERR_STEER_SENSOR_ERR\x10\x01"\xd2\x01\n\x16Turnsignal_status__513\x12R\n\x0fturn_signal_sts\x18\x01 \x01(\x0e29.apollo.canbus.Turnsignal_status__513.Turn_signal_stsType"d\n\x13Turn_signal_stsType\x12\x18\n\x14TURN_SIGNAL_STS_NONE\x10\x00\x12\x18\n\x14TURN_SIGNAL_STS_LEFT\x10\x01\x12\x19\n\x15TURN_SIGNAL_STS_RIGHT\x10\x02"\xb3\x01\n\x0fGear_status_514\x12=\n\x08gear_sts\x18\x01 \x01(\x0e2+.apollo.canbus.Gear_status_514.Gear_stsType"a\n\x0cGear_stsType\x12\x11\n\rGEAR_STS_PARK\x10\x01\x12\x14\n\x10GEAR_STS_REVERSE\x10\x02\x12\x14\n\x10GEAR_STS_NEUTRAL\x10\x03\x12\x12\n\x0eGEAR_STS_DRIVE\x10\x04"\xe7\x01\n\x10Ecu_status_1_515\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x11\n\tacc_speed\x18\x02 \x01(\x01\x12>\n\x08ctrl_sts\x18\x03 \x01(\x0e2,.apollo.canbus.Ecu_status_1_515.Ctrl_stsType\x12\x13\n\x0bchassis_sts\x18\x04 \x01(\x05\x12\x13\n\x0bchassis_err\x18\x05 \x01(\x05"G\n\x0cCtrl_stsType\x12\x1b\n\x17CTRL_STS_OUT_OF_CONTROL\x10\x00\x12\x1a\n\x16CTRL_STS_UNDER_CONTROL\x10\x01"\x90\x01\n\x10Ecu_status_2_516\x12\x13\n\x0bbattery_soc\x18\x01 \x01(\x05\x12\x18\n\x10battery_capacity\x18\x02 \x01(\x05\x12\x17\n\x0fbattery_voltage\x18\x03 \x01(\x01\x12\x17\n\x0fbattery_current\x18\x04 \x01(\x01\x12\x1b\n\x13battery_temperature\x18\x05 \x01(\x05"\xea\x01\n\x10Ecu_status_3_517\x12\x19\n\x11ultrasound_dist_1\x18\x01 \x01(\x01\x12\x19\n\x11ultrasound_dist_2\x18\x02 \x01(\x01\x12\x19\n\x11ultrasound_dist_3\x18\x03 \x01(\x01\x12\x19\n\x11ultrasound_dist_4\x18\x04 \x01(\x01\x12\x19\n\x11ultrasound_dist_5\x18\x05 \x01(\x01\x12\x19\n\x11ultrasound_dist_6\x18\x06 \x01(\x01\x12\x19\n\x11ultrasound_dist_7\x18\x07 \x01(\x01\x12\x19\n\x11ultrasound_dist_8\x18\x08 \x01(\x01"\xf2\x06\n\x02Ch\x12A\n\x14throttle_command_110\x18\x01 \x01(\x0b2#.apollo.canbus.Throttle_command_110\x12;\n\x11brake_command_111\x18\x02 \x01(\x0b2 .apollo.canbus.Brake_command_111\x12;\n\x11steer_command_112\x18\x03 \x01(\x0b2 .apollo.canbus.Steer_command_112\x12E\n\x16turnsignal_command_113\x18\x04 \x01(\x0b2%.apollo.canbus.Turnsignal_command_113\x129\n\x10gear_command_114\x18\x05 \x01(\x0b2\x1f.apollo.canbus.Gear_command_114\x12?\n\x13control_command_115\x18\x06 \x01(\x0b2".apollo.canbus.Control_command_115\x12A\n\x14throttle_status__510\x18\x07 \x01(\x0b2#.apollo.canbus.Throttle_status__510\x12;\n\x11brake_status__511\x18\x08 \x01(\x0b2 .apollo.canbus.Brake_status__511\x12;\n\x11steer_status__512\x18\t \x01(\x0b2 .apollo.canbus.Steer_status__512\x12E\n\x16turnsignal_status__513\x18\n \x01(\x0b2%.apollo.canbus.Turnsignal_status__513\x127\n\x0fgear_status_514\x18\x0b \x01(\x0b2\x1e.apollo.canbus.Gear_status_514\x129\n\x10ecu_status_1_515\x18\x0c \x01(\x0b2\x1f.apollo.canbus.Ecu_status_1_515\x129\n\x10ecu_status_2_516\x18\r \x01(\x0b2\x1f.apollo.canbus.Ecu_status_2_516\x129\n\x10ecu_status_3_517\x18\x0e \x01(\x0b2\x1f.apollo.canbus.Ecu_status_3_517')
_THROTTLE_COMMAND_110 = DESCRIPTOR.message_types_by_name['Throttle_command_110']
_BRAKE_COMMAND_111 = DESCRIPTOR.message_types_by_name['Brake_command_111']
_STEER_COMMAND_112 = DESCRIPTOR.message_types_by_name['Steer_command_112']
_TURNSIGNAL_COMMAND_113 = DESCRIPTOR.message_types_by_name['Turnsignal_command_113']
_GEAR_COMMAND_114 = DESCRIPTOR.message_types_by_name['Gear_command_114']
_CONTROL_COMMAND_115 = DESCRIPTOR.message_types_by_name['Control_command_115']
_THROTTLE_STATUS__510 = DESCRIPTOR.message_types_by_name['Throttle_status__510']
_BRAKE_STATUS__511 = DESCRIPTOR.message_types_by_name['Brake_status__511']
_STEER_STATUS__512 = DESCRIPTOR.message_types_by_name['Steer_status__512']
_TURNSIGNAL_STATUS__513 = DESCRIPTOR.message_types_by_name['Turnsignal_status__513']
_GEAR_STATUS_514 = DESCRIPTOR.message_types_by_name['Gear_status_514']
_ECU_STATUS_1_515 = DESCRIPTOR.message_types_by_name['Ecu_status_1_515']
_ECU_STATUS_2_516 = DESCRIPTOR.message_types_by_name['Ecu_status_2_516']
_ECU_STATUS_3_517 = DESCRIPTOR.message_types_by_name['Ecu_status_3_517']
_CH = DESCRIPTOR.message_types_by_name['Ch']
_THROTTLE_COMMAND_110_THROTTLE_PEDAL_EN_CTRLTYPE = _THROTTLE_COMMAND_110.enum_types_by_name['Throttle_pedal_en_ctrlType']
_BRAKE_COMMAND_111_BRAKE_PEDAL_EN_CTRLTYPE = _BRAKE_COMMAND_111.enum_types_by_name['Brake_pedal_en_ctrlType']
_STEER_COMMAND_112_STEER_ANGLE_EN_CTRLTYPE = _STEER_COMMAND_112.enum_types_by_name['Steer_angle_en_ctrlType']
_TURNSIGNAL_COMMAND_113_TURN_SIGNAL_CMDTYPE = _TURNSIGNAL_COMMAND_113.enum_types_by_name['Turn_signal_cmdType']
_GEAR_COMMAND_114_GEAR_CMDTYPE = _GEAR_COMMAND_114.enum_types_by_name['Gear_cmdType']
_CONTROL_COMMAND_115_CTRL_CMDTYPE = _CONTROL_COMMAND_115.enum_types_by_name['Ctrl_cmdType']
_THROTTLE_STATUS__510_THROTTLE_PEDAL_EN_STSTYPE = _THROTTLE_STATUS__510.enum_types_by_name['Throttle_pedal_en_stsType']
_THROTTLE_STATUS__510_DRIVE_MOTOR_ERRTYPE = _THROTTLE_STATUS__510.enum_types_by_name['Drive_motor_errType']
_THROTTLE_STATUS__510_BATTERY_BMS_ERRTYPE = _THROTTLE_STATUS__510.enum_types_by_name['Battery_bms_errType']
_BRAKE_STATUS__511_BRAKE_PEDAL_EN_STSTYPE = _BRAKE_STATUS__511.enum_types_by_name['Brake_pedal_en_stsType']
_BRAKE_STATUS__511_BRAKE_ERRTYPE = _BRAKE_STATUS__511.enum_types_by_name['Brake_errType']
_BRAKE_STATUS__511_EMERGENCY_BTN_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Emergency_btn_envType']
_BRAKE_STATUS__511_FRONT_BUMP_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Front_bump_envType']
_BRAKE_STATUS__511_BACK_BUMP_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Back_bump_envType']
_BRAKE_STATUS__511_OVERSPD_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Overspd_envType']
_STEER_STATUS__512_STEER_ANGLE_EN_STSTYPE = _STEER_STATUS__512.enum_types_by_name['Steer_angle_en_stsType']
_STEER_STATUS__512_STEER_ERRTYPE = _STEER_STATUS__512.enum_types_by_name['Steer_errType']
_STEER_STATUS__512_SENSOR_ERRTYPE = _STEER_STATUS__512.enum_types_by_name['Sensor_errType']
_TURNSIGNAL_STATUS__513_TURN_SIGNAL_STSTYPE = _TURNSIGNAL_STATUS__513.enum_types_by_name['Turn_signal_stsType']
_GEAR_STATUS_514_GEAR_STSTYPE = _GEAR_STATUS_514.enum_types_by_name['Gear_stsType']
_ECU_STATUS_1_515_CTRL_STSTYPE = _ECU_STATUS_1_515.enum_types_by_name['Ctrl_stsType']
Throttle_command_110 = _reflection.GeneratedProtocolMessageType('Throttle_command_110', (_message.Message,), {'DESCRIPTOR': _THROTTLE_COMMAND_110, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Throttle_command_110)
Brake_command_111 = _reflection.GeneratedProtocolMessageType('Brake_command_111', (_message.Message,), {'DESCRIPTOR': _BRAKE_COMMAND_111, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Brake_command_111)
Steer_command_112 = _reflection.GeneratedProtocolMessageType('Steer_command_112', (_message.Message,), {'DESCRIPTOR': _STEER_COMMAND_112, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Steer_command_112)
Turnsignal_command_113 = _reflection.GeneratedProtocolMessageType('Turnsignal_command_113', (_message.Message,), {'DESCRIPTOR': _TURNSIGNAL_COMMAND_113, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Turnsignal_command_113)
Gear_command_114 = _reflection.GeneratedProtocolMessageType('Gear_command_114', (_message.Message,), {'DESCRIPTOR': _GEAR_COMMAND_114, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Gear_command_114)
Control_command_115 = _reflection.GeneratedProtocolMessageType('Control_command_115', (_message.Message,), {'DESCRIPTOR': _CONTROL_COMMAND_115, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Control_command_115)
Throttle_status__510 = _reflection.GeneratedProtocolMessageType('Throttle_status__510', (_message.Message,), {'DESCRIPTOR': _THROTTLE_STATUS__510, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Throttle_status__510)
Brake_status__511 = _reflection.GeneratedProtocolMessageType('Brake_status__511', (_message.Message,), {'DESCRIPTOR': _BRAKE_STATUS__511, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Brake_status__511)
Steer_status__512 = _reflection.GeneratedProtocolMessageType('Steer_status__512', (_message.Message,), {'DESCRIPTOR': _STEER_STATUS__512, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Steer_status__512)
Turnsignal_status__513 = _reflection.GeneratedProtocolMessageType('Turnsignal_status__513', (_message.Message,), {'DESCRIPTOR': _TURNSIGNAL_STATUS__513, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Turnsignal_status__513)
Gear_status_514 = _reflection.GeneratedProtocolMessageType('Gear_status_514', (_message.Message,), {'DESCRIPTOR': _GEAR_STATUS_514, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Gear_status_514)
Ecu_status_1_515 = _reflection.GeneratedProtocolMessageType('Ecu_status_1_515', (_message.Message,), {'DESCRIPTOR': _ECU_STATUS_1_515, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Ecu_status_1_515)
Ecu_status_2_516 = _reflection.GeneratedProtocolMessageType('Ecu_status_2_516', (_message.Message,), {'DESCRIPTOR': _ECU_STATUS_2_516, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Ecu_status_2_516)
Ecu_status_3_517 = _reflection.GeneratedProtocolMessageType('Ecu_status_3_517', (_message.Message,), {'DESCRIPTOR': _ECU_STATUS_3_517, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Ecu_status_3_517)
Ch = _reflection.GeneratedProtocolMessageType('Ch', (_message.Message,), {'DESCRIPTOR': _CH, '__module__': 'modules.canbus.proto.ch_pb2'})
_sym_db.RegisterMessage(Ch)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _THROTTLE_COMMAND_110._serialized_start = 49
    _THROTTLE_COMMAND_110._serialized_end = 296
    _THROTTLE_COMMAND_110_THROTTLE_PEDAL_EN_CTRLTYPE._serialized_start = 197
    _THROTTLE_COMMAND_110_THROTTLE_PEDAL_EN_CTRLTYPE._serialized_end = 296
    _BRAKE_COMMAND_111._serialized_start = 299
    _BRAKE_COMMAND_111._serialized_end = 522
    _BRAKE_COMMAND_111_BRAKE_PEDAL_EN_CTRLTYPE._serialized_start = 432
    _BRAKE_COMMAND_111_BRAKE_PEDAL_EN_CTRLTYPE._serialized_end = 522
    _STEER_COMMAND_112._serialized_start = 525
    _STEER_COMMAND_112._serialized_end = 748
    _STEER_COMMAND_112_STEER_ANGLE_EN_CTRLTYPE._serialized_start = 658
    _STEER_COMMAND_112_STEER_ANGLE_EN_CTRLTYPE._serialized_end = 748
    _TURNSIGNAL_COMMAND_113._serialized_start = 751
    _TURNSIGNAL_COMMAND_113._serialized_end = 961
    _TURNSIGNAL_COMMAND_113_TURN_SIGNAL_CMDTYPE._serialized_start = 861
    _TURNSIGNAL_COMMAND_113_TURN_SIGNAL_CMDTYPE._serialized_end = 961
    _GEAR_COMMAND_114._serialized_start = 964
    _GEAR_COMMAND_114._serialized_end = 1145
    _GEAR_COMMAND_114_GEAR_CMDTYPE._serialized_start = 1048
    _GEAR_COMMAND_114_GEAR_CMDTYPE._serialized_end = 1145
    _CONTROL_COMMAND_115._serialized_start = 1148
    _CONTROL_COMMAND_115._serialized_end = 1309
    _CONTROL_COMMAND_115_CTRL_CMDTYPE._serialized_start = 1238
    _CONTROL_COMMAND_115_CTRL_CMDTYPE._serialized_end = 1309
    _THROTTLE_STATUS__510._serialized_start = 1312
    _THROTTLE_STATUS__510._serialized_end = 1923
    _THROTTLE_STATUS__510_THROTTLE_PEDAL_EN_STSTYPE._serialized_start = 1623
    _THROTTLE_STATUS__510_THROTTLE_PEDAL_EN_STSTYPE._serialized_end = 1755
    _THROTTLE_STATUS__510_DRIVE_MOTOR_ERRTYPE._serialized_start = 1757
    _THROTTLE_STATUS__510_DRIVE_MOTOR_ERRTYPE._serialized_end = 1840
    _THROTTLE_STATUS__510_BATTERY_BMS_ERRTYPE._serialized_start = 1842
    _THROTTLE_STATUS__510_BATTERY_BMS_ERRTYPE._serialized_end = 1923
    _BRAKE_STATUS__511._serialized_start = 1926
    _BRAKE_STATUS__511._serialized_end = 2957
    _BRAKE_STATUS__511_BRAKE_PEDAL_EN_STSTYPE._serialized_start = 2430
    _BRAKE_STATUS__511_BRAKE_PEDAL_EN_STSTYPE._serialized_end = 2550
    _BRAKE_STATUS__511_BRAKE_ERRTYPE._serialized_start = 2552
    _BRAKE_STATUS__511_BRAKE_ERRTYPE._serialized_end = 2620
    _BRAKE_STATUS__511_EMERGENCY_BTN_ENVTYPE._serialized_start = 2622
    _BRAKE_STATUS__511_EMERGENCY_BTN_ENVTYPE._serialized_end = 2718
    _BRAKE_STATUS__511_FRONT_BUMP_ENVTYPE._serialized_start = 2720
    _BRAKE_STATUS__511_FRONT_BUMP_ENVTYPE._serialized_end = 2803
    _BRAKE_STATUS__511_BACK_BUMP_ENVTYPE._serialized_start = 2805
    _BRAKE_STATUS__511_BACK_BUMP_ENVTYPE._serialized_end = 2884
    _BRAKE_STATUS__511_OVERSPD_ENVTYPE._serialized_start = 2886
    _BRAKE_STATUS__511_OVERSPD_ENVTYPE._serialized_end = 2957
    _STEER_STATUS__512._serialized_start = 2960
    _STEER_STATUS__512._serialized_end = 3489
    _STEER_STATUS__512_STEER_ANGLE_EN_STSTYPE._serialized_start = 3227
    _STEER_STATUS__512_STEER_ANGLE_EN_STSTYPE._serialized_end = 3347
    _STEER_STATUS__512_STEER_ERRTYPE._serialized_start = 3349
    _STEER_STATUS__512_STEER_ERRTYPE._serialized_end = 3416
    _STEER_STATUS__512_SENSOR_ERRTYPE._serialized_start = 3418
    _STEER_STATUS__512_SENSOR_ERRTYPE._serialized_end = 3489
    _TURNSIGNAL_STATUS__513._serialized_start = 3492
    _TURNSIGNAL_STATUS__513._serialized_end = 3702
    _TURNSIGNAL_STATUS__513_TURN_SIGNAL_STSTYPE._serialized_start = 3602
    _TURNSIGNAL_STATUS__513_TURN_SIGNAL_STSTYPE._serialized_end = 3702
    _GEAR_STATUS_514._serialized_start = 3705
    _GEAR_STATUS_514._serialized_end = 3884
    _GEAR_STATUS_514_GEAR_STSTYPE._serialized_start = 3787
    _GEAR_STATUS_514_GEAR_STSTYPE._serialized_end = 3884
    _ECU_STATUS_1_515._serialized_start = 3887
    _ECU_STATUS_1_515._serialized_end = 4118
    _ECU_STATUS_1_515_CTRL_STSTYPE._serialized_start = 4047
    _ECU_STATUS_1_515_CTRL_STSTYPE._serialized_end = 4118
    _ECU_STATUS_2_516._serialized_start = 4121
    _ECU_STATUS_2_516._serialized_end = 4265
    _ECU_STATUS_3_517._serialized_start = 4268
    _ECU_STATUS_3_517._serialized_end = 4502
    _CH._serialized_start = 4505
    _CH._serialized_end = 5387