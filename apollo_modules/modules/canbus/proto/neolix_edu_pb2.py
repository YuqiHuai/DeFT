"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/canbus/proto/neolix_edu.proto\x12\rapollo.canbus"\xc9\x02\n\x12Aeb_systemstate_11\x12\x11\n\taeb_state\x18\x01 \x01(\x05\x12\x16\n\x0eaeb_brakestate\x18\x02 \x01(\x08\x12\x11\n\tfaultrank\x18\x03 \x01(\x05\x12\x1a\n\x12currenttemperature\x18\x04 \x01(\x05\x12\x13\n\x0bpas_f1_stop\x18\x05 \x01(\x08\x12\x13\n\x0bpas_f2_stop\x18\x06 \x01(\x08\x12\x13\n\x0bpas_f3_stop\x18\x07 \x01(\x08\x12\x13\n\x0bpas_f4_stop\x18\x08 \x01(\x08\x12\x13\n\x0bpas_b1_stop\x18\t \x01(\x08\x12\x13\n\x0bpas_b2_stop\x18\n \x01(\x08\x12\x13\n\x0bpas_b3_stop\x18\x0b \x01(\x08\x12\x13\n\x0bpas_b4_stop\x18\x0c \x01(\x08\x12\x1c\n\x14aeb_livecounter_rear\x18\r \x01(\x05\x12\x13\n\x0baeb_cheksum\x18\x0e \x01(\x05"\xd6\x04\n\x1eVcu_vehicle_fault_response_201\x12$\n\x1cvehicle_error_indicationsvcu\x18\x01 \x01(\x05\x12\x1d\n\x15brake_system_errorehb\x18\x02 \x01(\x05\x12\x11\n\teps_error\x18\x03 \x01(\x05\x12\x13\n\x0bmotor_error\x18\x04 \x01(\x05\x12\x11\n\tepb_error\x18\x05 \x01(\x05\x12%\n\x1dhigh_voltage_battery_errorbcu\x18\x06 \x01(\x05\x12(\n automode_exit_reason_losscommuni\x18\x07 \x01(\x08\x12(\n automode_exit_reason_reqsignalno\x18\x08 \x01(\x08\x12&\n\x1eautomode_exit_reason_low_power\x18\t \x01(\x08\x12%\n\x1dautomode_exit_reason_highvolt\x18\n \x01(\x08\x12(\n automode_exit_reason_vehicle_flt\x18\x0b \x01(\x08\x12(\n automode_exit_reason_press_emerg\x18\x0c \x01(\x08\x12(\n automode_exit_reason_press_remot\x18\r \x01(\x08\x12(\n automode_exit_reason_pdu_control\x18\x0e \x01(\x08\x12"\n\x1avcu_faultrept_alivecounter\x18\x0f \x01(\x05\x12\x1e\n\x16vcu_faultrept_checksum\x18\x10 \x01(\x05"\x99\x02\n\x13Vcu_powerstatus_214\x12\x15\n\rvcu_powermode\x18\x01 \x01(\x05\x12\x1a\n\x12vcu_powermodevalid\x18\x02 \x01(\x05\x12%\n\x1dreplacebatterystateindication\x18\x03 \x01(\x08\x12\x1c\n\x14forbidden_aeb_signal\x18\x04 \x01(\x08\x12"\n\x1abcu_chargedischargecurrent\x18\x05 \x01(\x01\x12 \n\x18bcu_batt_internalvoltage\x18\x06 \x01(\x01\x12#\n\x1bvcu_driverinfo_alivecounter\x18\x07 \x01(\x05\x12\x1f\n\x17vcu_driverinfo_checksum\x18\x08 \x01(\x05"\xd1\x01\n\x1aAds_light_horn_command_310\x12 \n\x18turn_right_light_command\x18\x01 \x01(\x08\x12\x1f\n\x17turn_left_light_command\x18\x02 \x01(\x08\x12\x14\n\x0chorn_command\x18\x03 \x01(\x08\x12\x14\n\x0cbeam_command\x18\x04 \x01(\x05\x12#\n\x1bauto_drivercmd_alivecounter\x18\x05 \x01(\x05\x12\x1f\n\x17auto_drivercmd_checksum\x18\x06 \x01(\x05"\xce\x01\n\x14Ads_brake_command_46\x12\x14\n\x0cdrive_enable\x18\x01 \x01(\x08\x12\x1a\n\x12auto_brake_command\x18\x02 \x01(\x05\x12\x1c\n\x14auto_parking_command\x18\x03 \x01(\x08\x12 \n\x18epb_rampauxiliarycommand\x18\x04 \x01(\x08\x12#\n\x1bauto_drivercmd_alivecounter\x18\x05 \x01(\x05\x12\x1f\n\x17auto_drivercmd_checksum\x18\x06 \x01(\x05"\xc0\x04\n\x13Vcu_brake_report_47\x12\x19\n\x11brake_enable_resp\x18\x01 \x01(\x08\x12S\n\x11control_mode_resp\x18\x02 \x01(\x0e28.apollo.canbus.Vcu_brake_report_47.Control_mode_respType\x12\x1c\n\x14vcu_real_brake_valid\x18\x03 \x01(\x08\x12\x16\n\x0evcu_real_brake\x18\x04 \x01(\x05\x12\x1f\n\x17vcu_real_parking_status\x18\x05 \x01(\x05\x12\x1e\n\x16vcu_real_parking_valid\x18\x06 \x01(\x08\x12\x1f\n\x17rampauxiliaryindication\x18\x07 \x01(\x08\x12\x14\n\x0cvehicleslope\x18\x08 \x01(\x01\x12"\n\x1avcu_brakerept_alivecounter\x18\t \x01(\x05\x12\x1e\n\x16vcu_brakerept_checksum\x18\n \x01(\x05"\xc6\x01\n\x15Control_mode_respType\x12\x1d\n\x19CONTROL_MODE_RESP_STANDBY\x10\x00\x12 \n\x1cCONTROL_MODE_RESP_AUTO_DRIVE\x10\x01\x12\x1f\n\x1bCONTROL_MODE_RESP_NET_DRIVE\x10\x02\x12$\n CONTROL_MODE_RESP_REMOTE_CONTROL\x10\x03\x12%\n!CONTROL_MODE_RESP_EMERGENCY_BRAKE\x10\x04"\x94\x04\n\x11Vcu_eps_report_57\x12\x19\n\x11drive_enable_resp\x18\x01 \x01(\x08\x12Q\n\x11control_mode_resp\x18\x02 \x01(\x0e26.apollo.canbus.Vcu_eps_report_57.Control_mode_respType\x12\x16\n\x0evcu_eps_report\x18\x03 \x01(\x08\x12\x16\n\x0evcu_real_angle\x18\x04 \x01(\x01\x12\x1c\n\x14vcu_real_angle_valid\x18\x05 \x01(\x08\x12\x1e\n\x16vcu_target_angle_valid\x18\x06 \x01(\x08\x12\x18\n\x10vcu_target_angle\x18\x07 \x01(\x01\x12!\n\x19vcu_eps_rept_alivecounter\x18\x08 \x01(\x05\x12\x1d\n\x15vcu_eps_rept_checksum\x18\t \x01(\x05"\xc6\x01\n\x15Control_mode_respType\x12\x1d\n\x19CONTROL_MODE_RESP_STANDBY\x10\x00\x12 \n\x1cCONTROL_MODE_RESP_AUTO_DRIVE\x10\x01\x12\x1f\n\x1bCONTROL_MODE_RESP_NET_DRIVE\x10\x02\x12$\n CONTROL_MODE_RESP_REMOTE_CONTROL\x10\x03\x12%\n!CONTROL_MODE_RESP_EMERGENCY_BRAKE\x10\x04"\x8b\x01\n\x12Ads_eps_command_56\x12\x14\n\x0cdrive_enable\x18\x01 \x01(\x08\x12\x19\n\x11auto_target_angle\x18\x02 \x01(\x01\x12#\n\x1bauto_drivercmd_alivecounter\x18\x03 \x01(\x05\x12\x1f\n\x17auto_drivercmd_checksum\x18\x04 \x01(\x05"\xef\x02\n\x14Ads_drive_command_50\x12\x14\n\x0cdrive_enable\x18\x01 \x01(\x08\x12V\n\x12auto_shift_command\x18\x02 \x01(\x0e2:.apollo.canbus.Ads_drive_command_50.Auto_shift_commandType\x12\x19\n\x11auto_drive_torque\x18\x03 \x01(\x01\x12#\n\x1bauto_drivercmd_alivecounter\x18\x04 \x01(\x05\x12\x1f\n\x17auto_drivercmd_checksum\x18\x05 \x01(\x05"\x87\x01\n\x16Auto_shift_commandType\x12\x18\n\x14AUTO_SHIFT_COMMAND_N\x10\x00\x12\x18\n\x14AUTO_SHIFT_COMMAND_D\x10\x01\x12\x18\n\x14AUTO_SHIFT_COMMAND_R\x10\x02\x12\x1f\n\x1bAUTO_SHIFT_COMMAND_RESERVED\x10\x03"\xcb\x05\n\x13Vcu_drive_report_52\x12\x19\n\x11drive_enable_resp\x18\x01 \x01(\x08\x12S\n\x11control_mode_resp\x18\x02 \x01(\x0e28.apollo.canbus.Vcu_drive_report_52.Control_mode_respType\x12M\n\x0evcu_real_shift\x18\x03 \x01(\x0e25.apollo.canbus.Vcu_drive_report_52.Vcu_real_shiftType\x12\x1c\n\x14vcu_real_shift_valid\x18\x04 \x01(\x08\x12\x1d\n\x15vcu_real_torque_valid\x18\x05 \x01(\x08\x12\x17\n\x0fvcu_real_torque\x18\x06 \x01(\x01\x12\x1d\n\x15vcu_limitedtorquemode\x18\x07 \x01(\x08\x12"\n\x1avcu_driverept_alivecounter\x18\x08 \x01(\x05\x12\x1e\n\x16vcu_driverept_checksum\x18\t \x01(\x05"\xc6\x01\n\x15Control_mode_respType\x12\x1d\n\x19CONTROL_MODE_RESP_STANDBY\x10\x00\x12 \n\x1cCONTROL_MODE_RESP_AUTO_DRIVE\x10\x01\x12\x1f\n\x1bCONTROL_MODE_RESP_NET_DRIVE\x10\x02\x12$\n CONTROL_MODE_RESP_REMOTE_CONTROL\x10\x03\x12%\n!CONTROL_MODE_RESP_EMERGENCY_BRAKE\x10\x04"s\n\x12Vcu_real_shiftType\x12\x14\n\x10VCU_REAL_SHIFT_N\x10\x00\x12\x14\n\x10VCU_REAL_SHIFT_D\x10\x01\x12\x14\n\x10VCU_REAL_SHIFT_R\x10\x02\x12\x1b\n\x17VCU_REAL_SHIFT_RESERVED\x10\x03"{\n\x11Ads_diagnosis_628\x12\x11\n\tfaultrank\x18\x01 \x01(\x05\x12\x17\n\x0fadas_fault_code\x18\x02 \x01(\x05\x12\x1c\n\x14adas_softwareversion\x18\x03 \x01(\x05\x12\x1c\n\x14adas_hardwareversion\x18\x04 \x01(\x05"&\n\nVcu_nm_401\x12\x18\n\x10vcu_sleepcommand\x18\x01 \x01(\x08"\xa0\x05\n\x1dVcu_vehicle_status_report_101\x12\x19\n\x11drive_enable_resp\x18\x01 \x01(\x08\x12#\n\x1bvcu_highvoltagecircuitstate\x18\x02 \x01(\x08\x12\x1e\n\x16vcu_dcdc_enabledstates\x18\x03 \x01(\x08\x12]\n\x11control_mode_resp\x18\x04 \x01(\x0e2B.apollo.canbus.Vcu_vehicle_status_report_101.Control_mode_respType\x12\x19\n\x11vcu_vehicle_speed\x18\x05 \x01(\x01\x12(\n vcu_lowbatterychargingfunctionst\x18\x06 \x01(\x05\x12\x17\n\x0fvcu_display_soc\x18\x07 \x01(\x05\x12\x17\n\x0fvcu_motor_speed\x18\x08 \x01(\x01\x12\x1b\n\x13vcu_motor_direction\x18\t \x01(\x05\x12\x1d\n\x15vcu_motor_speed_valid\x18\n \x01(\x08\x12#\n\x1bvcu_statusrept_alivecounter\x18\x0b \x01(\x05\x12\x1f\n\x17vcu_statusrept_checksum\x18\x0c \x01(\x05"\xc6\x01\n\x15Control_mode_respType\x12\x1d\n\x19CONTROL_MODE_RESP_STANDBY\x10\x00\x12 \n\x1cCONTROL_MODE_RESP_AUTO_DRIVE\x10\x01\x12\x1f\n\x1bCONTROL_MODE_RESP_NET_DRIVE\x10\x02\x12$\n CONTROL_MODE_RESP_REMOTE_CONTROL\x10\x03\x12%\n!CONTROL_MODE_RESP_EMERGENCY_BRAKE\x10\x04"\xb9\x01\n\x1dVcu_vehicle_info_response_502\x12(\n vehicle_softwareversion_indicati\x18\x01 \x01(\x05\x12\x0f\n\x07project\x18\x02 \x01(\x05\x12\x14\n\x0cmanufacturer\x18\x03 \x01(\x05\x12\x0c\n\x04year\x18\x04 \x01(\x05\x12\r\n\x05month\x18\x05 \x01(\x05\x12\x0b\n\x03day\x18\x06 \x01(\x05\x12\x1d\n\x15vehicle_serial_number\x18\x07 \x01(\x05"N\n\x12Aeb_diagnosis1_626\x12\x1b\n\x13aeb_softwareversion\x18\x01 \x01(\x01\x12\x1b\n\x13aeb_hardwareversion\x18\x02 \x01(\x01"(\n\x10Aeb_diagresp_718\x12\x14\n\x0caeb_diagresp\x18\x01 \x01(\x08"\xc6\x01\n\x10Pas_1st_data_311\x12\x14\n\x0cpasdistance4\x18\x01 \x01(\x01\x12\x14\n\x0cpasdistance3\x18\x02 \x01(\x01\x12\x15\n\rpas_f1_status\x18\x03 \x01(\x08\x12\x15\n\rpas_f2_status\x18\x04 \x01(\x08\x12\x15\n\rpas_f3_status\x18\x05 \x01(\x08\x12\x15\n\rpas_f4_status\x18\x06 \x01(\x08\x12\x14\n\x0cpasdistance2\x18\x07 \x01(\x01\x12\x14\n\x0cpasdistance1\x18\x08 \x01(\x01"\xc6\x01\n\x10Pas_2nd_data_312\x12\x15\n\rpas_b1_status\x18\x01 \x01(\x08\x12\x15\n\rpas_b2_status\x18\x02 \x01(\x08\x12\x15\n\rpas_b3_status\x18\x03 \x01(\x08\x12\x15\n\rpas_b4_status\x18\x04 \x01(\x08\x12\x14\n\x0cpasdistance1\x18\x05 \x01(\x01\x12\x14\n\x0cpasdistance2\x18\x06 \x01(\x01\x12\x14\n\x0cpasdistance3\x18\x07 \x01(\x01\x12\x14\n\x0cpasdistance4\x18\x08 \x01(\x01"\xea\x01\n\x14Aeb_wheelimpulse_355\x12\x11\n\tflimpulse\x18\x01 \x01(\x01\x12\x16\n\x0eflimpulsevalid\x18\x02 \x01(\x08\x12\x11\n\tfrimpulse\x18\x03 \x01(\x01\x12\x16\n\x0efrimpulsevalid\x18\x04 \x01(\x08\x12\x11\n\trlimpulse\x18\x05 \x01(\x01\x12\x16\n\x0erlimpulsevalid\x18\x06 \x01(\x08\x12\x11\n\trrimpulse\x18\x07 \x01(\x01\x12\x16\n\x0errimpulsevalid\x18\x08 \x01(\x08\x12\x14\n\x0calivecounter\x18\t \x01(\x01\x12\x10\n\x08checksum\x18\n \x01(\x01"\xee\x01\n\x16Aeb_rearwheelspeed_354\x12\x1b\n\x13wheelspeed_rl_valid\x18\x01 \x01(\x08\x12\x15\n\rwheelspeed_rl\x18\x02 \x01(\x01\x12\x1b\n\x13wheelspeed_rr_valid\x18\x03 \x01(\x08\x12\x15\n\rwheelspeed_rr\x18\x04 \x01(\x01\x12\x1c\n\x14wheelspeed_rl_direct\x18\x05 \x01(\x01\x12\x1c\n\x14wheelspeed_rr_direct\x18\x06 \x01(\x01\x12\x19\n\x11alivecounter_rear\x18\x07 \x01(\x01\x12\x15\n\rchecksum_rear\x18\x08 \x01(\x01"\xbd\x02\n\x17Aeb_frontwheelspeed_353\x12\x19\n\x11vehiclespeedvalid\x18\x01 \x01(\x08\x12\x14\n\x0cvehiclespeed\x18\x02 \x01(\x01\x12\x19\n\x11vehiclerealdirect\x18\x03 \x01(\x01\x12\x1b\n\x13wheelspeed_fl_valid\x18\x04 \x01(\x08\x12\x15\n\rwheelspeed_fl\x18\x05 \x01(\x01\x12\x1b\n\x13wheelspeed_fr_valid\x18\x06 \x01(\x08\x12\x15\n\rwheelspeed_fr\x18\x07 \x01(\x01\x12\x1c\n\x14wheelspeed_fl_direct\x18\x08 \x01(\x01\x12\x1c\n\x14wheelspeed_fr_direct\x18\t \x01(\x01\x12\x1a\n\x12alivecounter_front\x18\n \x01(\x01\x12\x16\n\x0echecksum_front\x18\x0b \x01(\x01"\x8f\x0b\n\nNeolix_edu\x12=\n\x12aeb_systemstate_11\x18\x01 \x01(\x0b2!.apollo.canbus.Aeb_systemstate_11\x12U\n\x1evcu_vehicle_fault_response_201\x18\x02 \x01(\x0b2-.apollo.canbus.Vcu_vehicle_fault_response_201\x12?\n\x13vcu_powerstatus_214\x18\x03 \x01(\x0b2".apollo.canbus.Vcu_powerstatus_214\x12M\n\x1aads_light_horn_command_310\x18\x04 \x01(\x0b2).apollo.canbus.Ads_light_horn_command_310\x12A\n\x14ads_brake_command_46\x18\x05 \x01(\x0b2#.apollo.canbus.Ads_brake_command_46\x12?\n\x13vcu_brake_report_47\x18\x06 \x01(\x0b2".apollo.canbus.Vcu_brake_report_47\x12;\n\x11vcu_eps_report_57\x18\x07 \x01(\x0b2 .apollo.canbus.Vcu_eps_report_57\x12=\n\x12ads_eps_command_56\x18\x08 \x01(\x0b2!.apollo.canbus.Ads_eps_command_56\x12A\n\x14ads_drive_command_50\x18\t \x01(\x0b2#.apollo.canbus.Ads_drive_command_50\x12?\n\x13vcu_drive_report_52\x18\n \x01(\x0b2".apollo.canbus.Vcu_drive_report_52\x12;\n\x11ads_diagnosis_628\x18\x0b \x01(\x0b2 .apollo.canbus.Ads_diagnosis_628\x12-\n\nvcu_nm_401\x18\x0c \x01(\x0b2\x19.apollo.canbus.Vcu_nm_401\x12S\n\x1dvcu_vehicle_status_report_101\x18\r \x01(\x0b2,.apollo.canbus.Vcu_vehicle_status_report_101\x12S\n\x1dvcu_vehicle_info_response_502\x18\x0e \x01(\x0b2,.apollo.canbus.Vcu_vehicle_info_response_502\x12=\n\x12aeb_diagnosis1_626\x18\x0f \x01(\x0b2!.apollo.canbus.Aeb_diagnosis1_626\x129\n\x10aeb_diagresp_718\x18\x10 \x01(\x0b2\x1f.apollo.canbus.Aeb_diagresp_718\x129\n\x10pas_1st_data_311\x18\x11 \x01(\x0b2\x1f.apollo.canbus.Pas_1st_data_311\x129\n\x10pas_2nd_data_312\x18\x12 \x01(\x0b2\x1f.apollo.canbus.Pas_2nd_data_312\x12A\n\x14aeb_wheelimpulse_355\x18\x13 \x01(\x0b2#.apollo.canbus.Aeb_wheelimpulse_355\x12E\n\x16aeb_rearwheelspeed_354\x18\x14 \x01(\x0b2%.apollo.canbus.Aeb_rearwheelspeed_354\x12G\n\x17aeb_frontwheelspeed_353\x18\x15 \x01(\x0b2&.apollo.canbus.Aeb_frontwheelspeed_353')
_AEB_SYSTEMSTATE_11 = DESCRIPTOR.message_types_by_name['Aeb_systemstate_11']
_VCU_VEHICLE_FAULT_RESPONSE_201 = DESCRIPTOR.message_types_by_name['Vcu_vehicle_fault_response_201']
_VCU_POWERSTATUS_214 = DESCRIPTOR.message_types_by_name['Vcu_powerstatus_214']
_ADS_LIGHT_HORN_COMMAND_310 = DESCRIPTOR.message_types_by_name['Ads_light_horn_command_310']
_ADS_BRAKE_COMMAND_46 = DESCRIPTOR.message_types_by_name['Ads_brake_command_46']
_VCU_BRAKE_REPORT_47 = DESCRIPTOR.message_types_by_name['Vcu_brake_report_47']
_VCU_EPS_REPORT_57 = DESCRIPTOR.message_types_by_name['Vcu_eps_report_57']
_ADS_EPS_COMMAND_56 = DESCRIPTOR.message_types_by_name['Ads_eps_command_56']
_ADS_DRIVE_COMMAND_50 = DESCRIPTOR.message_types_by_name['Ads_drive_command_50']
_VCU_DRIVE_REPORT_52 = DESCRIPTOR.message_types_by_name['Vcu_drive_report_52']
_ADS_DIAGNOSIS_628 = DESCRIPTOR.message_types_by_name['Ads_diagnosis_628']
_VCU_NM_401 = DESCRIPTOR.message_types_by_name['Vcu_nm_401']
_VCU_VEHICLE_STATUS_REPORT_101 = DESCRIPTOR.message_types_by_name['Vcu_vehicle_status_report_101']
_VCU_VEHICLE_INFO_RESPONSE_502 = DESCRIPTOR.message_types_by_name['Vcu_vehicle_info_response_502']
_AEB_DIAGNOSIS1_626 = DESCRIPTOR.message_types_by_name['Aeb_diagnosis1_626']
_AEB_DIAGRESP_718 = DESCRIPTOR.message_types_by_name['Aeb_diagresp_718']
_PAS_1ST_DATA_311 = DESCRIPTOR.message_types_by_name['Pas_1st_data_311']
_PAS_2ND_DATA_312 = DESCRIPTOR.message_types_by_name['Pas_2nd_data_312']
_AEB_WHEELIMPULSE_355 = DESCRIPTOR.message_types_by_name['Aeb_wheelimpulse_355']
_AEB_REARWHEELSPEED_354 = DESCRIPTOR.message_types_by_name['Aeb_rearwheelspeed_354']
_AEB_FRONTWHEELSPEED_353 = DESCRIPTOR.message_types_by_name['Aeb_frontwheelspeed_353']
_NEOLIX_EDU = DESCRIPTOR.message_types_by_name['Neolix_edu']
_VCU_BRAKE_REPORT_47_CONTROL_MODE_RESPTYPE = _VCU_BRAKE_REPORT_47.enum_types_by_name['Control_mode_respType']
_VCU_EPS_REPORT_57_CONTROL_MODE_RESPTYPE = _VCU_EPS_REPORT_57.enum_types_by_name['Control_mode_respType']
_ADS_DRIVE_COMMAND_50_AUTO_SHIFT_COMMANDTYPE = _ADS_DRIVE_COMMAND_50.enum_types_by_name['Auto_shift_commandType']
_VCU_DRIVE_REPORT_52_CONTROL_MODE_RESPTYPE = _VCU_DRIVE_REPORT_52.enum_types_by_name['Control_mode_respType']
_VCU_DRIVE_REPORT_52_VCU_REAL_SHIFTTYPE = _VCU_DRIVE_REPORT_52.enum_types_by_name['Vcu_real_shiftType']
_VCU_VEHICLE_STATUS_REPORT_101_CONTROL_MODE_RESPTYPE = _VCU_VEHICLE_STATUS_REPORT_101.enum_types_by_name['Control_mode_respType']
Aeb_systemstate_11 = _reflection.GeneratedProtocolMessageType('Aeb_systemstate_11', (_message.Message,), {'DESCRIPTOR': _AEB_SYSTEMSTATE_11, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Aeb_systemstate_11)
Vcu_vehicle_fault_response_201 = _reflection.GeneratedProtocolMessageType('Vcu_vehicle_fault_response_201', (_message.Message,), {'DESCRIPTOR': _VCU_VEHICLE_FAULT_RESPONSE_201, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_vehicle_fault_response_201)
Vcu_powerstatus_214 = _reflection.GeneratedProtocolMessageType('Vcu_powerstatus_214', (_message.Message,), {'DESCRIPTOR': _VCU_POWERSTATUS_214, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_powerstatus_214)
Ads_light_horn_command_310 = _reflection.GeneratedProtocolMessageType('Ads_light_horn_command_310', (_message.Message,), {'DESCRIPTOR': _ADS_LIGHT_HORN_COMMAND_310, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Ads_light_horn_command_310)
Ads_brake_command_46 = _reflection.GeneratedProtocolMessageType('Ads_brake_command_46', (_message.Message,), {'DESCRIPTOR': _ADS_BRAKE_COMMAND_46, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Ads_brake_command_46)
Vcu_brake_report_47 = _reflection.GeneratedProtocolMessageType('Vcu_brake_report_47', (_message.Message,), {'DESCRIPTOR': _VCU_BRAKE_REPORT_47, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_brake_report_47)
Vcu_eps_report_57 = _reflection.GeneratedProtocolMessageType('Vcu_eps_report_57', (_message.Message,), {'DESCRIPTOR': _VCU_EPS_REPORT_57, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_eps_report_57)
Ads_eps_command_56 = _reflection.GeneratedProtocolMessageType('Ads_eps_command_56', (_message.Message,), {'DESCRIPTOR': _ADS_EPS_COMMAND_56, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Ads_eps_command_56)
Ads_drive_command_50 = _reflection.GeneratedProtocolMessageType('Ads_drive_command_50', (_message.Message,), {'DESCRIPTOR': _ADS_DRIVE_COMMAND_50, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Ads_drive_command_50)
Vcu_drive_report_52 = _reflection.GeneratedProtocolMessageType('Vcu_drive_report_52', (_message.Message,), {'DESCRIPTOR': _VCU_DRIVE_REPORT_52, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_drive_report_52)
Ads_diagnosis_628 = _reflection.GeneratedProtocolMessageType('Ads_diagnosis_628', (_message.Message,), {'DESCRIPTOR': _ADS_DIAGNOSIS_628, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Ads_diagnosis_628)
Vcu_nm_401 = _reflection.GeneratedProtocolMessageType('Vcu_nm_401', (_message.Message,), {'DESCRIPTOR': _VCU_NM_401, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_nm_401)
Vcu_vehicle_status_report_101 = _reflection.GeneratedProtocolMessageType('Vcu_vehicle_status_report_101', (_message.Message,), {'DESCRIPTOR': _VCU_VEHICLE_STATUS_REPORT_101, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_vehicle_status_report_101)
Vcu_vehicle_info_response_502 = _reflection.GeneratedProtocolMessageType('Vcu_vehicle_info_response_502', (_message.Message,), {'DESCRIPTOR': _VCU_VEHICLE_INFO_RESPONSE_502, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Vcu_vehicle_info_response_502)
Aeb_diagnosis1_626 = _reflection.GeneratedProtocolMessageType('Aeb_diagnosis1_626', (_message.Message,), {'DESCRIPTOR': _AEB_DIAGNOSIS1_626, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Aeb_diagnosis1_626)
Aeb_diagresp_718 = _reflection.GeneratedProtocolMessageType('Aeb_diagresp_718', (_message.Message,), {'DESCRIPTOR': _AEB_DIAGRESP_718, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Aeb_diagresp_718)
Pas_1st_data_311 = _reflection.GeneratedProtocolMessageType('Pas_1st_data_311', (_message.Message,), {'DESCRIPTOR': _PAS_1ST_DATA_311, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Pas_1st_data_311)
Pas_2nd_data_312 = _reflection.GeneratedProtocolMessageType('Pas_2nd_data_312', (_message.Message,), {'DESCRIPTOR': _PAS_2ND_DATA_312, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Pas_2nd_data_312)
Aeb_wheelimpulse_355 = _reflection.GeneratedProtocolMessageType('Aeb_wheelimpulse_355', (_message.Message,), {'DESCRIPTOR': _AEB_WHEELIMPULSE_355, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Aeb_wheelimpulse_355)
Aeb_rearwheelspeed_354 = _reflection.GeneratedProtocolMessageType('Aeb_rearwheelspeed_354', (_message.Message,), {'DESCRIPTOR': _AEB_REARWHEELSPEED_354, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Aeb_rearwheelspeed_354)
Aeb_frontwheelspeed_353 = _reflection.GeneratedProtocolMessageType('Aeb_frontwheelspeed_353', (_message.Message,), {'DESCRIPTOR': _AEB_FRONTWHEELSPEED_353, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Aeb_frontwheelspeed_353)
Neolix_edu = _reflection.GeneratedProtocolMessageType('Neolix_edu', (_message.Message,), {'DESCRIPTOR': _NEOLIX_EDU, '__module__': 'modules.canbus.proto.neolix_edu_pb2'})
_sym_db.RegisterMessage(Neolix_edu)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _AEB_SYSTEMSTATE_11._serialized_start = 57
    _AEB_SYSTEMSTATE_11._serialized_end = 386
    _VCU_VEHICLE_FAULT_RESPONSE_201._serialized_start = 389
    _VCU_VEHICLE_FAULT_RESPONSE_201._serialized_end = 987
    _VCU_POWERSTATUS_214._serialized_start = 990
    _VCU_POWERSTATUS_214._serialized_end = 1271
    _ADS_LIGHT_HORN_COMMAND_310._serialized_start = 1274
    _ADS_LIGHT_HORN_COMMAND_310._serialized_end = 1483
    _ADS_BRAKE_COMMAND_46._serialized_start = 1486
    _ADS_BRAKE_COMMAND_46._serialized_end = 1692
    _VCU_BRAKE_REPORT_47._serialized_start = 1695
    _VCU_BRAKE_REPORT_47._serialized_end = 2271
    _VCU_BRAKE_REPORT_47_CONTROL_MODE_RESPTYPE._serialized_start = 2073
    _VCU_BRAKE_REPORT_47_CONTROL_MODE_RESPTYPE._serialized_end = 2271
    _VCU_EPS_REPORT_57._serialized_start = 2274
    _VCU_EPS_REPORT_57._serialized_end = 2806
    _VCU_EPS_REPORT_57_CONTROL_MODE_RESPTYPE._serialized_start = 2073
    _VCU_EPS_REPORT_57_CONTROL_MODE_RESPTYPE._serialized_end = 2271
    _ADS_EPS_COMMAND_56._serialized_start = 2809
    _ADS_EPS_COMMAND_56._serialized_end = 2948
    _ADS_DRIVE_COMMAND_50._serialized_start = 2951
    _ADS_DRIVE_COMMAND_50._serialized_end = 3318
    _ADS_DRIVE_COMMAND_50_AUTO_SHIFT_COMMANDTYPE._serialized_start = 3183
    _ADS_DRIVE_COMMAND_50_AUTO_SHIFT_COMMANDTYPE._serialized_end = 3318
    _VCU_DRIVE_REPORT_52._serialized_start = 3321
    _VCU_DRIVE_REPORT_52._serialized_end = 4036
    _VCU_DRIVE_REPORT_52_CONTROL_MODE_RESPTYPE._serialized_start = 2073
    _VCU_DRIVE_REPORT_52_CONTROL_MODE_RESPTYPE._serialized_end = 2271
    _VCU_DRIVE_REPORT_52_VCU_REAL_SHIFTTYPE._serialized_start = 3921
    _VCU_DRIVE_REPORT_52_VCU_REAL_SHIFTTYPE._serialized_end = 4036
    _ADS_DIAGNOSIS_628._serialized_start = 4038
    _ADS_DIAGNOSIS_628._serialized_end = 4161
    _VCU_NM_401._serialized_start = 4163
    _VCU_NM_401._serialized_end = 4201
    _VCU_VEHICLE_STATUS_REPORT_101._serialized_start = 4204
    _VCU_VEHICLE_STATUS_REPORT_101._serialized_end = 4876
    _VCU_VEHICLE_STATUS_REPORT_101_CONTROL_MODE_RESPTYPE._serialized_start = 2073
    _VCU_VEHICLE_STATUS_REPORT_101_CONTROL_MODE_RESPTYPE._serialized_end = 2271
    _VCU_VEHICLE_INFO_RESPONSE_502._serialized_start = 4879
    _VCU_VEHICLE_INFO_RESPONSE_502._serialized_end = 5064
    _AEB_DIAGNOSIS1_626._serialized_start = 5066
    _AEB_DIAGNOSIS1_626._serialized_end = 5144
    _AEB_DIAGRESP_718._serialized_start = 5146
    _AEB_DIAGRESP_718._serialized_end = 5186
    _PAS_1ST_DATA_311._serialized_start = 5189
    _PAS_1ST_DATA_311._serialized_end = 5387
    _PAS_2ND_DATA_312._serialized_start = 5390
    _PAS_2ND_DATA_312._serialized_end = 5588
    _AEB_WHEELIMPULSE_355._serialized_start = 5591
    _AEB_WHEELIMPULSE_355._serialized_end = 5825
    _AEB_REARWHEELSPEED_354._serialized_start = 5828
    _AEB_REARWHEELSPEED_354._serialized_end = 6066
    _AEB_FRONTWHEELSPEED_353._serialized_start = 6069
    _AEB_FRONTWHEELSPEED_353._serialized_end = 6386
    _NEOLIX_EDU._serialized_start = 6389
    _NEOLIX_EDU._serialized_end = 7812