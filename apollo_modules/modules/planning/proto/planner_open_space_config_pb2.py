"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.planning.proto.math import fem_pos_deviation_smoother_config_pb2 as modules_dot_planning_dot_proto_dot_math_dot_fem__pos__deviation__smoother__config__pb2
from ....modules.planning.proto import task_config_pb2 as modules_dot_planning_dot_proto_dot_task__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/planning/proto/planner_open_space_config.proto\x12\x0fapollo.planning\x1aCmodules/planning/proto/math/fem_pos_deviation_smoother_config.proto\x1a(modules/planning/proto/task_config.proto"\xa2\x05\n\x16PlannerOpenSpaceConfig\x12.\n\nroi_config\x18\x01 \x01(\x0b2\x1a.apollo.planning.ROIConfig\x12;\n\x11warm_start_config\x18\x02 \x01(\x0b2 .apollo.planning.WarmStartConfig\x12U\n\x1fdual_variable_warm_start_config\x18\x03 \x01(\x0b2,.apollo.planning.DualVariableWarmStartConfig\x12I\n\x18distance_approach_config\x18\x04 \x01(\x0b2\'.apollo.planning.DistanceApproachConfig\x12V\n#iterative_anchoring_smoother_config\x18\x05 \x01(\x0b2).apollo.planning.IterativeAnchoringConfig\x12O\n\x1btrajectory_partition_config\x18\x06 \x01(\x0b2*.apollo.planning.TrajectoryPartitionConfig\x12\x12\n\x07delta_t\x18\x07 \x01(\x02:\x011\x12,\n\x1dis_near_destination_threshold\x18\x08 \x01(\x01:\x050.001\x12/\n enable_check_parallel_trajectory\x18\t \x01(\x08:\x05false\x12*\n\x1benable_linear_interpolation\x18\n \x01(\x08:\x05false\x121\n#is_near_destination_theta_threshold\x18\x0b \x01(\x01:\x040.05"\x9d\x01\n\tROIConfig\x12(\n\x1croi_longitudinal_range_start\x18\x01 \x01(\x01:\x0210\x12&\n\x1aroi_longitudinal_range_end\x18\x02 \x01(\x01:\x0210\x12\x1e\n\x13parking_start_range\x18\x03 \x01(\x01:\x017\x12\x1e\n\x0fparking_inwards\x18\x04 \x01(\x08:\x05false"\xc3\x03\n\x0fWarmStartConfig\x12\x1f\n\x12xy_grid_resolution\x18\x01 \x01(\x01:\x030.2\x12!\n\x13phi_grid_resolution\x18\x02 \x01(\x01:\x040.05\x12\x19\n\rnext_node_num\x18\x03 \x01(\x04:\x0210\x12\x16\n\tstep_size\x18\x04 \x01(\x01:\x030.5\x12\x1f\n\x14traj_forward_penalty\x18\x05 \x01(\x01:\x010\x12\x1c\n\x11traj_back_penalty\x18\x06 \x01(\x01:\x010\x12$\n\x18traj_gear_switch_penalty\x18\x07 \x01(\x01:\x0210\x12\x1f\n\x12traj_steer_penalty\x18\x08 \x01(\x01:\x03100\x12%\n\x19traj_steer_change_penalty\x18\t \x01(\x01:\x0210\x12&\n\x19grid_a_star_xy_resolution\x18\x0f \x01(\x01:\x030.1\x12\x18\n\x0bnode_radius\x18\x10 \x01(\x01:\x030.5\x12J\n\x0es_curve_config\x18\x11 \x01(\x0b22.apollo.planning.PiecewiseJerkSpeedOptimizerConfig"\x98\x02\n\x1bDualVariableWarmStartConfig\x12\x13\n\x08weight_d\x18\x01 \x01(\x01:\x011\x122\n\x0cipopt_config\x18\x02 \x01(\x0b2\x1c.apollo.planning.IpoptConfig\x122\n\tqp_format\x18\x03 \x01(\x0e2\x1f.apollo.planning.DualWarmUpMode\x12\x1e\n\x13min_safety_distance\x18\x04 \x01(\x01:\x010\x12\x19\n\ndebug_osqp\x18\x05 \x01(\x08:\x05false\x12\x0f\n\x04beta\x18\x06 \x01(\x01:\x011\x120\n\x0bosqp_config\x18\x07 \x01(\x0b2\x1b.apollo.planning.OSQPConfig"\xd5\x07\n\x16DistanceApproachConfig\x12\x14\n\x0cweight_steer\x18\x01 \x01(\x01\x12\x10\n\x08weight_a\x18\x02 \x01(\x01\x12\x19\n\x11weight_steer_rate\x18\x03 \x01(\x01\x12\x15\n\rweight_a_rate\x18\x04 \x01(\x01\x12\x10\n\x08weight_x\x18\x05 \x01(\x01\x12\x10\n\x08weight_y\x18\x06 \x01(\x01\x12\x12\n\nweight_phi\x18\x07 \x01(\x01\x12\x10\n\x08weight_v\x18\x08 \x01(\x01\x12\x1e\n\x16weight_steer_stitching\x18\t \x01(\x01\x12\x1a\n\x12weight_a_stitching\x18\n \x01(\x01\x12\x1f\n\x17weight_first_order_time\x18\x0b \x01(\x01\x12 \n\x18weight_second_order_time\x18\x0c \x01(\x01\x12\x1e\n\x13min_safety_distance\x18\r \x01(\x01:\x010\x12\x1c\n\x11max_speed_forward\x18\x0e \x01(\x01:\x013\x12\x1c\n\x11max_speed_reverse\x18\x0f \x01(\x01:\x012\x12#\n\x18max_acceleration_forward\x18\x10 \x01(\x01:\x012\x12#\n\x18max_acceleration_reverse\x18\x11 \x01(\x01:\x012\x12$\n\x17min_time_sample_scaling\x18\x12 \x01(\x01:\x030.1\x12#\n\x17max_time_sample_scaling\x18\x13 \x01(\x01:\x0210\x12\x1b\n\x0cuse_fix_time\x18\x14 \x01(\x08:\x05false\x122\n\x0cipopt_config\x18\x15 \x01(\x0b2\x1c.apollo.planning.IpoptConfig\x12\x1f\n\x17enable_constraint_check\x18\x16 \x01(\x08\x12\x1e\n\x16enable_hand_derivative\x18\x17 \x01(\x08\x12\x1f\n\x17enable_derivative_check\x18\x18 \x01(\x08\x12)\n\x1aenable_initial_final_check\x18\x19 \x01(\x08:\x05false\x12E\n\x16distance_approach_mode\x18\x1a \x01(\x0e2%.apollo.planning.DistanceApproachMode\x12!\n\x12enable_jacobian_ad\x18\x1b \x01(\x08:\x05false\x12)\n\x1aenable_check_initial_state\x18\x1c \x01(\x08:\x05false\x12\x1b\n\x10weight_end_state\x18\x1d \x01(\x01:\x010\x12\x17\n\x0cweight_slack\x18\x1e \x01(\x01:\x010"\xf9\x02\n\x0bIpoptConfig\x12\x19\n\x11ipopt_print_level\x18\x01 \x01(\x05\x12\x19\n\x11mumps_mem_percent\x18\x02 \x01(\x05\x12\x14\n\x0cmumps_pivtol\x18\x03 \x01(\x01\x12\x16\n\x0eipopt_max_iter\x18\x04 \x01(\x05\x12\x11\n\tipopt_tol\x18\x05 \x01(\x01\x12(\n ipopt_acceptable_constr_viol_tol\x18\x06 \x01(\x01\x12&\n\x1eipopt_min_hessian_perturbation\x18\x07 \x01(\x01\x12+\n#ipopt_jacobian_regularization_value\x18\x08 \x01(\x01\x12%\n\x1dipopt_print_timing_statistics\x18\t \x01(\t\x12\x19\n\x11ipopt_alpha_for_y\x18\n \x01(\t\x12\x16\n\x0eipopt_recalc_y\x18\x0b \x01(\t\x12\x1a\n\ripopt_mu_init\x18\x0c \x01(\x01:\x030.1"\x9c\x01\n\nOSQPConfig\x12\x10\n\x05alpha\x18\x01 \x01(\x01:\x011\x12\x16\n\x07eps_abs\x18\x02 \x01(\x01:\x050.001\x12\x16\n\x07eps_rel\x18\x03 \x01(\x01:\x050.001\x12\x17\n\x08max_iter\x18\x04 \x01(\x05:\x0510000\x12\x14\n\x06polish\x18\x05 \x01(\x08:\x04true\x12\x1d\n\x0eosqp_debug_log\x18\x06 \x01(\x08:\x05false"\xf9\x04\n\x18IterativeAnchoringConfig\x12!\n\x14interpolated_delta_s\x18\x01 \x01(\x01:\x030.1\x12"\n\x16reanchoring_trails_num\x18\x02 \x01(\x05:\x0250\x12$\n\x16reanchoring_pos_stddev\x18\x03 \x01(\x01:\x040.25\x12$\n\x19reanchoring_length_stddev\x18\x04 \x01(\x01:\x011\x12\x1d\n\x0eestimate_bound\x18\x05 \x01(\x08:\x05false\x12\x18\n\rdefault_bound\x18\x06 \x01(\x01:\x012\x12(\n\x1avehicle_shortest_dimension\x18\x07 \x01(\x01:\x041.04\x12Y\n!fem_pos_deviation_smoother_config\x18\x08 \x01(\x0b2..apollo.planning.FemPosDeviationSmootherConfig\x12%\n\x18collision_decrease_ratio\x18\t \x01(\x01:\x030.9\x12\x18\n\rmax_forward_v\x18\n \x01(\x01:\x012\x12\x18\n\rmax_reverse_v\x18\x0b \x01(\x01:\x012\x12\x1a\n\x0fmax_forward_acc\x18\x0c \x01(\x01:\x013\x12\x1a\n\x0fmax_reverse_acc\x18\r \x01(\x01:\x012\x12\x17\n\x0cmax_acc_jerk\x18\x0e \x01(\x01:\x014\x12\x14\n\x07delta_t\x18\x0f \x01(\x01:\x030.2\x12J\n\x0es_curve_config\x18\x10 \x01(\x0b22.apollo.planning.PiecewiseJerkSpeedOptimizerConfig"\xf2\x01\n\x19TrajectoryPartitionConfig\x12#\n\x17interpolated_pieces_num\x18\x01 \x01(\x04:\x0250\x12%\n\x1ainitial_gear_check_horizon\x18\x02 \x01(\x04:\x013\x12$\n\x17heading_searching_range\x18\x03 \x01(\x01:\x030.3\x12%\n\x1agear_shift_period_duration\x18\x04 \x01(\x01:\x012\x12\x1b\n\x10gear_shift_max_t\x18\x05 \x01(\x01:\x013\x12\x1f\n\x11gear_shift_unit_t\x18\x06 \x01(\x01:\x040.02*J\n\x0eDualWarmUpMode\x12\t\n\x05IPOPT\x10\x00\x12\x0b\n\x07IPOPTQP\x10\x01\x12\x08\n\x04OSQP\x10\x02\x12\t\n\x05DEBUG\x10\x03\x12\x0b\n\x07SLACKQP\x10\x04*\xf7\x01\n\x14DistanceApproachMode\x12\x1b\n\x17DISTANCE_APPROACH_IPOPT\x10\x00\x12 \n\x1cDISTANCE_APPROACH_IPOPT_CUDA\x10\x01\x12$\n DISTANCE_APPROACH_IPOPT_FIXED_TS\x10\x02\x12&\n"DISTANCE_APPROACH_IPOPT_FIXED_DUAL\x10\x03\x12%\n!DISTANCE_APPROACH_IPOPT_RELAX_END\x10\x04\x12+\n\'DISTANCE_APPROACH_IPOPT_RELAX_END_SLACK\x10\x05')
_DUALWARMUPMODE = DESCRIPTOR.enum_types_by_name['DualWarmUpMode']
DualWarmUpMode = enum_type_wrapper.EnumTypeWrapper(_DUALWARMUPMODE)
_DISTANCEAPPROACHMODE = DESCRIPTOR.enum_types_by_name['DistanceApproachMode']
DistanceApproachMode = enum_type_wrapper.EnumTypeWrapper(_DISTANCEAPPROACHMODE)
IPOPT = 0
IPOPTQP = 1
OSQP = 2
DEBUG = 3
SLACKQP = 4
DISTANCE_APPROACH_IPOPT = 0
DISTANCE_APPROACH_IPOPT_CUDA = 1
DISTANCE_APPROACH_IPOPT_FIXED_TS = 2
DISTANCE_APPROACH_IPOPT_FIXED_DUAL = 3
DISTANCE_APPROACH_IPOPT_RELAX_END = 4
DISTANCE_APPROACH_IPOPT_RELAX_END_SLACK = 5
_PLANNEROPENSPACECONFIG = DESCRIPTOR.message_types_by_name['PlannerOpenSpaceConfig']
_ROICONFIG = DESCRIPTOR.message_types_by_name['ROIConfig']
_WARMSTARTCONFIG = DESCRIPTOR.message_types_by_name['WarmStartConfig']
_DUALVARIABLEWARMSTARTCONFIG = DESCRIPTOR.message_types_by_name['DualVariableWarmStartConfig']
_DISTANCEAPPROACHCONFIG = DESCRIPTOR.message_types_by_name['DistanceApproachConfig']
_IPOPTCONFIG = DESCRIPTOR.message_types_by_name['IpoptConfig']
_OSQPCONFIG = DESCRIPTOR.message_types_by_name['OSQPConfig']
_ITERATIVEANCHORINGCONFIG = DESCRIPTOR.message_types_by_name['IterativeAnchoringConfig']
_TRAJECTORYPARTITIONCONFIG = DESCRIPTOR.message_types_by_name['TrajectoryPartitionConfig']
PlannerOpenSpaceConfig = _reflection.GeneratedProtocolMessageType('PlannerOpenSpaceConfig', (_message.Message,), {'DESCRIPTOR': _PLANNEROPENSPACECONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(PlannerOpenSpaceConfig)
ROIConfig = _reflection.GeneratedProtocolMessageType('ROIConfig', (_message.Message,), {'DESCRIPTOR': _ROICONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(ROIConfig)
WarmStartConfig = _reflection.GeneratedProtocolMessageType('WarmStartConfig', (_message.Message,), {'DESCRIPTOR': _WARMSTARTCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(WarmStartConfig)
DualVariableWarmStartConfig = _reflection.GeneratedProtocolMessageType('DualVariableWarmStartConfig', (_message.Message,), {'DESCRIPTOR': _DUALVARIABLEWARMSTARTCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(DualVariableWarmStartConfig)
DistanceApproachConfig = _reflection.GeneratedProtocolMessageType('DistanceApproachConfig', (_message.Message,), {'DESCRIPTOR': _DISTANCEAPPROACHCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(DistanceApproachConfig)
IpoptConfig = _reflection.GeneratedProtocolMessageType('IpoptConfig', (_message.Message,), {'DESCRIPTOR': _IPOPTCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(IpoptConfig)
OSQPConfig = _reflection.GeneratedProtocolMessageType('OSQPConfig', (_message.Message,), {'DESCRIPTOR': _OSQPCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(OSQPConfig)
IterativeAnchoringConfig = _reflection.GeneratedProtocolMessageType('IterativeAnchoringConfig', (_message.Message,), {'DESCRIPTOR': _ITERATIVEANCHORINGCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(IterativeAnchoringConfig)
TrajectoryPartitionConfig = _reflection.GeneratedProtocolMessageType('TrajectoryPartitionConfig', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYPARTITIONCONFIG, '__module__': 'modules.planning.proto.planner_open_space_config_pb2'})
_sym_db.RegisterMessage(TrajectoryPartitionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DUALWARMUPMODE._serialized_start = 4164
    _DUALWARMUPMODE._serialized_end = 4238
    _DISTANCEAPPROACHMODE._serialized_start = 4241
    _DISTANCEAPPROACHMODE._serialized_end = 4488
    _PLANNEROPENSPACECONFIG._serialized_start = 187
    _PLANNEROPENSPACECONFIG._serialized_end = 861
    _ROICONFIG._serialized_start = 864
    _ROICONFIG._serialized_end = 1021
    _WARMSTARTCONFIG._serialized_start = 1024
    _WARMSTARTCONFIG._serialized_end = 1475
    _DUALVARIABLEWARMSTARTCONFIG._serialized_start = 1478
    _DUALVARIABLEWARMSTARTCONFIG._serialized_end = 1758
    _DISTANCEAPPROACHCONFIG._serialized_start = 1761
    _DISTANCEAPPROACHCONFIG._serialized_end = 2742
    _IPOPTCONFIG._serialized_start = 2745
    _IPOPTCONFIG._serialized_end = 3122
    _OSQPCONFIG._serialized_start = 3125
    _OSQPCONFIG._serialized_end = 3281
    _ITERATIVEANCHORINGCONFIG._serialized_start = 3284
    _ITERATIVEANCHORINGCONFIG._serialized_end = 3917
    _TRAJECTORYPARTITIONCONFIG._serialized_start = 3920
    _TRAJECTORYPARTITIONCONFIG._serialized_end = 4162