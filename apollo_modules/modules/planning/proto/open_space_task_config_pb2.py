"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.planning.proto import planner_open_space_config_pb2 as modules_dot_planning_dot_proto_dot_planner__open__space__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/planning/proto/open_space_task_config.proto\x12\x0fapollo.planning\x1a6modules/planning/proto/planner_open_space_config.proto"\xe6\x01\n\x1eOpenSpaceFallBackDeciderConfig\x12,\n!open_space_prediction_time_period\x18\x01 \x01(\x01:\x015\x121\n&open_space_fallback_collision_distance\x18\x02 \x01(\x01:\x015\x12,\n!open_space_fallback_stop_distance\x18\x03 \x01(\x01:\x012\x125\n)open_space_fallback_collision_time_buffer\x18\x04 \x01(\x01:\x0210"\x9d\x02\n\x1dOpenSpacePreStopDeciderConfig\x12J\n\tstop_type\x18\x01 \x01(\x0e27.apollo.planning.OpenSpacePreStopDeciderConfig.StopType\x12"\n\x17rightaway_stop_distance\x18\x02 \x01(\x01:\x012\x12"\n\x17stop_distance_to_target\x18\x03 \x01(\x01:\x015"h\n\x08StopType\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x0b\n\x07PARKING\x10\x01\x12\r\n\tPULL_OVER\x10\x02\x12\x18\n\x14NARROW_STREET_U_TURN\x10\x03\x12\x15\n\x11DEAD_END_PRE_STOP\x10\x04"\xc2\x06\n\x19OpenSpaceRoiDeciderConfig\x12D\n\x08roi_type\x18\x01 \x01(\x0e22.apollo.planning.OpenSpaceRoiDeciderConfig.RoiType\x12(\n\x1croi_longitudinal_range_start\x18\x02 \x01(\x01:\x0210\x12&\n\x1aroi_longitudinal_range_end\x18\x03 \x01(\x01:\x0210\x12\x1e\n\x13parking_start_range\x18\x04 \x01(\x01:\x017\x12\x1e\n\x0fparking_inwards\x18\x05 \x01(\x08:\x05false\x12#\n\x1benable_perception_obstacles\x18\x06 \x01(\x08\x12!\n\x14parking_depth_buffer\x18\x07 \x01(\x01:\x030.1\x12\'\n\x1aroi_line_segment_min_angle\x18\x08 \x01(\x01:\x030.3\x12"\n\x17roi_line_segment_length\x18\t \x01(\x01:\x011\x12,\n roi_line_segment_length_from_map\x18\n \x01(\x01:\x0210\x124\n&perception_obstacle_filtering_distance\x18\x0b \x01(\x01:\x041000\x12"\n\x1aperception_obstacle_buffer\x18\x0c \x01(\x01\x122\n\'curb_heading_tangent_change_upper_limit\x18\r \x01(\x01:\x011\x12\x1f\n\x13end_pose_s_distance\x18\x0e \x01(\x01:\x0210\x12\'\n\x1aparallel_park_end_x_buffer\x18\x0f \x01(\x01:\x030.2\x12 \n\x15extend_right_x_buffer\x18\x10 \x01(\x01:\x010\x12\x1f\n\x14extend_left_x_buffer\x18\x11 \x01(\x01:\x010"o\n\x07RoiType\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x0b\n\x07PARKING\x10\x01\x12\r\n\tPULL_OVER\x10\x02\x12\x0f\n\x0bPARK_AND_GO\x10\x03\x12\x18\n\x14NARROW_STREET_U_TURN\x10\x04\x12\x0c\n\x08DEAD_END\x10\x05"\x82\x04\n"OpenSpaceTrajectoryPartitionConfig\x12\x18\n\x10gear_shift_max_t\x18\x01 \x01(\x01\x12\x19\n\x11gear_shift_unit_t\x18\x02 \x01(\x01\x12"\n\x1agear_shift_period_duration\x18\x03 \x01(\x01\x12\x1f\n\x17interpolated_pieces_num\x18\x04 \x01(\x04\x12"\n\x1ainitial_gear_check_horizon\x18\x05 \x01(\x04\x12\x1c\n\x14heading_search_range\x18\x06 \x01(\x01\x12\x1b\n\x13heading_track_range\x18\x07 \x01(\x01\x12$\n\x15distance_search_range\x18\x08 \x01(\x01:\x051e-06\x12"\n\x1aheading_offset_to_midpoint\x18\t \x01(\x01\x12\'\n\x1alateral_offset_to_midpoint\x18\n \x01(\x01:\x030.1\x12,\n\x1flongitudinal_offset_to_midpoint\x18\x0b \x01(\x01:\x030.1\x123\n%vehicle_box_iou_threshold_to_midpoint\x18\x0c \x01(\x01:\x040.95\x12-\n linear_velocity_threshold_on_ego\x18\r \x01(\x01:\x030.2"\x88\x01\n!OpenSpaceTrajectoryProviderConfig\x12c\n&open_space_trajectory_optimizer_config\x18\x01 \x01(\x0b23.apollo.planning.OpenSpaceTrajectoryOptimizerConfig"\xb5\x03\n"OpenSpaceTrajectoryOptimizerConfig\x12@\n\x14hybrid_a_star_config\x18\x01 \x01(\x0b2".apollo.planning.HybridAStarConfig\x12L\n\x1fdual_variable_warm_start_config\x18\x02 \x01(\x0b2#.apollo.planning.DualVariableConfig\x12o\n,distance_approach_trajectory_smoother_config\x18\x03 \x01(\x0b29.apollo.planning.DistanceApproachTrajectorySmootherConfig\x12\x14\n\x07delta_t\x18\x04 \x01(\x02:\x030.5\x12,\n\x1dis_near_destination_threshold\x18\x05 \x01(\x01:\x050.001\x12J\n\x19planner_open_space_config\x18\x06 \x01(\x0b2\'.apollo.planning.PlannerOpenSpaceConfig"\xf9\x02\n\x11HybridAStarConfig\x12\x1f\n\x12xy_grid_resolution\x18\x01 \x01(\x01:\x030.2\x12!\n\x13phi_grid_resolution\x18\x02 \x01(\x01:\x040.05\x12\x19\n\rnext_node_num\x18\x03 \x01(\x04:\x0210\x12\x16\n\tstep_size\x18\x04 \x01(\x01:\x030.5\x12\x1f\n\x14traj_forward_penalty\x18\x05 \x01(\x01:\x010\x12\x1c\n\x11traj_back_penalty\x18\x06 \x01(\x01:\x010\x12$\n\x18traj_gear_switch_penalty\x18\x07 \x01(\x01:\x0210\x12\x1f\n\x12traj_steer_penalty\x18\x08 \x01(\x01:\x03100\x12%\n\x19traj_steer_change_penalty\x18\t \x01(\x01:\x0210\x12&\n\x19grid_a_star_xy_resolution\x18\x0f \x01(\x01:\x030.1\x12\x18\n\x0bnode_radius\x18\x10 \x01(\x01:\x030.5"\xe5\x01\n\x12DualVariableConfig\x12\x13\n\x08weight_d\x18\x01 \x01(\x01:\x011\x128\n\x0cipopt_config\x18\x02 \x01(\x0b2".apollo.planning.IpoptSolverConfig\x124\n\tqp_format\x18\x03 \x01(\x0e2!.apollo.planning.DualVariableMode\x12\x1e\n\x13min_safety_distance\x18\x04 \x01(\x01:\x010\x12\x19\n\ndebug_osqp\x18\x05 \x01(\x08:\x05false\x12\x0f\n\x04beta\x18\x06 \x01(\x01:\x011"\xa2\x06\n(DistanceApproachTrajectorySmootherConfig\x12\x14\n\x0cweight_steer\x18\x01 \x01(\x01\x12\x10\n\x08weight_a\x18\x02 \x01(\x01\x12\x19\n\x11weight_steer_rate\x18\x03 \x01(\x01\x12\x15\n\rweight_a_rate\x18\x04 \x01(\x01\x12\x10\n\x08weight_x\x18\x05 \x01(\x01\x12\x10\n\x08weight_y\x18\x06 \x01(\x01\x12\x12\n\nweight_phi\x18\x07 \x01(\x01\x12\x10\n\x08weight_v\x18\x08 \x01(\x01\x12\x1e\n\x16weight_steer_stitching\x18\t \x01(\x01\x12\x1a\n\x12weight_a_stitching\x18\n \x01(\x01\x12\x1f\n\x17weight_first_order_time\x18\x0b \x01(\x01\x12 \n\x18weight_second_order_time\x18\x0c \x01(\x01\x12\x1e\n\x13min_safety_distance\x18\r \x01(\x01:\x010\x12\x1c\n\x11max_speed_forward\x18\x0e \x01(\x01:\x013\x12\x1c\n\x11max_speed_reverse\x18\x0f \x01(\x01:\x012\x12#\n\x18max_acceleration_forward\x18\x10 \x01(\x01:\x012\x12#\n\x18max_acceleration_reverse\x18\x11 \x01(\x01:\x012\x12$\n\x17min_time_sample_scaling\x18\x12 \x01(\x01:\x030.1\x12#\n\x17max_time_sample_scaling\x18\x13 \x01(\x01:\x0210\x12\x1b\n\x0cuse_fix_time\x18\x14 \x01(\x08:\x05false\x128\n\x0cipopt_config\x18\x15 \x01(\x0b2".apollo.planning.IpoptSolverConfig\x12\x1f\n\x17enable_constraint_check\x18\x16 \x01(\x08\x12\x1e\n\x16enable_hand_derivative\x18\x17 \x01(\x08\x12\x1f\n\x17enable_derivative_check\x18\x18 \x01(\x08\x12)\n\x1aenable_initial_final_check\x18\x19 \x01(\x08:\x05false"\xff\x02\n\x11IpoptSolverConfig\x12\x19\n\x11ipopt_print_level\x18\x01 \x01(\x05\x12\x19\n\x11mumps_mem_percent\x18\x02 \x01(\x05\x12\x14\n\x0cmumps_pivtol\x18\x03 \x01(\x01\x12\x16\n\x0eipopt_max_iter\x18\x04 \x01(\x05\x12\x11\n\tipopt_tol\x18\x05 \x01(\x01\x12(\n ipopt_acceptable_constr_viol_tol\x18\x06 \x01(\x01\x12&\n\x1eipopt_min_hessian_perturbation\x18\x07 \x01(\x01\x12+\n#ipopt_jacobian_regularization_value\x18\x08 \x01(\x01\x12%\n\x1dipopt_print_timing_statistics\x18\t \x01(\t\x12\x19\n\x11ipopt_alpha_for_y\x18\n \x01(\t\x12\x16\n\x0eipopt_recalc_y\x18\x0b \x01(\t\x12\x1a\n\ripopt_mu_init\x18\x0c \x01(\x01:\x030.1*w\n\x10DualVariableMode\x12\x17\n\x13DUAL_VARIABLE_IPOPT\x10\x00\x12\x19\n\x15DUAL_VARIABLE_IPOPTQP\x10\x01\x12\x16\n\x12DUAL_VARIABLE_OSQP\x10\x02\x12\x17\n\x13DUAL_VARIABLE_DEBUG\x10\x03')
_DUALVARIABLEMODE = DESCRIPTOR.enum_types_by_name['DualVariableMode']
DualVariableMode = enum_type_wrapper.EnumTypeWrapper(_DUALVARIABLEMODE)
DUAL_VARIABLE_IPOPT = 0
DUAL_VARIABLE_IPOPTQP = 1
DUAL_VARIABLE_OSQP = 2
DUAL_VARIABLE_DEBUG = 3
_OPENSPACEFALLBACKDECIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceFallBackDeciderConfig']
_OPENSPACEPRESTOPDECIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpacePreStopDeciderConfig']
_OPENSPACEROIDECIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceRoiDeciderConfig']
_OPENSPACETRAJECTORYPARTITIONCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryPartitionConfig']
_OPENSPACETRAJECTORYPROVIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryProviderConfig']
_OPENSPACETRAJECTORYOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryOptimizerConfig']
_HYBRIDASTARCONFIG = DESCRIPTOR.message_types_by_name['HybridAStarConfig']
_DUALVARIABLECONFIG = DESCRIPTOR.message_types_by_name['DualVariableConfig']
_DISTANCEAPPROACHTRAJECTORYSMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['DistanceApproachTrajectorySmootherConfig']
_IPOPTSOLVERCONFIG = DESCRIPTOR.message_types_by_name['IpoptSolverConfig']
_OPENSPACEPRESTOPDECIDERCONFIG_STOPTYPE = _OPENSPACEPRESTOPDECIDERCONFIG.enum_types_by_name['StopType']
_OPENSPACEROIDECIDERCONFIG_ROITYPE = _OPENSPACEROIDECIDERCONFIG.enum_types_by_name['RoiType']
OpenSpaceFallBackDeciderConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceFallBackDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEFALLBACKDECIDERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(OpenSpaceFallBackDeciderConfig)
OpenSpacePreStopDeciderConfig = _reflection.GeneratedProtocolMessageType('OpenSpacePreStopDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEPRESTOPDECIDERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(OpenSpacePreStopDeciderConfig)
OpenSpaceRoiDeciderConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceRoiDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEROIDECIDERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(OpenSpaceRoiDeciderConfig)
OpenSpaceTrajectoryPartitionConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryPartitionConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYPARTITIONCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryPartitionConfig)
OpenSpaceTrajectoryProviderConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryProviderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYPROVIDERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryProviderConfig)
OpenSpaceTrajectoryOptimizerConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYOPTIMIZERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryOptimizerConfig)
HybridAStarConfig = _reflection.GeneratedProtocolMessageType('HybridAStarConfig', (_message.Message,), {'DESCRIPTOR': _HYBRIDASTARCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(HybridAStarConfig)
DualVariableConfig = _reflection.GeneratedProtocolMessageType('DualVariableConfig', (_message.Message,), {'DESCRIPTOR': _DUALVARIABLECONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(DualVariableConfig)
DistanceApproachTrajectorySmootherConfig = _reflection.GeneratedProtocolMessageType('DistanceApproachTrajectorySmootherConfig', (_message.Message,), {'DESCRIPTOR': _DISTANCEAPPROACHTRAJECTORYSMOOTHERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(DistanceApproachTrajectorySmootherConfig)
IpoptSolverConfig = _reflection.GeneratedProtocolMessageType('IpoptSolverConfig', (_message.Message,), {'DESCRIPTOR': _IPOPTSOLVERCONFIG, '__module__': 'modules.planning.proto.open_space_task_config_pb2'})
_sym_db.RegisterMessage(IpoptSolverConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DUALVARIABLEMODE._serialized_start = 4385
    _DUALVARIABLEMODE._serialized_end = 4504
    _OPENSPACEFALLBACKDECIDERCONFIG._serialized_start = 129
    _OPENSPACEFALLBACKDECIDERCONFIG._serialized_end = 359
    _OPENSPACEPRESTOPDECIDERCONFIG._serialized_start = 362
    _OPENSPACEPRESTOPDECIDERCONFIG._serialized_end = 647
    _OPENSPACEPRESTOPDECIDERCONFIG_STOPTYPE._serialized_start = 543
    _OPENSPACEPRESTOPDECIDERCONFIG_STOPTYPE._serialized_end = 647
    _OPENSPACEROIDECIDERCONFIG._serialized_start = 650
    _OPENSPACEROIDECIDERCONFIG._serialized_end = 1484
    _OPENSPACEROIDECIDERCONFIG_ROITYPE._serialized_start = 1373
    _OPENSPACEROIDECIDERCONFIG_ROITYPE._serialized_end = 1484
    _OPENSPACETRAJECTORYPARTITIONCONFIG._serialized_start = 1487
    _OPENSPACETRAJECTORYPARTITIONCONFIG._serialized_end = 2001
    _OPENSPACETRAJECTORYPROVIDERCONFIG._serialized_start = 2004
    _OPENSPACETRAJECTORYPROVIDERCONFIG._serialized_end = 2140
    _OPENSPACETRAJECTORYOPTIMIZERCONFIG._serialized_start = 2143
    _OPENSPACETRAJECTORYOPTIMIZERCONFIG._serialized_end = 2580
    _HYBRIDASTARCONFIG._serialized_start = 2583
    _HYBRIDASTARCONFIG._serialized_end = 2960
    _DUALVARIABLECONFIG._serialized_start = 2963
    _DUALVARIABLECONFIG._serialized_end = 3192
    _DISTANCEAPPROACHTRAJECTORYSMOOTHERCONFIG._serialized_start = 3195
    _DISTANCEAPPROACHTRAJECTORYSMOOTHERCONFIG._serialized_end = 3997
    _IPOPTSOLVERCONFIG._serialized_start = 4000
    _IPOPTSOLVERCONFIG._serialized_end = 4383