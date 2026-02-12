"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"modules/canbus/proto/transit.proto\x12\rapollo.canbus"Y\n\x14Llc_vehiclelimits_24\x12 \n\x18llc_fbk_maxsteeringangle\x18\x01 \x01(\x05\x12\x1f\n\x17llc_fbk_maxbrakepercent\x18\x02 \x01(\x01"\x99\x0b\n\x15Adc_motioncontrol1_10\x12\x1f\n\x17adc_cmd_steerwheelangle\x18\x01 \x01(\x01\x12i\n\x1badc_cmd_steeringcontrolmode\x18\x02 \x01(\x0e2D.apollo.canbus.Adc_motioncontrol1_10.Adc_cmd_steeringcontrolmodeType\x12\x1c\n\x14adc_cmd_parkingbrake\x18\x03 \x01(\x08\x12K\n\x0cadc_cmd_gear\x18\x04 \x01(\x0e25.apollo.canbus.Adc_motioncontrol1_10.Adc_cmd_gearType\x12#\n\x1badc_motioncontrol1_checksum\x18\x05 \x01(\x05\x12\x1f\n\x17adc_cmd_brakepercentage\x18\x06 \x01(\x01\x12 \n\x18adc_cmd_throttleposition\x18\x07 \x01(\x01\x12"\n\x1aadc_motioncontrol1_counter\x18\x08 \x01(\x05\x12a\n\x17adc_cmd_autonomyrequest\x18\t \x01(\x0e2@.apollo.canbus.Adc_motioncontrol1_10.Adc_cmd_autonomyrequestType\x12q\n\x1fadc_cmd_longitudinalcontrolmode\x18\n \x01(\x0e2H.apollo.canbus.Adc_motioncontrol1_10.Adc_cmd_longitudinalcontrolmodeType"\xcc\x01\n\x1fAdc_cmd_steeringcontrolmodeType\x12$\n ADC_CMD_STEERINGCONTROLMODE_NONE\x10\x00\x12%\n!ADC_CMD_STEERINGCONTROLMODE_ANGLE\x10\x01\x122\n.ADC_CMD_STEERINGCONTROLMODE_RESERVED_CURVATURE\x10\x02\x12(\n$ADC_CMD_STEERINGCONTROLMODE_RESERVED\x10\x03"}\n\x10Adc_cmd_gearType\x12\x17\n\x13ADC_CMD_GEAR_P_PARK\x10\x00\x12\x18\n\x14ADC_CMD_GEAR_D_DRIVE\x10\x01\x12\x1a\n\x16ADC_CMD_GEAR_N_NEUTRAL\x10\x02\x12\x1a\n\x16ADC_CMD_GEAR_R_REVERSE\x10\x03"\xcf\x01\n\x1bAdc_cmd_autonomyrequestType\x122\n.ADC_CMD_AUTONOMYREQUEST_AUTONOMY_NOT_REQUESTED\x10\x00\x12.\n*ADC_CMD_AUTONOMYREQUEST_AUTONOMY_REQUESTED\x10\x01\x12%\n!ADC_CMD_AUTONOMYREQUEST_RESERVED0\x10\x02\x12%\n!ADC_CMD_AUTONOMYREQUEST_RESERVED1\x10\x03"\x86\x02\n#Adc_cmd_longitudinalcontrolmodeType\x12(\n$ADC_CMD_LONGITUDINALCONTROLMODE_NONE\x10\x00\x12F\nBADC_CMD_LONGITUDINALCONTROLMODE_RESERVED_VELOCITY_AND_ACCELERATION\x10\x01\x122\n.ADC_CMD_LONGITUDINALCONTROLMODE_RESERVED_FORCE\x10\x02\x129\n5ADC_CMD_LONGITUDINALCONTROLMODE_DIRECT_THROTTLE_BRAKE\x10\x03"\x87\x01\n\x1bAdc_motioncontrollimits1_12\x12$\n\x1cadc_cmd_throttlecommandlimit\x18\x01 \x01(\x01\x12\x1c\n\x14adc_cmd_steeringrate\x18\x02 \x01(\x01\x12$\n\x1cadc_cmd_steerwheelanglelimit\x18\x03 \x01(\x01"\xc5\x0e\n\x16Llc_motionfeedback1_20\x12L\n\x0cllc_fbk_gear\x18\x01 \x01(\x0e26.apollo.canbus.Llc_motionfeedback1_20.Llc_fbk_gearType\x12\x1c\n\x14llc_fbk_parkingbrake\x18\x02 \x01(\x08\x12 \n\x18llc_fbk_throttleposition\x18\x03 \x01(\x01\x12 \n\x18llc_fbk_brakepercentrear\x18\x04 \x01(\x01\x12!\n\x19llc_fbk_brakepercentfront\x18\x05 \x01(\x01\x12j\n\x1bllc_fbk_steeringcontrolmode\x18\x06 \x01(\x0e2E.apollo.canbus.Llc_motionfeedback1_20.Llc_fbk_steeringcontrolmodeType\x12#\n\x1bllc_motionfeedback1_counter\x18\x07 \x01(\x05\x12$\n\x1cllc_motionfeedback1_checksum\x18\x08 \x01(\x05\x12\x1e\n\x16llc_fbk_commandaligned\x18\t \x01(\x08\x12\x1c\n\x14llc_fbk_estoppressed\x18\n \x01(\x08\x12"\n\x1allc_fbk_adcrequestautonomy\x18\x0b \x01(\x08\x12\x1d\n\x15llc_fbk_allowautonomy\x18\x0c \x01(\x08\x12r\n\x1fllc_fbk_longitudinalcontrolmode\x18\r \x01(\x0e2I.apollo.canbus.Llc_motionfeedback1_20.Llc_fbk_longitudinalcontrolmodeType\x12N\n\rllc_fbk_state\x18\x0e \x01(\x0e27.apollo.canbus.Llc_motionfeedback1_20.Llc_fbk_stateType"}\n\x10Llc_fbk_gearType\x12\x17\n\x13LLC_FBK_GEAR_P_PARK\x10\x00\x12\x18\n\x14LLC_FBK_GEAR_D_DRIVE\x10\x01\x12\x1a\n\x16LLC_FBK_GEAR_N_NEUTRAL\x10\x02\x12\x1a\n\x16LLC_FBK_GEAR_R_REVERSE\x10\x03"\xcc\x01\n\x1fLlc_fbk_steeringcontrolmodeType\x12$\n LLC_FBK_STEERINGCONTROLMODE_NONE\x10\x00\x12%\n!LLC_FBK_STEERINGCONTROLMODE_ANGLE\x10\x01\x122\n.LLC_FBK_STEERINGCONTROLMODE_RESERVED_CURVATURE\x10\x02\x12(\n$LLC_FBK_STEERINGCONTROLMODE_RESERVED\x10\x03"\x86\x02\n#Llc_fbk_longitudinalcontrolmodeType\x12(\n$LLC_FBK_LONGITUDINALCONTROLMODE_NONE\x10\x00\x12F\nBLLC_FBK_LONGITUDINALCONTROLMODE_RESERVED_VELOCITY_AND_ACCELERATION\x10\x01\x122\n.LLC_FBK_LONGITUDINALCONTROLMODE_RESERVED_FORCE\x10\x02\x129\n5LLC_FBK_LONGITUDINALCONTROLMODE_DIRECT_THROTTLE_BRAKE\x10\x03"\x84\x04\n\x11Llc_fbk_stateType\x12\x1b\n\x17LLC_FBK_STATE_RESERVED0\x10\x00\x12&\n"LLC_FBK_STATE_AUTONOMY_NOT_ALLOWED\x10\x01\x12"\n\x1eLLC_FBK_STATE_AUTONOMY_ALLOWED\x10\x02\x12$\n LLC_FBK_STATE_AUTONOMY_REQUESTED\x10\x03\x12\x1a\n\x16LLC_FBK_STATE_AUTONOMY\x10\x04\x12\x1b\n\x17LLC_FBK_STATE_RESERVED1\x10\x05\x12\x1b\n\x17LLC_FBK_STATE_RESERVED2\x10\x06\x12\x1b\n\x17LLC_FBK_STATE_RESERVED3\x10\x07\x12\x1b\n\x17LLC_FBK_STATE_RESERVED4\x10\x08\x12\x1b\n\x17LLC_FBK_STATE_RESERVED5\x10\t\x12\x1b\n\x17LLC_FBK_STATE_RESERVED6\x10\n\x12\x1b\n\x17LLC_FBK_STATE_RESERVED7\x10\x0b\x12\x1b\n\x17LLC_FBK_STATE_RESERVED8\x10\x0c\x12%\n!LLC_FBK_STATE_DISENGAGE_REQUESTED\x10\r\x12\x1c\n\x18LLC_FBK_STATE_DISENGAGED\x10\x0e\x12\x17\n\x13LLC_FBK_STATE_FAULT\x10\x0f"\xbe\x01\n\x16Llc_motionfeedback2_21\x12\x1c\n\x14llc_fbk_vehiclespeed\x18\x01 \x01(\x01\x12#\n\x1bllc_motionfeedback2_counter\x18\x02 \x01(\x05\x12$\n\x1cllc_motionfeedback2_checksum\x18\x03 \x01(\x05\x12\x1c\n\x14llc_fbk_steeringrate\x18\x04 \x01(\x01\x12\x1d\n\x15llc_fbk_steeringangle\x18\x05 \x01(\x01"\xe2\x01\n\x1dLlc_motioncommandfeedback1_22\x12%\n\x1dllc_fbk_steeringanglesetpoint\x18\x01 \x01(\x01\x12 \n\x18llc_fbk_throttlesetpoint\x18\x02 \x01(\x01\x12$\n\x1cllc_fbk_brakepercentsetpoint\x18\x03 \x01(\x01\x12(\n llc_motioncommandfeedback1_count\x18\x04 \x01(\x05\x12(\n llc_motioncommandfeedback1_check\x18\x05 \x01(\x05"1\n\x14Llc_vehiclestatus_25\x12\x19\n\x11llc_fbk_12voltage\x18\x01 \x01(\x01"\xcb\x05\n\x19Llc_auxiliaryfeedback_120\x12\x18\n\x10llc_fbk_inverter\x18\x01 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch8\x18\x02 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch7\x18\x03 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch6\x18\x04 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch5\x18\x05 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch4\x18\x06 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch3\x18\x07 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch2\x18\x08 \x01(\x08\x12\x17\n\x0fllc_fbk_pdu_ch1\x18\t \x01(\x08\x12\x1c\n\x14llc_fbk_hazardlights\x18\n \x01(\x08\x12\x1a\n\x12llc_fbk_ledgreenon\x18\x0b \x01(\x08\x12\x14\n\x0cllc_fbk_horn\x18\x0c \x01(\x08\x12\x18\n\x10llc_fbk_buzzeron\x18\r \x01(\x08\x12[\n\x12llc_fbk_turnsignal\x18\x0e \x01(\x0e2?.apollo.canbus.Llc_auxiliaryfeedback_120.Llc_fbk_turnsignalType\x12\x17\n\x0fllc_fbk_lowbeam\x18\x0f \x01(\x08\x12\x18\n\x10llc_fbk_highbeam\x18\x10 \x01(\x08\x12\x18\n\x10llc_fbk_ledredon\x18\x11 \x01(\x08\x12%\n\x1dllc_fbk_autonomybuttonpressed\x18\x12 \x01(\x08"\x90\x01\n\x16Llc_fbk_turnsignalType\x12\x1b\n\x17LLC_FBK_TURNSIGNAL_NONE\x10\x00\x12\x1b\n\x17LLC_FBK_TURNSIGNAL_LEFT\x10\x01\x12\x1c\n\x18LLC_FBK_TURNSIGNAL_RIGHT\x10\x02\x12\x1e\n\x1aLLC_FBK_TURNSIGNAL_RESERVE\x10\x03"\xbe\x02\n\x12Llc_diag_fault_620\x12"\n\x1allc_disengagecounter_brake\x18\x01 \x01(\x05\x12"\n\x1allc_disengagecounter_steer\x18\x02 \x01(\x05\x12%\n\x1dllc_disengagecounter_throttle\x18\x03 \x01(\x05\x12\x1c\n\x14llc_fbk_faultcounter\x18\x04 \x01(\x05\x12#\n\x1bllc_disengagecounter_button\x18\x05 \x01(\x05\x12\x1c\n\x14llc_fbk_version_year\x18\x06 \x01(\x05\x12\x1d\n\x15llc_fbk_version_month\x18\x07 \x01(\x05\x12\x1b\n\x13llc_fbk_version_day\x18\x08 \x01(\x05\x12\x1c\n\x14llc_fbk_version_hour\x18\t \x01(\x05"\x96\x01\n\x1cLlc_diag_steeringcontrol_722\x12&\n\x1ellc_dbg_steeringsensorposition\x18\x01 \x01(\x01\x12\'\n\x1fllc_dbg_steeringrackinputtorque\x18\x02 \x01(\x05\x12%\n\x1dllc_dbg_steeringmotorposition\x18\x03 \x01(\x01"\xf5\x05\n\x18Adc_auxiliarycontrol_110\x12\x1e\n\x16adc_auxcontrol_counter\x18\x01 \x01(\x05\x12\x1f\n\x17adc_auxcontrol_checksum\x18\x02 \x01(\x05\x12&\n\x1eadc_cmd_inverter_controlenable\x18\x03 \x01(\x08\x12\x18\n\x10adc_cmd_inverter\x18\x04 \x01(\x08\x12\x15\n\radc_cmd_wiper\x18\x05 \x01(\x05\x12!\n\x19adc_cmd_pdu_controlenable\x18\x06 \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch8\x18\x07 \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch7\x18\x08 \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch6\x18\t \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch5\x18\n \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch4\x18\x0b \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch3\x18\x0c \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch2\x18\r \x01(\x08\x12\x17\n\x0fadc_cmd_pdu_ch1\x18\x0e \x01(\x08\x12\x1c\n\x14adc_cmd_hazardlights\x18\x0f \x01(\x08\x12\x18\n\x10adc_cmd_highbeam\x18\x10 \x01(\x08\x12\x17\n\x0fadc_cmd_lowbeam\x18\x11 \x01(\x08\x12\x14\n\x0cadc_cmd_horn\x18\x12 \x01(\x08\x12Z\n\x12adc_cmd_turnsignal\x18\x13 \x01(\x0e2>.apollo.canbus.Adc_auxiliarycontrol_110.Adc_cmd_turnsignalType"\x90\x01\n\x16Adc_cmd_turnsignalType\x12\x1b\n\x17ADC_CMD_TURNSIGNAL_NONE\x10\x00\x12\x1b\n\x17ADC_CMD_TURNSIGNAL_LEFT\x10\x01\x12\x1c\n\x18ADC_CMD_TURNSIGNAL_RIGHT\x10\x02\x12\x1e\n\x1aADC_CMD_TURNSIGNAL_RESERVE\x10\x03"\xf6\x01\n\x19Llc_diag_brakecontrol_721\x12&\n\x1ellc_dbg_brakepidcontribution_p\x18\x01 \x01(\x01\x12&\n\x1ellc_dbg_brakepidcontribution_i\x18\x02 \x01(\x01\x12&\n\x1ellc_dbg_brakepidcontribution_d\x18\x03 \x01(\x01\x12\x1f\n\x17llc_dbg_brakepid_output\x18\x04 \x01(\x01\x12\x1e\n\x16llc_dbg_brakepid_error\x18\x05 \x01(\x05\x12 \n\x18llc_dbg_brakefeedforward\x18\x06 \x01(\x01"\xff\x06\n\x07Transit\x12A\n\x14llc_vehiclelimits_24\x18\x01 \x01(\x0b2#.apollo.canbus.Llc_vehiclelimits_24\x12C\n\x15adc_motioncontrol1_10\x18\x02 \x01(\x0b2$.apollo.canbus.Adc_motioncontrol1_10\x12O\n\x1badc_motioncontrollimits1_12\x18\x03 \x01(\x0b2*.apollo.canbus.Adc_motioncontrollimits1_12\x12E\n\x16llc_motionfeedback1_20\x18\x04 \x01(\x0b2%.apollo.canbus.Llc_motionfeedback1_20\x12E\n\x16llc_motionfeedback2_21\x18\x05 \x01(\x0b2%.apollo.canbus.Llc_motionfeedback2_21\x12S\n\x1dllc_motioncommandfeedback1_22\x18\x06 \x01(\x0b2,.apollo.canbus.Llc_motioncommandfeedback1_22\x12A\n\x14llc_vehiclestatus_25\x18\x07 \x01(\x0b2#.apollo.canbus.Llc_vehiclestatus_25\x12K\n\x19llc_auxiliaryfeedback_120\x18\x08 \x01(\x0b2(.apollo.canbus.Llc_auxiliaryfeedback_120\x12=\n\x12llc_diag_fault_620\x18\t \x01(\x0b2!.apollo.canbus.Llc_diag_fault_620\x12Q\n\x1cllc_diag_steeringcontrol_722\x18\n \x01(\x0b2+.apollo.canbus.Llc_diag_steeringcontrol_722\x12I\n\x18adc_auxiliarycontrol_110\x18\x0b \x01(\x0b2\'.apollo.canbus.Adc_auxiliarycontrol_110\x12K\n\x19llc_diag_brakecontrol_721\x18\x0c \x01(\x0b2(.apollo.canbus.Llc_diag_brakecontrol_721')
_LLC_VEHICLELIMITS_24 = DESCRIPTOR.message_types_by_name['Llc_vehiclelimits_24']
_ADC_MOTIONCONTROL1_10 = DESCRIPTOR.message_types_by_name['Adc_motioncontrol1_10']
_ADC_MOTIONCONTROLLIMITS1_12 = DESCRIPTOR.message_types_by_name['Adc_motioncontrollimits1_12']
_LLC_MOTIONFEEDBACK1_20 = DESCRIPTOR.message_types_by_name['Llc_motionfeedback1_20']
_LLC_MOTIONFEEDBACK2_21 = DESCRIPTOR.message_types_by_name['Llc_motionfeedback2_21']
_LLC_MOTIONCOMMANDFEEDBACK1_22 = DESCRIPTOR.message_types_by_name['Llc_motioncommandfeedback1_22']
_LLC_VEHICLESTATUS_25 = DESCRIPTOR.message_types_by_name['Llc_vehiclestatus_25']
_LLC_AUXILIARYFEEDBACK_120 = DESCRIPTOR.message_types_by_name['Llc_auxiliaryfeedback_120']
_LLC_DIAG_FAULT_620 = DESCRIPTOR.message_types_by_name['Llc_diag_fault_620']
_LLC_DIAG_STEERINGCONTROL_722 = DESCRIPTOR.message_types_by_name['Llc_diag_steeringcontrol_722']
_ADC_AUXILIARYCONTROL_110 = DESCRIPTOR.message_types_by_name['Adc_auxiliarycontrol_110']
_LLC_DIAG_BRAKECONTROL_721 = DESCRIPTOR.message_types_by_name['Llc_diag_brakecontrol_721']
_TRANSIT = DESCRIPTOR.message_types_by_name['Transit']
_ADC_MOTIONCONTROL1_10_ADC_CMD_STEERINGCONTROLMODETYPE = _ADC_MOTIONCONTROL1_10.enum_types_by_name['Adc_cmd_steeringcontrolmodeType']
_ADC_MOTIONCONTROL1_10_ADC_CMD_GEARTYPE = _ADC_MOTIONCONTROL1_10.enum_types_by_name['Adc_cmd_gearType']
_ADC_MOTIONCONTROL1_10_ADC_CMD_AUTONOMYREQUESTTYPE = _ADC_MOTIONCONTROL1_10.enum_types_by_name['Adc_cmd_autonomyrequestType']
_ADC_MOTIONCONTROL1_10_ADC_CMD_LONGITUDINALCONTROLMODETYPE = _ADC_MOTIONCONTROL1_10.enum_types_by_name['Adc_cmd_longitudinalcontrolmodeType']
_LLC_MOTIONFEEDBACK1_20_LLC_FBK_GEARTYPE = _LLC_MOTIONFEEDBACK1_20.enum_types_by_name['Llc_fbk_gearType']
_LLC_MOTIONFEEDBACK1_20_LLC_FBK_STEERINGCONTROLMODETYPE = _LLC_MOTIONFEEDBACK1_20.enum_types_by_name['Llc_fbk_steeringcontrolmodeType']
_LLC_MOTIONFEEDBACK1_20_LLC_FBK_LONGITUDINALCONTROLMODETYPE = _LLC_MOTIONFEEDBACK1_20.enum_types_by_name['Llc_fbk_longitudinalcontrolmodeType']
_LLC_MOTIONFEEDBACK1_20_LLC_FBK_STATETYPE = _LLC_MOTIONFEEDBACK1_20.enum_types_by_name['Llc_fbk_stateType']
_LLC_AUXILIARYFEEDBACK_120_LLC_FBK_TURNSIGNALTYPE = _LLC_AUXILIARYFEEDBACK_120.enum_types_by_name['Llc_fbk_turnsignalType']
_ADC_AUXILIARYCONTROL_110_ADC_CMD_TURNSIGNALTYPE = _ADC_AUXILIARYCONTROL_110.enum_types_by_name['Adc_cmd_turnsignalType']
Llc_vehiclelimits_24 = _reflection.GeneratedProtocolMessageType('Llc_vehiclelimits_24', (_message.Message,), {'DESCRIPTOR': _LLC_VEHICLELIMITS_24, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_vehiclelimits_24)
Adc_motioncontrol1_10 = _reflection.GeneratedProtocolMessageType('Adc_motioncontrol1_10', (_message.Message,), {'DESCRIPTOR': _ADC_MOTIONCONTROL1_10, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Adc_motioncontrol1_10)
Adc_motioncontrollimits1_12 = _reflection.GeneratedProtocolMessageType('Adc_motioncontrollimits1_12', (_message.Message,), {'DESCRIPTOR': _ADC_MOTIONCONTROLLIMITS1_12, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Adc_motioncontrollimits1_12)
Llc_motionfeedback1_20 = _reflection.GeneratedProtocolMessageType('Llc_motionfeedback1_20', (_message.Message,), {'DESCRIPTOR': _LLC_MOTIONFEEDBACK1_20, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_motionfeedback1_20)
Llc_motionfeedback2_21 = _reflection.GeneratedProtocolMessageType('Llc_motionfeedback2_21', (_message.Message,), {'DESCRIPTOR': _LLC_MOTIONFEEDBACK2_21, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_motionfeedback2_21)
Llc_motioncommandfeedback1_22 = _reflection.GeneratedProtocolMessageType('Llc_motioncommandfeedback1_22', (_message.Message,), {'DESCRIPTOR': _LLC_MOTIONCOMMANDFEEDBACK1_22, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_motioncommandfeedback1_22)
Llc_vehiclestatus_25 = _reflection.GeneratedProtocolMessageType('Llc_vehiclestatus_25', (_message.Message,), {'DESCRIPTOR': _LLC_VEHICLESTATUS_25, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_vehiclestatus_25)
Llc_auxiliaryfeedback_120 = _reflection.GeneratedProtocolMessageType('Llc_auxiliaryfeedback_120', (_message.Message,), {'DESCRIPTOR': _LLC_AUXILIARYFEEDBACK_120, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_auxiliaryfeedback_120)
Llc_diag_fault_620 = _reflection.GeneratedProtocolMessageType('Llc_diag_fault_620', (_message.Message,), {'DESCRIPTOR': _LLC_DIAG_FAULT_620, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_diag_fault_620)
Llc_diag_steeringcontrol_722 = _reflection.GeneratedProtocolMessageType('Llc_diag_steeringcontrol_722', (_message.Message,), {'DESCRIPTOR': _LLC_DIAG_STEERINGCONTROL_722, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_diag_steeringcontrol_722)
Adc_auxiliarycontrol_110 = _reflection.GeneratedProtocolMessageType('Adc_auxiliarycontrol_110', (_message.Message,), {'DESCRIPTOR': _ADC_AUXILIARYCONTROL_110, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Adc_auxiliarycontrol_110)
Llc_diag_brakecontrol_721 = _reflection.GeneratedProtocolMessageType('Llc_diag_brakecontrol_721', (_message.Message,), {'DESCRIPTOR': _LLC_DIAG_BRAKECONTROL_721, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Llc_diag_brakecontrol_721)
Transit = _reflection.GeneratedProtocolMessageType('Transit', (_message.Message,), {'DESCRIPTOR': _TRANSIT, '__module__': 'modules.canbus.proto.transit_pb2'})
_sym_db.RegisterMessage(Transit)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LLC_VEHICLELIMITS_24._serialized_start = 53
    _LLC_VEHICLELIMITS_24._serialized_end = 142
    _ADC_MOTIONCONTROL1_10._serialized_start = 145
    _ADC_MOTIONCONTROL1_10._serialized_end = 1578
    _ADC_MOTIONCONTROL1_10_ADC_CMD_STEERINGCONTROLMODETYPE._serialized_start = 772
    _ADC_MOTIONCONTROL1_10_ADC_CMD_STEERINGCONTROLMODETYPE._serialized_end = 976
    _ADC_MOTIONCONTROL1_10_ADC_CMD_GEARTYPE._serialized_start = 978
    _ADC_MOTIONCONTROL1_10_ADC_CMD_GEARTYPE._serialized_end = 1103
    _ADC_MOTIONCONTROL1_10_ADC_CMD_AUTONOMYREQUESTTYPE._serialized_start = 1106
    _ADC_MOTIONCONTROL1_10_ADC_CMD_AUTONOMYREQUESTTYPE._serialized_end = 1313
    _ADC_MOTIONCONTROL1_10_ADC_CMD_LONGITUDINALCONTROLMODETYPE._serialized_start = 1316
    _ADC_MOTIONCONTROL1_10_ADC_CMD_LONGITUDINALCONTROLMODETYPE._serialized_end = 1578
    _ADC_MOTIONCONTROLLIMITS1_12._serialized_start = 1581
    _ADC_MOTIONCONTROLLIMITS1_12._serialized_end = 1716
    _LLC_MOTIONFEEDBACK1_20._serialized_start = 1719
    _LLC_MOTIONFEEDBACK1_20._serialized_end = 3580
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_GEARTYPE._serialized_start = 2464
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_GEARTYPE._serialized_end = 2589
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_STEERINGCONTROLMODETYPE._serialized_start = 2592
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_STEERINGCONTROLMODETYPE._serialized_end = 2796
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_LONGITUDINALCONTROLMODETYPE._serialized_start = 2799
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_LONGITUDINALCONTROLMODETYPE._serialized_end = 3061
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_STATETYPE._serialized_start = 3064
    _LLC_MOTIONFEEDBACK1_20_LLC_FBK_STATETYPE._serialized_end = 3580
    _LLC_MOTIONFEEDBACK2_21._serialized_start = 3583
    _LLC_MOTIONFEEDBACK2_21._serialized_end = 3773
    _LLC_MOTIONCOMMANDFEEDBACK1_22._serialized_start = 3776
    _LLC_MOTIONCOMMANDFEEDBACK1_22._serialized_end = 4002
    _LLC_VEHICLESTATUS_25._serialized_start = 4004
    _LLC_VEHICLESTATUS_25._serialized_end = 4053
    _LLC_AUXILIARYFEEDBACK_120._serialized_start = 4056
    _LLC_AUXILIARYFEEDBACK_120._serialized_end = 4771
    _LLC_AUXILIARYFEEDBACK_120_LLC_FBK_TURNSIGNALTYPE._serialized_start = 4627
    _LLC_AUXILIARYFEEDBACK_120_LLC_FBK_TURNSIGNALTYPE._serialized_end = 4771
    _LLC_DIAG_FAULT_620._serialized_start = 4774
    _LLC_DIAG_FAULT_620._serialized_end = 5092
    _LLC_DIAG_STEERINGCONTROL_722._serialized_start = 5095
    _LLC_DIAG_STEERINGCONTROL_722._serialized_end = 5245
    _ADC_AUXILIARYCONTROL_110._serialized_start = 5248
    _ADC_AUXILIARYCONTROL_110._serialized_end = 6005
    _ADC_AUXILIARYCONTROL_110_ADC_CMD_TURNSIGNALTYPE._serialized_start = 5861
    _ADC_AUXILIARYCONTROL_110_ADC_CMD_TURNSIGNALTYPE._serialized_end = 6005
    _LLC_DIAG_BRAKECONTROL_721._serialized_start = 6008
    _LLC_DIAG_BRAKECONTROL_721._serialized_end = 6254
    _TRANSIT._serialized_start = 6257
    _TRANSIT._serialized_end = 7152