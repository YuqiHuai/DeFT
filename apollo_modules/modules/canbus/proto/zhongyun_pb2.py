"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/canbus/proto/zhongyun.proto\x12\rapollo.canbus"\xc5\x03\n\x0fGear_control_a1\x12O\n\x11gear_state_target\x18\x01 \x01(\x0e24.apollo.canbus.Gear_control_a1.Gear_state_targetType\x12S\n\x13gear_enable_control\x18\x02 \x01(\x0e26.apollo.canbus.Gear_control_a1.Gear_enable_controlType"\x9a\x01\n\x15Gear_state_targetType\x12\x17\n\x13GEAR_STATE_TARGET_P\x10\x01\x12\x17\n\x13GEAR_STATE_TARGET_N\x10\x02\x12\x17\n\x13GEAR_STATE_TARGET_D\x10\x03\x12\x17\n\x13GEAR_STATE_TARGET_R\x10\x04\x12\x1d\n\x19GEAR_STATE_TARGET_INVALID\x10\x05"o\n\x17Gear_enable_controlType\x12*\n&GEAR_ENABLE_CONTROL_GEAR_MANUALCONTROL\x10\x00\x12(\n$GEAR_ENABLE_CONTROL_GEAR_AUTOCONTROL\x10\x01"\xf0\x01\n\x11Torque_control_a3\x12\x15\n\rdriven_torque\x18\x01 \x01(\x01\x12Y\n\x15driven_enable_control\x18\x02 \x01(\x0e2:.apollo.canbus.Torque_control_a3.Driven_enable_controlType"i\n\x19Driven_enable_controlType\x12&\n"DRIVEN_ENABLE_CONTROL_DRIVE_MANUAL\x10\x00\x12$\n DRIVEN_ENABLE_CONTROL_DRIVE_AUTO\x10\x01"\x95\x02\n\x13Steering_control_a2\x12\x17\n\x0fsteering_target\x18\x01 \x01(\x01\x12_\n\x17steering_enable_control\x18\x02 \x01(\x0e2>.apollo.canbus.Steering_control_a2.Steering_enable_controlType"\x83\x01\n\x1bSteering_enable_controlType\x122\n.STEERING_ENABLE_CONTROL_STEERING_MANUALCONTROL\x10\x00\x120\n,STEERING_ENABLE_CONTROL_STEERING_AUTOCONTROL\x10\x01"\x96\x03\n\x12Parking_control_a5\x12L\n\x0eparking_target\x18\x01 \x01(\x0e24.apollo.canbus.Parking_control_a5.Parking_targetType\x12\\\n\x16parking_enable_control\x18\x02 \x01(\x0e2<.apollo.canbus.Parking_control_a5.Parking_enable_controlType"T\n\x12Parking_targetType\x12\x1a\n\x16PARKING_TARGET_RELEASE\x10\x00\x12"\n\x1ePARKING_TARGET_PARKING_TRIGGER\x10\x01"~\n\x1aParking_enable_controlType\x120\n,PARKING_ENABLE_CONTROL_PARKING_MANUALCONTROL\x10\x00\x12.\n*PARKING_ENABLE_CONTROL_PARKING_AUTOCONTROL\x10\x01"\xe8\x01\n\x10Brake_control_a4\x12\x14\n\x0cbrake_torque\x18\x01 \x01(\x01\x12V\n\x14brake_enable_control\x18\x02 \x01(\x0e28.apollo.canbus.Brake_control_a4.Brake_enable_controlType"f\n\x18Brake_enable_controlType\x12%\n!BRAKE_ENABLE_CONTROL_BRAKE_MANUAL\x10\x00\x12#\n\x1fBRAKE_ENABLE_CONTROL_BRAKE_AUTO\x10\x01"\x80\n\n\x18Enable_state_feedback_c3\x12^\n\x14parking_enable_state\x18\x01 \x01(\x0e2@.apollo.canbus.Enable_state_feedback_c3.Parking_enable_stateType\x12`\n\x15steering_enable_state\x18\x02 \x01(\x0e2A.apollo.canbus.Enable_state_feedback_c3.Steering_enable_stateType\x12Z\n\x12gear_enable_actual\x18\x03 \x01(\x0e2>.apollo.canbus.Enable_state_feedback_c3.Gear_enable_actualType\x12\\\n\x13driven_enable_state\x18\x04 \x01(\x0e2?.apollo.canbus.Enable_state_feedback_c3.Driven_enable_stateType\x12Z\n\x12brake_enable_state\x18\x05 \x01(\x0e2>.apollo.canbus.Enable_state_feedback_c3.Brake_enable_stateType"\xa3\x01\n\x18Parking_enable_stateType\x12.\n*PARKING_ENABLE_STATE_PARKING_MANUALCONTROL\x10\x00\x12,\n(PARKING_ENABLE_STATE_PARKING_AUTOCONTROL\x10\x01\x12)\n%PARKING_ENABLE_STATE_PARKING_TAKEOVER\x10\x02"\xb1\x01\n\x19Steering_enable_stateType\x120\n,STEERING_ENABLE_STATE_STEERING_MANUALCONTROL\x10\x00\x12.\n*STEERING_ENABLE_STATE_STEERING_AUTOCONTROL\x10\x01\x122\n.STEERING_ENABLE_STATE_STEERING_MANUAL_TAKEOVER\x10\x02"\x99\x01\n\x16Gear_enable_actualType\x12)\n%GEAR_ENABLE_ACTUAL_GEAR_MANUALCONTROL\x10\x00\x12\'\n#GEAR_ENABLE_ACTUAL_GEAR_AUTOCONTROL\x10\x01\x12+\n\'GEAR_ENABLE_ACTUAL_GEAR_MANUAL_TAKEOVER\x10\x02"\x8b\x01\n\x17Driven_enable_stateType\x12$\n DRIVEN_ENABLE_STATE_DRIVE_MANUAL\x10\x00\x12"\n\x1eDRIVEN_ENABLE_STATE_DRIVE_AUTO\x10\x01\x12&\n"DRIVEN_ENABLE_STATE_DRIVE_TAKEOVER\x10\x02"\x87\x01\n\x16Brake_enable_stateType\x12#\n\x1fBRAKE_ENABLE_STATE_BRAKE_MANUAL\x10\x00\x12!\n\x1dBRAKE_ENABLE_STATE_BRAKE_AUTO\x10\x01\x12%\n!BRAKE_ENABLE_STATE_BRAKE_TAKEOVER\x10\x02"\x85\x04\n\x19Vehicle_state_feedback_c1\x12S\n\x0eparking_actual\x18\x01 \x01(\x0e2;.apollo.canbus.Vehicle_state_feedback_c1.Parking_actualType\x12\x1d\n\x15brake_torque_feedback\x18\x02 \x01(\x01\x12Y\n\x11gear_state_actual\x18\x03 \x01(\x0e2>.apollo.canbus.Vehicle_state_feedback_c1.Gear_state_actualType\x12\x17\n\x0fsteering_actual\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x01"T\n\x12Parking_actualType\x12\x1a\n\x16PARKING_ACTUAL_RELEASE\x10\x00\x12"\n\x1ePARKING_ACTUAL_PARKING_TRIGGER\x10\x01"\x9a\x01\n\x15Gear_state_actualType\x12\x17\n\x13GEAR_STATE_ACTUAL_P\x10\x01\x12\x17\n\x13GEAR_STATE_ACTUAL_N\x10\x02\x12\x17\n\x13GEAR_STATE_ACTUAL_D\x10\x03\x12\x17\n\x13GEAR_STATE_ACTUAL_R\x10\x04\x12\x1d\n\x19GEAR_STATE_ACTUAL_INVALID\x10\x05"\xc9\x06\n\x0eError_state_e1\x12L\n\x10brake_error_code\x18\x01 \x01(\x0e22.apollo.canbus.Error_state_e1.Brake_error_codeType\x12N\n\x11driven_error_code\x18\x02 \x01(\x0e23.apollo.canbus.Error_state_e1.Driven_error_codeType\x12R\n\x13steering_error_code\x18\x03 \x01(\x0e25.apollo.canbus.Error_state_e1.Steering_error_codeType\x12P\n\x12parking_error_code\x18\x04 \x01(\x0e24.apollo.canbus.Error_state_e1.Parking_error_codeType\x12H\n\x0egear_error_msg\x18\x05 \x01(\x0e20.apollo.canbus.Error_state_e1.Gear_error_msgType"Q\n\x14Brake_error_codeType\x12\x1d\n\x19BRAKE_ERROR_CODE_NO_ERROR\x10\x00\x12\x1a\n\x16BRAKE_ERROR_CODE_ERROR\x10\x01"T\n\x15Driven_error_codeType\x12\x1e\n\x1aDRIVEN_ERROR_CODE_NO_ERROR\x10\x00\x12\x1b\n\x17DRIVEN_ERROR_CODE_ERROR\x10\x01"Z\n\x17Steering_error_codeType\x12 \n\x1cSTEERING_ERROR_CODE_NO_ERROR\x10\x00\x12\x1d\n\x19STEERING_ERROR_CODE_ERROR\x10\x01"W\n\x16Parking_error_codeType\x12\x1f\n\x1bPARKING_ERROR_CODE_NO_ERROR\x10\x00\x12\x1c\n\x18PARKING_ERROR_CODE_ERROR\x10\x01"K\n\x12Gear_error_msgType\x12\x1b\n\x17GEAR_ERROR_MSG_NO_ERROR\x10\x00\x12\x18\n\x14GEAR_ERROR_MSG_ERROR\x10\x01"R\n\x1bVehicle_state_feedback_2_c4\x12\x13\n\x0bmotor_speed\x18\x01 \x01(\x05\x12\x1e\n\x16driven_torque_feedback\x18\x02 \x01(\x01"\xdb\x04\n\x08Zhongyun\x127\n\x0fgear_control_a1\x18\x01 \x01(\x0b2\x1e.apollo.canbus.Gear_control_a1\x12;\n\x11torque_control_a3\x18\x02 \x01(\x0b2 .apollo.canbus.Torque_control_a3\x12?\n\x13steering_control_a2\x18\x03 \x01(\x0b2".apollo.canbus.Steering_control_a2\x12=\n\x12parking_control_a5\x18\x04 \x01(\x0b2!.apollo.canbus.Parking_control_a5\x129\n\x10brake_control_a4\x18\x05 \x01(\x0b2\x1f.apollo.canbus.Brake_control_a4\x12I\n\x18enable_state_feedback_c3\x18\x06 \x01(\x0b2\'.apollo.canbus.Enable_state_feedback_c3\x12K\n\x19vehicle_state_feedback_c1\x18\x07 \x01(\x0b2(.apollo.canbus.Vehicle_state_feedback_c1\x125\n\x0eerror_state_e1\x18\x08 \x01(\x0b2\x1d.apollo.canbus.Error_state_e1\x12O\n\x1bvehicle_state_feedback_2_c4\x18\t \x01(\x0b2*.apollo.canbus.Vehicle_state_feedback_2_c4')
_GEAR_CONTROL_A1 = DESCRIPTOR.message_types_by_name['Gear_control_a1']
_TORQUE_CONTROL_A3 = DESCRIPTOR.message_types_by_name['Torque_control_a3']
_STEERING_CONTROL_A2 = DESCRIPTOR.message_types_by_name['Steering_control_a2']
_PARKING_CONTROL_A5 = DESCRIPTOR.message_types_by_name['Parking_control_a5']
_BRAKE_CONTROL_A4 = DESCRIPTOR.message_types_by_name['Brake_control_a4']
_ENABLE_STATE_FEEDBACK_C3 = DESCRIPTOR.message_types_by_name['Enable_state_feedback_c3']
_VEHICLE_STATE_FEEDBACK_C1 = DESCRIPTOR.message_types_by_name['Vehicle_state_feedback_c1']
_ERROR_STATE_E1 = DESCRIPTOR.message_types_by_name['Error_state_e1']
_VEHICLE_STATE_FEEDBACK_2_C4 = DESCRIPTOR.message_types_by_name['Vehicle_state_feedback_2_c4']
_ZHONGYUN = DESCRIPTOR.message_types_by_name['Zhongyun']
_GEAR_CONTROL_A1_GEAR_STATE_TARGETTYPE = _GEAR_CONTROL_A1.enum_types_by_name['Gear_state_targetType']
_GEAR_CONTROL_A1_GEAR_ENABLE_CONTROLTYPE = _GEAR_CONTROL_A1.enum_types_by_name['Gear_enable_controlType']
_TORQUE_CONTROL_A3_DRIVEN_ENABLE_CONTROLTYPE = _TORQUE_CONTROL_A3.enum_types_by_name['Driven_enable_controlType']
_STEERING_CONTROL_A2_STEERING_ENABLE_CONTROLTYPE = _STEERING_CONTROL_A2.enum_types_by_name['Steering_enable_controlType']
_PARKING_CONTROL_A5_PARKING_TARGETTYPE = _PARKING_CONTROL_A5.enum_types_by_name['Parking_targetType']
_PARKING_CONTROL_A5_PARKING_ENABLE_CONTROLTYPE = _PARKING_CONTROL_A5.enum_types_by_name['Parking_enable_controlType']
_BRAKE_CONTROL_A4_BRAKE_ENABLE_CONTROLTYPE = _BRAKE_CONTROL_A4.enum_types_by_name['Brake_enable_controlType']
_ENABLE_STATE_FEEDBACK_C3_PARKING_ENABLE_STATETYPE = _ENABLE_STATE_FEEDBACK_C3.enum_types_by_name['Parking_enable_stateType']
_ENABLE_STATE_FEEDBACK_C3_STEERING_ENABLE_STATETYPE = _ENABLE_STATE_FEEDBACK_C3.enum_types_by_name['Steering_enable_stateType']
_ENABLE_STATE_FEEDBACK_C3_GEAR_ENABLE_ACTUALTYPE = _ENABLE_STATE_FEEDBACK_C3.enum_types_by_name['Gear_enable_actualType']
_ENABLE_STATE_FEEDBACK_C3_DRIVEN_ENABLE_STATETYPE = _ENABLE_STATE_FEEDBACK_C3.enum_types_by_name['Driven_enable_stateType']
_ENABLE_STATE_FEEDBACK_C3_BRAKE_ENABLE_STATETYPE = _ENABLE_STATE_FEEDBACK_C3.enum_types_by_name['Brake_enable_stateType']
_VEHICLE_STATE_FEEDBACK_C1_PARKING_ACTUALTYPE = _VEHICLE_STATE_FEEDBACK_C1.enum_types_by_name['Parking_actualType']
_VEHICLE_STATE_FEEDBACK_C1_GEAR_STATE_ACTUALTYPE = _VEHICLE_STATE_FEEDBACK_C1.enum_types_by_name['Gear_state_actualType']
_ERROR_STATE_E1_BRAKE_ERROR_CODETYPE = _ERROR_STATE_E1.enum_types_by_name['Brake_error_codeType']
_ERROR_STATE_E1_DRIVEN_ERROR_CODETYPE = _ERROR_STATE_E1.enum_types_by_name['Driven_error_codeType']
_ERROR_STATE_E1_STEERING_ERROR_CODETYPE = _ERROR_STATE_E1.enum_types_by_name['Steering_error_codeType']
_ERROR_STATE_E1_PARKING_ERROR_CODETYPE = _ERROR_STATE_E1.enum_types_by_name['Parking_error_codeType']
_ERROR_STATE_E1_GEAR_ERROR_MSGTYPE = _ERROR_STATE_E1.enum_types_by_name['Gear_error_msgType']
Gear_control_a1 = _reflection.GeneratedProtocolMessageType('Gear_control_a1', (_message.Message,), {'DESCRIPTOR': _GEAR_CONTROL_A1, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Gear_control_a1)
Torque_control_a3 = _reflection.GeneratedProtocolMessageType('Torque_control_a3', (_message.Message,), {'DESCRIPTOR': _TORQUE_CONTROL_A3, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Torque_control_a3)
Steering_control_a2 = _reflection.GeneratedProtocolMessageType('Steering_control_a2', (_message.Message,), {'DESCRIPTOR': _STEERING_CONTROL_A2, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Steering_control_a2)
Parking_control_a5 = _reflection.GeneratedProtocolMessageType('Parking_control_a5', (_message.Message,), {'DESCRIPTOR': _PARKING_CONTROL_A5, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Parking_control_a5)
Brake_control_a4 = _reflection.GeneratedProtocolMessageType('Brake_control_a4', (_message.Message,), {'DESCRIPTOR': _BRAKE_CONTROL_A4, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Brake_control_a4)
Enable_state_feedback_c3 = _reflection.GeneratedProtocolMessageType('Enable_state_feedback_c3', (_message.Message,), {'DESCRIPTOR': _ENABLE_STATE_FEEDBACK_C3, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Enable_state_feedback_c3)
Vehicle_state_feedback_c1 = _reflection.GeneratedProtocolMessageType('Vehicle_state_feedback_c1', (_message.Message,), {'DESCRIPTOR': _VEHICLE_STATE_FEEDBACK_C1, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Vehicle_state_feedback_c1)
Error_state_e1 = _reflection.GeneratedProtocolMessageType('Error_state_e1', (_message.Message,), {'DESCRIPTOR': _ERROR_STATE_E1, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Error_state_e1)
Vehicle_state_feedback_2_c4 = _reflection.GeneratedProtocolMessageType('Vehicle_state_feedback_2_c4', (_message.Message,), {'DESCRIPTOR': _VEHICLE_STATE_FEEDBACK_2_C4, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Vehicle_state_feedback_2_c4)
Zhongyun = _reflection.GeneratedProtocolMessageType('Zhongyun', (_message.Message,), {'DESCRIPTOR': _ZHONGYUN, '__module__': 'modules.canbus.proto.zhongyun_pb2'})
_sym_db.RegisterMessage(Zhongyun)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GEAR_CONTROL_A1._serialized_start = 55
    _GEAR_CONTROL_A1._serialized_end = 508
    _GEAR_CONTROL_A1_GEAR_STATE_TARGETTYPE._serialized_start = 241
    _GEAR_CONTROL_A1_GEAR_STATE_TARGETTYPE._serialized_end = 395
    _GEAR_CONTROL_A1_GEAR_ENABLE_CONTROLTYPE._serialized_start = 397
    _GEAR_CONTROL_A1_GEAR_ENABLE_CONTROLTYPE._serialized_end = 508
    _TORQUE_CONTROL_A3._serialized_start = 511
    _TORQUE_CONTROL_A3._serialized_end = 751
    _TORQUE_CONTROL_A3_DRIVEN_ENABLE_CONTROLTYPE._serialized_start = 646
    _TORQUE_CONTROL_A3_DRIVEN_ENABLE_CONTROLTYPE._serialized_end = 751
    _STEERING_CONTROL_A2._serialized_start = 754
    _STEERING_CONTROL_A2._serialized_end = 1031
    _STEERING_CONTROL_A2_STEERING_ENABLE_CONTROLTYPE._serialized_start = 900
    _STEERING_CONTROL_A2_STEERING_ENABLE_CONTROLTYPE._serialized_end = 1031
    _PARKING_CONTROL_A5._serialized_start = 1034
    _PARKING_CONTROL_A5._serialized_end = 1440
    _PARKING_CONTROL_A5_PARKING_TARGETTYPE._serialized_start = 1228
    _PARKING_CONTROL_A5_PARKING_TARGETTYPE._serialized_end = 1312
    _PARKING_CONTROL_A5_PARKING_ENABLE_CONTROLTYPE._serialized_start = 1314
    _PARKING_CONTROL_A5_PARKING_ENABLE_CONTROLTYPE._serialized_end = 1440
    _BRAKE_CONTROL_A4._serialized_start = 1443
    _BRAKE_CONTROL_A4._serialized_end = 1675
    _BRAKE_CONTROL_A4_BRAKE_ENABLE_CONTROLTYPE._serialized_start = 1573
    _BRAKE_CONTROL_A4_BRAKE_ENABLE_CONTROLTYPE._serialized_end = 1675
    _ENABLE_STATE_FEEDBACK_C3._serialized_start = 1678
    _ENABLE_STATE_FEEDBACK_C3._serialized_end = 2958
    _ENABLE_STATE_FEEDBACK_C3_PARKING_ENABLE_STATETYPE._serialized_start = 2179
    _ENABLE_STATE_FEEDBACK_C3_PARKING_ENABLE_STATETYPE._serialized_end = 2342
    _ENABLE_STATE_FEEDBACK_C3_STEERING_ENABLE_STATETYPE._serialized_start = 2345
    _ENABLE_STATE_FEEDBACK_C3_STEERING_ENABLE_STATETYPE._serialized_end = 2522
    _ENABLE_STATE_FEEDBACK_C3_GEAR_ENABLE_ACTUALTYPE._serialized_start = 2525
    _ENABLE_STATE_FEEDBACK_C3_GEAR_ENABLE_ACTUALTYPE._serialized_end = 2678
    _ENABLE_STATE_FEEDBACK_C3_DRIVEN_ENABLE_STATETYPE._serialized_start = 2681
    _ENABLE_STATE_FEEDBACK_C3_DRIVEN_ENABLE_STATETYPE._serialized_end = 2820
    _ENABLE_STATE_FEEDBACK_C3_BRAKE_ENABLE_STATETYPE._serialized_start = 2823
    _ENABLE_STATE_FEEDBACK_C3_BRAKE_ENABLE_STATETYPE._serialized_end = 2958
    _VEHICLE_STATE_FEEDBACK_C1._serialized_start = 2961
    _VEHICLE_STATE_FEEDBACK_C1._serialized_end = 3478
    _VEHICLE_STATE_FEEDBACK_C1_PARKING_ACTUALTYPE._serialized_start = 3237
    _VEHICLE_STATE_FEEDBACK_C1_PARKING_ACTUALTYPE._serialized_end = 3321
    _VEHICLE_STATE_FEEDBACK_C1_GEAR_STATE_ACTUALTYPE._serialized_start = 3324
    _VEHICLE_STATE_FEEDBACK_C1_GEAR_STATE_ACTUALTYPE._serialized_end = 3478
    _ERROR_STATE_E1._serialized_start = 3481
    _ERROR_STATE_E1._serialized_end = 4322
    _ERROR_STATE_E1_BRAKE_ERROR_CODETYPE._serialized_start = 3897
    _ERROR_STATE_E1_BRAKE_ERROR_CODETYPE._serialized_end = 3978
    _ERROR_STATE_E1_DRIVEN_ERROR_CODETYPE._serialized_start = 3980
    _ERROR_STATE_E1_DRIVEN_ERROR_CODETYPE._serialized_end = 4064
    _ERROR_STATE_E1_STEERING_ERROR_CODETYPE._serialized_start = 4066
    _ERROR_STATE_E1_STEERING_ERROR_CODETYPE._serialized_end = 4156
    _ERROR_STATE_E1_PARKING_ERROR_CODETYPE._serialized_start = 4158
    _ERROR_STATE_E1_PARKING_ERROR_CODETYPE._serialized_end = 4245
    _ERROR_STATE_E1_GEAR_ERROR_MSGTYPE._serialized_start = 4247
    _ERROR_STATE_E1_GEAR_ERROR_MSGTYPE._serialized_end = 4322
    _VEHICLE_STATE_FEEDBACK_2_C4._serialized_start = 4324
    _VEHICLE_STATE_FEEDBACK_2_C4._serialized_end = 4406
    _ZHONGYUN._serialized_start = 4409
    _ZHONGYUN._serialized_end = 5012