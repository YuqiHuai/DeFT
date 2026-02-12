"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.configs.proto import vehicle_config_pb2 as modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from ....modules.canbus.proto import ch_pb2 as modules_dot_canbus_dot_proto_dot_ch__pb2
from ....modules.canbus.proto import devkit_pb2 as modules_dot_canbus_dot_proto_dot_devkit__pb2
from ....modules.canbus.proto import ge3_pb2 as modules_dot_canbus_dot_proto_dot_ge3__pb2
from ....modules.canbus.proto import lexus_pb2 as modules_dot_canbus_dot_proto_dot_lexus__pb2
from ....modules.canbus.proto import transit_pb2 as modules_dot_canbus_dot_proto_dot_transit__pb2
from ....modules.canbus.proto import wey_pb2 as modules_dot_canbus_dot_proto_dot_wey__pb2
from ....modules.canbus.proto import zhongyun_pb2 as modules_dot_canbus_dot_proto_dot_zhongyun__pb2
from ....modules.canbus.proto import neolix_edu_pb2 as modules_dot_canbus_dot_proto_dot_neolix__edu__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/canbus/proto/chassis_detail.proto\x12\rapollo.canbus\x1a1modules/common/configs/proto/vehicle_config.proto\x1a"modules/canbus/proto/chassis.proto\x1a\x1dmodules/canbus/proto/ch.proto\x1a!modules/canbus/proto/devkit.proto\x1a\x1emodules/canbus/proto/ge3.proto\x1a modules/canbus/proto/lexus.proto\x1a"modules/canbus/proto/transit.proto\x1a\x1emodules/canbus/proto/wey.proto\x1a#modules/canbus/proto/zhongyun.proto\x1a%modules/canbus/proto/neolix_edu.proto"\xf4\x08\n\rChassisDetail\x123\n\x08car_type\x18\x01 \x01(\x0e2!.apollo.canbus.ChassisDetail.Type\x12\'\n\x05basic\x18\x02 \x01(\x0b2\x18.apollo.canbus.BasicInfo\x12%\n\x06safety\x18\x03 \x01(\x0b2\x15.apollo.canbus.Safety\x12!\n\x04gear\x18\x04 \x01(\x0b2\x13.apollo.canbus.Gear\x12\x1f\n\x03ems\x18\x05 \x01(\x0b2\x12.apollo.canbus.Ems\x12\x1f\n\x03esp\x18\x06 \x01(\x0b2\x12.apollo.canbus.Esp\x12\x1f\n\x03gas\x18\x07 \x01(\x0b2\x12.apollo.canbus.Gas\x12\x1f\n\x03epb\x18\x08 \x01(\x0b2\x12.apollo.canbus.Epb\x12#\n\x05brake\x18\t \x01(\x0b2\x14.apollo.canbus.Brake\x121\n\x0cdeceleration\x18\n \x01(\x0b2\x1b.apollo.canbus.Deceleration\x12.\n\x0bvehicle_spd\x18\x0b \x01(\x0b2\x19.apollo.canbus.VehicleSpd\x12\x1f\n\x03eps\x18\x0c \x01(\x0b2\x12.apollo.canbus.Eps\x12#\n\x05light\x18\r \x01(\x0b2\x14.apollo.canbus.Light\x12\'\n\x07battery\x18\x0e \x01(\x0b2\x16.apollo.canbus.Battery\x12:\n\x0echeck_response\x18\x0f \x01(\x0b2".apollo.canbus.CheckResponseSignal\x12+\n\x07license\x18\x10 \x01(\x0b2\x16.apollo.canbus.LicenseB\x02\x18\x01\x12)\n\x08surround\x18\x11 \x01(\x0b2\x17.apollo.canbus.Surround\x12\x1f\n\x03gem\x18\x12 \x01(\x0b2\x12.apollo.canbus.Gem\x12#\n\x05lexus\x18\x13 \x01(\x0b2\x14.apollo.canbus.Lexus\x12\'\n\x07transit\x18\x14 \x01(\x0b2\x16.apollo.canbus.Transit\x12\x1f\n\x03ge3\x18\x15 \x01(\x0b2\x12.apollo.canbus.Ge3\x12\x1f\n\x03wey\x18\x16 \x01(\x0b2\x12.apollo.canbus.Wey\x12)\n\x08zhongyun\x18\x17 \x01(\x0b2\x17.apollo.canbus.Zhongyun\x12\x1d\n\x02ch\x18\x18 \x01(\x0b2\x11.apollo.canbus.Ch\x12%\n\x06devkit\x18\x19 \x01(\x0b2\x15.apollo.canbus.Devkit\x12-\n\nneolix_edu\x18\x1a \x01(\x0b2\x19.apollo.canbus.Neolix_edu\x12,\n\nvehicle_id\x18e \x01(\x0b2\x18.apollo.common.VehicleID"-\n\x04Type\x12\x0f\n\x0bQIRUI_EQ_15\x10\x00\x12\x14\n\x10CHANGAN_RUICHENG\x10\x01"\xeb\x01\n\x13CheckResponseSignal\x12\x1c\n\ris_eps_online\x18\x01 \x01(\x08:\x05false\x12\x1c\n\ris_epb_online\x18\x02 \x01(\x08:\x05false\x12\x1c\n\ris_esp_online\x18\x03 \x01(\x08:\x05false\x12\x1d\n\x0eis_vtog_online\x18\x04 \x01(\x08:\x05false\x12\x1c\n\ris_scu_online\x18\x05 \x01(\x08:\x05false\x12\x1f\n\x10is_switch_online\x18\x06 \x01(\x08:\x05false\x12\x1c\n\ris_vcu_online\x18\x07 \x01(\x08:\x05false"6\n\x07Battery\x12\x17\n\x0fbattery_percent\x18\x01 \x01(\x01\x12\x12\n\nfuel_level\x18\x02 \x01(\x01"\xb1\t\n\x05Light\x12;\n\x0fturn_light_type\x18\x01 \x01(\x0e2".apollo.canbus.Light.TurnLightType\x129\n\x0ebeam_lamp_type\x18\x02 \x01(\x0e2!.apollo.canbus.Light.BeamLampType\x12\x18\n\x10is_brake_lamp_on\x18\x03 \x01(\x08\x12\x15\n\ris_auto_light\x18\x04 \x01(\x08\x12\x12\n\nwiper_gear\x18\x05 \x01(\x05\x12\x13\n\x0blotion_gear\x18\x06 \x01(\x05\x12\x12\n\nis_horn_on\x18\x07 \x01(\x08\x12?\n\x11lincoln_lamp_type\x18\x08 \x01(\x0e2$.apollo.canbus.Light.LincolnLampType\x12<\n\rlincoln_wiper\x18\t \x01(\x0e2%.apollo.canbus.Light.LincolnWiperType\x12@\n\x0flincoln_ambient\x18\n \x01(\x0e2\'.apollo.canbus.Light.LincolnAmbientType"[\n\rTurnLightType\x12\x12\n\x0eTURN_LIGHT_OFF\x10\x00\x12\x10\n\x0cTURN_LEFT_ON\x10\x01\x12\x11\n\rTURN_RIGHT_ON\x10\x02\x12\x11\n\rTURN_LIGHT_ON\x10\x03"?\n\x0cBeamLampType\x12\x0c\n\x08BEAM_OFF\x10\x00\x12\x10\n\x0cHIGH_BEAM_ON\x10\x01\x12\x0f\n\x0bLOW_BEAM_ON\x10\x02"Y\n\x0fLincolnLampType\x12\r\n\tBEAM_NULL\x10\x00\x12\x16\n\x12BEAM_FLASH_TO_PASS\x10\x01\x12\r\n\tBEAM_HIGH\x10\x02\x12\x10\n\x0cBEAM_INVALID\x10\x03"\xdc\x02\n\x10LincolnWiperType\x12\r\n\tWIPER_OFF\x10\x00\x12\x12\n\x0eWIPER_AUTO_OFF\x10\x01\x12\x14\n\x10WIPER_OFF_MOVING\x10\x02\x12\x14\n\x10WIPER_MANUAL_OFF\x10\x03\x12\x13\n\x0fWIPER_MANUAL_ON\x10\x04\x12\x14\n\x10WIPER_MANUAL_LOW\x10\x05\x12\x15\n\x11WIPER_MANUAL_HIGH\x10\x06\x12\x14\n\x10WIPER_MIST_FLICK\x10\x07\x12\x0e\n\nWIPER_WASH\x10\x08\x12\x12\n\x0eWIPER_AUTO_LOW\x10\t\x12\x13\n\x0fWIPER_AUTO_HIGH\x10\n\x12\x17\n\x13WIPER_COURTESY_WIPE\x10\x0b\x12\x15\n\x11WIPER_AUTO_ADJUST\x10\x0c\x12\x12\n\x0eWIPER_RESERVED\x10\r\x12\x11\n\rWIPER_STALLED\x10\x0e\x12\x11\n\rWIPER_NO_DATA\x10\x0f"\xa8\x01\n\x12LincolnAmbientType\x12\x10\n\x0cAMBIENT_DARK\x10\x00\x12\x11\n\rAMBIENT_LIGHT\x10\x01\x12\x14\n\x10AMBIENT_TWILIGHT\x10\x02\x12\x15\n\x11AMBIENT_TUNNEL_ON\x10\x03\x12\x16\n\x12AMBIENT_TUNNEL_OFF\x10\x04\x12\x13\n\x0fAMBIENT_INVALID\x10\x05\x12\x13\n\x0fAMBIENT_NO_DATA\x10\x07"\x85\x06\n\x03Eps\x12\x13\n\x0bis_eps_fail\x18\x01 \x01(\x08\x122\n\x11eps_control_state\x18\x02 \x01(\x0e2\x17.apollo.canbus.Eps.Type\x12\x1c\n\x14eps_driver_hand_torq\x18\x03 \x01(\x01\x12\x1f\n\x17is_steering_angle_valid\x18\x04 \x01(\x08\x12\x16\n\x0esteering_angle\x18\x05 \x01(\x01\x12\x1a\n\x12steering_angle_spd\x18\x06 \x01(\x01\x12\x1a\n\x12is_trimming_status\x18\x07 \x01(\x08\x12\x1d\n\x15is_calibration_status\x18\x08 \x01(\x08\x12\x19\n\x11is_failure_status\x18\t \x01(\x08\x12#\n\x1ballow_enter_autonomous_mode\x18\n \x01(\x05\x12\x1c\n\x14current_driving_mode\x18\x0b \x01(\x05\x12\x1a\n\x12steering_angle_cmd\x18\x0c \x01(\x01\x12\x15\n\rvehicle_speed\x18\r \x01(\x01\x12\x13\n\x0bepas_torque\x18\x0e \x01(\x01\x12\x18\n\x10steering_enabled\x18\x0f \x01(\x08\x12\x17\n\x0fdriver_override\x18\x10 \x01(\x08\x12\x17\n\x0fdriver_activity\x18\x11 \x01(\x08\x12\x16\n\x0ewatchdog_fault\x18\x12 \x01(\x08\x12\x17\n\x0fchannel_1_fault\x18\x13 \x01(\x08\x12\x17\n\x0fchannel_2_fault\x18\x14 \x01(\x08\x12\x19\n\x11calibration_fault\x18\x15 \x01(\x08\x12\x17\n\x0fconnector_fault\x18\x16 \x01(\x08\x12\x14\n\x0ctimestamp_65\x18\x17 \x01(\x01\x12\x15\n\rmajor_version\x18\x18 \x01(\x05\x12\x15\n\rminor_version\x18\x19 \x01(\x05\x12\x14\n\x0cbuild_number\x18\x1a \x01(\x05"=\n\x04Type\x12\x11\n\rNOT_AVAILABLE\x10\x00\x12\t\n\x05READY\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0b\n\x07INVALID\x10\x03"\xeb\x06\n\nVehicleSpd\x12\x1d\n\x15is_vehicle_standstill\x18\x01 \x01(\x08\x12\x1c\n\x14is_vehicle_spd_valid\x18\x02 \x01(\x08\x12\x16\n\x0bvehicle_spd\x18\x03 \x01(\x01:\x010\x12\x1d\n\x15is_wheel_spd_rr_valid\x18\x04 \x01(\x08\x12D\n\x12wheel_direction_rr\x18\x05 \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType\x12\x14\n\x0cwheel_spd_rr\x18\x06 \x01(\x01\x12\x1d\n\x15is_wheel_spd_rl_valid\x18\x07 \x01(\x08\x12D\n\x12wheel_direction_rl\x18\x08 \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType\x12\x14\n\x0cwheel_spd_rl\x18\t \x01(\x01\x12\x1d\n\x15is_wheel_spd_fr_valid\x18\n \x01(\x08\x12D\n\x12wheel_direction_fr\x18\x0b \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType\x12\x14\n\x0cwheel_spd_fr\x18\x0c \x01(\x01\x12\x1d\n\x15is_wheel_spd_fl_valid\x18\r \x01(\x08\x12D\n\x12wheel_direction_fl\x18\x0e \x01(\x0e2(.apollo.canbus.WheelSpeed.WheelSpeedType\x12\x14\n\x0cwheel_spd_fl\x18\x0f \x01(\x01\x12\x19\n\x11is_yaw_rate_valid\x18\x10 \x01(\x08\x12\x10\n\x08yaw_rate\x18\x11 \x01(\x01\x12\x17\n\x0fyaw_rate_offset\x18\x12 \x01(\x01\x12\x13\n\x0bis_ax_valid\x18\x13 \x01(\x08\x12\n\n\x02ax\x18\x14 \x01(\x01\x12\x11\n\tax_offset\x18\x15 \x01(\x01\x12\x13\n\x0bis_ay_valid\x18\x16 \x01(\x08\x12\n\n\x02ay\x18\x17 \x01(\x01\x12\x11\n\tay_offset\x18\x18 \x01(\x01\x12\x0f\n\x07lat_acc\x18\x19 \x01(\x01\x12\x10\n\x08long_acc\x18\x1a \x01(\x01\x12\x10\n\x08vert_acc\x18\x1b \x01(\x01\x12\x11\n\troll_rate\x18\x1c \x01(\x01\x12\x0f\n\x07acc_est\x18\x1d \x01(\x01\x12\x15\n\rtimestamp_sec\x18\x1e \x01(\x01"\xd2\x01\n\x0cDeceleration\x12!\n\x19is_deceleration_available\x18\x01 \x01(\x08\x12\x1e\n\x16is_deceleration_active\x18\x02 \x01(\x08\x12\x17\n\x0cdeceleration\x18\x03 \x01(\x01:\x010\x12\x13\n\x0bis_evb_fail\x18\x04 \x01(\x01\x12\x17\n\x0cevb_pressure\x18\x05 \x01(\x01:\x010\x12\x19\n\x0ebrake_pressure\x18\x06 \x01(\x01:\x010\x12\x1d\n\x12brake_pressure_spd\x18\x07 \x01(\x01:\x010"\xb6\x08\n\x05Brake\x12%\n\x16is_brake_pedal_pressed\x18\x01 \x01(\x08:\x05false\x12\x1c\n\x14is_brake_force_exist\x18\x02 \x01(\x08\x12\x1a\n\x12is_brake_over_heat\x18\x03 \x01(\x08\x12\x18\n\x10is_hand_brake_on\x18\x04 \x01(\x08\x12\x1c\n\x14brake_pedal_position\x18\x05 \x01(\x01\x12\x16\n\x0eis_brake_valid\x18\x06 \x01(\x08\x12\x13\n\x0bbrake_input\x18\x07 \x01(\x01\x12\x11\n\tbrake_cmd\x18\x08 \x01(\x01\x12\x14\n\x0cbrake_output\x18\t \x01(\x01\x12\x11\n\tboo_input\x18\n \x01(\x08\x12\x0f\n\x07boo_cmd\x18\x0b \x01(\x08\x12\x12\n\nboo_output\x18\x0c \x01(\x08\x12 \n\x18watchdog_applying_brakes\x18\r \x01(\x08\x12\x17\n\x0fwatchdog_source\x18\x0e \x01(\x05\x12\x15\n\rbrake_enabled\x18\x0f \x01(\x08\x12\x17\n\x0fdriver_override\x18\x10 \x01(\x08\x12\x17\n\x0fdriver_activity\x18\x11 \x01(\x08\x12\x16\n\x0ewatchdog_fault\x18\x12 \x01(\x08\x12\x17\n\x0fchannel_1_fault\x18\x13 \x01(\x08\x12\x17\n\x0fchannel_2_fault\x18\x14 \x01(\x08\x12\x11\n\tboo_fault\x18\x15 \x01(\x08\x12\x17\n\x0fconnector_fault\x18\x16 \x01(\x08\x12\x18\n\x10brake_torque_req\x18\x17 \x01(\x01\x126\n\nhsa_status\x18\x18 \x01(\x0e2".apollo.canbus.Brake.HSAStatusType\x12\x18\n\x10brake_torque_act\x18\x19 \x01(\x01\x122\n\x08hsa_mode\x18\x1a \x01(\x0e2 .apollo.canbus.Brake.HSAModeType\x12\x18\n\x10wheel_torque_act\x18\x1b \x01(\x01\x12\x15\n\rmajor_version\x18\x1c \x01(\x05\x12\x15\n\rminor_version\x18\x1d \x01(\x05\x12\x14\n\x0cbuild_number\x18\x1e \x01(\x05"\xbb\x01\n\rHSAStatusType\x12\x10\n\x0cHSA_INACTIVE\x10\x00\x12\x18\n\x14HSA_FINDING_GRADIENT\x10\x01\x12\x16\n\x12HSA_ACTIVE_PRESSED\x10\x02\x12\x17\n\x13HSA_ACTIVE_RELEASED\x10\x03\x12\x14\n\x10HSA_FAST_RELEASE\x10\x04\x12\x14\n\x10HSA_SLOW_RELEASE\x10\x05\x12\x0e\n\nHSA_FAILED\x10\x06\x12\x11\n\rHSA_UNDEFINED\x10\x07"P\n\x0bHSAModeType\x12\x0b\n\x07HSA_OFF\x10\x00\x12\x0c\n\x08HSA_AUTO\x10\x01\x12\x0e\n\nHSA_MANUAL\x10\x02\x12\x16\n\x12HSA_MODE_UNDEFINED\x10\x03"\xdb\x01\n\x03Epb\x12\x14\n\x0cis_epb_error\x18\x01 \x01(\x08\x12\x17\n\x0fis_epb_released\x18\x02 \x01(\x08\x12\x12\n\nepb_status\x18\x03 \x01(\x05\x12;\n\x14parking_brake_status\x18\x04 \x01(\x0e2\x1d.apollo.canbus.Epb.PBrakeType"T\n\nPBrakeType\x12\x0e\n\nPBRAKE_OFF\x10\x00\x12\x15\n\x11PBRAKE_TRANSITION\x10\x01\x12\r\n\tPBRAKE_ON\x10\x02\x12\x10\n\x0cPBRAKE_FAULT\x10\x03"\x8e\x04\n\x03Gas\x12\x1a\n\x12is_gas_pedal_error\x18\x01 \x01(\x08\x12!\n\x19is_gas_pedal_pressed_more\x18\x02 \x01(\x08\x12\x1d\n\x12gas_pedal_position\x18\x03 \x01(\x01:\x010\x12\x1b\n\x0cis_gas_valid\x18\x04 \x01(\x08:\x05false\x12\x16\n\x0ethrottle_input\x18\x05 \x01(\x01\x12\x14\n\x0cthrottle_cmd\x18\x06 \x01(\x01\x12\x17\n\x0fthrottle_output\x18\x07 \x01(\x01\x12\x17\n\x0fwatchdog_source\x18\x08 \x01(\x05\x12\x18\n\x10throttle_enabled\x18\t \x01(\x08\x12\x17\n\x0fdriver_override\x18\n \x01(\x08\x12\x17\n\x0fdriver_activity\x18\x0b \x01(\x08\x12\x16\n\x0ewatchdog_fault\x18\x0c \x01(\x08\x12\x17\n\x0fchannel_1_fault\x18\r \x01(\x08\x12\x17\n\x0fchannel_2_fault\x18\x0e \x01(\x08\x12\x17\n\x0fconnector_fault\x18\x0f \x01(\x08\x12\x19\n\x11accelerator_pedal\x18\x10 \x01(\x01\x12\x1e\n\x16accelerator_pedal_rate\x18\x11 \x01(\x01\x12\x15\n\rmajor_version\x18\x12 \x01(\x05\x12\x15\n\rminor_version\x18\x13 \x01(\x05\x12\x14\n\x0cbuild_number\x18\x14 \x01(\x05"\x88\x02\n\x03Esp\x12\x18\n\x10is_esp_acc_error\x18\x01 \x01(\x08\x12\x11\n\tis_esp_on\x18\x02 \x01(\x08\x12\x15\n\ris_esp_active\x18\x03 \x01(\x08\x12\x14\n\x0cis_abs_error\x18\x04 \x01(\x08\x12\x15\n\ris_abs_active\x18\x05 \x01(\x08\x12\x16\n\x0eis_tcsvdc_fail\x18\x06 \x01(\x08\x12\x16\n\x0eis_abs_enabled\x18\x07 \x01(\x08\x12\x16\n\x0eis_stab_active\x18\x08 \x01(\x08\x12\x17\n\x0fis_stab_enabled\x18\t \x01(\x08\x12\x16\n\x0eis_trac_active\x18\n \x01(\x08\x12\x17\n\x0fis_trac_enabled\x18\x0b \x01(\x08"\x8d\x03\n\x03Ems\x12\x1f\n\x17is_engine_acc_available\x18\x01 \x01(\x08\x12\x1b\n\x13is_engine_acc_error\x18\x02 \x01(\x08\x12-\n\x0cengine_state\x18\x03 \x01(\x0e2\x17.apollo.canbus.Ems.Type\x12\x1f\n\x17max_engine_torq_percent\x18\x04 \x01(\x01\x12\x1f\n\x17min_engine_torq_percent\x18\x05 \x01(\x01\x12!\n\x19base_engine_torq_constant\x18\x06 \x01(\x05\x12\x1d\n\x15is_engine_speed_error\x18\x07 \x01(\x08\x12\x14\n\x0cengine_speed\x18\x08 \x01(\x01\x12\x15\n\rengine_torque\x18\t \x01(\x05\x12\x1d\n\x15is_over_engine_torque\x18\n \x01(\x08\x12\x12\n\nengine_rpm\x18\x0b \x01(\x01"5\n\x04Type\x12\x08\n\x04STOP\x10\x00\x12\t\n\x05CRANK\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0b\n\x07INVALID\x10\x03"\xc6\x01\n\x04Gear\x12\x1f\n\x17is_shift_position_valid\x18\x01 \x01(\x08\x127\n\ngear_state\x18\x02 \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x12\x17\n\x0fdriver_override\x18\x03 \x01(\x08\x125\n\x08gear_cmd\x18\x04 \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x12\x14\n\x0ccanbus_fault\x18\x05 \x01(\x08"\xee\x05\n\x06Safety\x12 \n\x18is_driver_car_door_close\x18\x01 \x01(\x08\x12\x19\n\x11is_driver_buckled\x18\x02 \x01(\x08\x12\x18\n\x10emergency_button\x18\x03 \x01(\x05\x12\x18\n\thas_error\x18\x04 \x01(\x08:\x05false\x12\x1f\n\x17is_motor_invertor_fault\x18\x05 \x01(\x08\x12\x17\n\x0fis_system_fault\x18\x06 \x01(\x08\x12\x1e\n\x16is_power_battery_fault\x18\x07 \x01(\x08\x12*\n"is_motor_invertor_over_temperature\x18\x08 \x01(\x08\x12/\n\'is_small_battery_charge_discharge_fault\x18\t \x01(\x08\x12\x14\n\x0cdriving_mode\x18\n \x01(\x05\x12\x1e\n\x16is_passenger_door_open\x18\x0b \x01(\x08\x12\x1d\n\x15is_rearleft_door_open\x18\x0c \x01(\x08\x12\x1e\n\x16is_rearright_door_open\x18\r \x01(\x08\x12\x14\n\x0cis_hood_open\x18\x0e \x01(\x08\x12\x15\n\ris_trunk_open\x18\x0f \x01(\x08\x12\x1d\n\x15is_passenger_detected\x18\x10 \x01(\x08\x12#\n\x1bis_passenger_airbag_enabled\x18\x11 \x01(\x08\x12\x1c\n\x14is_passenger_buckled\x18\x12 \x01(\x08\x12\x1d\n\x15front_left_tire_press\x18\x13 \x01(\x05\x12\x1e\n\x16front_right_tire_press\x18\x14 \x01(\x05\x12\x1c\n\x14rear_left_tire_press\x18\x15 \x01(\x05\x12\x1d\n\x15rear_right_tire_press\x18\x16 \x01(\x05\x12<\n\x10car_driving_mode\x18\x17 \x01(\x0e2".apollo.canbus.Chassis.DrivingMode"\xbc\x07\n\tBasicInfo\x12\x14\n\x0cis_auto_mode\x18\x01 \x01(\x08\x122\n\x0bpower_state\x18\x02 \x01(\x0e2\x1d.apollo.canbus.BasicInfo.Type\x12\x1b\n\x13is_air_bag_deployed\x18\x03 \x01(\x08\x12\x11\n\todo_meter\x18\x04 \x01(\x01\x12\x13\n\x0bdrive_range\x18\x05 \x01(\x01\x12\x17\n\x0fis_system_error\x18\x06 \x01(\x08\x12\x1a\n\x12is_human_interrupt\x18\x07 \x01(\x08\x12\x15\n\racc_on_button\x18\x08 \x01(\x08\x12\x16\n\x0eacc_off_button\x18\t \x01(\x08\x12\x16\n\x0eacc_res_button\x18\n \x01(\x08\x12\x19\n\x11acc_cancel_button\x18\x0b \x01(\x08\x12\x19\n\x11acc_on_off_button\x18\x0c \x01(\x08\x12\x1d\n\x15acc_res_cancel_button\x18\r \x01(\x08\x12\x1a\n\x12acc_inc_spd_button\x18\x0e \x01(\x08\x12\x1a\n\x12acc_dec_spd_button\x18\x0f \x01(\x08\x12\x1a\n\x12acc_inc_gap_button\x18\x10 \x01(\x08\x12\x1a\n\x12acc_dec_gap_button\x18\x11 \x01(\x08\x12\x12\n\nlka_button\x18\x12 \x01(\x08\x12\x14\n\x0ccanbus_fault\x18\x13 \x01(\x08\x12\x10\n\x08latitude\x18\x14 \x01(\x01\x12\x11\n\tlongitude\x18\x15 \x01(\x01\x12\x11\n\tgps_valid\x18\x16 \x01(\x08\x12\x0c\n\x04year\x18\x17 \x01(\x05\x12\r\n\x05month\x18\x18 \x01(\x05\x12\x0b\n\x03day\x18\x19 \x01(\x05\x12\r\n\x05hours\x18\x1a \x01(\x05\x12\x0f\n\x07minutes\x18\x1b \x01(\x05\x12\x0f\n\x07seconds\x18\x1c \x01(\x05\x12\x19\n\x11compass_direction\x18\x1d \x01(\x01\x12\x0c\n\x04pdop\x18\x1e \x01(\x01\x12\x14\n\x0cis_gps_fault\x18\x1f \x01(\x08\x12\x13\n\x0bis_inferred\x18  \x01(\x08\x12\x10\n\x08altitude\x18! \x01(\x01\x12\x0f\n\x07heading\x18" \x01(\x01\x12\x0c\n\x04hdop\x18# \x01(\x01\x12\x0c\n\x04vdop\x18$ \x01(\x01\x12*\n\x07quality\x18% \x01(\x0e2\x19.apollo.canbus.GpsQuality\x12\x16\n\x0enum_satellites\x18& \x01(\x05\x12\x11\n\tgps_speed\x18\' \x01(\x01"8\n\x04Type\x12\x07\n\x03OFF\x10\x00\x12\x07\n\x03ACC\x10\x01\x12\x06\n\x02ON\x10\x02\x12\t\n\x05START\x10\x03\x12\x0b\n\x07INVALID\x10\x04"\xf5\x04\n\rGlobal_rpt_6a\x12E\n\rpacmod_status\x18\x01 \x01(\x0e2..apollo.canbus.Global_rpt_6a.Pacmod_statusType\x12I\n\x0foverride_status\x18\x02 \x01(\x0e20.apollo.canbus.Global_rpt_6a.Override_statusType\x12\x17\n\x0fveh_can_timeout\x18\x03 \x01(\x08\x12\x17\n\x0fstr_can_timeout\x18\x04 \x01(\x08\x12I\n\x0fbrk_can_timeout\x18\x05 \x01(\x0e20.apollo.canbus.Global_rpt_6a.Brk_can_timeoutType\x12\x17\n\x0fusr_can_timeout\x18\x06 \x01(\x08\x12\x1b\n\x13usr_can_read_errors\x18\x07 \x01(\x05"Z\n\x11Pacmod_statusType\x12"\n\x1ePACMOD_STATUS_CONTROL_DISABLED\x10\x00\x12!\n\x1dPACMOD_STATUS_CONTROL_ENABLED\x10\x01"Y\n\x13Override_statusType\x12"\n\x1eOVERRIDE_STATUS_NOT_OVERRIDDEN\x10\x00\x12\x1e\n\x1aOVERRIDE_STATUS_OVERRIDDEN\x10\x01"h\n\x13Brk_can_timeoutType\x12)\n%BRK_CAN_TIMEOUT_NO_ACTIVE_CAN_TIMEOUT\x10\x00\x12&\n"BRK_CAN_TIMEOUT_ACTIVE_CAN_TIMEOUT\x10\x01"!\n\x0cBrake_cmd_6b\x12\x11\n\tbrake_cmd\x18\x01 \x01(\x01"\xd6\x01\n\x0cBrake_rpt_6c\x12\x14\n\x0cmanual_input\x18\x01 \x01(\x01\x12\x17\n\x0fcommanded_value\x18\x02 \x01(\x01\x12\x14\n\x0coutput_value\x18\x03 \x01(\x01\x12B\n\x0cbrake_on_off\x18\x04 \x01(\x0e2,.apollo.canbus.Brake_rpt_6c.Brake_on_offType"=\n\x10Brake_on_offType\x12\x14\n\x10BRAKE_ON_OFF_OFF\x10\x00\x12\x13\n\x0fBRAKE_ON_OFF_ON\x10\x01">\n\x0fSteering_cmd_6d\x12\x16\n\x0eposition_value\x18\x01 \x01(\x01\x12\x13\n\x0bspeed_limit\x18\x02 \x01(\x01"X\n\x11Steering_rpt_1_6e\x12\x14\n\x0cmanual_input\x18\x01 \x01(\x01\x12\x17\n\x0fcommanded_value\x18\x02 \x01(\x01\x12\x14\n\x0coutput_value\x18\x03 \x01(\x01"\x8c\x01\n\x12Wheel_speed_rpt_7a\x12\x1c\n\x14wheel_spd_rear_right\x18\x01 \x01(\x05\x12\x1b\n\x13wheel_spd_rear_left\x18\x02 \x01(\x05\x12\x1d\n\x15wheel_spd_front_right\x18\x03 \x01(\x05\x12\x1c\n\x14wheel_spd_front_left\x18\x04 \x01(\x05"\x88\x01\n\x10Date_time_rpt_83\x12\x13\n\x0btime_second\x18\x01 \x01(\x05\x12\x13\n\x0btime_minute\x18\x02 \x01(\x05\x12\x11\n\ttime_hour\x18\x03 \x01(\x05\x12\x10\n\x08date_day\x18\x04 \x01(\x05\x12\x12\n\ndate_month\x18\x05 \x01(\x05\x12\x11\n\tdate_year\x18\x06 \x01(\x05"E\n\x14Brake_motor_rpt_1_70\x12\x15\n\rmotor_current\x18\x01 \x01(\x01\x12\x16\n\x0eshaft_position\x18\x02 \x01(\x01"\xc6\x04\n\x10Headlight_rpt_77\x12F\n\x0coutput_value\x18\x01 \x01(\x0e20.apollo.canbus.Headlight_rpt_77.Output_valueType\x12F\n\x0cmanual_input\x18\x02 \x01(\x0e20.apollo.canbus.Headlight_rpt_77.Manual_inputType\x12L\n\x0fcommanded_value\x18\x03 \x01(\x0e23.apollo.canbus.Headlight_rpt_77.Commanded_valueType"l\n\x10Output_valueType\x12\x1f\n\x1bOUTPUT_VALUE_HEADLIGHTS_OFF\x10\x00\x12\x1a\n\x16OUTPUT_VALUE_LOW_BEAMS\x10\x01\x12\x1b\n\x17OUTPUT_VALUE_HIGH_BEAMS\x10\x02"l\n\x10Manual_inputType\x12\x1f\n\x1bMANUAL_INPUT_HEADLIGHTS_OFF\x10\x00\x12\x1a\n\x16MANUAL_INPUT_LOW_BEAMS\x10\x01\x12\x1b\n\x17MANUAL_INPUT_HIGH_BEAMS\x10\x02"x\n\x13Commanded_valueType\x12"\n\x1eCOMMANDED_VALUE_HEADLIGHTS_OFF\x10\x00\x12\x1d\n\x19COMMANDED_VALUE_LOW_BEAMS\x10\x01\x12\x1e\n\x1aCOMMANDED_VALUE_HIGH_BEAMS\x10\x02"S\n\x0cAccel_rpt_68\x12\x14\n\x0cmanual_input\x18\x01 \x01(\x01\x12\x17\n\x0fcommanded_value\x18\x02 \x01(\x01\x12\x14\n\x0coutput_value\x18\x03 \x01(\x01"F\n\x17Steering_motor_rpt_3_75\x12\x15\n\rtorque_output\x18\x01 \x01(\x01\x12\x14\n\x0ctorque_input\x18\x02 \x01(\x01"\xd9\x01\n\x0bTurn_cmd_63\x12G\n\x0fturn_signal_cmd\x18\x01 \x01(\x0e2..apollo.canbus.Turn_cmd_63.Turn_signal_cmdType"\x80\x01\n\x13Turn_signal_cmdType\x12\x19\n\x15TURN_SIGNAL_CMD_RIGHT\x10\x00\x12\x18\n\x14TURN_SIGNAL_CMD_NONE\x10\x01\x12\x18\n\x14TURN_SIGNAL_CMD_LEFT\x10\x02\x12\x1a\n\x16TURN_SIGNAL_CMD_HAZARD\x10\x03"\xc5\x04\n\x0bTurn_rpt_64\x12A\n\x0cmanual_input\x18\x01 \x01(\x0e2+.apollo.canbus.Turn_rpt_64.Manual_inputType\x12G\n\x0fcommanded_value\x18\x02 \x01(\x0e2..apollo.canbus.Turn_rpt_64.Commanded_valueType\x12A\n\x0coutput_value\x18\x03 \x01(\x0e2+.apollo.canbus.Turn_rpt_64.Output_valueType"q\n\x10Manual_inputType\x12\x16\n\x12MANUAL_INPUT_RIGHT\x10\x00\x12\x15\n\x11MANUAL_INPUT_NONE\x10\x01\x12\x15\n\x11MANUAL_INPUT_LEFT\x10\x02\x12\x17\n\x13MANUAL_INPUT_HAZARD\x10\x03"\x80\x01\n\x13Commanded_valueType\x12\x19\n\x15COMMANDED_VALUE_RIGHT\x10\x00\x12\x18\n\x14COMMANDED_VALUE_NONE\x10\x01\x12\x18\n\x14COMMANDED_VALUE_LEFT\x10\x02\x12\x1a\n\x16COMMANDED_VALUE_HAZARD\x10\x03"q\n\x10Output_valueType\x12\x16\n\x12OUTPUT_VALUE_RIGHT\x10\x00\x12\x15\n\x11OUTPUT_VALUE_NONE\x10\x01\x12\x15\n\x11OUTPUT_VALUE_LEFT\x10\x02\x12\x17\n\x13OUTPUT_VALUE_HAZARD\x10\x03"\xc9\x01\n\x0cShift_cmd_65\x12<\n\tshift_cmd\x18\x01 \x01(\x0e2).apollo.canbus.Shift_cmd_65.Shift_cmdType"{\n\rShift_cmdType\x12\x12\n\x0eSHIFT_CMD_PARK\x10\x00\x12\x15\n\x11SHIFT_CMD_REVERSE\x10\x01\x12\x15\n\x11SHIFT_CMD_NEUTRAL\x10\x02\x12\x15\n\x11SHIFT_CMD_FORWARD\x10\x03\x12\x11\n\rSHIFT_CMD_LOW\x10\x04"\xa5\x05\n\x0cShift_rpt_66\x12B\n\x0cmanual_input\x18\x01 \x01(\x0e2,.apollo.canbus.Shift_rpt_66.Manual_inputType\x12H\n\x0fcommanded_value\x18\x02 \x01(\x0e2/.apollo.canbus.Shift_rpt_66.Commanded_valueType\x12B\n\x0coutput_value\x18\x03 \x01(\x0e2,.apollo.canbus.Shift_rpt_66.Output_valueType"\x8e\x01\n\x10Manual_inputType\x12\x15\n\x11MANUAL_INPUT_PARK\x10\x00\x12\x18\n\x14MANUAL_INPUT_REVERSE\x10\x01\x12\x18\n\x14MANUAL_INPUT_NEUTRAL\x10\x02\x12\x18\n\x14MANUAL_INPUT_FORWARD\x10\x03\x12\x15\n\x11MANUAL_INPUT_HIGH\x10\x04"\xa0\x01\n\x13Commanded_valueType\x12\x18\n\x14COMMANDED_VALUE_PARK\x10\x00\x12\x1b\n\x17COMMANDED_VALUE_REVERSE\x10\x01\x12\x1b\n\x17COMMANDED_VALUE_NEUTRAL\x10\x02\x12\x1b\n\x17COMMANDED_VALUE_FORWARD\x10\x03\x12\x18\n\x14COMMANDED_VALUE_HIGH\x10\x04"\x8e\x01\n\x10Output_valueType\x12\x15\n\x11OUTPUT_VALUE_PARK\x10\x00\x12\x18\n\x14OUTPUT_VALUE_REVERSE\x10\x01\x12\x18\n\x14OUTPUT_VALUE_NEUTRAL\x10\x02\x12\x18\n\x14OUTPUT_VALUE_FORWARD\x10\x03\x12\x15\n\x11OUTPUT_VALUE_HIGH\x10\x04"!\n\x0cAccel_cmd_67\x12\x11\n\taccel_cmd\x18\x01 \x01(\x01"\xc8\x01\n\x16Lat_lon_heading_rpt_82\x12\x0f\n\x07heading\x18\x01 \x01(\x01\x12\x19\n\x11longitude_seconds\x18\x02 \x01(\x05\x12\x19\n\x11longitude_minutes\x18\x03 \x01(\x05\x12\x19\n\x11longitude_degrees\x18\x04 \x01(\x05\x12\x18\n\x10latitude_seconds\x18\x05 \x01(\x05\x12\x18\n\x10latitude_minutes\x18\x06 \x01(\x05\x12\x18\n\x10latitude_degrees\x18\x07 \x01(\x05"\xab\x04\n\rGlobal_cmd_69\x12E\n\rpacmod_enable\x18\x01 \x01(\x0e2..apollo.canbus.Global_cmd_69.Pacmod_enableType\x12G\n\x0eclear_override\x18\x02 \x01(\x0e2/.apollo.canbus.Global_cmd_69.Clear_overrideType\x12I\n\x0fignore_override\x18\x03 \x01(\x0e20.apollo.canbus.Global_cmd_69.Ignore_overrideType"Z\n\x11Pacmod_enableType\x12"\n\x1ePACMOD_ENABLE_CONTROL_DISABLED\x10\x00\x12!\n\x1dPACMOD_ENABLE_CONTROL_ENABLED\x10\x01"p\n\x12Clear_overrideType\x12/\n+CLEAR_OVERRIDE_DON_T_CLEAR_ACTIVE_OVERRIDES\x10\x00\x12)\n%CLEAR_OVERRIDE_CLEAR_ACTIVE_OVERRIDES\x10\x01"q\n\x13Ignore_overrideType\x12/\n+IGNORE_OVERRIDE_DON_T_IGNORE_USER_OVERRIDES\x10\x00\x12)\n%IGNORE_OVERRIDE_IGNORE_USER_OVERRIDES\x10\x01"\xdc\x01\n\x1bParking_brake_status_rpt_80\x12c\n\x15parking_brake_enabled\x18\x01 \x01(\x0e2D.apollo.canbus.Parking_brake_status_rpt_80.Parking_brake_enabledType"X\n\x19Parking_brake_enabledType\x12\x1d\n\x19PARKING_BRAKE_ENABLED_OFF\x10\x00\x12\x1c\n\x18PARKING_BRAKE_ENABLED_ON\x10\x01"#\n\x0fYaw_rate_rpt_81\x12\x10\n\x08yaw_rate\x18\x01 \x01(\x01"\xa2\x03\n\x0bHorn_rpt_79\x12A\n\x0coutput_value\x18\x01 \x01(\x0e2+.apollo.canbus.Horn_rpt_79.Output_valueType\x12G\n\x0fcommanded_value\x18\x02 \x01(\x0e2..apollo.canbus.Horn_rpt_79.Commanded_valueType\x12A\n\x0cmanual_input\x18\x03 \x01(\x0e2+.apollo.canbus.Horn_rpt_79.Manual_inputType"=\n\x10Output_valueType\x12\x14\n\x10OUTPUT_VALUE_OFF\x10\x00\x12\x13\n\x0fOUTPUT_VALUE_ON\x10\x01"F\n\x13Commanded_valueType\x12\x17\n\x13COMMANDED_VALUE_OFF\x10\x00\x12\x16\n\x12COMMANDED_VALUE_ON\x10\x01"=\n\x10Manual_inputType\x12\x14\n\x10MANUAL_INPUT_OFF\x10\x00\x12\x13\n\x0fMANUAL_INPUT_ON\x10\x01"{\n\x0bHorn_cmd_78\x129\n\x08horn_cmd\x18\x01 \x01(\x0e2\'.apollo.canbus.Horn_cmd_78.Horn_cmdType"1\n\x0cHorn_cmdType\x12\x10\n\x0cHORN_CMD_OFF\x10\x00\x12\x0f\n\x0bHORN_CMD_ON\x10\x01"\x87\x08\n\x0cWiper_rpt_91\x12B\n\x0coutput_value\x18\x01 \x01(\x0e2,.apollo.canbus.Wiper_rpt_91.Output_valueType\x12H\n\x0fcommanded_value\x18\x02 \x01(\x0e2/.apollo.canbus.Wiper_rpt_91.Commanded_valueType\x12B\n\x0cmanual_input\x18\x03 \x01(\x0e2,.apollo.canbus.Wiper_rpt_91.Manual_inputType"\x81\x02\n\x10Output_valueType\x12\x1b\n\x17OUTPUT_VALUE_WIPERS_OFF\x10\x00\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_1\x10\x01\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_2\x10\x02\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_3\x10\x03\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_4\x10\x04\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_5\x10\x05\x12\x14\n\x10OUTPUT_VALUE_LOW\x10\x06\x12\x15\n\x11OUTPUT_VALUE_HIGH\x10\x07"\x9c\x02\n\x13Commanded_valueType\x12\x1e\n\x1aCOMMANDED_VALUE_WIPERS_OFF\x10\x00\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_1\x10\x01\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_2\x10\x02\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_3\x10\x03\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_4\x10\x04\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_5\x10\x05\x12\x17\n\x13COMMANDED_VALUE_LOW\x10\x06\x12\x18\n\x14COMMANDED_VALUE_HIGH\x10\x07"\x81\x02\n\x10Manual_inputType\x12\x1b\n\x17MANUAL_INPUT_WIPERS_OFF\x10\x00\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_1\x10\x01\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_2\x10\x02\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_3\x10\x03\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_4\x10\x04\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_5\x10\x05\x12\x14\n\x10MANUAL_INPUT_LOW\x10\x06\x12\x15\n\x11MANUAL_INPUT_HIGH\x10\x07"\xe2\x01\n\x14Vehicle_speed_rpt_6f\x12\x15\n\rvehicle_speed\x18\x01 \x01(\x01\x12X\n\x13vehicle_speed_valid\x18\x02 \x01(\x0e2;.apollo.canbus.Vehicle_speed_rpt_6f.Vehicle_speed_validType"Y\n\x17Vehicle_speed_validType\x12\x1f\n\x1bVEHICLE_SPEED_VALID_INVALID\x10\x00\x12\x1d\n\x19VEHICLE_SPEED_VALID_VALID\x10\x01"\xce\x01\n\x10Headlight_cmd_76\x12H\n\rheadlight_cmd\x18\x01 \x01(\x0e21.apollo.canbus.Headlight_cmd_76.Headlight_cmdType"p\n\x11Headlight_cmdType\x12 \n\x1cHEADLIGHT_CMD_HEADLIGHTS_OFF\x10\x00\x12\x1b\n\x17HEADLIGHT_CMD_LOW_BEAMS\x10\x01\x12\x1c\n\x18HEADLIGHT_CMD_HIGH_BEAMS\x10\x02"h\n\x17Steering_motor_rpt_2_74\x12\x1b\n\x13encoder_temperature\x18\x01 \x01(\x05\x12\x19\n\x11motor_temperature\x18\x02 \x01(\x05\x12\x15\n\rangular_speed\x18\x03 \x01(\x01"e\n\x14Brake_motor_rpt_2_71\x12\x1b\n\x13encoder_temperature\x18\x01 \x01(\x05\x12\x19\n\x11motor_temperature\x18\x02 \x01(\x05\x12\x15\n\rangular_speed\x18\x03 \x01(\x01"H\n\x17Steering_motor_rpt_1_73\x12\x15\n\rmotor_current\x18\x01 \x01(\x01\x12\x16\n\x0eshaft_position\x18\x02 \x01(\x01"\xb5\x02\n\x0cWiper_cmd_90\x12<\n\twiper_cmd\x18\x01 \x01(\x0e2).apollo.canbus.Wiper_cmd_90.Wiper_cmdType"\xe6\x01\n\rWiper_cmdType\x12\x18\n\x14WIPER_CMD_WIPERS_OFF\x10\x00\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_1\x10\x01\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_2\x10\x02\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_3\x10\x03\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_4\x10\x04\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_5\x10\x05\x12\x11\n\rWIPER_CMD_LOW\x10\x06\x12\x12\n\x0eWIPER_CMD_HIGH\x10\x07"C\n\x14Brake_motor_rpt_3_72\x12\x15\n\rtorque_output\x18\x01 \x01(\x01\x12\x14\n\x0ctorque_input\x18\x02 \x01(\x01"\xe9\r\n\x03Gem\x123\n\rglobal_rpt_6a\x18\x01 \x01(\x0b2\x1c.apollo.canbus.Global_rpt_6a\x121\n\x0cbrake_cmd_6b\x18\x02 \x01(\x0b2\x1b.apollo.canbus.Brake_cmd_6b\x121\n\x0cbrake_rpt_6c\x18\x03 \x01(\x0b2\x1b.apollo.canbus.Brake_rpt_6c\x127\n\x0fsteering_cmd_6d\x18\x04 \x01(\x0b2\x1e.apollo.canbus.Steering_cmd_6d\x12;\n\x11steering_rpt_1_6e\x18\x05 \x01(\x0b2 .apollo.canbus.Steering_rpt_1_6e\x12=\n\x12wheel_speed_rpt_7a\x18\x06 \x01(\x0b2!.apollo.canbus.Wheel_speed_rpt_7a\x129\n\x10date_time_rpt_83\x18\x07 \x01(\x0b2\x1f.apollo.canbus.Date_time_rpt_83\x12A\n\x14brake_motor_rpt_1_70\x18\x08 \x01(\x0b2#.apollo.canbus.Brake_motor_rpt_1_70\x129\n\x10headlight_rpt_77\x18\t \x01(\x0b2\x1f.apollo.canbus.Headlight_rpt_77\x121\n\x0caccel_rpt_68\x18\n \x01(\x0b2\x1b.apollo.canbus.Accel_rpt_68\x12G\n\x17steering_motor_rpt_3_75\x18\x0b \x01(\x0b2&.apollo.canbus.Steering_motor_rpt_3_75\x12/\n\x0bturn_cmd_63\x18\x0c \x01(\x0b2\x1a.apollo.canbus.Turn_cmd_63\x12/\n\x0bturn_rpt_64\x18\r \x01(\x0b2\x1a.apollo.canbus.Turn_rpt_64\x121\n\x0cshift_cmd_65\x18\x0e \x01(\x0b2\x1b.apollo.canbus.Shift_cmd_65\x121\n\x0cshift_rpt_66\x18\x0f \x01(\x0b2\x1b.apollo.canbus.Shift_rpt_66\x121\n\x0caccel_cmd_67\x18\x10 \x01(\x0b2\x1b.apollo.canbus.Accel_cmd_67\x12E\n\x16lat_lon_heading_rpt_82\x18\x11 \x01(\x0b2%.apollo.canbus.Lat_lon_heading_rpt_82\x123\n\rglobal_cmd_69\x18\x12 \x01(\x0b2\x1c.apollo.canbus.Global_cmd_69\x12O\n\x1bparking_brake_status_rpt_80\x18\x13 \x01(\x0b2*.apollo.canbus.Parking_brake_status_rpt_80\x127\n\x0fyaw_rate_rpt_81\x18\x14 \x01(\x0b2\x1e.apollo.canbus.Yaw_rate_rpt_81\x12/\n\x0bhorn_rpt_79\x18\x15 \x01(\x0b2\x1a.apollo.canbus.Horn_rpt_79\x12/\n\x0bhorn_cmd_78\x18\x16 \x01(\x0b2\x1a.apollo.canbus.Horn_cmd_78\x121\n\x0cwiper_rpt_91\x18\x17 \x01(\x0b2\x1b.apollo.canbus.Wiper_rpt_91\x12A\n\x14vehicle_speed_rpt_6f\x18\x18 \x01(\x0b2#.apollo.canbus.Vehicle_speed_rpt_6f\x129\n\x10headlight_cmd_76\x18\x19 \x01(\x0b2\x1f.apollo.canbus.Headlight_cmd_76\x12G\n\x17steering_motor_rpt_2_74\x18\x1a \x01(\x0b2&.apollo.canbus.Steering_motor_rpt_2_74\x12A\n\x14brake_motor_rpt_2_71\x18\x1b \x01(\x0b2#.apollo.canbus.Brake_motor_rpt_2_71\x12G\n\x17steering_motor_rpt_1_73\x18\x1c \x01(\x0b2&.apollo.canbus.Steering_motor_rpt_1_73\x121\n\x0cwiper_cmd_90\x18\x1d \x01(\x0b2\x1b.apollo.canbus.Wiper_cmd_90\x12A\n\x14brake_motor_rpt_3_72\x18\x1e \x01(\x0b2#.apollo.canbus.Brake_motor_rpt_3_72')
_CHASSISDETAIL = DESCRIPTOR.message_types_by_name['ChassisDetail']
_CHECKRESPONSESIGNAL = DESCRIPTOR.message_types_by_name['CheckResponseSignal']
_BATTERY = DESCRIPTOR.message_types_by_name['Battery']
_LIGHT = DESCRIPTOR.message_types_by_name['Light']
_EPS = DESCRIPTOR.message_types_by_name['Eps']
_VEHICLESPD = DESCRIPTOR.message_types_by_name['VehicleSpd']
_DECELERATION = DESCRIPTOR.message_types_by_name['Deceleration']
_BRAKE = DESCRIPTOR.message_types_by_name['Brake']
_EPB = DESCRIPTOR.message_types_by_name['Epb']
_GAS = DESCRIPTOR.message_types_by_name['Gas']
_ESP = DESCRIPTOR.message_types_by_name['Esp']
_EMS = DESCRIPTOR.message_types_by_name['Ems']
_GEAR = DESCRIPTOR.message_types_by_name['Gear']
_SAFETY = DESCRIPTOR.message_types_by_name['Safety']
_BASICINFO = DESCRIPTOR.message_types_by_name['BasicInfo']
_GLOBAL_RPT_6A = DESCRIPTOR.message_types_by_name['Global_rpt_6a']
_BRAKE_CMD_6B = DESCRIPTOR.message_types_by_name['Brake_cmd_6b']
_BRAKE_RPT_6C = DESCRIPTOR.message_types_by_name['Brake_rpt_6c']
_STEERING_CMD_6D = DESCRIPTOR.message_types_by_name['Steering_cmd_6d']
_STEERING_RPT_1_6E = DESCRIPTOR.message_types_by_name['Steering_rpt_1_6e']
_WHEEL_SPEED_RPT_7A = DESCRIPTOR.message_types_by_name['Wheel_speed_rpt_7a']
_DATE_TIME_RPT_83 = DESCRIPTOR.message_types_by_name['Date_time_rpt_83']
_BRAKE_MOTOR_RPT_1_70 = DESCRIPTOR.message_types_by_name['Brake_motor_rpt_1_70']
_HEADLIGHT_RPT_77 = DESCRIPTOR.message_types_by_name['Headlight_rpt_77']
_ACCEL_RPT_68 = DESCRIPTOR.message_types_by_name['Accel_rpt_68']
_STEERING_MOTOR_RPT_3_75 = DESCRIPTOR.message_types_by_name['Steering_motor_rpt_3_75']
_TURN_CMD_63 = DESCRIPTOR.message_types_by_name['Turn_cmd_63']
_TURN_RPT_64 = DESCRIPTOR.message_types_by_name['Turn_rpt_64']
_SHIFT_CMD_65 = DESCRIPTOR.message_types_by_name['Shift_cmd_65']
_SHIFT_RPT_66 = DESCRIPTOR.message_types_by_name['Shift_rpt_66']
_ACCEL_CMD_67 = DESCRIPTOR.message_types_by_name['Accel_cmd_67']
_LAT_LON_HEADING_RPT_82 = DESCRIPTOR.message_types_by_name['Lat_lon_heading_rpt_82']
_GLOBAL_CMD_69 = DESCRIPTOR.message_types_by_name['Global_cmd_69']
_PARKING_BRAKE_STATUS_RPT_80 = DESCRIPTOR.message_types_by_name['Parking_brake_status_rpt_80']
_YAW_RATE_RPT_81 = DESCRIPTOR.message_types_by_name['Yaw_rate_rpt_81']
_HORN_RPT_79 = DESCRIPTOR.message_types_by_name['Horn_rpt_79']
_HORN_CMD_78 = DESCRIPTOR.message_types_by_name['Horn_cmd_78']
_WIPER_RPT_91 = DESCRIPTOR.message_types_by_name['Wiper_rpt_91']
_VEHICLE_SPEED_RPT_6F = DESCRIPTOR.message_types_by_name['Vehicle_speed_rpt_6f']
_HEADLIGHT_CMD_76 = DESCRIPTOR.message_types_by_name['Headlight_cmd_76']
_STEERING_MOTOR_RPT_2_74 = DESCRIPTOR.message_types_by_name['Steering_motor_rpt_2_74']
_BRAKE_MOTOR_RPT_2_71 = DESCRIPTOR.message_types_by_name['Brake_motor_rpt_2_71']
_STEERING_MOTOR_RPT_1_73 = DESCRIPTOR.message_types_by_name['Steering_motor_rpt_1_73']
_WIPER_CMD_90 = DESCRIPTOR.message_types_by_name['Wiper_cmd_90']
_BRAKE_MOTOR_RPT_3_72 = DESCRIPTOR.message_types_by_name['Brake_motor_rpt_3_72']
_GEM = DESCRIPTOR.message_types_by_name['Gem']
_CHASSISDETAIL_TYPE = _CHASSISDETAIL.enum_types_by_name['Type']
_LIGHT_TURNLIGHTTYPE = _LIGHT.enum_types_by_name['TurnLightType']
_LIGHT_BEAMLAMPTYPE = _LIGHT.enum_types_by_name['BeamLampType']
_LIGHT_LINCOLNLAMPTYPE = _LIGHT.enum_types_by_name['LincolnLampType']
_LIGHT_LINCOLNWIPERTYPE = _LIGHT.enum_types_by_name['LincolnWiperType']
_LIGHT_LINCOLNAMBIENTTYPE = _LIGHT.enum_types_by_name['LincolnAmbientType']
_EPS_TYPE = _EPS.enum_types_by_name['Type']
_BRAKE_HSASTATUSTYPE = _BRAKE.enum_types_by_name['HSAStatusType']
_BRAKE_HSAMODETYPE = _BRAKE.enum_types_by_name['HSAModeType']
_EPB_PBRAKETYPE = _EPB.enum_types_by_name['PBrakeType']
_EMS_TYPE = _EMS.enum_types_by_name['Type']
_BASICINFO_TYPE = _BASICINFO.enum_types_by_name['Type']
_GLOBAL_RPT_6A_PACMOD_STATUSTYPE = _GLOBAL_RPT_6A.enum_types_by_name['Pacmod_statusType']
_GLOBAL_RPT_6A_OVERRIDE_STATUSTYPE = _GLOBAL_RPT_6A.enum_types_by_name['Override_statusType']
_GLOBAL_RPT_6A_BRK_CAN_TIMEOUTTYPE = _GLOBAL_RPT_6A.enum_types_by_name['Brk_can_timeoutType']
_BRAKE_RPT_6C_BRAKE_ON_OFFTYPE = _BRAKE_RPT_6C.enum_types_by_name['Brake_on_offType']
_HEADLIGHT_RPT_77_OUTPUT_VALUETYPE = _HEADLIGHT_RPT_77.enum_types_by_name['Output_valueType']
_HEADLIGHT_RPT_77_MANUAL_INPUTTYPE = _HEADLIGHT_RPT_77.enum_types_by_name['Manual_inputType']
_HEADLIGHT_RPT_77_COMMANDED_VALUETYPE = _HEADLIGHT_RPT_77.enum_types_by_name['Commanded_valueType']
_TURN_CMD_63_TURN_SIGNAL_CMDTYPE = _TURN_CMD_63.enum_types_by_name['Turn_signal_cmdType']
_TURN_RPT_64_MANUAL_INPUTTYPE = _TURN_RPT_64.enum_types_by_name['Manual_inputType']
_TURN_RPT_64_COMMANDED_VALUETYPE = _TURN_RPT_64.enum_types_by_name['Commanded_valueType']
_TURN_RPT_64_OUTPUT_VALUETYPE = _TURN_RPT_64.enum_types_by_name['Output_valueType']
_SHIFT_CMD_65_SHIFT_CMDTYPE = _SHIFT_CMD_65.enum_types_by_name['Shift_cmdType']
_SHIFT_RPT_66_MANUAL_INPUTTYPE = _SHIFT_RPT_66.enum_types_by_name['Manual_inputType']
_SHIFT_RPT_66_COMMANDED_VALUETYPE = _SHIFT_RPT_66.enum_types_by_name['Commanded_valueType']
_SHIFT_RPT_66_OUTPUT_VALUETYPE = _SHIFT_RPT_66.enum_types_by_name['Output_valueType']
_GLOBAL_CMD_69_PACMOD_ENABLETYPE = _GLOBAL_CMD_69.enum_types_by_name['Pacmod_enableType']
_GLOBAL_CMD_69_CLEAR_OVERRIDETYPE = _GLOBAL_CMD_69.enum_types_by_name['Clear_overrideType']
_GLOBAL_CMD_69_IGNORE_OVERRIDETYPE = _GLOBAL_CMD_69.enum_types_by_name['Ignore_overrideType']
_PARKING_BRAKE_STATUS_RPT_80_PARKING_BRAKE_ENABLEDTYPE = _PARKING_BRAKE_STATUS_RPT_80.enum_types_by_name['Parking_brake_enabledType']
_HORN_RPT_79_OUTPUT_VALUETYPE = _HORN_RPT_79.enum_types_by_name['Output_valueType']
_HORN_RPT_79_COMMANDED_VALUETYPE = _HORN_RPT_79.enum_types_by_name['Commanded_valueType']
_HORN_RPT_79_MANUAL_INPUTTYPE = _HORN_RPT_79.enum_types_by_name['Manual_inputType']
_HORN_CMD_78_HORN_CMDTYPE = _HORN_CMD_78.enum_types_by_name['Horn_cmdType']
_WIPER_RPT_91_OUTPUT_VALUETYPE = _WIPER_RPT_91.enum_types_by_name['Output_valueType']
_WIPER_RPT_91_COMMANDED_VALUETYPE = _WIPER_RPT_91.enum_types_by_name['Commanded_valueType']
_WIPER_RPT_91_MANUAL_INPUTTYPE = _WIPER_RPT_91.enum_types_by_name['Manual_inputType']
_VEHICLE_SPEED_RPT_6F_VEHICLE_SPEED_VALIDTYPE = _VEHICLE_SPEED_RPT_6F.enum_types_by_name['Vehicle_speed_validType']
_HEADLIGHT_CMD_76_HEADLIGHT_CMDTYPE = _HEADLIGHT_CMD_76.enum_types_by_name['Headlight_cmdType']
_WIPER_CMD_90_WIPER_CMDTYPE = _WIPER_CMD_90.enum_types_by_name['Wiper_cmdType']
ChassisDetail = _reflection.GeneratedProtocolMessageType('ChassisDetail', (_message.Message,), {'DESCRIPTOR': _CHASSISDETAIL, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(ChassisDetail)
CheckResponseSignal = _reflection.GeneratedProtocolMessageType('CheckResponseSignal', (_message.Message,), {'DESCRIPTOR': _CHECKRESPONSESIGNAL, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(CheckResponseSignal)
Battery = _reflection.GeneratedProtocolMessageType('Battery', (_message.Message,), {'DESCRIPTOR': _BATTERY, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Battery)
Light = _reflection.GeneratedProtocolMessageType('Light', (_message.Message,), {'DESCRIPTOR': _LIGHT, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Light)
Eps = _reflection.GeneratedProtocolMessageType('Eps', (_message.Message,), {'DESCRIPTOR': _EPS, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Eps)
VehicleSpd = _reflection.GeneratedProtocolMessageType('VehicleSpd', (_message.Message,), {'DESCRIPTOR': _VEHICLESPD, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(VehicleSpd)
Deceleration = _reflection.GeneratedProtocolMessageType('Deceleration', (_message.Message,), {'DESCRIPTOR': _DECELERATION, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Deceleration)
Brake = _reflection.GeneratedProtocolMessageType('Brake', (_message.Message,), {'DESCRIPTOR': _BRAKE, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Brake)
Epb = _reflection.GeneratedProtocolMessageType('Epb', (_message.Message,), {'DESCRIPTOR': _EPB, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Epb)
Gas = _reflection.GeneratedProtocolMessageType('Gas', (_message.Message,), {'DESCRIPTOR': _GAS, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Gas)
Esp = _reflection.GeneratedProtocolMessageType('Esp', (_message.Message,), {'DESCRIPTOR': _ESP, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Esp)
Ems = _reflection.GeneratedProtocolMessageType('Ems', (_message.Message,), {'DESCRIPTOR': _EMS, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Ems)
Gear = _reflection.GeneratedProtocolMessageType('Gear', (_message.Message,), {'DESCRIPTOR': _GEAR, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Gear)
Safety = _reflection.GeneratedProtocolMessageType('Safety', (_message.Message,), {'DESCRIPTOR': _SAFETY, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Safety)
BasicInfo = _reflection.GeneratedProtocolMessageType('BasicInfo', (_message.Message,), {'DESCRIPTOR': _BASICINFO, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(BasicInfo)
Global_rpt_6a = _reflection.GeneratedProtocolMessageType('Global_rpt_6a', (_message.Message,), {'DESCRIPTOR': _GLOBAL_RPT_6A, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Global_rpt_6a)
Brake_cmd_6b = _reflection.GeneratedProtocolMessageType('Brake_cmd_6b', (_message.Message,), {'DESCRIPTOR': _BRAKE_CMD_6B, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Brake_cmd_6b)
Brake_rpt_6c = _reflection.GeneratedProtocolMessageType('Brake_rpt_6c', (_message.Message,), {'DESCRIPTOR': _BRAKE_RPT_6C, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Brake_rpt_6c)
Steering_cmd_6d = _reflection.GeneratedProtocolMessageType('Steering_cmd_6d', (_message.Message,), {'DESCRIPTOR': _STEERING_CMD_6D, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Steering_cmd_6d)
Steering_rpt_1_6e = _reflection.GeneratedProtocolMessageType('Steering_rpt_1_6e', (_message.Message,), {'DESCRIPTOR': _STEERING_RPT_1_6E, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Steering_rpt_1_6e)
Wheel_speed_rpt_7a = _reflection.GeneratedProtocolMessageType('Wheel_speed_rpt_7a', (_message.Message,), {'DESCRIPTOR': _WHEEL_SPEED_RPT_7A, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Wheel_speed_rpt_7a)
Date_time_rpt_83 = _reflection.GeneratedProtocolMessageType('Date_time_rpt_83', (_message.Message,), {'DESCRIPTOR': _DATE_TIME_RPT_83, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Date_time_rpt_83)
Brake_motor_rpt_1_70 = _reflection.GeneratedProtocolMessageType('Brake_motor_rpt_1_70', (_message.Message,), {'DESCRIPTOR': _BRAKE_MOTOR_RPT_1_70, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Brake_motor_rpt_1_70)
Headlight_rpt_77 = _reflection.GeneratedProtocolMessageType('Headlight_rpt_77', (_message.Message,), {'DESCRIPTOR': _HEADLIGHT_RPT_77, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Headlight_rpt_77)
Accel_rpt_68 = _reflection.GeneratedProtocolMessageType('Accel_rpt_68', (_message.Message,), {'DESCRIPTOR': _ACCEL_RPT_68, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Accel_rpt_68)
Steering_motor_rpt_3_75 = _reflection.GeneratedProtocolMessageType('Steering_motor_rpt_3_75', (_message.Message,), {'DESCRIPTOR': _STEERING_MOTOR_RPT_3_75, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Steering_motor_rpt_3_75)
Turn_cmd_63 = _reflection.GeneratedProtocolMessageType('Turn_cmd_63', (_message.Message,), {'DESCRIPTOR': _TURN_CMD_63, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Turn_cmd_63)
Turn_rpt_64 = _reflection.GeneratedProtocolMessageType('Turn_rpt_64', (_message.Message,), {'DESCRIPTOR': _TURN_RPT_64, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Turn_rpt_64)
Shift_cmd_65 = _reflection.GeneratedProtocolMessageType('Shift_cmd_65', (_message.Message,), {'DESCRIPTOR': _SHIFT_CMD_65, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Shift_cmd_65)
Shift_rpt_66 = _reflection.GeneratedProtocolMessageType('Shift_rpt_66', (_message.Message,), {'DESCRIPTOR': _SHIFT_RPT_66, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Shift_rpt_66)
Accel_cmd_67 = _reflection.GeneratedProtocolMessageType('Accel_cmd_67', (_message.Message,), {'DESCRIPTOR': _ACCEL_CMD_67, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Accel_cmd_67)
Lat_lon_heading_rpt_82 = _reflection.GeneratedProtocolMessageType('Lat_lon_heading_rpt_82', (_message.Message,), {'DESCRIPTOR': _LAT_LON_HEADING_RPT_82, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Lat_lon_heading_rpt_82)
Global_cmd_69 = _reflection.GeneratedProtocolMessageType('Global_cmd_69', (_message.Message,), {'DESCRIPTOR': _GLOBAL_CMD_69, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Global_cmd_69)
Parking_brake_status_rpt_80 = _reflection.GeneratedProtocolMessageType('Parking_brake_status_rpt_80', (_message.Message,), {'DESCRIPTOR': _PARKING_BRAKE_STATUS_RPT_80, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Parking_brake_status_rpt_80)
Yaw_rate_rpt_81 = _reflection.GeneratedProtocolMessageType('Yaw_rate_rpt_81', (_message.Message,), {'DESCRIPTOR': _YAW_RATE_RPT_81, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Yaw_rate_rpt_81)
Horn_rpt_79 = _reflection.GeneratedProtocolMessageType('Horn_rpt_79', (_message.Message,), {'DESCRIPTOR': _HORN_RPT_79, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Horn_rpt_79)
Horn_cmd_78 = _reflection.GeneratedProtocolMessageType('Horn_cmd_78', (_message.Message,), {'DESCRIPTOR': _HORN_CMD_78, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Horn_cmd_78)
Wiper_rpt_91 = _reflection.GeneratedProtocolMessageType('Wiper_rpt_91', (_message.Message,), {'DESCRIPTOR': _WIPER_RPT_91, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Wiper_rpt_91)
Vehicle_speed_rpt_6f = _reflection.GeneratedProtocolMessageType('Vehicle_speed_rpt_6f', (_message.Message,), {'DESCRIPTOR': _VEHICLE_SPEED_RPT_6F, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Vehicle_speed_rpt_6f)
Headlight_cmd_76 = _reflection.GeneratedProtocolMessageType('Headlight_cmd_76', (_message.Message,), {'DESCRIPTOR': _HEADLIGHT_CMD_76, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Headlight_cmd_76)
Steering_motor_rpt_2_74 = _reflection.GeneratedProtocolMessageType('Steering_motor_rpt_2_74', (_message.Message,), {'DESCRIPTOR': _STEERING_MOTOR_RPT_2_74, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Steering_motor_rpt_2_74)
Brake_motor_rpt_2_71 = _reflection.GeneratedProtocolMessageType('Brake_motor_rpt_2_71', (_message.Message,), {'DESCRIPTOR': _BRAKE_MOTOR_RPT_2_71, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Brake_motor_rpt_2_71)
Steering_motor_rpt_1_73 = _reflection.GeneratedProtocolMessageType('Steering_motor_rpt_1_73', (_message.Message,), {'DESCRIPTOR': _STEERING_MOTOR_RPT_1_73, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Steering_motor_rpt_1_73)
Wiper_cmd_90 = _reflection.GeneratedProtocolMessageType('Wiper_cmd_90', (_message.Message,), {'DESCRIPTOR': _WIPER_CMD_90, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Wiper_cmd_90)
Brake_motor_rpt_3_72 = _reflection.GeneratedProtocolMessageType('Brake_motor_rpt_3_72', (_message.Message,), {'DESCRIPTOR': _BRAKE_MOTOR_RPT_3_72, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Brake_motor_rpt_3_72)
Gem = _reflection.GeneratedProtocolMessageType('Gem', (_message.Message,), {'DESCRIPTOR': _GEM, '__module__': 'modules.canbus.proto.chassis_detail_pb2'})
_sym_db.RegisterMessage(Gem)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CHASSISDETAIL.fields_by_name['license']._options = None
    _CHASSISDETAIL.fields_by_name['license']._serialized_options = b'\x18\x01'
    _CHASSISDETAIL._serialized_start = 424
    _CHASSISDETAIL._serialized_end = 1564
    _CHASSISDETAIL_TYPE._serialized_start = 1519
    _CHASSISDETAIL_TYPE._serialized_end = 1564
    _CHECKRESPONSESIGNAL._serialized_start = 1567
    _CHECKRESPONSESIGNAL._serialized_end = 1802
    _BATTERY._serialized_start = 1804
    _BATTERY._serialized_end = 1858
    _LIGHT._serialized_start = 1861
    _LIGHT._serialized_end = 3062
    _LIGHT_TURNLIGHTTYPE._serialized_start = 2293
    _LIGHT_TURNLIGHTTYPE._serialized_end = 2384
    _LIGHT_BEAMLAMPTYPE._serialized_start = 2386
    _LIGHT_BEAMLAMPTYPE._serialized_end = 2449
    _LIGHT_LINCOLNLAMPTYPE._serialized_start = 2451
    _LIGHT_LINCOLNLAMPTYPE._serialized_end = 2540
    _LIGHT_LINCOLNWIPERTYPE._serialized_start = 2543
    _LIGHT_LINCOLNWIPERTYPE._serialized_end = 2891
    _LIGHT_LINCOLNAMBIENTTYPE._serialized_start = 2894
    _LIGHT_LINCOLNAMBIENTTYPE._serialized_end = 3062
    _EPS._serialized_start = 3065
    _EPS._serialized_end = 3838
    _EPS_TYPE._serialized_start = 3777
    _EPS_TYPE._serialized_end = 3838
    _VEHICLESPD._serialized_start = 3841
    _VEHICLESPD._serialized_end = 4716
    _DECELERATION._serialized_start = 4719
    _DECELERATION._serialized_end = 4929
    _BRAKE._serialized_start = 4932
    _BRAKE._serialized_end = 6010
    _BRAKE_HSASTATUSTYPE._serialized_start = 5741
    _BRAKE_HSASTATUSTYPE._serialized_end = 5928
    _BRAKE_HSAMODETYPE._serialized_start = 5930
    _BRAKE_HSAMODETYPE._serialized_end = 6010
    _EPB._serialized_start = 6013
    _EPB._serialized_end = 6232
    _EPB_PBRAKETYPE._serialized_start = 6148
    _EPB_PBRAKETYPE._serialized_end = 6232
    _GAS._serialized_start = 6235
    _GAS._serialized_end = 6761
    _ESP._serialized_start = 6764
    _ESP._serialized_end = 7028
    _EMS._serialized_start = 7031
    _EMS._serialized_end = 7428
    _EMS_TYPE._serialized_start = 7375
    _EMS_TYPE._serialized_end = 7428
    _GEAR._serialized_start = 7431
    _GEAR._serialized_end = 7629
    _SAFETY._serialized_start = 7632
    _SAFETY._serialized_end = 8382
    _BASICINFO._serialized_start = 8385
    _BASICINFO._serialized_end = 9341
    _BASICINFO_TYPE._serialized_start = 9285
    _BASICINFO_TYPE._serialized_end = 9341
    _GLOBAL_RPT_6A._serialized_start = 9344
    _GLOBAL_RPT_6A._serialized_end = 9973
    _GLOBAL_RPT_6A_PACMOD_STATUSTYPE._serialized_start = 9686
    _GLOBAL_RPT_6A_PACMOD_STATUSTYPE._serialized_end = 9776
    _GLOBAL_RPT_6A_OVERRIDE_STATUSTYPE._serialized_start = 9778
    _GLOBAL_RPT_6A_OVERRIDE_STATUSTYPE._serialized_end = 9867
    _GLOBAL_RPT_6A_BRK_CAN_TIMEOUTTYPE._serialized_start = 9869
    _GLOBAL_RPT_6A_BRK_CAN_TIMEOUTTYPE._serialized_end = 9973
    _BRAKE_CMD_6B._serialized_start = 9975
    _BRAKE_CMD_6B._serialized_end = 10008
    _BRAKE_RPT_6C._serialized_start = 10011
    _BRAKE_RPT_6C._serialized_end = 10225
    _BRAKE_RPT_6C_BRAKE_ON_OFFTYPE._serialized_start = 10164
    _BRAKE_RPT_6C_BRAKE_ON_OFFTYPE._serialized_end = 10225
    _STEERING_CMD_6D._serialized_start = 10227
    _STEERING_CMD_6D._serialized_end = 10289
    _STEERING_RPT_1_6E._serialized_start = 10291
    _STEERING_RPT_1_6E._serialized_end = 10379
    _WHEEL_SPEED_RPT_7A._serialized_start = 10382
    _WHEEL_SPEED_RPT_7A._serialized_end = 10522
    _DATE_TIME_RPT_83._serialized_start = 10525
    _DATE_TIME_RPT_83._serialized_end = 10661
    _BRAKE_MOTOR_RPT_1_70._serialized_start = 10663
    _BRAKE_MOTOR_RPT_1_70._serialized_end = 10732
    _HEADLIGHT_RPT_77._serialized_start = 10735
    _HEADLIGHT_RPT_77._serialized_end = 11317
    _HEADLIGHT_RPT_77_OUTPUT_VALUETYPE._serialized_start = 10977
    _HEADLIGHT_RPT_77_OUTPUT_VALUETYPE._serialized_end = 11085
    _HEADLIGHT_RPT_77_MANUAL_INPUTTYPE._serialized_start = 11087
    _HEADLIGHT_RPT_77_MANUAL_INPUTTYPE._serialized_end = 11195
    _HEADLIGHT_RPT_77_COMMANDED_VALUETYPE._serialized_start = 11197
    _HEADLIGHT_RPT_77_COMMANDED_VALUETYPE._serialized_end = 11317
    _ACCEL_RPT_68._serialized_start = 11319
    _ACCEL_RPT_68._serialized_end = 11402
    _STEERING_MOTOR_RPT_3_75._serialized_start = 11404
    _STEERING_MOTOR_RPT_3_75._serialized_end = 11474
    _TURN_CMD_63._serialized_start = 11477
    _TURN_CMD_63._serialized_end = 11694
    _TURN_CMD_63_TURN_SIGNAL_CMDTYPE._serialized_start = 11566
    _TURN_CMD_63_TURN_SIGNAL_CMDTYPE._serialized_end = 11694
    _TURN_RPT_64._serialized_start = 11697
    _TURN_RPT_64._serialized_end = 12278
    _TURN_RPT_64_MANUAL_INPUTTYPE._serialized_start = 11919
    _TURN_RPT_64_MANUAL_INPUTTYPE._serialized_end = 12032
    _TURN_RPT_64_COMMANDED_VALUETYPE._serialized_start = 12035
    _TURN_RPT_64_COMMANDED_VALUETYPE._serialized_end = 12163
    _TURN_RPT_64_OUTPUT_VALUETYPE._serialized_start = 12165
    _TURN_RPT_64_OUTPUT_VALUETYPE._serialized_end = 12278
    _SHIFT_CMD_65._serialized_start = 12281
    _SHIFT_CMD_65._serialized_end = 12482
    _SHIFT_CMD_65_SHIFT_CMDTYPE._serialized_start = 12359
    _SHIFT_CMD_65_SHIFT_CMDTYPE._serialized_end = 12482
    _SHIFT_RPT_66._serialized_start = 12485
    _SHIFT_RPT_66._serialized_end = 13162
    _SHIFT_RPT_66_MANUAL_INPUTTYPE._serialized_start = 12712
    _SHIFT_RPT_66_MANUAL_INPUTTYPE._serialized_end = 12854
    _SHIFT_RPT_66_COMMANDED_VALUETYPE._serialized_start = 12857
    _SHIFT_RPT_66_COMMANDED_VALUETYPE._serialized_end = 13017
    _SHIFT_RPT_66_OUTPUT_VALUETYPE._serialized_start = 13020
    _SHIFT_RPT_66_OUTPUT_VALUETYPE._serialized_end = 13162
    _ACCEL_CMD_67._serialized_start = 13164
    _ACCEL_CMD_67._serialized_end = 13197
    _LAT_LON_HEADING_RPT_82._serialized_start = 13200
    _LAT_LON_HEADING_RPT_82._serialized_end = 13400
    _GLOBAL_CMD_69._serialized_start = 13403
    _GLOBAL_CMD_69._serialized_end = 13958
    _GLOBAL_CMD_69_PACMOD_ENABLETYPE._serialized_start = 13639
    _GLOBAL_CMD_69_PACMOD_ENABLETYPE._serialized_end = 13729
    _GLOBAL_CMD_69_CLEAR_OVERRIDETYPE._serialized_start = 13731
    _GLOBAL_CMD_69_CLEAR_OVERRIDETYPE._serialized_end = 13843
    _GLOBAL_CMD_69_IGNORE_OVERRIDETYPE._serialized_start = 13845
    _GLOBAL_CMD_69_IGNORE_OVERRIDETYPE._serialized_end = 13958
    _PARKING_BRAKE_STATUS_RPT_80._serialized_start = 13961
    _PARKING_BRAKE_STATUS_RPT_80._serialized_end = 14181
    _PARKING_BRAKE_STATUS_RPT_80_PARKING_BRAKE_ENABLEDTYPE._serialized_start = 14093
    _PARKING_BRAKE_STATUS_RPT_80_PARKING_BRAKE_ENABLEDTYPE._serialized_end = 14181
    _YAW_RATE_RPT_81._serialized_start = 14183
    _YAW_RATE_RPT_81._serialized_end = 14218
    _HORN_RPT_79._serialized_start = 14221
    _HORN_RPT_79._serialized_end = 14639
    _HORN_RPT_79_OUTPUT_VALUETYPE._serialized_start = 14443
    _HORN_RPT_79_OUTPUT_VALUETYPE._serialized_end = 14504
    _HORN_RPT_79_COMMANDED_VALUETYPE._serialized_start = 14506
    _HORN_RPT_79_COMMANDED_VALUETYPE._serialized_end = 14576
    _HORN_RPT_79_MANUAL_INPUTTYPE._serialized_start = 14578
    _HORN_RPT_79_MANUAL_INPUTTYPE._serialized_end = 14639
    _HORN_CMD_78._serialized_start = 14641
    _HORN_CMD_78._serialized_end = 14764
    _HORN_CMD_78_HORN_CMDTYPE._serialized_start = 14715
    _HORN_CMD_78_HORN_CMDTYPE._serialized_end = 14764
    _WIPER_RPT_91._serialized_start = 14767
    _WIPER_RPT_91._serialized_end = 15798
    _WIPER_RPT_91_OUTPUT_VALUETYPE._serialized_start = 14994
    _WIPER_RPT_91_OUTPUT_VALUETYPE._serialized_end = 15251
    _WIPER_RPT_91_COMMANDED_VALUETYPE._serialized_start = 15254
    _WIPER_RPT_91_COMMANDED_VALUETYPE._serialized_end = 15538
    _WIPER_RPT_91_MANUAL_INPUTTYPE._serialized_start = 15541
    _WIPER_RPT_91_MANUAL_INPUTTYPE._serialized_end = 15798
    _VEHICLE_SPEED_RPT_6F._serialized_start = 15801
    _VEHICLE_SPEED_RPT_6F._serialized_end = 16027
    _VEHICLE_SPEED_RPT_6F_VEHICLE_SPEED_VALIDTYPE._serialized_start = 15938
    _VEHICLE_SPEED_RPT_6F_VEHICLE_SPEED_VALIDTYPE._serialized_end = 16027
    _HEADLIGHT_CMD_76._serialized_start = 16030
    _HEADLIGHT_CMD_76._serialized_end = 16236
    _HEADLIGHT_CMD_76_HEADLIGHT_CMDTYPE._serialized_start = 16124
    _HEADLIGHT_CMD_76_HEADLIGHT_CMDTYPE._serialized_end = 16236
    _STEERING_MOTOR_RPT_2_74._serialized_start = 16238
    _STEERING_MOTOR_RPT_2_74._serialized_end = 16342
    _BRAKE_MOTOR_RPT_2_71._serialized_start = 16344
    _BRAKE_MOTOR_RPT_2_71._serialized_end = 16445
    _STEERING_MOTOR_RPT_1_73._serialized_start = 16447
    _STEERING_MOTOR_RPT_1_73._serialized_end = 16519
    _WIPER_CMD_90._serialized_start = 16522
    _WIPER_CMD_90._serialized_end = 16831
    _WIPER_CMD_90_WIPER_CMDTYPE._serialized_start = 16601
    _WIPER_CMD_90_WIPER_CMDTYPE._serialized_end = 16831
    _BRAKE_MOTOR_RPT_3_72._serialized_start = 16833
    _BRAKE_MOTOR_RPT_3_72._serialized_end = 16900
    _GEM._serialized_start = 16903
    _GEM._serialized_end = 18672