"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/drivers/proto/delphi_esr.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto"\xfc\x01\n\x0fEsr_status9_5e8\x12\x1c\n\x14can_tx_path_id_acc_3\x18\x01 \x01(\x05\x12\x1c\n\x14can_tx_path_id_acc_2\x18\x02 \x01(\x05\x12%\n\x1dcan_tx_filtered_xohp_acc_cipv\x18\x03 \x01(\x01\x12$\n\x1ccan_tx_water_spray_target_id\x18\x04 \x01(\x05\x12"\n\x1acan_tx_serial_num_3rd_byte\x18\x05 \x01(\x05\x12\x1d\n\x15can_tx_sideslip_angle\x18\x06 \x01(\x01\x12\x1d\n\x15can_tx_avg_pwr_cwblkg\x18\x07 \x01(\x05"\x9a\x11\n\x0fEsr_status6_5e5\x12&\n\x1ecan_tx_sw_version_dsp_3rd_byte\x18\x01 \x01(\x05\x12h\n\x1dcan_tx_vertical_align_updated\x18\x02 \x01(\x0e2A.apollo.drivers.Esr_status6_5e5.Can_tx_vertical_align_updatedType\x12$\n\x1ccan_tx_vertical_misalignment\x18\x03 \x01(\x01\x12&\n\x1ecan_tx_serv_align_updates_done\x18\x04 \x01(\x05\x12T\n\x13can_tx_found_target\x18\x05 \x01(\x0e27.apollo.drivers.Esr_status6_5e5.Can_tx_found_targetType\x12#\n\x1bcan_tx_factory_misalignment\x18\x06 \x01(\x01\x12h\n\x1dcan_tx_factory_align_status_2\x18\x07 \x01(\x0e2A.apollo.drivers.Esr_status6_5e5.Can_tx_factory_align_status_2Type\x12h\n\x1dcan_tx_factory_align_status_1\x18\x08 \x01(\x0e2A.apollo.drivers.Esr_status6_5e5.Can_tx_factory_align_status_1Type\x12d\n\x1bcan_tx_recommend_unconverge\x18\t \x01(\x0e2?.apollo.drivers.Esr_status6_5e5.Can_tx_recommend_unconvergeType\x12\x1c\n\x14can_tx_wave_diff_a2d\x18\n \x01(\x05\x12^\n\x18can_tx_system_power_mode\x18\x0b \x01(\x0e2<.apollo.drivers.Esr_status6_5e5.Can_tx_system_power_modeType\x12\x1d\n\x15can_tx_supply_n5v_a2d\x18\x0c \x01(\x05\x12\x1e\n\x16can_tx_supply_1p8v_a2d\x18\r \x01(\x05"}\n!Can_tx_vertical_align_updatedType\x12-\n)CAN_TX_VERTICAL_ALIGN_UPDATED_NOT_UPDATED\x10\x00\x12)\n%CAN_TX_VERTICAL_ALIGN_UPDATED_UPDATED\x10\x01"[\n\x17Can_tx_found_targetType\x12!\n\x1dCAN_TX_FOUND_TARGET_NOT_FOUND\x10\x00\x12\x1d\n\x19CAN_TX_FOUND_TARGET_FOUND\x10\x01"\xbb\x02\n!Can_tx_factory_align_status_2Type\x12%\n!CAN_TX_FACTORY_ALIGN_STATUS_2_OFF\x10\x00\x12&\n"CAN_TX_FACTORY_ALIGN_STATUS_2_BUSY\x10\x01\x12)\n%CAN_TX_FACTORY_ALIGN_STATUS_2_SUCCESS\x10\x02\x120\n,CAN_TX_FACTORY_ALIGN_STATUS_2_FAIL_NO_TARGET\x10\x03\x124\n0CAN_TX_FACTORY_ALIGN_STATUS_2_FAIL_DEV_TOO_LARGE\x10\x04\x124\n0CAN_TX_FACTORY_ALIGN_STATUS_2_FAIL_VAR_TOO_LARGE\x10\x05"\xbb\x02\n!Can_tx_factory_align_status_1Type\x12%\n!CAN_TX_FACTORY_ALIGN_STATUS_1_OFF\x10\x00\x12&\n"CAN_TX_FACTORY_ALIGN_STATUS_1_BUSY\x10\x01\x12)\n%CAN_TX_FACTORY_ALIGN_STATUS_1_SUCCESS\x10\x02\x120\n,CAN_TX_FACTORY_ALIGN_STATUS_1_FAIL_NO_TARGET\x10\x03\x124\n0CAN_TX_FACTORY_ALIGN_STATUS_1_FAIL_DEV_TOO_LARGE\x10\x04\x124\n0CAN_TX_FACTORY_ALIGN_STATUS_1_FAIL_VAR_TOO_LARGE\x10\x05"{\n\x1fCan_tx_recommend_unconvergeType\x12-\n)CAN_TX_RECOMMEND_UNCONVERGE_NOT_RECOMMEND\x10\x00\x12)\n%CAN_TX_RECOMMEND_UNCONVERGE_RECOMMEND\x10\x01"\xdf\x02\n\x1cCan_tx_system_power_modeType\x12%\n!CAN_TX_SYSTEM_POWER_MODE_DSP_INIT\x10\x00\x12(\n$CAN_TX_SYSTEM_POWER_MODE_RADIATE_OFF\x10\x01\x12\'\n#CAN_TX_SYSTEM_POWER_MODE_RADIATE_ON\x10\x02\x12)\n%CAN_TX_SYSTEM_POWER_MODE_DSP_SHUTDOWN\x10\x03\x12$\n CAN_TX_SYSTEM_POWER_MODE_DSP_OFF\x10\x04\x12*\n&CAN_TX_SYSTEM_POWER_MODE_HOST_SHUTDOWN\x10\x05\x12!\n\x1dCAN_TX_SYSTEM_POWER_MODE_TEST\x10\x06\x12%\n!CAN_TX_SYSTEM_POWER_MODE_7INVALID\x10\x07"\xf7\x01\n\x0fEsr_status5_5e4\x12\x1d\n\x15can_tx_supply_10v_a2d\x18\x01 \x01(\x05\x12\x18\n\x10can_tx_temp2_a2d\x18\x02 \x01(\x05\x12\x18\n\x10can_tx_temp1_a2d\x18\x03 \x01(\x05\x12\x19\n\x11can_tx_swbatt_a2d\x18\x04 \x01(\x05\x12\x1e\n\x16can_tx_supply_5vdx_a2d\x18\x05 \x01(\x05\x12\x1d\n\x15can_tx_supply_5va_a2d\x18\x06 \x01(\x05\x12\x1e\n\x16can_tx_supply_3p3v_a2d\x18\x07 \x01(\x05\x12\x17\n\x0fcan_tx_ignp_a2d\x18\x08 \x01(\x05"\xa8\x01\n\x0fEsr_status3_4e2\x12\x1d\n\x15can_tx_sw_version_pld\x18\x01 \x01(\x05\x12\x1e\n\x16can_tx_sw_version_host\x18\x02 \x01(\x05\x12\x19\n\x11can_tx_hw_version\x18\x03 \x01(\x05\x12 \n\x18can_tx_interface_version\x18\x04 \x01(\x05\x12\x19\n\x11can_tx_serial_num\x18\x05 \x01(\x05"\x96\x0b\n\x0fEsr_status4_4e3\x12\\\n\x17can_tx_truck_target_det\x18\x01 \x01(\x0e2;.apollo.drivers.Esr_status4_4e3.Can_tx_truck_target_detType\x12l\n\x1fcan_tx_lr_only_grating_lobe_det\x18\x02 \x01(\x0e2C.apollo.drivers.Esr_status4_4e3.Can_tx_lr_only_grating_lobe_detType\x12^\n\x18can_tx_sidelobe_blockage\x18\x03 \x01(\x0e2<.apollo.drivers.Esr_status4_4e3.Can_tx_sidelobe_blockageType\x12\\\n\x17can_tx_partial_blockage\x18\x04 \x01(\x0e2;.apollo.drivers.Esr_status4_4e3.Can_tx_partial_blockageType\x12\x1f\n\x17can_tx_path_id_acc_stat\x18\x05 \x01(\x05\x12P\n\x11can_tx_mr_lr_mode\x18\x06 \x01(\x0e25.apollo.drivers.Esr_status4_4e3.Can_tx_mr_lr_modeType\x12\x1f\n\x17can_tx_auto_align_angle\x18\x07 \x01(\x01\x12\x1e\n\x16can_tx_rolling_count_3\x18\x08 \x01(\x05\x12\x1f\n\x17can_tx_path_id_fcw_stat\x18\t \x01(\x05\x12\x1f\n\x17can_tx_path_id_fcw_move\x18\n \x01(\x05\x12 \n\x18can_tx_path_id_cmbb_stat\x18\x0b \x01(\x05\x12 \n\x18can_tx_path_id_cmbb_move\x18\x0c \x01(\x05\x12\x1a\n\x12can_tx_path_id_acc\x18\r \x01(\x05"m\n\x1bCan_tx_truck_target_detType\x12(\n$CAN_TX_TRUCK_TARGET_DET_NOT_DETECTED\x10\x00\x12$\n CAN_TX_TRUCK_TARGET_DET_DETECTED\x10\x01"\x85\x01\n#Can_tx_lr_only_grating_lobe_detType\x120\n,CAN_TX_LR_ONLY_GRATING_LOBE_DET_NOT_DETECTED\x10\x00\x12,\n(CAN_TX_LR_ONLY_GRATING_LOBE_DET_DETECTED\x10\x01"a\n\x1cCan_tx_sidelobe_blockageType\x12 \n\x1cCAN_TX_SIDELOBE_BLOCKAGE_OFF\x10\x00\x12\x1f\n\x1bCAN_TX_SIDELOBE_BLOCKAGE_ON\x10\x01"k\n\x1bCan_tx_partial_blockageType\x12\'\n#CAN_TX_PARTIAL_BLOCKAGE_NOT_BLOCKED\x10\x00\x12#\n\x1fCAN_TX_PARTIAL_BLOCKAGE_BLOCKED\x10\x01"\xdb\x01\n\x15Can_tx_mr_lr_modeType\x12\x1e\n\x1aCAN_TX_MR_LR_MODE_RESERVED\x10\x00\x125\n1CAN_TX_MR_LR_MODE_OUTPUT_ONLY_MEDIUM_RANGE_TRACKS\x10\x01\x123\n/CAN_TX_MR_LR_MODE_OUTPUT_ONLY_LONG_RANGE_TRACKS\x10\x02\x126\n2CAN_TX_MR_LR_MODE_OUTPUT_ALL_MEDIUM_RANGE_AND_LONG\x10\x03"\xc9\x02\n\x18Esr_trackmotionpower_540\x12$\n\x1ccan_tx_track_rolling_count_2\x18\x01 \x01(\x08\x12!\n\x19can_tx_track_can_id_group\x18\x02 \x01(\x05\x12W\n\x19can_tx_track_motion_power\x18\x03 \x03(\x0b24.apollo.drivers.Esr_trackmotionpower_540.Motionpower\x1a\x8a\x01\n\x0bMotionpower\x12\x1b\n\x13can_tx_track_moving\x18\x01 \x01(\x08\x12 \n\x18can_tx_track_moving_fast\x18\x02 \x01(\x08\x12 \n\x18can_tx_track_moving_slow\x18\x03 \x01(\x08\x12\x1a\n\x12can_tx_track_power\x18\x04 \x01(\x05"\x89\x01\n\x10Acm_inst_req_7e0\x12\x13\n\x0bcommand_ctr\x18\x01 \x01(\x05\x12\x14\n\x0ccommand_code\x18\x02 \x01(\x05\x12\x11\n\tcc_word_2\x18\x03 \x01(\x05\x12\x11\n\tcc_word_1\x18\x04 \x01(\x05\x12\x11\n\tcc_byte_2\x18\x05 \x01(\x05\x12\x11\n\tcc_byte_1\x18\x06 \x01(\x05"\x83\r\n\x0fEsr_track01_500\x12h\n\x1dcan_tx_track_grouping_changed\x18\x01 \x01(\x0e2A.apollo.drivers.Esr_track01_500.Can_tx_track_grouping_changedType\x12X\n\x15can_tx_track_oncoming\x18\x02 \x01(\x0e29.apollo.drivers.Esr_track01_500.Can_tx_track_oncomingType\x12\x1d\n\x15can_tx_track_lat_rate\x18\x03 \x01(\x01\x12b\n\x1acan_tx_track_bridge_object\x18\x04 \x01(\x0e2>.apollo.drivers.Esr_track01_500.Can_tx_track_bridge_objectType\x12\x1a\n\x12can_tx_track_width\x18\x05 \x01(\x01\x12T\n\x13can_tx_track_status\x18\x06 \x01(\x0e27.apollo.drivers.Esr_track01_500.Can_tx_track_statusType\x12"\n\x1acan_tx_track_rolling_count\x18\x07 \x01(\x08\x12\x1f\n\x17can_tx_track_range_rate\x18\x08 \x01(\x01\x12 \n\x18can_tx_track_range_accel\x18\t \x01(\x01\x12\x1a\n\x12can_tx_track_range\x18\n \x01(\x01\x12d\n\x1bcan_tx_track_med_range_mode\x18\x0b \x01(\x0e2?.apollo.drivers.Esr_track01_500.Can_tx_track_med_range_modeType\x12\x1a\n\x12can_tx_track_angle\x18\x0c \x01(\x01"\x8b\x01\n!Can_tx_track_grouping_changedType\x123\n/CAN_TX_TRACK_GROUPING_CHANGED_GROUPINGUNCHANGED\x10\x00\x121\n-CAN_TX_TRACK_GROUPING_CHANGED_GROUPINGCHANGED\x10\x01"f\n\x19Can_tx_track_oncomingType\x12%\n!CAN_TX_TRACK_ONCOMING_NOTONCOMING\x10\x00\x12"\n\x1eCAN_TX_TRACK_ONCOMING_ONCOMING\x10\x01"r\n\x1eCan_tx_track_bridge_objectType\x12)\n%CAN_TX_TRACK_BRIDGE_OBJECT_NOT_BRIDGE\x10\x00\x12%\n!CAN_TX_TRACK_BRIDGE_OBJECT_BRIDGE\x10\x01"\xdf\x02\n\x17Can_tx_track_statusType\x12!\n\x1dCAN_TX_TRACK_STATUS_NO_TARGET\x10\x00\x12"\n\x1eCAN_TX_TRACK_STATUS_NEW_TARGET\x10\x01\x12*\n&CAN_TX_TRACK_STATUS_NEW_UPDATED_TARGET\x10\x02\x12&\n"CAN_TX_TRACK_STATUS_UPDATED_TARGET\x10\x03\x12&\n"CAN_TX_TRACK_STATUS_COASTED_TARGET\x10\x04\x12%\n!CAN_TX_TRACK_STATUS_MERGED_TARGET\x10\x05\x12.\n*CAN_TX_TRACK_STATUS_INVALID_COASTED_TARGET\x10\x06\x12*\n&CAN_TX_TRACK_STATUS_NEW_COASTED_TARGET\x10\x07"\xe5\x01\n\x1fCan_tx_track_med_range_modeType\x12/\n+CAN_TX_TRACK_MED_RANGE_MODE_NO_MR_LR_UPDATE\x10\x00\x12.\n*CAN_TX_TRACK_MED_RANGE_MODE_MR_UPDATE_ONLY\x10\x01\x12.\n*CAN_TX_TRACK_MED_RANGE_MODE_LR_UPDATE_ONLY\x10\x02\x121\n-CAN_TX_TRACK_MED_RANGE_MODE_BOTH_MR_LR_UPDATE\x10\x03"\xad\x01\n\x0eEsr_valid1_5d0\x12\x1a\n\x12can_tx_valid_lr_sn\x18\x01 \x01(\x05\x12"\n\x1acan_tx_valid_lr_range_rate\x18\x02 \x01(\x01\x12\x1d\n\x15can_tx_valid_lr_range\x18\x03 \x01(\x01\x12\x1d\n\x15can_tx_valid_lr_power\x18\x04 \x01(\x05\x12\x1d\n\x15can_tx_valid_lr_angle\x18\x05 \x01(\x01"\xad\x01\n\x0eEsr_valid2_5d1\x12\x1a\n\x12can_tx_valid_mr_sn\x18\x01 \x01(\x05\x12"\n\x1acan_tx_valid_mr_range_rate\x18\x02 \x01(\x01\x12\x1d\n\x15can_tx_valid_mr_range\x18\x03 \x01(\x01\x12\x1d\n\x15can_tx_valid_mr_power\x18\x04 \x01(\x05\x12\x1d\n\x15can_tx_valid_mr_angle\x18\x05 \x01(\x01"\xa6\x01\n\x11Acm_inst_resp_7e4\x12\x0e\n\x06data_7\x18\x01 \x01(\x05\x12\x0e\n\x06data_6\x18\x02 \x01(\x05\x12\x0e\n\x06data_5\x18\x03 \x01(\x05\x12\x0e\n\x06data_4\x18\x04 \x01(\x05\x12\x0e\n\x06data_3\x18\x05 \x01(\x05\x12\x17\n\x0frtn_cmd_counter\x18\x06 \x01(\x05\x12\x1b\n\x13command_return_code\x18\x07 \x01(\x05\x12\x0b\n\x03pid\x18\x08 \x01(\x05"\x9f\x15\n\x0cVehicle2_4f1\x12$\n\x1ccan_rx_volvo_short_track_roc\x18\x01 \x01(\x01\x12Y\n\x17can_rx_mr_only_transmit\x18\x02 \x01(\x0e28.apollo.drivers.Vehicle2_4f1.Can_rx_mr_only_transmitType\x12Y\n\x17can_rx_lr_only_transmit\x18\x03 \x01(\x0e28.apollo.drivers.Vehicle2_4f1.Can_rx_lr_only_transmitType\x12\x1d\n\x15can_rx_high_yaw_angle\x18\x04 \x01(\x05\x12Q\n\x13can_rx_clear_faults\x18\x05 \x01(\x0e24.apollo.drivers.Vehicle2_4f1.Can_rx_clear_faultsType\x12e\n\x1dcan_rx_use_angle_misalignment\x18\x06 \x01(\x0e2>.apollo.drivers.Vehicle2_4f1.Can_rx_use_angle_misalignmentType\x12]\n\x19can_rx_turn_signal_status\x18\x07 \x01(\x0e2:.apollo.drivers.Vehicle2_4f1.Can_rx_turn_signal_statusType\x12Y\n\x17can_rx_blockage_disable\x18\x08 \x01(\x0e28.apollo.drivers.Vehicle2_4f1.Can_rx_blockage_disableType\x12e\n\x1dcan_rx_vehicle_speed_validity\x18\t \x01(\x0e2>.apollo.drivers.Vehicle2_4f1.Can_rx_vehicle_speed_validityType\x12W\n\x16can_rx_mmr_upside_down\x18\n \x01(\x0e27.apollo.drivers.Vehicle2_4f1.Can_rx_mmr_upside_downType\x12Q\n\x13can_rx_wiper_status\x18\x0b \x01(\x0e24.apollo.drivers.Vehicle2_4f1.Can_rx_wiper_statusType\x12W\n\x16can_rx_raw_data_enable\x18\x0c \x01(\x0e27.apollo.drivers.Vehicle2_4f1.Can_rx_raw_data_enableType\x12[\n\x18can_rx_radar_cmd_radiate\x18\r \x01(\x0e29.apollo.drivers.Vehicle2_4f1.Can_rx_radar_cmd_radiateType\x12S\n\x14can_rx_grouping_mode\x18\x0e \x01(\x0e25.apollo.drivers.Vehicle2_4f1.Can_rx_grouping_modeType\x12\x1d\n\x15can_rx_maximum_tracks\x18\x0f \x01(\x05\x12&\n\x1ecan_rx_lateral_mounting_offset\x18\x10 \x01(\x01\x12!\n\x19can_rx_angle_misalignment\x18\x11 \x01(\x01\x12\x1d\n\x15can_rx_scan_index_ack\x18\x12 \x01(\x05"^\n\x1bCan_rx_mr_only_transmitType\x12\x1f\n\x1bCAN_RX_MR_ONLY_TRANSMIT_OFF\x10\x00\x12\x1e\n\x1aCAN_RX_MR_ONLY_TRANSMIT_ON\x10\x01"^\n\x1bCan_rx_lr_only_transmitType\x12\x1f\n\x1bCAN_RX_LR_ONLY_TRANSMIT_OFF\x10\x00\x12\x1e\n\x1aCAN_RX_LR_ONLY_TRANSMIT_ON\x10\x01"R\n\x17Can_rx_clear_faultsType\x12\x1b\n\x17CAN_RX_CLEAR_FAULTS_OFF\x10\x00\x12\x1a\n\x16CAN_RX_CLEAR_FAULTS_ON\x10\x01"p\n!Can_rx_use_angle_misalignmentType\x12%\n!CAN_RX_USE_ANGLE_MISALIGNMENT_OFF\x10\x00\x12$\n CAN_RX_USE_ANGLE_MISALIGNMENT_ON\x10\x01"\xb4\x01\n\x1dCan_rx_turn_signal_statusType\x12!\n\x1dCAN_RX_TURN_SIGNAL_STATUS_OFF\x10\x00\x12"\n\x1eCAN_RX_TURN_SIGNAL_STATUS_LEFT\x10\x01\x12#\n\x1fCAN_RX_TURN_SIGNAL_STATUS_RIGHT\x10\x02\x12\'\n#CAN_RX_TURN_SIGNAL_STATUS_INVALID_3\x10\x03"h\n\x1bCan_rx_blockage_disableType\x12#\n\x1fCAN_RX_BLOCKAGE_DISABLE_ENABLED\x10\x00\x12$\n CAN_RX_BLOCKAGE_DISABLE_DISABLED\x10\x01"w\n!Can_rx_vehicle_speed_validityType\x12)\n%CAN_RX_VEHICLE_SPEED_VALIDITY_INVALID\x10\x00\x12\'\n#CAN_RX_VEHICLE_SPEED_VALIDITY_VALID\x10\x01"n\n\x1aCan_rx_mmr_upside_downType\x12(\n$CAN_RX_MMR_UPSIDE_DOWN_RIGHT_SIDE_UP\x10\x00\x12&\n"CAN_RX_MMR_UPSIDE_DOWN_UPSIDE_DOWN\x10\x01"R\n\x17Can_rx_wiper_statusType\x12\x1b\n\x17CAN_RX_WIPER_STATUS_OFF\x10\x00\x12\x1a\n\x16CAN_RX_WIPER_STATUS_ON\x10\x01"a\n\x1aCan_rx_raw_data_enableType\x12#\n\x1fCAN_RX_RAW_DATA_ENABLE_FILTERED\x10\x00\x12\x1e\n\x1aCAN_RX_RAW_DATA_ENABLE_RAW\x10\x01"a\n\x1cCan_rx_radar_cmd_radiateType\x12 \n\x1cCAN_RX_RADAR_CMD_RADIATE_OFF\x10\x00\x12\x1f\n\x1bCAN_RX_RADAR_CMD_RADIATE_ON\x10\x01"\xce\x01\n\x18Can_rx_grouping_modeType\x12$\n CAN_RX_GROUPING_MODE_NO_GROUPING\x10\x00\x12*\n&CAN_RX_GROUPING_MODE_GROUP_MOVING_ONLY\x10\x01\x12.\n*CAN_RX_GROUPING_MODE_GROUP_STATIONARY_ONLY\x10\x02\x120\n,CAN_RX_GROUPING_MODE_GROUP_MOVING_STATIONARY\x10\x03"\x92\n\n\x0cVehicle1_4f0\x12g\n\x1ecan_rx_steering_angle_validity\x18\x01 \x01(\x0e2?.apollo.drivers.Vehicle1_4f0.Can_rx_steering_angle_validityType\x12"\n\x1acan_rx_steering_angle_rate\x18\x02 \x01(\x05\x12_\n\x1acan_rx_steering_angle_sign\x18\x03 \x01(\x0e2;.apollo.drivers.Vehicle1_4f0.Can_rx_steering_angle_signType\x12i\n\x1fcan_rx_steering_angle_rate_sign\x18\x04 \x01(\x0e2@.apollo.drivers.Vehicle1_4f0.Can_rx_steering_angle_rate_signType\x12\x1d\n\x15can_rx_steering_angle\x18\x05 \x01(\x05\x12\x1f\n\x17can_rx_radius_curvature\x18\x06 \x01(\x05\x12[\n\x18can_rx_yaw_rate_validity\x18\x07 \x01(\x0e29.apollo.drivers.Vehicle1_4f0.Can_rx_yaw_rate_validityType\x12\x17\n\x0fcan_rx_yaw_rate\x18\x08 \x01(\x01\x12g\n\x1ecan_rx_vehicle_speed_direction\x18\t \x01(\x0e2?.apollo.drivers.Vehicle1_4f0.Can_rx_vehicle_speed_directionType\x12\x1c\n\x14can_rx_vehicle_speed\x18\n \x01(\x01"z\n"Can_rx_steering_angle_validityType\x12*\n&CAN_RX_STEERING_ANGLE_VALIDITY_INVALID\x10\x00\x12(\n$CAN_RX_STEERING_ANGLE_VALIDITY_VALID\x10\x01"{\n\x1eCan_rx_steering_angle_signType\x12/\n+CAN_RX_STEERING_ANGLE_SIGN_COUNTERCLOCKWISE\x10\x00\x12(\n$CAN_RX_STEERING_ANGLE_SIGN_CLOCKWISE\x10\x01"\x8a\x01\n#Can_rx_steering_angle_rate_signType\x124\n0CAN_RX_STEERING_ANGLE_RATE_SIGN_COUNTERCLOCKWISE\x10\x00\x12-\n)CAN_RX_STEERING_ANGLE_RATE_SIGN_CLOCKWISE\x10\x01"h\n\x1cCan_rx_yaw_rate_validityType\x12$\n CAN_RX_YAW_RATE_VALIDITY_INVALID\x10\x00\x12"\n\x1eCAN_RX_YAW_RATE_VALIDITY_VALID\x10\x01"|\n"Can_rx_vehicle_speed_directionType\x12*\n&CAN_RX_VEHICLE_SPEED_DIRECTION_FORWARD\x10\x00\x12*\n&CAN_RX_VEHICLE_SPEED_DIRECTION_REVERSE\x10\x01"\x82\x08\n\x0cEsr_sim1_5c0\x12Q\n\x13can_rx_sim_track_id\x18\x01 \x01(\x0e24.apollo.drivers.Esr_sim1_5c0.Can_rx_sim_track_idType\x12M\n\x11can_rx_sim_status\x18\x02 \x01(\x0e22.apollo.drivers.Esr_sim1_5c0.Can_rx_sim_statusType\x12\x1d\n\x15can_rx_sim_range_rate\x18\x03 \x01(\x01\x12\x1e\n\x16can_rx_sim_range_accel\x18\x04 \x01(\x01\x12\x18\n\x10can_rx_sim_range\x18\x05 \x01(\x05\x12\x1b\n\x13can_rx_sim_lat_rate\x18\x06 \x01(\x01\x12\x1a\n\x12can_rx_sim_lat_pos\x18\x07 \x01(\x01\x12Q\n\x13can_rx_sim_function\x18\x08 \x01(\x0e24.apollo.drivers.Esr_sim1_5c0.Can_rx_sim_functionType\x12\x18\n\x10can_rx_sim_angle\x18\t \x01(\x01"\x80\x01\n\x17Can_rx_sim_track_idType\x12!\n\x1dCAN_RX_SIM_TRACK_ID_NO_TARGET\x10\x00\x12 \n\x1cCAN_RX_SIM_TRACK_ID_TARGET_1\x10\x01\x12 \n\x1cCAN_RX_SIM_TRACK_ID_TARGET_2\x10\x02"\x8f\x01\n\x15Can_rx_sim_statusType\x12\x1d\n\x19CAN_RX_SIM_STATUS_INVALID\x10\x00\x12\x19\n\x15CAN_RX_SIM_STATUS_NEW\x10\x01\x12\x1d\n\x19CAN_RX_SIM_STATUS_UPDATED\x10\x02\x12\x1d\n\x19CAN_RX_SIM_STATUS_COASTED\x10\x03"\xbb\x02\n\x17Can_rx_sim_functionType\x12\x1b\n\x17CAN_RX_SIM_FUNCTION_ACC\x10\x00\x12\x1a\n\x16CAN_RX_SIM_FUNCTION_RI\x10\x01\x12 \n\x1cCAN_RX_SIM_FUNCTION_FCW_MOVE\x10\x02\x12 \n\x1cCAN_RX_SIM_FUNCTION_FCW_STAT\x10\x03\x12!\n\x1dCAN_RX_SIM_FUNCTION_CMBB_MOVE\x10\x04\x12!\n\x1dCAN_RX_SIM_FUNCTION_CMBB_STAT\x10\x05\x12/\n+CAN_RX_SIM_FUNCTION_ALL_MOVING_ACC_FCW_CMBB\x10\x06\x12,\n(CAN_RX_SIM_FUNCTION_ALL_STAT_RI_FCW_CMBB\x10\x07"\xec\x01\n\x0fEsr_status1_4e0\x12\x1c\n\x14can_tx_dsp_timestamp\x18\x01 \x01(\x01\x12\x19\n\x11can_tx_comm_error\x18\x02 \x01(\x08\x12\x1c\n\x14can_tx_yaw_rate_calc\x18\x03 \x01(\x01\x12!\n\x19can_tx_vehicle_speed_calc\x18\x04 \x01(\x01\x12\x19\n\x11can_tx_scan_index\x18\x05 \x01(\x05\x12\x1e\n\x16can_tx_rolling_count_1\x18\x06 \x01(\x05\x12$\n\x1ccan_tx_radius_curvature_calc\x18\x07 \x01(\x05"\xdd\x0b\n\x0fEsr_status2_4e1\x12\x1c\n\x14can_tx_yaw_rate_bias\x18\x01 \x01(\x01\x12"\n\x1acan_tx_veh_spd_comp_factor\x18\x02 \x01(\x01\x12\x1d\n\x15can_tx_sw_version_dsp\x18\x03 \x01(\x05\x12\x1a\n\x12can_tx_temperature\x18\x04 \x01(\x05\x12V\n\x14can_tx_raw_data_mode\x18\x05 \x01(\x0e28.apollo.drivers.Esr_status2_4e1.Can_tx_raw_data_modeType\x12\\\n\x17can_tx_range_perf_error\x18\x06 \x01(\x0e2;.apollo.drivers.Esr_status2_4e1.Can_tx_range_perf_errorType\x12X\n\x15can_tx_overheat_error\x18\x07 \x01(\x0e29.apollo.drivers.Esr_status2_4e1.Can_tx_overheat_errorType\x12!\n\x19can_tx_maximum_tracks_ack\x18\x08 \x01(\x05\x12X\n\x15can_tx_internal_error\x18\t \x01(\x0e29.apollo.drivers.Esr_status2_4e1.Can_tx_internal_errorType\x12V\n\x14can_tx_grouping_mode\x18\n \x01(\x0e28.apollo.drivers.Esr_status2_4e1.Can_tx_grouping_modeType\x12\\\n\x17can_tx_xcvr_operational\x18\x0b \x01(\x0e2;.apollo.drivers.Esr_status2_4e1.Can_tx_xcvr_operationalType\x12!\n\x19can_tx_steering_angle_ack\x18\x0c \x01(\x05\x12\x1e\n\x16can_tx_rolling_count_2\x18\r \x01(\x05"[\n\x18Can_tx_raw_data_modeType\x12!\n\x1dCAN_TX_RAW_DATA_MODE_FILTERED\x10\x00\x12\x1c\n\x18CAN_TX_RAW_DATA_MODE_RAW\x10\x01"k\n\x1bCan_tx_range_perf_errorType\x12\'\n#CAN_TX_RANGE_PERF_ERROR_NOT_BLOCKED\x10\x00\x12#\n\x1fCAN_TX_RANGE_PERF_ERROR_BLOCKED\x10\x01"g\n\x19Can_tx_overheat_errorType\x12&\n"CAN_TX_OVERHEAT_ERROR_NOT_OVERTEMP\x10\x00\x12"\n\x1eCAN_TX_OVERHEAT_ERROR_OVERTEMP\x10\x01"c\n\x19Can_tx_internal_errorType\x12$\n CAN_TX_INTERNAL_ERROR_NOT_FAILED\x10\x00\x12 \n\x1cCAN_TX_INTERNAL_ERROR_FAILED\x10\x01"\xce\x01\n\x18Can_tx_grouping_modeType\x12$\n CAN_TX_GROUPING_MODE_NO_GROUPING\x10\x00\x12*\n&CAN_TX_GROUPING_MODE_GROUP_MOVING_ONLY\x10\x01\x12.\n*CAN_TX_GROUPING_MODE_GROUP_STATIONARY_ONLY\x10\x02\x120\n,CAN_TX_GROUPING_MODE_GROUP_MOVING_STATIONARY\x10\x03"^\n\x1bCan_tx_xcvr_operationalType\x12\x1f\n\x1bCAN_TX_XCVR_OPERATIONAL_OFF\x10\x00\x12\x1e\n\x1aCAN_TX_XCVR_OPERATIONAL_ON\x10\x01"\x91\x02\n\x0fEsr_status8_5e7\x12\x1e\n\x16can_tx_history_fault_7\x18\x01 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_6\x18\x02 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_5\x18\x03 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_4\x18\x04 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_3\x18\x05 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_2\x18\x06 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_1\x18\x07 \x01(\x05\x12\x1e\n\x16can_tx_history_fault_0\x18\x08 \x01(\x05"\x89\x02\n\x0fEsr_status7_5e6\x12\x1d\n\x15can_tx_active_fault_7\x18\x01 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_6\x18\x02 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_5\x18\x03 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_4\x18\x04 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_3\x18\x05 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_2\x18\x06 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_0\x18\x07 \x01(\x05\x12\x1d\n\x15can_tx_active_fault_1\x18\x08 \x01(\x05"\xf6\r\n\x0cVehicle3_5f2\x12&\n\x1ecan_rx_serv_align_updates_need\x18\x01 \x01(\x05\x12W\n\x16can_rx_serv_align_type\x18\x02 \x01(\x0e27.apollo.drivers.Vehicle3_5f2.Can_rx_serv_align_typeType\x12[\n\x18can_rx_serv_align_enable\x18\x03 \x01(\x0e29.apollo.drivers.Vehicle3_5f2.Can_rx_serv_align_enableType\x12#\n\x1bcan_rx_aalign_avg_ctr_total\x18\x04 \x01(\x01\x12a\n\x1bcan_rx_auto_align_converged\x18\x05 \x01(\x0e2<.apollo.drivers.Vehicle3_5f2.Can_rx_auto_align_convergedType\x12]\n\x19can_rx_auto_align_disable\x18\x06 \x01(\x0e2:.apollo.drivers.Vehicle3_5f2.Can_rx_auto_align_disableType\x12$\n\x1ccan_rx_angle_mounting_offset\x18\x07 \x01(\x01\x12M\n\x11can_rx_wheel_slip\x18\x08 \x01(\x0e22.apollo.drivers.Vehicle3_5f2.Can_rx_wheel_slipType\x12\x1b\n\x13can_rx_radar_height\x18\t \x01(\x05\x12\x1b\n\x13can_rx_radar_fov_mr\x18\n \x01(\x05\x12\x1b\n\x13can_rx_radar_fov_lr\x18\x0b \x01(\x05\x12_\n\x1acan_rx_long_accel_validity\x18\x0c \x01(\x0e2;.apollo.drivers.Vehicle3_5f2.Can_rx_long_accel_validityType\x12\x19\n\x11can_rx_long_accel\x18\r \x01(\x01\x12]\n\x19can_rx_lat_accel_validity\x18\x0e \x01(\x0e2:.apollo.drivers.Vehicle3_5f2.Can_rx_lat_accel_validityType\x12\x18\n\x10can_rx_lat_accel\x18\x0f \x01(\x01"u\n\x1aCan_rx_serv_align_typeType\x12)\n%CAN_RX_SERV_ALIGN_TYPE_AUTO_OR_DEALER\x10\x00\x12,\n(CAN_RX_SERV_ALIGN_TYPE_VOLVO_SHORT_TRACK\x10\x01"k\n\x1cCan_rx_serv_align_enableType\x12%\n!CAN_RX_SERV_ALIGN_ENABLE_DISABLED\x10\x00\x12$\n CAN_RX_SERV_ALIGN_ENABLE_ENABLED\x10\x01"{\n\x1fCan_rx_auto_align_convergedType\x12-\n)CAN_RX_AUTO_ALIGN_CONVERGED_NOT_CONVERGED\x10\x00\x12)\n%CAN_RX_AUTO_ALIGN_CONVERGED_CONVERGED\x10\x01"n\n\x1dCan_rx_auto_align_disableType\x12%\n!CAN_RX_AUTO_ALIGN_DISABLE_ENABLED\x10\x00\x12&\n"CAN_RX_AUTO_ALIGN_DISABLE_DISABLED\x10\x01"\xb1\x01\n\x15Can_rx_wheel_slipType\x12 \n\x1cCAN_RX_WHEEL_SLIP_NO_CONTROL\x10\x00\x12(\n$CAN_RX_WHEEL_SLIP_BRAKE_SLIP_CONTROL\x10\x01\x12+\n\'CAN_RX_WHEEL_SLIP_TRACTION_SLIP_CONTROL\x10\x02\x12\x1f\n\x1bCAN_RX_WHEEL_SLIP_INVALID_3\x10\x03"n\n\x1eCan_rx_long_accel_validityType\x12&\n"CAN_RX_LONG_ACCEL_VALIDITY_INVALID\x10\x00\x12$\n CAN_RX_LONG_ACCEL_VALIDITY_VALID\x10\x01"k\n\x1dCan_rx_lat_accel_validityType\x12%\n!CAN_RX_LAT_ACCEL_VALIDITY_INVALID\x10\x00\x12#\n\x1fCAN_RX_LAT_ACCEL_VALIDITY_VALID\x10\x01"\x91\x05\n\x0cVehicle4_5f3\x12 \n\x18can_rx_fac_tgt_range_r2m\x18\x01 \x01(\x01\x12 \n\x18can_rx_fac_tgt_range_m2t\x18\x02 \x01(\x01\x12\x1e\n\x16can_rx_fac_tgt_range_1\x18\x03 \x01(\x01\x12$\n\x1ccan_rx_fac_tgt_mtg_space_ver\x18\x04 \x01(\x05\x12$\n\x1ccan_rx_fac_tgt_mtg_space_hor\x18\x05 \x01(\x05\x12!\n\x19can_rx_fac_tgt_mtg_offset\x18\x06 \x01(\x05\x12!\n\x19can_rx_fac_align_samp_req\x18\x07 \x01(\x05\x12\x1f\n\x17can_rx_fac_align_max_nt\x18\x08 \x01(\x05\x12W\n\x16can_rx_fac_align_cmd_2\x18\t \x01(\x0e27.apollo.drivers.Vehicle4_5f3.Can_rx_fac_align_cmd_2Type\x12W\n\x16can_rx_fac_align_cmd_1\x18\n \x01(\x0e27.apollo.drivers.Vehicle4_5f3.Can_rx_fac_align_cmd_1Type"[\n\x1aCan_rx_fac_align_cmd_2Type\x12\x1e\n\x1aCAN_RX_FAC_ALIGN_CMD_2_OFF\x10\x00\x12\x1d\n\x19CAN_RX_FAC_ALIGN_CMD_2_ON\x10\x01"[\n\x1aCan_rx_fac_align_cmd_1Type\x12\x1e\n\x1aCAN_RX_FAC_ALIGN_CMD_1_OFF\x10\x00\x12\x1d\n\x19CAN_RX_FAC_ALIGN_CMD_1_ON\x10\x01"\xf4\x03\n\x0cVehicle5_5f4\x12_\n\x1acan_rx_yaw_rate_bias_shift\x18\x01 \x01(\x0e2;.apollo.drivers.Vehicle5_5f4.Can_rx_yaw_rate_bias_shiftType\x12"\n\x1acan_rx_steering_gear_ratio\x18\x02 \x01(\x01\x12\x18\n\x10can_rx_wheelbase\x18\x03 \x01(\x01\x12!\n\x19can_rx_distance_rear_axle\x18\x04 \x01(\x01\x12$\n\x1ccan_rx_cw_blockage_threshold\x18\x05 \x01(\x01\x12"\n\x1acan_rx_funnel_offset_right\x18\x06 \x01(\x01\x12!\n\x19can_rx_funnel_offset_left\x18\x07 \x01(\x01\x12\x1d\n\x15can_rx_beamwidth_vert\x18\x08 \x01(\x01\x12#\n\x1bcan_rx_oversteer_understeer\x18\t \x01(\x05"q\n\x1eCan_rx_yaw_rate_bias_shiftType\x12(\n$CAN_RX_YAW_RATE_BIAS_SHIFT_NO_DETECT\x10\x00\x12%\n!CAN_RX_YAW_RATE_BIAS_SHIFT_DETECT\x10\x01"\xd4\x01\n\x0cVehicle6_5f5\x12(\n can_rx_inner_funnel_offset_right\x18\x01 \x01(\x01\x12\'\n\x1fcan_rx_inner_funnel_offset_left\x18\x02 \x01(\x01\x12$\n\x1ccan_volvo_fa_range_max_short\x18\x03 \x01(\x05\x12%\n\x1dcan_volvo_fa_min_vspeed_short\x18\x04 \x01(\x01\x12$\n\x1ccan_volvo_fa_aalign_estimate\x18\x05 \x01(\x01"\x98\n\n\tDelphiESR\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x128\n\x0fesr_status9_5e8\x18\x02 \x01(\x0b2\x1f.apollo.drivers.Esr_status9_5e8\x128\n\x0fesr_status6_5e5\x18\x03 \x01(\x0b2\x1f.apollo.drivers.Esr_status6_5e5\x128\n\x0fesr_status5_5e4\x18\x04 \x01(\x0b2\x1f.apollo.drivers.Esr_status5_5e4\x128\n\x0fesr_status3_4e2\x18\x05 \x01(\x0b2\x1f.apollo.drivers.Esr_status3_4e2\x128\n\x0fesr_status4_4e3\x18\x06 \x01(\x0b2\x1f.apollo.drivers.Esr_status4_4e3\x12J\n\x18esr_trackmotionpower_540\x18\x07 \x03(\x0b2(.apollo.drivers.Esr_trackmotionpower_540\x12:\n\x10acm_inst_req_7e0\x18\x08 \x01(\x0b2 .apollo.drivers.Acm_inst_req_7e0\x128\n\x0fesr_track01_500\x18\t \x03(\x0b2\x1f.apollo.drivers.Esr_track01_500\x126\n\x0eesr_valid1_5d0\x18\n \x01(\x0b2\x1e.apollo.drivers.Esr_valid1_5d0\x126\n\x0eesr_valid2_5d1\x18\x0b \x01(\x0b2\x1e.apollo.drivers.Esr_valid2_5d1\x12<\n\x11acm_inst_resp_7e4\x18\x0c \x01(\x0b2!.apollo.drivers.Acm_inst_resp_7e4\x122\n\x0cvehicle2_4f1\x18\r \x01(\x0b2\x1c.apollo.drivers.Vehicle2_4f1\x122\n\x0cvehicle1_4f0\x18\x0e \x01(\x0b2\x1c.apollo.drivers.Vehicle1_4f0\x122\n\x0cesr_sim1_5c0\x18\x0f \x01(\x0b2\x1c.apollo.drivers.Esr_sim1_5c0\x128\n\x0fesr_status1_4e0\x18\x10 \x01(\x0b2\x1f.apollo.drivers.Esr_status1_4e0\x128\n\x0fesr_status2_4e1\x18\x11 \x01(\x0b2\x1f.apollo.drivers.Esr_status2_4e1\x128\n\x0fesr_status8_5e7\x18\x12 \x01(\x0b2\x1f.apollo.drivers.Esr_status8_5e7\x128\n\x0fesr_status7_5e6\x18\x13 \x01(\x0b2\x1f.apollo.drivers.Esr_status7_5e6\x122\n\x0cvehicle3_5f2\x18\x14 \x01(\x0b2\x1c.apollo.drivers.Vehicle3_5f2\x122\n\x0cvehicle4_5f3\x18\x15 \x01(\x0b2\x1c.apollo.drivers.Vehicle4_5f3\x122\n\x0cvehicle5_5f4\x18\x16 \x01(\x0b2\x1c.apollo.drivers.Vehicle5_5f4\x122\n\x0cvehicle6_5f5\x18\x17 \x01(\x0b2\x1c.apollo.drivers.Vehicle6_5f5')
_ESR_STATUS9_5E8 = DESCRIPTOR.message_types_by_name['Esr_status9_5e8']
_ESR_STATUS6_5E5 = DESCRIPTOR.message_types_by_name['Esr_status6_5e5']
_ESR_STATUS5_5E4 = DESCRIPTOR.message_types_by_name['Esr_status5_5e4']
_ESR_STATUS3_4E2 = DESCRIPTOR.message_types_by_name['Esr_status3_4e2']
_ESR_STATUS4_4E3 = DESCRIPTOR.message_types_by_name['Esr_status4_4e3']
_ESR_TRACKMOTIONPOWER_540 = DESCRIPTOR.message_types_by_name['Esr_trackmotionpower_540']
_ESR_TRACKMOTIONPOWER_540_MOTIONPOWER = _ESR_TRACKMOTIONPOWER_540.nested_types_by_name['Motionpower']
_ACM_INST_REQ_7E0 = DESCRIPTOR.message_types_by_name['Acm_inst_req_7e0']
_ESR_TRACK01_500 = DESCRIPTOR.message_types_by_name['Esr_track01_500']
_ESR_VALID1_5D0 = DESCRIPTOR.message_types_by_name['Esr_valid1_5d0']
_ESR_VALID2_5D1 = DESCRIPTOR.message_types_by_name['Esr_valid2_5d1']
_ACM_INST_RESP_7E4 = DESCRIPTOR.message_types_by_name['Acm_inst_resp_7e4']
_VEHICLE2_4F1 = DESCRIPTOR.message_types_by_name['Vehicle2_4f1']
_VEHICLE1_4F0 = DESCRIPTOR.message_types_by_name['Vehicle1_4f0']
_ESR_SIM1_5C0 = DESCRIPTOR.message_types_by_name['Esr_sim1_5c0']
_ESR_STATUS1_4E0 = DESCRIPTOR.message_types_by_name['Esr_status1_4e0']
_ESR_STATUS2_4E1 = DESCRIPTOR.message_types_by_name['Esr_status2_4e1']
_ESR_STATUS8_5E7 = DESCRIPTOR.message_types_by_name['Esr_status8_5e7']
_ESR_STATUS7_5E6 = DESCRIPTOR.message_types_by_name['Esr_status7_5e6']
_VEHICLE3_5F2 = DESCRIPTOR.message_types_by_name['Vehicle3_5f2']
_VEHICLE4_5F3 = DESCRIPTOR.message_types_by_name['Vehicle4_5f3']
_VEHICLE5_5F4 = DESCRIPTOR.message_types_by_name['Vehicle5_5f4']
_VEHICLE6_5F5 = DESCRIPTOR.message_types_by_name['Vehicle6_5f5']
_DELPHIESR = DESCRIPTOR.message_types_by_name['DelphiESR']
_ESR_STATUS6_5E5_CAN_TX_VERTICAL_ALIGN_UPDATEDTYPE = _ESR_STATUS6_5E5.enum_types_by_name['Can_tx_vertical_align_updatedType']
_ESR_STATUS6_5E5_CAN_TX_FOUND_TARGETTYPE = _ESR_STATUS6_5E5.enum_types_by_name['Can_tx_found_targetType']
_ESR_STATUS6_5E5_CAN_TX_FACTORY_ALIGN_STATUS_2TYPE = _ESR_STATUS6_5E5.enum_types_by_name['Can_tx_factory_align_status_2Type']
_ESR_STATUS6_5E5_CAN_TX_FACTORY_ALIGN_STATUS_1TYPE = _ESR_STATUS6_5E5.enum_types_by_name['Can_tx_factory_align_status_1Type']
_ESR_STATUS6_5E5_CAN_TX_RECOMMEND_UNCONVERGETYPE = _ESR_STATUS6_5E5.enum_types_by_name['Can_tx_recommend_unconvergeType']
_ESR_STATUS6_5E5_CAN_TX_SYSTEM_POWER_MODETYPE = _ESR_STATUS6_5E5.enum_types_by_name['Can_tx_system_power_modeType']
_ESR_STATUS4_4E3_CAN_TX_TRUCK_TARGET_DETTYPE = _ESR_STATUS4_4E3.enum_types_by_name['Can_tx_truck_target_detType']
_ESR_STATUS4_4E3_CAN_TX_LR_ONLY_GRATING_LOBE_DETTYPE = _ESR_STATUS4_4E3.enum_types_by_name['Can_tx_lr_only_grating_lobe_detType']
_ESR_STATUS4_4E3_CAN_TX_SIDELOBE_BLOCKAGETYPE = _ESR_STATUS4_4E3.enum_types_by_name['Can_tx_sidelobe_blockageType']
_ESR_STATUS4_4E3_CAN_TX_PARTIAL_BLOCKAGETYPE = _ESR_STATUS4_4E3.enum_types_by_name['Can_tx_partial_blockageType']
_ESR_STATUS4_4E3_CAN_TX_MR_LR_MODETYPE = _ESR_STATUS4_4E3.enum_types_by_name['Can_tx_mr_lr_modeType']
_ESR_TRACK01_500_CAN_TX_TRACK_GROUPING_CHANGEDTYPE = _ESR_TRACK01_500.enum_types_by_name['Can_tx_track_grouping_changedType']
_ESR_TRACK01_500_CAN_TX_TRACK_ONCOMINGTYPE = _ESR_TRACK01_500.enum_types_by_name['Can_tx_track_oncomingType']
_ESR_TRACK01_500_CAN_TX_TRACK_BRIDGE_OBJECTTYPE = _ESR_TRACK01_500.enum_types_by_name['Can_tx_track_bridge_objectType']
_ESR_TRACK01_500_CAN_TX_TRACK_STATUSTYPE = _ESR_TRACK01_500.enum_types_by_name['Can_tx_track_statusType']
_ESR_TRACK01_500_CAN_TX_TRACK_MED_RANGE_MODETYPE = _ESR_TRACK01_500.enum_types_by_name['Can_tx_track_med_range_modeType']
_VEHICLE2_4F1_CAN_RX_MR_ONLY_TRANSMITTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_mr_only_transmitType']
_VEHICLE2_4F1_CAN_RX_LR_ONLY_TRANSMITTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_lr_only_transmitType']
_VEHICLE2_4F1_CAN_RX_CLEAR_FAULTSTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_clear_faultsType']
_VEHICLE2_4F1_CAN_RX_USE_ANGLE_MISALIGNMENTTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_use_angle_misalignmentType']
_VEHICLE2_4F1_CAN_RX_TURN_SIGNAL_STATUSTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_turn_signal_statusType']
_VEHICLE2_4F1_CAN_RX_BLOCKAGE_DISABLETYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_blockage_disableType']
_VEHICLE2_4F1_CAN_RX_VEHICLE_SPEED_VALIDITYTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_vehicle_speed_validityType']
_VEHICLE2_4F1_CAN_RX_MMR_UPSIDE_DOWNTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_mmr_upside_downType']
_VEHICLE2_4F1_CAN_RX_WIPER_STATUSTYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_wiper_statusType']
_VEHICLE2_4F1_CAN_RX_RAW_DATA_ENABLETYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_raw_data_enableType']
_VEHICLE2_4F1_CAN_RX_RADAR_CMD_RADIATETYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_radar_cmd_radiateType']
_VEHICLE2_4F1_CAN_RX_GROUPING_MODETYPE = _VEHICLE2_4F1.enum_types_by_name['Can_rx_grouping_modeType']
_VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_VALIDITYTYPE = _VEHICLE1_4F0.enum_types_by_name['Can_rx_steering_angle_validityType']
_VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_SIGNTYPE = _VEHICLE1_4F0.enum_types_by_name['Can_rx_steering_angle_signType']
_VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_RATE_SIGNTYPE = _VEHICLE1_4F0.enum_types_by_name['Can_rx_steering_angle_rate_signType']
_VEHICLE1_4F0_CAN_RX_YAW_RATE_VALIDITYTYPE = _VEHICLE1_4F0.enum_types_by_name['Can_rx_yaw_rate_validityType']
_VEHICLE1_4F0_CAN_RX_VEHICLE_SPEED_DIRECTIONTYPE = _VEHICLE1_4F0.enum_types_by_name['Can_rx_vehicle_speed_directionType']
_ESR_SIM1_5C0_CAN_RX_SIM_TRACK_IDTYPE = _ESR_SIM1_5C0.enum_types_by_name['Can_rx_sim_track_idType']
_ESR_SIM1_5C0_CAN_RX_SIM_STATUSTYPE = _ESR_SIM1_5C0.enum_types_by_name['Can_rx_sim_statusType']
_ESR_SIM1_5C0_CAN_RX_SIM_FUNCTIONTYPE = _ESR_SIM1_5C0.enum_types_by_name['Can_rx_sim_functionType']
_ESR_STATUS2_4E1_CAN_TX_RAW_DATA_MODETYPE = _ESR_STATUS2_4E1.enum_types_by_name['Can_tx_raw_data_modeType']
_ESR_STATUS2_4E1_CAN_TX_RANGE_PERF_ERRORTYPE = _ESR_STATUS2_4E1.enum_types_by_name['Can_tx_range_perf_errorType']
_ESR_STATUS2_4E1_CAN_TX_OVERHEAT_ERRORTYPE = _ESR_STATUS2_4E1.enum_types_by_name['Can_tx_overheat_errorType']
_ESR_STATUS2_4E1_CAN_TX_INTERNAL_ERRORTYPE = _ESR_STATUS2_4E1.enum_types_by_name['Can_tx_internal_errorType']
_ESR_STATUS2_4E1_CAN_TX_GROUPING_MODETYPE = _ESR_STATUS2_4E1.enum_types_by_name['Can_tx_grouping_modeType']
_ESR_STATUS2_4E1_CAN_TX_XCVR_OPERATIONALTYPE = _ESR_STATUS2_4E1.enum_types_by_name['Can_tx_xcvr_operationalType']
_VEHICLE3_5F2_CAN_RX_SERV_ALIGN_TYPETYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_serv_align_typeType']
_VEHICLE3_5F2_CAN_RX_SERV_ALIGN_ENABLETYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_serv_align_enableType']
_VEHICLE3_5F2_CAN_RX_AUTO_ALIGN_CONVERGEDTYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_auto_align_convergedType']
_VEHICLE3_5F2_CAN_RX_AUTO_ALIGN_DISABLETYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_auto_align_disableType']
_VEHICLE3_5F2_CAN_RX_WHEEL_SLIPTYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_wheel_slipType']
_VEHICLE3_5F2_CAN_RX_LONG_ACCEL_VALIDITYTYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_long_accel_validityType']
_VEHICLE3_5F2_CAN_RX_LAT_ACCEL_VALIDITYTYPE = _VEHICLE3_5F2.enum_types_by_name['Can_rx_lat_accel_validityType']
_VEHICLE4_5F3_CAN_RX_FAC_ALIGN_CMD_2TYPE = _VEHICLE4_5F3.enum_types_by_name['Can_rx_fac_align_cmd_2Type']
_VEHICLE4_5F3_CAN_RX_FAC_ALIGN_CMD_1TYPE = _VEHICLE4_5F3.enum_types_by_name['Can_rx_fac_align_cmd_1Type']
_VEHICLE5_5F4_CAN_RX_YAW_RATE_BIAS_SHIFTTYPE = _VEHICLE5_5F4.enum_types_by_name['Can_rx_yaw_rate_bias_shiftType']
Esr_status9_5e8 = _reflection.GeneratedProtocolMessageType('Esr_status9_5e8', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS9_5E8, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status9_5e8)
Esr_status6_5e5 = _reflection.GeneratedProtocolMessageType('Esr_status6_5e5', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS6_5E5, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status6_5e5)
Esr_status5_5e4 = _reflection.GeneratedProtocolMessageType('Esr_status5_5e4', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS5_5E4, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status5_5e4)
Esr_status3_4e2 = _reflection.GeneratedProtocolMessageType('Esr_status3_4e2', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS3_4E2, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status3_4e2)
Esr_status4_4e3 = _reflection.GeneratedProtocolMessageType('Esr_status4_4e3', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS4_4E3, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status4_4e3)
Esr_trackmotionpower_540 = _reflection.GeneratedProtocolMessageType('Esr_trackmotionpower_540', (_message.Message,), {'Motionpower': _reflection.GeneratedProtocolMessageType('Motionpower', (_message.Message,), {'DESCRIPTOR': _ESR_TRACKMOTIONPOWER_540_MOTIONPOWER, '__module__': 'modules.drivers.proto.delphi_esr_pb2'}), 'DESCRIPTOR': _ESR_TRACKMOTIONPOWER_540, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_trackmotionpower_540)
_sym_db.RegisterMessage(Esr_trackmotionpower_540.Motionpower)
Acm_inst_req_7e0 = _reflection.GeneratedProtocolMessageType('Acm_inst_req_7e0', (_message.Message,), {'DESCRIPTOR': _ACM_INST_REQ_7E0, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Acm_inst_req_7e0)
Esr_track01_500 = _reflection.GeneratedProtocolMessageType('Esr_track01_500', (_message.Message,), {'DESCRIPTOR': _ESR_TRACK01_500, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_track01_500)
Esr_valid1_5d0 = _reflection.GeneratedProtocolMessageType('Esr_valid1_5d0', (_message.Message,), {'DESCRIPTOR': _ESR_VALID1_5D0, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_valid1_5d0)
Esr_valid2_5d1 = _reflection.GeneratedProtocolMessageType('Esr_valid2_5d1', (_message.Message,), {'DESCRIPTOR': _ESR_VALID2_5D1, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_valid2_5d1)
Acm_inst_resp_7e4 = _reflection.GeneratedProtocolMessageType('Acm_inst_resp_7e4', (_message.Message,), {'DESCRIPTOR': _ACM_INST_RESP_7E4, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Acm_inst_resp_7e4)
Vehicle2_4f1 = _reflection.GeneratedProtocolMessageType('Vehicle2_4f1', (_message.Message,), {'DESCRIPTOR': _VEHICLE2_4F1, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Vehicle2_4f1)
Vehicle1_4f0 = _reflection.GeneratedProtocolMessageType('Vehicle1_4f0', (_message.Message,), {'DESCRIPTOR': _VEHICLE1_4F0, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Vehicle1_4f0)
Esr_sim1_5c0 = _reflection.GeneratedProtocolMessageType('Esr_sim1_5c0', (_message.Message,), {'DESCRIPTOR': _ESR_SIM1_5C0, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_sim1_5c0)
Esr_status1_4e0 = _reflection.GeneratedProtocolMessageType('Esr_status1_4e0', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS1_4E0, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status1_4e0)
Esr_status2_4e1 = _reflection.GeneratedProtocolMessageType('Esr_status2_4e1', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS2_4E1, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status2_4e1)
Esr_status8_5e7 = _reflection.GeneratedProtocolMessageType('Esr_status8_5e7', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS8_5E7, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status8_5e7)
Esr_status7_5e6 = _reflection.GeneratedProtocolMessageType('Esr_status7_5e6', (_message.Message,), {'DESCRIPTOR': _ESR_STATUS7_5E6, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Esr_status7_5e6)
Vehicle3_5f2 = _reflection.GeneratedProtocolMessageType('Vehicle3_5f2', (_message.Message,), {'DESCRIPTOR': _VEHICLE3_5F2, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Vehicle3_5f2)
Vehicle4_5f3 = _reflection.GeneratedProtocolMessageType('Vehicle4_5f3', (_message.Message,), {'DESCRIPTOR': _VEHICLE4_5F3, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Vehicle4_5f3)
Vehicle5_5f4 = _reflection.GeneratedProtocolMessageType('Vehicle5_5f4', (_message.Message,), {'DESCRIPTOR': _VEHICLE5_5F4, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Vehicle5_5f4)
Vehicle6_5f5 = _reflection.GeneratedProtocolMessageType('Vehicle6_5f5', (_message.Message,), {'DESCRIPTOR': _VEHICLE6_5F5, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(Vehicle6_5f5)
DelphiESR = _reflection.GeneratedProtocolMessageType('DelphiESR', (_message.Message,), {'DESCRIPTOR': _DELPHIESR, '__module__': 'modules.drivers.proto.delphi_esr_pb2'})
_sym_db.RegisterMessage(DelphiESR)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ESR_STATUS9_5E8._serialized_start = 94
    _ESR_STATUS9_5E8._serialized_end = 346
    _ESR_STATUS6_5E5._serialized_start = 349
    _ESR_STATUS6_5E5._serialized_end = 2551
    _ESR_STATUS6_5E5_CAN_TX_VERTICAL_ALIGN_UPDATEDTYPE._serialized_start = 1218
    _ESR_STATUS6_5E5_CAN_TX_VERTICAL_ALIGN_UPDATEDTYPE._serialized_end = 1343
    _ESR_STATUS6_5E5_CAN_TX_FOUND_TARGETTYPE._serialized_start = 1345
    _ESR_STATUS6_5E5_CAN_TX_FOUND_TARGETTYPE._serialized_end = 1436
    _ESR_STATUS6_5E5_CAN_TX_FACTORY_ALIGN_STATUS_2TYPE._serialized_start = 1439
    _ESR_STATUS6_5E5_CAN_TX_FACTORY_ALIGN_STATUS_2TYPE._serialized_end = 1754
    _ESR_STATUS6_5E5_CAN_TX_FACTORY_ALIGN_STATUS_1TYPE._serialized_start = 1757
    _ESR_STATUS6_5E5_CAN_TX_FACTORY_ALIGN_STATUS_1TYPE._serialized_end = 2072
    _ESR_STATUS6_5E5_CAN_TX_RECOMMEND_UNCONVERGETYPE._serialized_start = 2074
    _ESR_STATUS6_5E5_CAN_TX_RECOMMEND_UNCONVERGETYPE._serialized_end = 2197
    _ESR_STATUS6_5E5_CAN_TX_SYSTEM_POWER_MODETYPE._serialized_start = 2200
    _ESR_STATUS6_5E5_CAN_TX_SYSTEM_POWER_MODETYPE._serialized_end = 2551
    _ESR_STATUS5_5E4._serialized_start = 2554
    _ESR_STATUS5_5E4._serialized_end = 2801
    _ESR_STATUS3_4E2._serialized_start = 2804
    _ESR_STATUS3_4E2._serialized_end = 2972
    _ESR_STATUS4_4E3._serialized_start = 2975
    _ESR_STATUS4_4E3._serialized_end = 4405
    _ESR_STATUS4_4E3_CAN_TX_TRUCK_TARGET_DETTYPE._serialized_start = 3730
    _ESR_STATUS4_4E3_CAN_TX_TRUCK_TARGET_DETTYPE._serialized_end = 3839
    _ESR_STATUS4_4E3_CAN_TX_LR_ONLY_GRATING_LOBE_DETTYPE._serialized_start = 3842
    _ESR_STATUS4_4E3_CAN_TX_LR_ONLY_GRATING_LOBE_DETTYPE._serialized_end = 3975
    _ESR_STATUS4_4E3_CAN_TX_SIDELOBE_BLOCKAGETYPE._serialized_start = 3977
    _ESR_STATUS4_4E3_CAN_TX_SIDELOBE_BLOCKAGETYPE._serialized_end = 4074
    _ESR_STATUS4_4E3_CAN_TX_PARTIAL_BLOCKAGETYPE._serialized_start = 4076
    _ESR_STATUS4_4E3_CAN_TX_PARTIAL_BLOCKAGETYPE._serialized_end = 4183
    _ESR_STATUS4_4E3_CAN_TX_MR_LR_MODETYPE._serialized_start = 4186
    _ESR_STATUS4_4E3_CAN_TX_MR_LR_MODETYPE._serialized_end = 4405
    _ESR_TRACKMOTIONPOWER_540._serialized_start = 4408
    _ESR_TRACKMOTIONPOWER_540._serialized_end = 4737
    _ESR_TRACKMOTIONPOWER_540_MOTIONPOWER._serialized_start = 4599
    _ESR_TRACKMOTIONPOWER_540_MOTIONPOWER._serialized_end = 4737
    _ACM_INST_REQ_7E0._serialized_start = 4740
    _ACM_INST_REQ_7E0._serialized_end = 4877
    _ESR_TRACK01_500._serialized_start = 4880
    _ESR_TRACK01_500._serialized_end = 6547
    _ESR_TRACK01_500_CAN_TX_TRACK_GROUPING_CHANGEDTYPE._serialized_start = 5602
    _ESR_TRACK01_500_CAN_TX_TRACK_GROUPING_CHANGEDTYPE._serialized_end = 5741
    _ESR_TRACK01_500_CAN_TX_TRACK_ONCOMINGTYPE._serialized_start = 5743
    _ESR_TRACK01_500_CAN_TX_TRACK_ONCOMINGTYPE._serialized_end = 5845
    _ESR_TRACK01_500_CAN_TX_TRACK_BRIDGE_OBJECTTYPE._serialized_start = 5847
    _ESR_TRACK01_500_CAN_TX_TRACK_BRIDGE_OBJECTTYPE._serialized_end = 5961
    _ESR_TRACK01_500_CAN_TX_TRACK_STATUSTYPE._serialized_start = 5964
    _ESR_TRACK01_500_CAN_TX_TRACK_STATUSTYPE._serialized_end = 6315
    _ESR_TRACK01_500_CAN_TX_TRACK_MED_RANGE_MODETYPE._serialized_start = 6318
    _ESR_TRACK01_500_CAN_TX_TRACK_MED_RANGE_MODETYPE._serialized_end = 6547
    _ESR_VALID1_5D0._serialized_start = 6550
    _ESR_VALID1_5D0._serialized_end = 6723
    _ESR_VALID2_5D1._serialized_start = 6726
    _ESR_VALID2_5D1._serialized_end = 6899
    _ACM_INST_RESP_7E4._serialized_start = 6902
    _ACM_INST_RESP_7E4._serialized_end = 7068
    _VEHICLE2_4F1._serialized_start = 7071
    _VEHICLE2_4F1._serialized_end = 9790
    _VEHICLE2_4F1_CAN_RX_MR_ONLY_TRANSMITTYPE._serialized_start = 8389
    _VEHICLE2_4F1_CAN_RX_MR_ONLY_TRANSMITTYPE._serialized_end = 8483
    _VEHICLE2_4F1_CAN_RX_LR_ONLY_TRANSMITTYPE._serialized_start = 8485
    _VEHICLE2_4F1_CAN_RX_LR_ONLY_TRANSMITTYPE._serialized_end = 8579
    _VEHICLE2_4F1_CAN_RX_CLEAR_FAULTSTYPE._serialized_start = 8581
    _VEHICLE2_4F1_CAN_RX_CLEAR_FAULTSTYPE._serialized_end = 8663
    _VEHICLE2_4F1_CAN_RX_USE_ANGLE_MISALIGNMENTTYPE._serialized_start = 8665
    _VEHICLE2_4F1_CAN_RX_USE_ANGLE_MISALIGNMENTTYPE._serialized_end = 8777
    _VEHICLE2_4F1_CAN_RX_TURN_SIGNAL_STATUSTYPE._serialized_start = 8780
    _VEHICLE2_4F1_CAN_RX_TURN_SIGNAL_STATUSTYPE._serialized_end = 8960
    _VEHICLE2_4F1_CAN_RX_BLOCKAGE_DISABLETYPE._serialized_start = 8962
    _VEHICLE2_4F1_CAN_RX_BLOCKAGE_DISABLETYPE._serialized_end = 9066
    _VEHICLE2_4F1_CAN_RX_VEHICLE_SPEED_VALIDITYTYPE._serialized_start = 9068
    _VEHICLE2_4F1_CAN_RX_VEHICLE_SPEED_VALIDITYTYPE._serialized_end = 9187
    _VEHICLE2_4F1_CAN_RX_MMR_UPSIDE_DOWNTYPE._serialized_start = 9189
    _VEHICLE2_4F1_CAN_RX_MMR_UPSIDE_DOWNTYPE._serialized_end = 9299
    _VEHICLE2_4F1_CAN_RX_WIPER_STATUSTYPE._serialized_start = 9301
    _VEHICLE2_4F1_CAN_RX_WIPER_STATUSTYPE._serialized_end = 9383
    _VEHICLE2_4F1_CAN_RX_RAW_DATA_ENABLETYPE._serialized_start = 9385
    _VEHICLE2_4F1_CAN_RX_RAW_DATA_ENABLETYPE._serialized_end = 9482
    _VEHICLE2_4F1_CAN_RX_RADAR_CMD_RADIATETYPE._serialized_start = 9484
    _VEHICLE2_4F1_CAN_RX_RADAR_CMD_RADIATETYPE._serialized_end = 9581
    _VEHICLE2_4F1_CAN_RX_GROUPING_MODETYPE._serialized_start = 9584
    _VEHICLE2_4F1_CAN_RX_GROUPING_MODETYPE._serialized_end = 9790
    _VEHICLE1_4F0._serialized_start = 9793
    _VEHICLE1_4F0._serialized_end = 11091
    _VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_VALIDITYTYPE._serialized_start = 10471
    _VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_VALIDITYTYPE._serialized_end = 10593
    _VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_SIGNTYPE._serialized_start = 10595
    _VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_SIGNTYPE._serialized_end = 10718
    _VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_RATE_SIGNTYPE._serialized_start = 10721
    _VEHICLE1_4F0_CAN_RX_STEERING_ANGLE_RATE_SIGNTYPE._serialized_end = 10859
    _VEHICLE1_4F0_CAN_RX_YAW_RATE_VALIDITYTYPE._serialized_start = 10861
    _VEHICLE1_4F0_CAN_RX_YAW_RATE_VALIDITYTYPE._serialized_end = 10965
    _VEHICLE1_4F0_CAN_RX_VEHICLE_SPEED_DIRECTIONTYPE._serialized_start = 10967
    _VEHICLE1_4F0_CAN_RX_VEHICLE_SPEED_DIRECTIONTYPE._serialized_end = 11091
    _ESR_SIM1_5C0._serialized_start = 11094
    _ESR_SIM1_5C0._serialized_end = 12120
    _ESR_SIM1_5C0_CAN_RX_SIM_TRACK_IDTYPE._serialized_start = 11528
    _ESR_SIM1_5C0_CAN_RX_SIM_TRACK_IDTYPE._serialized_end = 11656
    _ESR_SIM1_5C0_CAN_RX_SIM_STATUSTYPE._serialized_start = 11659
    _ESR_SIM1_5C0_CAN_RX_SIM_STATUSTYPE._serialized_end = 11802
    _ESR_SIM1_5C0_CAN_RX_SIM_FUNCTIONTYPE._serialized_start = 11805
    _ESR_SIM1_5C0_CAN_RX_SIM_FUNCTIONTYPE._serialized_end = 12120
    _ESR_STATUS1_4E0._serialized_start = 12123
    _ESR_STATUS1_4E0._serialized_end = 12359
    _ESR_STATUS2_4E1._serialized_start = 12362
    _ESR_STATUS2_4E1._serialized_end = 13863
    _ESR_STATUS2_4E1_CAN_TX_RAW_DATA_MODETYPE._serialized_start = 13152
    _ESR_STATUS2_4E1_CAN_TX_RAW_DATA_MODETYPE._serialized_end = 13243
    _ESR_STATUS2_4E1_CAN_TX_RANGE_PERF_ERRORTYPE._serialized_start = 13245
    _ESR_STATUS2_4E1_CAN_TX_RANGE_PERF_ERRORTYPE._serialized_end = 13352
    _ESR_STATUS2_4E1_CAN_TX_OVERHEAT_ERRORTYPE._serialized_start = 13354
    _ESR_STATUS2_4E1_CAN_TX_OVERHEAT_ERRORTYPE._serialized_end = 13457
    _ESR_STATUS2_4E1_CAN_TX_INTERNAL_ERRORTYPE._serialized_start = 13459
    _ESR_STATUS2_4E1_CAN_TX_INTERNAL_ERRORTYPE._serialized_end = 13558
    _ESR_STATUS2_4E1_CAN_TX_GROUPING_MODETYPE._serialized_start = 13561
    _ESR_STATUS2_4E1_CAN_TX_GROUPING_MODETYPE._serialized_end = 13767
    _ESR_STATUS2_4E1_CAN_TX_XCVR_OPERATIONALTYPE._serialized_start = 13769
    _ESR_STATUS2_4E1_CAN_TX_XCVR_OPERATIONALTYPE._serialized_end = 13863
    _ESR_STATUS8_5E7._serialized_start = 13866
    _ESR_STATUS8_5E7._serialized_end = 14139
    _ESR_STATUS7_5E6._serialized_start = 14142
    _ESR_STATUS7_5E6._serialized_end = 14407
    _VEHICLE3_5F2._serialized_start = 14410
    _VEHICLE3_5F2._serialized_end = 16192
    _VEHICLE3_5F2_CAN_RX_SERV_ALIGN_TYPETYPE._serialized_start = 15328
    _VEHICLE3_5F2_CAN_RX_SERV_ALIGN_TYPETYPE._serialized_end = 15445
    _VEHICLE3_5F2_CAN_RX_SERV_ALIGN_ENABLETYPE._serialized_start = 15447
    _VEHICLE3_5F2_CAN_RX_SERV_ALIGN_ENABLETYPE._serialized_end = 15554
    _VEHICLE3_5F2_CAN_RX_AUTO_ALIGN_CONVERGEDTYPE._serialized_start = 15556
    _VEHICLE3_5F2_CAN_RX_AUTO_ALIGN_CONVERGEDTYPE._serialized_end = 15679
    _VEHICLE3_5F2_CAN_RX_AUTO_ALIGN_DISABLETYPE._serialized_start = 15681
    _VEHICLE3_5F2_CAN_RX_AUTO_ALIGN_DISABLETYPE._serialized_end = 15791
    _VEHICLE3_5F2_CAN_RX_WHEEL_SLIPTYPE._serialized_start = 15794
    _VEHICLE3_5F2_CAN_RX_WHEEL_SLIPTYPE._serialized_end = 15971
    _VEHICLE3_5F2_CAN_RX_LONG_ACCEL_VALIDITYTYPE._serialized_start = 15973
    _VEHICLE3_5F2_CAN_RX_LONG_ACCEL_VALIDITYTYPE._serialized_end = 16083
    _VEHICLE3_5F2_CAN_RX_LAT_ACCEL_VALIDITYTYPE._serialized_start = 16085
    _VEHICLE3_5F2_CAN_RX_LAT_ACCEL_VALIDITYTYPE._serialized_end = 16192
    _VEHICLE4_5F3._serialized_start = 16195
    _VEHICLE4_5F3._serialized_end = 16852
    _VEHICLE4_5F3_CAN_RX_FAC_ALIGN_CMD_2TYPE._serialized_start = 16668
    _VEHICLE4_5F3_CAN_RX_FAC_ALIGN_CMD_2TYPE._serialized_end = 16759
    _VEHICLE4_5F3_CAN_RX_FAC_ALIGN_CMD_1TYPE._serialized_start = 16761
    _VEHICLE4_5F3_CAN_RX_FAC_ALIGN_CMD_1TYPE._serialized_end = 16852
    _VEHICLE5_5F4._serialized_start = 16855
    _VEHICLE5_5F4._serialized_end = 17355
    _VEHICLE5_5F4_CAN_RX_YAW_RATE_BIAS_SHIFTTYPE._serialized_start = 17242
    _VEHICLE5_5F4_CAN_RX_YAW_RATE_BIAS_SHIFTTYPE._serialized_end = 17355
    _VEHICLE6_5F5._serialized_start = 17358
    _VEHICLE6_5F5._serialized_end = 17570
    _DELPHIESR._serialized_start = 17573
    _DELPHIESR._serialized_end = 18877