"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/planning/proto/task_config.proto\x12\x0fapollo.planning"\xcc\x01\n\x12CreepDeciderConfig\x12\x1a\n\rstop_distance\x18\x01 \x01(\x01:\x030.5\x12\x16\n\x0bspeed_limit\x18\x02 \x01(\x01:\x011\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x030.3\x12\x19\n\x0emin_boundary_t\x18\x04 \x01(\x01:\x016\x12 \n\x13ignore_max_st_min_t\x18\x05 \x01(\x01:\x030.1\x12\x1f\n\x13ignore_min_st_min_s\x18\x06 \x01(\x01:\x0215"\x97\x02\n\x17LaneChangeDeciderConfig\x12(\n enable_lane_change_urgency_check\x18\x01 \x01(\x08\x12,\n\x1denable_prioritize_change_lane\x18\x02 \x01(\x08:\x05false\x12(\n\x19enable_remove_change_lane\x18\x03 \x01(\x08:\x05false\x12#\n\x14reckless_change_lane\x18\x04 \x01(\x08:\x05false\x12,\n\x1fchange_lane_success_freeze_time\x18\x05 \x01(\x01:\x031.5\x12\'\n\x1cchange_lane_fail_freeze_time\x18\x06 \x01(\x01:\x011"\xde\x02\n LearningModelInferenceTaskConfig\x12O\n\nmodel_type\x18\x01 \x01(\x0e2;.apollo.planning.LearningModelInferenceTaskConfig.ModelType\x12\x16\n\x0ecpu_model_file\x18\x02 \x01(\t\x12\x16\n\x0egpu_model_file\x18\x03 \x01(\t\x12\x16\n\x08use_cuda\x18\x04 \x01(\x08:\x04true\x12\x1f\n\x12trajectory_delta_t\x18\x05 \x01(\x01:\x030.2\x12.\n\x1fallow_empty_learning_based_data\x18\x06 \x01(\x08:\x05false\x12,\n\x1dallow_empty_output_trajectory\x18\x07 \x01(\x08:\x05false""\n\tModelType\x12\x07\n\x03CNN\x10\x01\x12\x0c\n\x08CNN_LSTM\x10\x02"^\n*LearningModelInferenceTrajectoryTaskConfig\x120\n%min_adc_future_trajectory_time_length\x18\x01 \x01(\x01:\x012"\x88\x03\n\x19NaviObstacleDeciderConfig\x12\x1f\n\x12min_nudge_distance\x18\x01 \x01(\x01:\x030.2\x12\x1f\n\x12max_nudge_distance\x18\x02 \x01(\x01:\x031.2\x12%\n\x15max_allow_nudge_speed\x18\x03 \x01(\x01:\x0616.667\x12\x1a\n\rsafe_distance\x18\x04 \x01(\x01:\x030.2\x12#\n\x15nudge_allow_tolerance\x18\x05 \x01(\x01:\x040.05\x12\x18\n\rcycles_number\x18\x06 \x01(\r:\x013\x12\x1a\n\x0fjudge_dis_coeff\x18\x07 \x01(\x01:\x012\x12\x1b\n\x0fbasis_dis_value\x18\x08 \x01(\x01:\x0230\x12#\n\x16lateral_velocity_value\x18\t \x01(\x01:\x030.5\x12%\n\x1aspeed_decider_detect_range\x18\n \x01(\x01:\x011\x12"\n\x15max_keep_nudge_cycles\x18\x0b \x01(\r:\x03100"\xd5\x03\n\x15NaviPathDeciderConfig\x12\x1a\n\x0fmin_path_length\x18\x01 \x01(\x01:\x015\x12 \n\x15min_look_forward_time\x18\x02 \x01(\r:\x012\x12#\n\x16max_keep_lane_distance\x18\x03 \x01(\x01:\x030.8\x12!\n\x15max_keep_lane_shift_y\x18\x04 \x01(\x01:\x0220\x12 \n\x14min_keep_lane_offset\x18\x05 \x01(\x01:\x0215\x12*\n\x1ckeep_lane_shift_compensation\x18\x06 \x01(\x01:\x040.01\x12M\n\x1bmove_dest_lane_config_talbe\x18\x07 \x01(\x0b2(.apollo.planning.MoveDestLaneConfigTable\x12)\n\x1bmove_dest_lane_compensation\x18\x08 \x01(\x01:\x040.35\x12\x1e\n\x13max_kappa_threshold\x18\t \x01(\x01:\x010\x12,\n!kappa_move_dest_lane_compensation\x18\n \x01(\x01:\x010\x12 \n\x15start_plan_point_from\x18\x0b \x01(\r:\x010"N\n\x17MoveDestLaneConfigTable\x123\n\rlateral_shift\x18\x01 \x03(\x0b2\x1c.apollo.planning.ShiftConfig"O\n\x0bShiftConfig\x12\x17\n\tmax_speed\x18\x01 \x01(\x01:\x044.16\x12\'\n\x1amax_move_dest_lane_shift_y\x18\x03 \x01(\x01:\x030.4"\xd2\x04\n\x16NaviSpeedDeciderConfig\x12\x1a\n\x0fpreferred_accel\x18\x01 \x01(\x01:\x012\x12\x1a\n\x0fpreferred_decel\x18\x02 \x01(\x01:\x012\x12\x19\n\x0epreferred_jerk\x18\x03 \x01(\x01:\x012\x12\x14\n\tmax_accel\x18\x04 \x01(\x01:\x014\x12\x14\n\tmax_decel\x18\x05 \x01(\x01:\x015\x12\x1c\n\x0fobstacle_buffer\x18\x06 \x01(\x01:\x030.5\x12\x1d\n\x12safe_distance_base\x18\x07 \x01(\x01:\x012\x12\x1e\n\x13safe_distance_ratio\x18\x08 \x01(\x01:\x011\x12"\n\x15following_accel_ratio\x18\t \x01(\x01:\x030.5\x12%\n\x18soft_centric_accel_limit\x18\n \x01(\x01:\x031.2\x12%\n\x18hard_centric_accel_limit\x18\x0b \x01(\x01:\x031.5\x12\x1d\n\x10hard_speed_limit\x18\x0c \x01(\x01:\x03100\x12\x1c\n\x10hard_accel_limit\x18\r \x01(\x01:\x0210\x12\x1e\n\x10enable_safe_path\x18\x0e \x01(\x08:\x04true\x12)\n\x1benable_planning_start_point\x18\x0f \x01(\x08:\x04true\x12,\n\x1eenable_accel_auto_compensation\x18\x10 \x01(\x08:\x04true\x12\x18\n\rkappa_preview\x18\x11 \x01(\x01:\x010\x12\x1a\n\x0fkappa_threshold\x18\x12 \x01(\x01:\x010"\x1d\n\x1bPathAssessmentDeciderConfig"\xe7\x02\n\x17PathBoundsDeciderConfig\x12\x19\n\x11is_lane_borrowing\x18\x01 \x01(\x08\x12\x14\n\x0cis_pull_over\x18\x02 \x01(\x08\x12/\n#pull_over_destination_to_adc_buffer\x18\x03 \x01(\x01:\x0225\x123\n\'pull_over_destination_to_pathend_buffer\x18\x04 \x01(\x01:\x0210\x12(\n\x1apull_over_road_edge_buffer\x18\x05 \x01(\x01:\x040.15\x12:\n-pull_over_approach_lon_distance_adjust_factor\x18\x06 \x01(\x01:\x031.5\x12\x1b\n\x10adc_buffer_coeff\x18\x07 \x01(\x01:\x011\x122\n$is_extend_lane_bounds_to_include_adc\x18\x08 \x01(\x08:\x04true"8\n\x11PathDeciderConfig\x12#\n\x16static_obstacle_buffer\x18\x01 \x01(\x01:\x030.3";\n\x1bPathLaneBorrowDeciderConfig\x12\x1c\n\x14allow_lane_borrowing\x18\x01 \x01(\x08"h\n\x1aPathReferenceDeciderConfig\x12%\n\x19min_path_reference_length\x18\x01 \x01(\r:\x0220\x12#\n\x1bweight_x_ref_path_reference\x18\x02 \x01(\x01",\n\x16PathReuseDeciderConfig\x12\x12\n\nreuse_path\x18\x01 \x01(\x08"\xdd\x02\n*PiecewiseJerkNonlinearSpeedOptimizerConfig\x12\x17\n\nacc_weight\x18\x01 \x01(\x01:\x03500\x12\x18\n\x0bjerk_weight\x18\x02 \x01(\x01:\x03100\x12\x1b\n\x0elat_acc_weight\x18\x03 \x01(\x01:\x03500\x12\x1e\n\x12s_potential_weight\x18\x04 \x01(\x01:\x0210\x12\x18\n\x0cref_v_weight\x18\x05 \x01(\x01:\x0210\x12\x18\n\x0cref_s_weight\x18\x06 \x01(\x01:\x0210\x12\x18\n\x0cend_s_weight\x18\x07 \x01(\x01:\x0210\x12\x18\n\x0cend_v_weight\x18\x08 \x01(\x01:\x0210\x12\x18\n\x0cend_a_weight\x18\t \x01(\x01:\x0210\x12\x1f\n\x13soft_s_bound_weight\x18\n \x01(\x01:\x0210\x12\x1c\n\x0euse_warm_start\x18d \x01(\x08:\x04true"\xda\x01\n PiecewiseJerkPathOptimizerConfig\x12F\n\x13default_path_config\x18\x01 \x01(\x0b2).apollo.planning.PiecewiseJerkPathWeights\x12J\n\x17lane_change_path_config\x18\x02 \x01(\x0b2).apollo.planning.PiecewiseJerkPathWeights\x12"\n\x17path_reference_l_weight\x18\x03 \x01(\x01:\x010"}\n\x18PiecewiseJerkPathWeights\x12\x13\n\x08l_weight\x18\x01 \x01(\x01:\x011\x12\x16\n\tdl_weight\x18\x02 \x01(\x01:\x03100\x12\x18\n\nddl_weight\x18\x03 \x01(\x01:\x041000\x12\x1a\n\x0bdddl_weight\x18\x04 \x01(\x01:\x0510000"\xab\x01\n!PiecewiseJerkSpeedOptimizerConfig\x12\x15\n\nacc_weight\x18\x01 \x01(\x01:\x011\x12\x17\n\x0bjerk_weight\x18\x02 \x01(\x01:\x0210\x12"\n\x14kappa_penalty_weight\x18\x03 \x01(\x01:\x041000\x12\x18\n\x0cref_s_weight\x18\x04 \x01(\x01:\x0210\x12\x18\n\x0cref_v_weight\x18\x05 \x01(\x01:\x0210"\xce\x02\n\x1aRuleBasedStopDeciderConfig\x12\x1f\n\x12max_adc_stop_speed\x18\x01 \x01(\x01:\x030.3\x12$\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x030.5\x12\x1d\n\x12search_beam_length\x18\x03 \x01(\x01:\x015\x12*\n\x1csearch_beam_radius_intensity\x18\x04 \x01(\x01:\x040.08\x12\x1a\n\x0csearch_range\x18\x05 \x01(\x01:\x043.14\x12&\n\x18is_block_angle_threshold\x18\x06 \x01(\x01:\x041.57\x12-\n!approach_distance_for_lane_change\x18\n \x01(\x01:\x0280\x12+\n\x1furgent_distance_for_lane_change\x18\x0b \x01(\x01:\x0250"\xbf\x02\n\x18SpeedBoundsDeciderConfig\x12\x15\n\ntotal_time\x18\x01 \x01(\x01:\x017\x12\x1c\n\x0fboundary_buffer\x18\x02 \x01(\x01:\x030.1\x12)\n\x1emax_centric_acceleration_limit\x18\x03 \x01(\x01:\x012\x12\x1c\n\rminimal_kappa\x18\x04 \x01(\x01:\x051e-05\x12\x1a\n\x0fpoint_extension\x18\x05 \x01(\x01:\x011\x12\x19\n\x0clowest_speed\x18\x06 \x01(\x01:\x032.5\x12!\n\x16collision_safety_range\x18\x07 \x01(\x01:\x011\x12$\n\x1cstatic_obs_nudge_speed_ratio\x18\x08 \x01(\x01\x12%\n\x1ddynamic_obs_nudge_speed_ratio\x18\t \x01(\x01"\xb5\x01\n\x1dSpeedHeuristicOptimizerConfig\x12G\n\x14default_speed_config\x18\x01 \x01(\x0b2).apollo.planning.DpStSpeedOptimizerConfig\x12K\n\x18lane_change_speed_config\x18\x02 \x01(\x0b2).apollo.planning.DpStSpeedOptimizerConfig"\xc9\x06\n\x18DpStSpeedOptimizerConfig\x12\x11\n\x06unit_t\x18\x01 \x01(\x01:\x011\x12\x1d\n\x11dense_dimension_s\x18\x02 \x01(\x05:\x0241\x12\x19\n\x0cdense_unit_s\x18\x03 \x01(\x01:\x030.5\x12\x18\n\rsparse_unit_s\x18\x04 \x01(\x01:\x011\x12\x17\n\x0cspeed_weight\x18\n \x01(\x01:\x010\x12\x18\n\x0caccel_weight\x18\x0b \x01(\x01:\x0210\x12\x17\n\x0bjerk_weight\x18\x0c \x01(\x01:\x0210\x12\x1a\n\x0fobstacle_weight\x18\r \x01(\x01:\x011\x12\x1b\n\x10reference_weight\x18\x0e \x01(\x01:\x010\x12\x19\n\x0ego_down_buffer\x18\x0f \x01(\x01:\x015\x12\x17\n\x0cgo_up_buffer\x18\x10 \x01(\x01:\x015\x12*\n\x15default_obstacle_cost\x18\x14 \x01(\x01:\x0b10000000000\x12\x1d\n\x12default_speed_cost\x18\x1f \x01(\x01:\x011\x12 \n\x14exceed_speed_penalty\x18  \x01(\x01:\x0210\x12\x1e\n\x11low_speed_penalty\x18! \x01(\x01:\x032.5\x12"\n\x17reference_speed_penalty\x18" \x01(\x01:\x011\x12(\n\x1ckeep_clear_low_speed_penalty\x18# \x01(\x01:\x0210\x12\x18\n\raccel_penalty\x18( \x01(\x01:\x012\x12\x18\n\rdecel_penalty\x18) \x01(\x01:\x012\x12\x1e\n\x13positive_jerk_coeff\x182 \x01(\x01:\x011\x12 \n\x13negative_jerk_coeff\x183 \x01(\x01:\x03300\x12\x1d\n\x10max_acceleration\x18< \x01(\x01:\x034.5\x12\x1e\n\x10max_deceleration\x18= \x01(\x01:\x04-4.5\x12\x1b\n\x10safe_time_buffer\x18F \x01(\x01:\x013\x12\x19\n\rsafe_distance\x18G \x01(\x01:\x0220\x12$\n\x19spatial_potential_penalty\x18P \x01(\x01:\x011\x12\x1f\n\x10is_lane_changing\x18Q \x01(\x08:\x05false".\n\x15STBoundsDeciderConfig\x12\x15\n\ntotal_time\x18\x01 \x01(\x01:\x017')
_CREEPDECIDERCONFIG = DESCRIPTOR.message_types_by_name['CreepDeciderConfig']
_LANECHANGEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['LaneChangeDeciderConfig']
_LEARNINGMODELINFERENCETASKCONFIG = DESCRIPTOR.message_types_by_name['LearningModelInferenceTaskConfig']
_LEARNINGMODELINFERENCETRAJECTORYTASKCONFIG = DESCRIPTOR.message_types_by_name['LearningModelInferenceTrajectoryTaskConfig']
_NAVIOBSTACLEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['NaviObstacleDeciderConfig']
_NAVIPATHDECIDERCONFIG = DESCRIPTOR.message_types_by_name['NaviPathDeciderConfig']
_MOVEDESTLANECONFIGTABLE = DESCRIPTOR.message_types_by_name['MoveDestLaneConfigTable']
_SHIFTCONFIG = DESCRIPTOR.message_types_by_name['ShiftConfig']
_NAVISPEEDDECIDERCONFIG = DESCRIPTOR.message_types_by_name['NaviSpeedDeciderConfig']
_PATHASSESSMENTDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathAssessmentDeciderConfig']
_PATHBOUNDSDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathBoundsDeciderConfig']
_PATHDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathDeciderConfig']
_PATHLANEBORROWDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathLaneBorrowDeciderConfig']
_PATHREFERENCEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathReferenceDeciderConfig']
_PATHREUSEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathReuseDeciderConfig']
_PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['PiecewiseJerkNonlinearSpeedOptimizerConfig']
_PIECEWISEJERKPATHOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['PiecewiseJerkPathOptimizerConfig']
_PIECEWISEJERKPATHWEIGHTS = DESCRIPTOR.message_types_by_name['PiecewiseJerkPathWeights']
_PIECEWISEJERKSPEEDOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['PiecewiseJerkSpeedOptimizerConfig']
_RULEBASEDSTOPDECIDERCONFIG = DESCRIPTOR.message_types_by_name['RuleBasedStopDeciderConfig']
_SPEEDBOUNDSDECIDERCONFIG = DESCRIPTOR.message_types_by_name['SpeedBoundsDeciderConfig']
_SPEEDHEURISTICOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['SpeedHeuristicOptimizerConfig']
_DPSTSPEEDOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['DpStSpeedOptimizerConfig']
_STBOUNDSDECIDERCONFIG = DESCRIPTOR.message_types_by_name['STBoundsDeciderConfig']
_LEARNINGMODELINFERENCETASKCONFIG_MODELTYPE = _LEARNINGMODELINFERENCETASKCONFIG.enum_types_by_name['ModelType']
CreepDeciderConfig = _reflection.GeneratedProtocolMessageType('CreepDeciderConfig', (_message.Message,), {'DESCRIPTOR': _CREEPDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(CreepDeciderConfig)
LaneChangeDeciderConfig = _reflection.GeneratedProtocolMessageType('LaneChangeDeciderConfig', (_message.Message,), {'DESCRIPTOR': _LANECHANGEDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(LaneChangeDeciderConfig)
LearningModelInferenceTaskConfig = _reflection.GeneratedProtocolMessageType('LearningModelInferenceTaskConfig', (_message.Message,), {'DESCRIPTOR': _LEARNINGMODELINFERENCETASKCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(LearningModelInferenceTaskConfig)
LearningModelInferenceTrajectoryTaskConfig = _reflection.GeneratedProtocolMessageType('LearningModelInferenceTrajectoryTaskConfig', (_message.Message,), {'DESCRIPTOR': _LEARNINGMODELINFERENCETRAJECTORYTASKCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(LearningModelInferenceTrajectoryTaskConfig)
NaviObstacleDeciderConfig = _reflection.GeneratedProtocolMessageType('NaviObstacleDeciderConfig', (_message.Message,), {'DESCRIPTOR': _NAVIOBSTACLEDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(NaviObstacleDeciderConfig)
NaviPathDeciderConfig = _reflection.GeneratedProtocolMessageType('NaviPathDeciderConfig', (_message.Message,), {'DESCRIPTOR': _NAVIPATHDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(NaviPathDeciderConfig)
MoveDestLaneConfigTable = _reflection.GeneratedProtocolMessageType('MoveDestLaneConfigTable', (_message.Message,), {'DESCRIPTOR': _MOVEDESTLANECONFIGTABLE, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(MoveDestLaneConfigTable)
ShiftConfig = _reflection.GeneratedProtocolMessageType('ShiftConfig', (_message.Message,), {'DESCRIPTOR': _SHIFTCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(ShiftConfig)
NaviSpeedDeciderConfig = _reflection.GeneratedProtocolMessageType('NaviSpeedDeciderConfig', (_message.Message,), {'DESCRIPTOR': _NAVISPEEDDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(NaviSpeedDeciderConfig)
PathAssessmentDeciderConfig = _reflection.GeneratedProtocolMessageType('PathAssessmentDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHASSESSMENTDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PathAssessmentDeciderConfig)
PathBoundsDeciderConfig = _reflection.GeneratedProtocolMessageType('PathBoundsDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHBOUNDSDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PathBoundsDeciderConfig)
PathDeciderConfig = _reflection.GeneratedProtocolMessageType('PathDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PathDeciderConfig)
PathLaneBorrowDeciderConfig = _reflection.GeneratedProtocolMessageType('PathLaneBorrowDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHLANEBORROWDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PathLaneBorrowDeciderConfig)
PathReferenceDeciderConfig = _reflection.GeneratedProtocolMessageType('PathReferenceDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHREFERENCEDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PathReferenceDeciderConfig)
PathReuseDeciderConfig = _reflection.GeneratedProtocolMessageType('PathReuseDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHREUSEDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PathReuseDeciderConfig)
PiecewiseJerkNonlinearSpeedOptimizerConfig = _reflection.GeneratedProtocolMessageType('PiecewiseJerkNonlinearSpeedOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PiecewiseJerkNonlinearSpeedOptimizerConfig)
PiecewiseJerkPathOptimizerConfig = _reflection.GeneratedProtocolMessageType('PiecewiseJerkPathOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _PIECEWISEJERKPATHOPTIMIZERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PiecewiseJerkPathOptimizerConfig)
PiecewiseJerkPathWeights = _reflection.GeneratedProtocolMessageType('PiecewiseJerkPathWeights', (_message.Message,), {'DESCRIPTOR': _PIECEWISEJERKPATHWEIGHTS, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PiecewiseJerkPathWeights)
PiecewiseJerkSpeedOptimizerConfig = _reflection.GeneratedProtocolMessageType('PiecewiseJerkSpeedOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _PIECEWISEJERKSPEEDOPTIMIZERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(PiecewiseJerkSpeedOptimizerConfig)
RuleBasedStopDeciderConfig = _reflection.GeneratedProtocolMessageType('RuleBasedStopDeciderConfig', (_message.Message,), {'DESCRIPTOR': _RULEBASEDSTOPDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(RuleBasedStopDeciderConfig)
SpeedBoundsDeciderConfig = _reflection.GeneratedProtocolMessageType('SpeedBoundsDeciderConfig', (_message.Message,), {'DESCRIPTOR': _SPEEDBOUNDSDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(SpeedBoundsDeciderConfig)
SpeedHeuristicOptimizerConfig = _reflection.GeneratedProtocolMessageType('SpeedHeuristicOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _SPEEDHEURISTICOPTIMIZERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(SpeedHeuristicOptimizerConfig)
DpStSpeedOptimizerConfig = _reflection.GeneratedProtocolMessageType('DpStSpeedOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _DPSTSPEEDOPTIMIZERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(DpStSpeedOptimizerConfig)
STBoundsDeciderConfig = _reflection.GeneratedProtocolMessageType('STBoundsDeciderConfig', (_message.Message,), {'DESCRIPTOR': _STBOUNDSDECIDERCONFIG, '__module__': 'modules.planning.proto.task_config_pb2'})
_sym_db.RegisterMessage(STBoundsDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CREEPDECIDERCONFIG._serialized_start = 62
    _CREEPDECIDERCONFIG._serialized_end = 266
    _LANECHANGEDECIDERCONFIG._serialized_start = 269
    _LANECHANGEDECIDERCONFIG._serialized_end = 548
    _LEARNINGMODELINFERENCETASKCONFIG._serialized_start = 551
    _LEARNINGMODELINFERENCETASKCONFIG._serialized_end = 901
    _LEARNINGMODELINFERENCETASKCONFIG_MODELTYPE._serialized_start = 867
    _LEARNINGMODELINFERENCETASKCONFIG_MODELTYPE._serialized_end = 901
    _LEARNINGMODELINFERENCETRAJECTORYTASKCONFIG._serialized_start = 903
    _LEARNINGMODELINFERENCETRAJECTORYTASKCONFIG._serialized_end = 997
    _NAVIOBSTACLEDECIDERCONFIG._serialized_start = 1000
    _NAVIOBSTACLEDECIDERCONFIG._serialized_end = 1392
    _NAVIPATHDECIDERCONFIG._serialized_start = 1395
    _NAVIPATHDECIDERCONFIG._serialized_end = 1864
    _MOVEDESTLANECONFIGTABLE._serialized_start = 1866
    _MOVEDESTLANECONFIGTABLE._serialized_end = 1944
    _SHIFTCONFIG._serialized_start = 1946
    _SHIFTCONFIG._serialized_end = 2025
    _NAVISPEEDDECIDERCONFIG._serialized_start = 2028
    _NAVISPEEDDECIDERCONFIG._serialized_end = 2622
    _PATHASSESSMENTDECIDERCONFIG._serialized_start = 2624
    _PATHASSESSMENTDECIDERCONFIG._serialized_end = 2653
    _PATHBOUNDSDECIDERCONFIG._serialized_start = 2656
    _PATHBOUNDSDECIDERCONFIG._serialized_end = 3015
    _PATHDECIDERCONFIG._serialized_start = 3017
    _PATHDECIDERCONFIG._serialized_end = 3073
    _PATHLANEBORROWDECIDERCONFIG._serialized_start = 3075
    _PATHLANEBORROWDECIDERCONFIG._serialized_end = 3134
    _PATHREFERENCEDECIDERCONFIG._serialized_start = 3136
    _PATHREFERENCEDECIDERCONFIG._serialized_end = 3240
    _PATHREUSEDECIDERCONFIG._serialized_start = 3242
    _PATHREUSEDECIDERCONFIG._serialized_end = 3286
    _PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG._serialized_start = 3289
    _PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG._serialized_end = 3638
    _PIECEWISEJERKPATHOPTIMIZERCONFIG._serialized_start = 3641
    _PIECEWISEJERKPATHOPTIMIZERCONFIG._serialized_end = 3859
    _PIECEWISEJERKPATHWEIGHTS._serialized_start = 3861
    _PIECEWISEJERKPATHWEIGHTS._serialized_end = 3986
    _PIECEWISEJERKSPEEDOPTIMIZERCONFIG._serialized_start = 3989
    _PIECEWISEJERKSPEEDOPTIMIZERCONFIG._serialized_end = 4160
    _RULEBASEDSTOPDECIDERCONFIG._serialized_start = 4163
    _RULEBASEDSTOPDECIDERCONFIG._serialized_end = 4497
    _SPEEDBOUNDSDECIDERCONFIG._serialized_start = 4500
    _SPEEDBOUNDSDECIDERCONFIG._serialized_end = 4819
    _SPEEDHEURISTICOPTIMIZERCONFIG._serialized_start = 4822
    _SPEEDHEURISTICOPTIMIZERCONFIG._serialized_end = 5003
    _DPSTSPEEDOPTIMIZERCONFIG._serialized_start = 5006
    _DPSTSPEEDOPTIMIZERCONFIG._serialized_end = 5847
    _STBOUNDSDECIDERCONFIG._serialized_start = 5849
    _STBOUNDSDECIDERCONFIG._serialized_end = 5895