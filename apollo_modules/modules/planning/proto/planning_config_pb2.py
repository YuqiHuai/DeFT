"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.planning.proto import open_space_task_config_pb2 as modules_dot_planning_dot_proto_dot_open__space__task__config__pb2
from ....modules.planning.proto import task_config_pb2 as modules_dot_planning_dot_proto_dot_task__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/planning/proto/planning_config.proto\x12\x0fapollo.planning\x1a3modules/planning/proto/open_space_task_config.proto\x1a(modules/planning/proto/task_config.proto"\xdd\x16\n\nTaskConfig\x127\n\ttask_type\x18\x01 \x01(\x0e2$.apollo.planning.TaskConfig.TaskType\x12C\n\x14creep_decider_config\x18\x02 \x01(\x0b2#.apollo.planning.CreepDeciderConfigH\x00\x12N\n\x1alane_change_decider_config\x18\x03 \x01(\x0b2(.apollo.planning.LaneChangeDeciderConfigH\x00\x12]\n"open_space_fallback_decider_config\x18\x04 \x01(\x0b2/.apollo.planning.OpenSpaceFallBackDeciderConfigH\x00\x12\\\n"open_space_pre_stop_decider_config\x18\x05 \x01(\x0b2..apollo.planning.OpenSpacePreStopDeciderConfigH\x00\x12S\n\x1dopen_space_roi_decider_config\x18\x06 \x01(\x0b2*.apollo.planning.OpenSpaceRoiDeciderConfigH\x00\x12V\n\x1epath_assessment_decider_config\x18\x07 \x01(\x0b2,.apollo.planning.PathAssessmentDeciderConfigH\x00\x12N\n\x1apath_bounds_decider_config\x18\x08 \x01(\x0b2(.apollo.planning.PathBoundsDeciderConfigH\x00\x12A\n\x13path_decider_config\x18\t \x01(\x0b2".apollo.planning.PathDeciderConfigH\x00\x12W\n\x1fpath_lane_borrow_decider_config\x18\n \x01(\x0b2,.apollo.planning.PathLaneBorrowDeciderConfigH\x00\x12T\n\x1dpath_reference_decider_config\x18\x0b \x01(\x0b2+.apollo.planning.PathReferenceDeciderConfigH\x00\x12L\n\x19path_reuse_decider_config\x18\x0c \x01(\x0b2\'.apollo.planning.PathReuseDeciderConfigH\x00\x12U\n\x1erule_based_stop_decider_config\x18\r \x01(\x0b2+.apollo.planning.RuleBasedStopDeciderConfigH\x00\x12P\n\x1bspeed_bounds_decider_config\x18\x0e \x01(\x0b2).apollo.planning.SpeedBoundsDeciderConfigH\x00\x12J\n\x18st_bounds_decider_config\x18\x0f \x01(\x0b2&.apollo.planning.STBoundsDeciderConfigH\x00\x12e\n&open_space_trajectory_partition_config\x18\x10 \x01(\x0b23.apollo.planning.OpenSpaceTrajectoryPartitionConfigH\x00\x12c\n%open_space_trajectory_provider_config\x18\x11 \x01(\x0b22.apollo.planning.OpenSpaceTrajectoryProviderConfigH\x00\x12v\n/piecewise_jerk_nonlinear_speed_optimizer_config\x18\x12 \x01(\x0b2;.apollo.planning.PiecewiseJerkNonlinearSpeedOptimizerConfigH\x00\x12a\n$piecewise_jerk_path_optimizer_config\x18\x13 \x01(\x0b21.apollo.planning.PiecewiseJerkPathOptimizerConfigH\x00\x12c\n%piecewise_jerk_speed_optimizer_config\x18\x14 \x01(\x0b22.apollo.planning.PiecewiseJerkSpeedOptimizerConfigH\x00\x12Z\n speed_heuristic_optimizer_config\x18\x15 \x01(\x0b2..apollo.planning.SpeedHeuristicOptimizerConfigH\x00\x12a\n$learning_model_inference_task_config\x18\x16 \x01(\x0b21.apollo.planning.LearningModelInferenceTaskConfigH\x00\x12v\n/learning_model_inference_trajectory_task_config\x18\x17 \x01(\x0b2;.apollo.planning.LearningModelInferenceTrajectoryTaskConfigH\x00"\xbf\x06\n\x08TaskType\x12\x11\n\rCREEP_DECIDER\x10\x01\x12\x17\n\x13LANE_CHANGE_DECIDER\x10\x02\x12\x19\n\x15NAVI_OBSTACLE_DECIDER\x10\x03\x12\x15\n\x11NAVI_PATH_DECIDER\x10\x04\x12\x16\n\x12NAVI_SPEED_DECIDER\x10\x05\x12\x1f\n\x1bOPEN_SPACE_FALLBACK_DECIDER\x10\x06\x12\x1f\n\x1bOPEN_SPACE_PRE_STOP_DECIDER\x10\x07\x12\x1a\n\x16OPEN_SPACE_ROI_DECIDER\x10\x08\x12\x1b\n\x17PATH_ASSESSMENT_DECIDER\x10\t\x12\x17\n\x13PATH_BOUNDS_DECIDER\x10\n\x12\x10\n\x0cPATH_DECIDER\x10\x0b\x12\x1c\n\x18PATH_LANE_BORROW_DECIDER\x10\x0c\x12\x1a\n\x16PATH_REFERENCE_DECIDER\x10\r\x12\x16\n\x12PATH_REUSE_DECIDER\x10\x0e\x12\x0f\n\x0bRSS_DECIDER\x10\x0f\x12\x1b\n\x17RULE_BASED_STOP_DECIDER\x10\x10\x12\x1f\n\x1bSPEED_BOUNDS_PRIORI_DECIDER\x10\x11\x12\x1e\n\x1aSPEED_BOUNDS_FINAL_DECIDER\x10\x12\x12\x11\n\rSPEED_DECIDER\x10\x13\x12\x15\n\x11ST_BOUNDS_DECIDER\x10\x14\x12#\n\x1fOPEN_SPACE_TRAJECTORY_PARTITION\x10\x15\x12"\n\x1eOPEN_SPACE_TRAJECTORY_PROVIDER\x10\x16\x12,\n(PIECEWISE_JERK_NONLINEAR_SPEED_OPTIMIZER\x10\x17\x12!\n\x1dPIECEWISE_JERK_PATH_OPTIMIZER\x10\x18\x12"\n\x1ePIECEWISE_JERK_SPEED_OPTIMIZER\x10\x19\x12\x1d\n\x19SPEED_HEURISTIC_OPTIMIZER\x10\x1a\x12!\n\x1dLEARNING_MODEL_INFERENCE_TASK\x10\x1b\x12,\n(LEARNING_MODEL_INFERENCE_TRAJECTORY_TASK\x10\x1cB\r\n\x0btask_config"\xa6\x02\n)ScenarioBareIntersectionUnprotectedConfig\x125\n)start_bare_intersection_scenario_distance\x18\x01 \x01(\x01:\x0225\x12#\n\x14enable_explicit_stop\x18\x02 \x01(\x08:\x05false\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x013\x12%\n\x15approach_cruise_speed\x18\x04 \x01(\x01:\x066.7056\x12\x1a\n\rstop_distance\x18\x05 \x01(\x01:\x030.5\x12\x1b\n\x10stop_timeout_sec\x18\x06 \x01(\x02:\x018\x12\x1d\n\x11creep_timeout_sec\x18\x07 \x01(\x02:\x0210"\xac\x01\n\x1fScenarioEmergencyPullOverConfig\x12 \n\x15max_stop_deceleration\x18\x01 \x01(\x01:\x013\x12&\n\x1bslow_down_deceleration_time\x18\x02 \x01(\x01:\x013\x12#\n\x16target_slow_down_speed\x18\x03 \x01(\x01:\x032.5\x12\x1a\n\rstop_distance\x18\x04 \x01(\x01:\x031.5"Y\n\x1bScenarioEmergencyStopConfig\x12 \n\x15max_stop_deceleration\x18\x01 \x01(\x01:\x016\x12\x18\n\rstop_distance\x18\x02 \x01(\x01:\x011"\x1a\n\x18ScenarioLaneFollowConfig"#\n!ScenarioLearningModelSampleConfig"!\n\x1fScenarioNarrowStreetUTurnConfig"\xa7\x01\n\x17ScenarioParkAndGoConfig\x12 \n\x15front_obstacle_buffer\x18\x01 \x01(\x01:\x014\x12\x1b\n\x0eheading_buffer\x18\x02 \x01(\x01:\x030.5\x12\x1c\n\x10min_dist_to_dest\x18\x03 \x01(\x01:\x0225\x12/\n#max_steering_percentage_when_cruise\x18\x04 \x01(\x01:\x0290"\xc1\x03\n\x16ScenarioPullOverConfig\x12-\n!start_pull_over_scenario_distance\x18\x01 \x01(\x01:\x0250\x12)\n\x1dpull_over_min_distance_buffer\x18\x02 \x01(\x01:\x0210\x12$\n\x18max_distance_stop_search\x18\x03 \x01(\x01:\x0225\x12%\n\x18max_s_error_to_end_point\x18\x04 \x01(\x01:\x030.2\x12%\n\x18max_l_error_to_end_point\x18\x05 \x01(\x01:\x030.5\x12)\n\x1cmax_theta_error_to_end_point\x18\x06 \x01(\x01:\x030.2\x12,\n\x1fmax_distance_error_to_end_point\x18\x07 \x01(\x01:\x030.2\x12&\n\x1apass_destination_threshold\x18\x08 \x01(\x01:\x0210\x12"\n\x17max_valid_stop_distance\x18\t \x01(\x01:\x011\x124\n)s_distance_to_stop_for_open_space_parking\x18\n \x01(\x01:\x017"\xa3\x02\n!ScenarioStopSignUnprotectedConfig\x12,\n!start_stop_sign_scenario_distance\x18\x01 \x01(\x01:\x015\x120\n%watch_vehicle_max_valid_stop_distance\x18\x02 \x01(\x01:\x015\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x033.5\x12\x1c\n\x11stop_duration_sec\x18\x04 \x01(\x02:\x011\x12\x1e\n\x13min_pass_s_distance\x18\x05 \x01(\x01:\x013\x12\x1b\n\x10stop_timeout_sec\x18\x06 \x01(\x02:\x018\x12\x1d\n\x11creep_timeout_sec\x18\x07 \x01(\x02:\x0210"\x9b\x01\n#ScenarioTrafficLightProtectedConfig\x120\n%start_traffic_light_scenario_distance\x18\x01 \x01(\x01:\x015\x12"\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x012\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x013"\x95\x02\n-ScenarioTrafficLightUnprotectedLeftTurnConfig\x120\n%start_traffic_light_scenario_distance\x18\x01 \x01(\x01:\x015\x12#\n\x15approach_cruise_speed\x18\x02 \x01(\x01:\x042.78\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x033.5\x12\x1e\n\x13min_pass_s_distance\x18\x04 \x01(\x01:\x013\x12\x1d\n\x11creep_timeout_sec\x18\x05 \x01(\x02:\x0210\x12(\n\x1amax_adc_speed_before_creep\x18\x06 \x01(\x01:\x045.56"\xca\x02\n.ScenarioTrafficLightUnprotectedRightTurnConfig\x120\n%start_traffic_light_scenario_distance\x18\x01 \x01(\x01:\x015\x12\'\n\x18enable_right_turn_on_red\x18\x02 \x01(\x08:\x05false\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x033.5\x12\x1e\n\x13min_pass_s_distance\x18\x04 \x01(\x01:\x013\x121\n&red_light_right_turn_stop_duration_sec\x18\x05 \x01(\x02:\x013\x12\x1d\n\x11creep_timeout_sec\x18\x06 \x01(\x02:\x0210\x12%\n\x1amax_adc_speed_before_creep\x18\x07 \x01(\x01:\x013"i\n\x1aScenarioValetParkingConfig\x12\'\n\x1bparking_spot_range_to_start\x18\x01 \x01(\x01:\x0220\x12"\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x011"g\n\x1fScenarioDeadEndTurnAroundConfig\x12 \n\x14dead_end_start_range\x18\x01 \x01(\x01:\x0220\x12"\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x011"\xae\x01\n\x17ScenarioYieldSignConfig\x12.\n"start_yield_sign_scenario_distance\x18\x01 \x01(\x01:\x0210\x12$\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x034.5\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x013\x12\x1d\n\x11creep_timeout_sec\x18\x04 \x01(\x02:\x0210"\xb6\x1b\n\x0eScenarioConfig\x12C\n\rscenario_type\x18\x01 \x01(\x0e2,.apollo.planning.ScenarioConfig.ScenarioType\x12G\n\x12lane_follow_config\x18\x02 \x01(\x0b2).apollo.planning.ScenarioLaneFollowConfigH\x00\x12j\n$bare_intersection_unprotected_config\x18\x03 \x01(\x0b2:.apollo.planning.ScenarioBareIntersectionUnprotectedConfigH\x00\x12V\n\x1aemergency_pull_over_config\x18\x04 \x01(\x0b20.apollo.planning.ScenarioEmergencyPullOverConfigH\x00\x12M\n\x15emergency_stop_config\x18\x05 \x01(\x0b2,.apollo.planning.ScenarioEmergencyStopConfigH\x00\x12Z\n\x1clearning_model_sample_config\x18\x06 \x01(\x0b22.apollo.planning.ScenarioLearningModelSampleConfigH\x00\x12W\n\x1bnarrow_street_u_turn_config\x18\x07 \x01(\x0b20.apollo.planning.ScenarioNarrowStreetUTurnConfigH\x00\x12F\n\x12park_and_go_config\x18\x08 \x01(\x0b2(.apollo.planning.ScenarioParkAndGoConfigH\x00\x12C\n\x10pull_over_config\x18\t \x01(\x0b2\'.apollo.planning.ScenarioPullOverConfigH\x00\x12Z\n\x1cstop_sign_unprotected_config\x18\n \x01(\x0b22.apollo.planning.ScenarioStopSignUnprotectedConfigH\x00\x12^\n\x1etraffic_light_protected_config\x18\x0b \x01(\x0b24.apollo.planning.ScenarioTrafficLightProtectedConfigH\x00\x12t\n*traffic_light_unprotected_left_turn_config\x18\x0c \x01(\x0b2>.apollo.planning.ScenarioTrafficLightUnprotectedLeftTurnConfigH\x00\x12v\n+traffic_light_unprotected_right_turn_config\x18\r \x01(\x0b2?.apollo.planning.ScenarioTrafficLightUnprotectedRightTurnConfigH\x00\x12K\n\x14valet_parking_config\x18\x0e \x01(\x0b2+.apollo.planning.ScenarioValetParkingConfigH\x00\x12E\n\x11yield_sign_config\x18\x0f \x01(\x0b2(.apollo.planning.ScenarioYieldSignConfigH\x00\x12U\n\x19deadend_turnaround_config\x18\x12 \x01(\x0b20.apollo.planning.ScenarioDeadEndTurnAroundConfigH\x00\x12=\n\nstage_type\x18\x10 \x03(\x0e2).apollo.planning.ScenarioConfig.StageType\x12A\n\x0cstage_config\x18\x11 \x03(\x0b2+.apollo.planning.ScenarioConfig.StageConfig\x1a\xce\x01\n\x0bStageConfig\x12=\n\nstage_type\x18\x01 \x01(\x0e2).apollo.planning.ScenarioConfig.StageType\x12\x15\n\x07enabled\x18\x02 \x01(\x08:\x04true\x127\n\ttask_type\x18\x03 \x03(\x0e2$.apollo.planning.TaskConfig.TaskType\x120\n\x0btask_config\x18\x04 \x03(\x0b2\x1b.apollo.planning.TaskConfig"\xa3\x03\n\x0cScenarioType\x12\x0f\n\x0bLANE_FOLLOW\x10\x00\x12!\n\x1dBARE_INTERSECTION_UNPROTECTED\x10\x02\x12\x17\n\x13STOP_SIGN_PROTECTED\x10\x03\x12\x19\n\x15STOP_SIGN_UNPROTECTED\x10\x04\x12\x1b\n\x17TRAFFIC_LIGHT_PROTECTED\x10\x05\x12\'\n#TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN\x10\x06\x12(\n$TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN\x10\x07\x12\x0e\n\nYIELD_SIGN\x10\x08\x12\r\n\tPULL_OVER\x10\t\x12\x11\n\rVALET_PARKING\x10\n\x12\x17\n\x13EMERGENCY_PULL_OVER\x10\x0b\x12\x12\n\x0eEMERGENCY_STOP\x10\x0c\x12\x18\n\x14NARROW_STREET_U_TURN\x10\r\x12\x0f\n\x0bPARK_AND_GO\x10\x0e\x12\x19\n\x15LEARNING_MODEL_SAMPLE\x10\x0f\x12\x16\n\x12DEADEND_TURNAROUND\x10\x10"\x9f\n\n\tStageType\x12\x0c\n\x08NO_STAGE\x10\x00\x12\x1d\n\x19LANE_FOLLOW_DEFAULT_STAGE\x10\x01\x12+\n&BARE_INTERSECTION_UNPROTECTED_APPROACH\x10\xc8\x01\x126\n1BARE_INTERSECTION_UNPROTECTED_INTERSECTION_CRUISE\x10\xc9\x01\x12#\n\x1eSTOP_SIGN_UNPROTECTED_PRE_STOP\x10\xac\x02\x12\x1f\n\x1aSTOP_SIGN_UNPROTECTED_STOP\x10\xad\x02\x12 \n\x1bSTOP_SIGN_UNPROTECTED_CREEP\x10\xae\x02\x12.\n)STOP_SIGN_UNPROTECTED_INTERSECTION_CRUISE\x10\xaf\x02\x12%\n TRAFFIC_LIGHT_PROTECTED_APPROACH\x10\x90\x03\x120\n+TRAFFIC_LIGHT_PROTECTED_INTERSECTION_CRUISE\x10\x91\x03\x121\n,TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_APPROACH\x10\x9a\x03\x12.\n)TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_CREEP\x10\x9b\x03\x12<\n7TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_INTERSECTION_CRUISE\x10\x9c\x03\x12.\n)TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_STOP\x10\xa4\x03\x12/\n*TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_CREEP\x10\xa5\x03\x12=\n8TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_INTERSECTION_CRUISE\x10\xa6\x03\x12\x17\n\x12PULL_OVER_APPROACH\x10\xf4\x03\x12%\n PULL_OVER_RETRY_APPROACH_PARKING\x10\xf5\x03\x12\x1c\n\x17PULL_OVER_RETRY_PARKING\x10\xf6\x03\x12"\n\x1dEMERGENCY_PULL_OVER_SLOW_DOWN\x10\xd8\x04\x12!\n\x1cEMERGENCY_PULL_OVER_APPROACH\x10\xd9\x04\x12 \n\x1bEMERGENCY_PULL_OVER_STANDBY\x10\xda\x04\x12\x1c\n\x17EMERGENCY_STOP_APPROACH\x10\xe2\x04\x12\x1b\n\x16EMERGENCY_STOP_STANDBY\x10\xe3\x04\x12+\n&VALET_PARKING_APPROACHING_PARKING_SPOT\x10\xbc\x05\x12\x1a\n\x15VALET_PARKING_PARKING\x10\xbd\x05\x121\n,DEADEND_TURNAROUND_APPROACHING_TURNING_POINT\x10\xcc\x08\x12\x1f\n\x1aDEADEND_TURNAROUND_TURNING\x10\xcd\x08\x12\x16\n\x11PARK_AND_GO_CHECK\x10\xa0\x06\x12\x17\n\x12PARK_AND_GO_CRUISE\x10\xa1\x06\x12\x17\n\x12PARK_AND_GO_ADJUST\x10\xa2\x06\x12\x1b\n\x16PARK_AND_GO_PRE_CRUISE\x10\xa3\x06\x12\x18\n\x13YIELD_SIGN_APPROACH\x10\x84\x07\x12\x15\n\x10YIELD_SIGN_CREEP\x10\x85\x07\x12\x17\n\x12LEARNING_MODEL_RUN\x10\xe8\x07B\x11\n\x0fscenario_config"\x19\n\x17PlannerPublicRoadConfig"\xaf\x02\n\x11PlannerNaviConfig\x122\n\x04task\x18\x01 \x03(\x0e2$.apollo.planning.TaskConfig.TaskType\x12H\n\x18navi_path_decider_config\x18\x02 \x01(\x0b2&.apollo.planning.NaviPathDeciderConfig\x12J\n\x19navi_speed_decider_config\x18\x03 \x01(\x0b2\'.apollo.planning.NaviSpeedDeciderConfig\x12P\n\x1cnavi_obstacle_decider_config\x18\x04 \x01(\x0b2*.apollo.planning.NaviObstacleDeciderConfig"G\n\x11RtkPlanningConfig\x122\n\x0cplanner_type\x18\x01 \x01(\x0e2\x1c.apollo.planning.PlannerType"\x9a\x01\n\x16StandardPlanningConfig\x122\n\x0cplanner_type\x18\x01 \x03(\x0e2\x1c.apollo.planning.PlannerType\x12L\n\x1aplanner_public_road_config\x18\x02 \x01(\x0b2(.apollo.planning.PlannerPublicRoadConfig"\x8f\x01\n\x18NavigationPlanningConfig\x122\n\x0cplanner_type\x18\x01 \x03(\x0e2\x1c.apollo.planning.PlannerType\x12?\n\x13planner_navi_config\x18\x04 \x01(\x0b2".apollo.planning.PlannerNaviConfig"\xf8\x02\n\x0bTopicConfig\x12\x15\n\rchassis_topic\x18\x01 \x01(\t\x12\x18\n\x10hmi_status_topic\x18\x02 \x01(\t\x12\x1a\n\x12localization_topic\x18\x03 \x01(\t\x12\x1a\n\x12planning_pad_topic\x18\x04 \x01(\t\x12!\n\x19planning_trajectory_topic\x18\x05 \x01(\t\x12\x18\n\x10prediction_topic\x18\x06 \x01(\t\x12\x1a\n\x12relative_map_topic\x18\x07 \x01(\t\x12\x1d\n\x15routing_request_topic\x18\x08 \x01(\t\x12\x1e\n\x16routing_response_topic\x18\t \x01(\t\x12\x1b\n\x13story_telling_topic\x18\n \x01(\t\x12%\n\x1dtraffic_light_detection_topic\x18\x0b \x01(\t\x12$\n\x1cplanning_learning_data_topic\x18\x0c \x01(\t"\xa9\x04\n\x0ePlanningConfig\x122\n\x0ctopic_config\x18\x01 \x01(\x0b2\x1c.apollo.planning.TopicConfig\x12K\n\rlearning_mode\x18\x02 \x01(\x0e24.apollo.planning.PlanningConfig.PlanningLearningMode\x12A\n\x13rtk_planning_config\x18\x03 \x01(\x0b2".apollo.planning.RtkPlanningConfigH\x00\x12K\n\x18standard_planning_config\x18\x04 \x01(\x0b2\'.apollo.planning.StandardPlanningConfigH\x00\x12O\n\x1anavigation_planning_config\x18\x05 \x01(\x0b2).apollo.planning.NavigationPlanningConfigH\x00\x128\n\x13default_task_config\x18\x06 \x03(\x0b2\x1b.apollo.planning.TaskConfig"h\n\x14PlanningLearningMode\x12\x0f\n\x0bNO_LEARNING\x10\x00\x12\x07\n\x03E2E\x10\x01\x12\n\n\x06HYBRID\x10\x02\x12\x0b\n\x07RL_TEST\x10\x03\x12\x0c\n\x08E2E_TEST\x10\x04\x12\x0f\n\x0bHYBRID_TEST\x10\x05B\x11\n\x0fplanning_config*>\n\x0bPlannerType\x12\x07\n\x03RTK\x10\x00\x12\x0f\n\x0bPUBLIC_ROAD\x10\x01\x12\x08\n\x04NAVI\x10\x02\x12\x0b\n\x07LATTICE\x10\x03')
_PLANNERTYPE = DESCRIPTOR.enum_types_by_name['PlannerType']
PlannerType = enum_type_wrapper.EnumTypeWrapper(_PLANNERTYPE)
RTK = 0
PUBLIC_ROAD = 1
NAVI = 2
LATTICE = 3
_TASKCONFIG = DESCRIPTOR.message_types_by_name['TaskConfig']
_SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioBareIntersectionUnprotectedConfig']
_SCENARIOEMERGENCYPULLOVERCONFIG = DESCRIPTOR.message_types_by_name['ScenarioEmergencyPullOverConfig']
_SCENARIOEMERGENCYSTOPCONFIG = DESCRIPTOR.message_types_by_name['ScenarioEmergencyStopConfig']
_SCENARIOLANEFOLLOWCONFIG = DESCRIPTOR.message_types_by_name['ScenarioLaneFollowConfig']
_SCENARIOLEARNINGMODELSAMPLECONFIG = DESCRIPTOR.message_types_by_name['ScenarioLearningModelSampleConfig']
_SCENARIONARROWSTREETUTURNCONFIG = DESCRIPTOR.message_types_by_name['ScenarioNarrowStreetUTurnConfig']
_SCENARIOPARKANDGOCONFIG = DESCRIPTOR.message_types_by_name['ScenarioParkAndGoConfig']
_SCENARIOPULLOVERCONFIG = DESCRIPTOR.message_types_by_name['ScenarioPullOverConfig']
_SCENARIOSTOPSIGNUNPROTECTEDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioStopSignUnprotectedConfig']
_SCENARIOTRAFFICLIGHTPROTECTEDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioTrafficLightProtectedConfig']
_SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG = DESCRIPTOR.message_types_by_name['ScenarioTrafficLightUnprotectedLeftTurnConfig']
_SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG = DESCRIPTOR.message_types_by_name['ScenarioTrafficLightUnprotectedRightTurnConfig']
_SCENARIOVALETPARKINGCONFIG = DESCRIPTOR.message_types_by_name['ScenarioValetParkingConfig']
_SCENARIODEADENDTURNAROUNDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioDeadEndTurnAroundConfig']
_SCENARIOYIELDSIGNCONFIG = DESCRIPTOR.message_types_by_name['ScenarioYieldSignConfig']
_SCENARIOCONFIG = DESCRIPTOR.message_types_by_name['ScenarioConfig']
_SCENARIOCONFIG_STAGECONFIG = _SCENARIOCONFIG.nested_types_by_name['StageConfig']
_PLANNERPUBLICROADCONFIG = DESCRIPTOR.message_types_by_name['PlannerPublicRoadConfig']
_PLANNERNAVICONFIG = DESCRIPTOR.message_types_by_name['PlannerNaviConfig']
_RTKPLANNINGCONFIG = DESCRIPTOR.message_types_by_name['RtkPlanningConfig']
_STANDARDPLANNINGCONFIG = DESCRIPTOR.message_types_by_name['StandardPlanningConfig']
_NAVIGATIONPLANNINGCONFIG = DESCRIPTOR.message_types_by_name['NavigationPlanningConfig']
_TOPICCONFIG = DESCRIPTOR.message_types_by_name['TopicConfig']
_PLANNINGCONFIG = DESCRIPTOR.message_types_by_name['PlanningConfig']
_TASKCONFIG_TASKTYPE = _TASKCONFIG.enum_types_by_name['TaskType']
_SCENARIOCONFIG_SCENARIOTYPE = _SCENARIOCONFIG.enum_types_by_name['ScenarioType']
_SCENARIOCONFIG_STAGETYPE = _SCENARIOCONFIG.enum_types_by_name['StageType']
_PLANNINGCONFIG_PLANNINGLEARNINGMODE = _PLANNINGCONFIG.enum_types_by_name['PlanningLearningMode']
TaskConfig = _reflection.GeneratedProtocolMessageType('TaskConfig', (_message.Message,), {'DESCRIPTOR': _TASKCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(TaskConfig)
ScenarioBareIntersectionUnprotectedConfig = _reflection.GeneratedProtocolMessageType('ScenarioBareIntersectionUnprotectedConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioBareIntersectionUnprotectedConfig)
ScenarioEmergencyPullOverConfig = _reflection.GeneratedProtocolMessageType('ScenarioEmergencyPullOverConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOEMERGENCYPULLOVERCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioEmergencyPullOverConfig)
ScenarioEmergencyStopConfig = _reflection.GeneratedProtocolMessageType('ScenarioEmergencyStopConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOEMERGENCYSTOPCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioEmergencyStopConfig)
ScenarioLaneFollowConfig = _reflection.GeneratedProtocolMessageType('ScenarioLaneFollowConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOLANEFOLLOWCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioLaneFollowConfig)
ScenarioLearningModelSampleConfig = _reflection.GeneratedProtocolMessageType('ScenarioLearningModelSampleConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOLEARNINGMODELSAMPLECONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioLearningModelSampleConfig)
ScenarioNarrowStreetUTurnConfig = _reflection.GeneratedProtocolMessageType('ScenarioNarrowStreetUTurnConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIONARROWSTREETUTURNCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioNarrowStreetUTurnConfig)
ScenarioParkAndGoConfig = _reflection.GeneratedProtocolMessageType('ScenarioParkAndGoConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOPARKANDGOCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioParkAndGoConfig)
ScenarioPullOverConfig = _reflection.GeneratedProtocolMessageType('ScenarioPullOverConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOPULLOVERCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioPullOverConfig)
ScenarioStopSignUnprotectedConfig = _reflection.GeneratedProtocolMessageType('ScenarioStopSignUnprotectedConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOSTOPSIGNUNPROTECTEDCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioStopSignUnprotectedConfig)
ScenarioTrafficLightProtectedConfig = _reflection.GeneratedProtocolMessageType('ScenarioTrafficLightProtectedConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOTRAFFICLIGHTPROTECTEDCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioTrafficLightProtectedConfig)
ScenarioTrafficLightUnprotectedLeftTurnConfig = _reflection.GeneratedProtocolMessageType('ScenarioTrafficLightUnprotectedLeftTurnConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioTrafficLightUnprotectedLeftTurnConfig)
ScenarioTrafficLightUnprotectedRightTurnConfig = _reflection.GeneratedProtocolMessageType('ScenarioTrafficLightUnprotectedRightTurnConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioTrafficLightUnprotectedRightTurnConfig)
ScenarioValetParkingConfig = _reflection.GeneratedProtocolMessageType('ScenarioValetParkingConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOVALETPARKINGCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioValetParkingConfig)
ScenarioDeadEndTurnAroundConfig = _reflection.GeneratedProtocolMessageType('ScenarioDeadEndTurnAroundConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIODEADENDTURNAROUNDCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioDeadEndTurnAroundConfig)
ScenarioYieldSignConfig = _reflection.GeneratedProtocolMessageType('ScenarioYieldSignConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOYIELDSIGNCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioYieldSignConfig)
ScenarioConfig = _reflection.GeneratedProtocolMessageType('ScenarioConfig', (_message.Message,), {'StageConfig': _reflection.GeneratedProtocolMessageType('StageConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOCONFIG_STAGECONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'}), 'DESCRIPTOR': _SCENARIOCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ScenarioConfig)
_sym_db.RegisterMessage(ScenarioConfig.StageConfig)
PlannerPublicRoadConfig = _reflection.GeneratedProtocolMessageType('PlannerPublicRoadConfig', (_message.Message,), {'DESCRIPTOR': _PLANNERPUBLICROADCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(PlannerPublicRoadConfig)
PlannerNaviConfig = _reflection.GeneratedProtocolMessageType('PlannerNaviConfig', (_message.Message,), {'DESCRIPTOR': _PLANNERNAVICONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(PlannerNaviConfig)
RtkPlanningConfig = _reflection.GeneratedProtocolMessageType('RtkPlanningConfig', (_message.Message,), {'DESCRIPTOR': _RTKPLANNINGCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(RtkPlanningConfig)
StandardPlanningConfig = _reflection.GeneratedProtocolMessageType('StandardPlanningConfig', (_message.Message,), {'DESCRIPTOR': _STANDARDPLANNINGCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(StandardPlanningConfig)
NavigationPlanningConfig = _reflection.GeneratedProtocolMessageType('NavigationPlanningConfig', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONPLANNINGCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(NavigationPlanningConfig)
TopicConfig = _reflection.GeneratedProtocolMessageType('TopicConfig', (_message.Message,), {'DESCRIPTOR': _TOPICCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(TopicConfig)
PlanningConfig = _reflection.GeneratedProtocolMessageType('PlanningConfig', (_message.Message,), {'DESCRIPTOR': _PLANNINGCONFIG, '__module__': 'modules.planning.proto.planning_config_pb2'})
_sym_db.RegisterMessage(PlanningConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PLANNERTYPE._serialized_start = 10968
    _PLANNERTYPE._serialized_end = 11030
    _TASKCONFIG._serialized_start = 161
    _TASKCONFIG._serialized_end = 3070
    _TASKCONFIG_TASKTYPE._serialized_start = 2224
    _TASKCONFIG_TASKTYPE._serialized_end = 3055
    _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG._serialized_start = 3073
    _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG._serialized_end = 3367
    _SCENARIOEMERGENCYPULLOVERCONFIG._serialized_start = 3370
    _SCENARIOEMERGENCYPULLOVERCONFIG._serialized_end = 3542
    _SCENARIOEMERGENCYSTOPCONFIG._serialized_start = 3544
    _SCENARIOEMERGENCYSTOPCONFIG._serialized_end = 3633
    _SCENARIOLANEFOLLOWCONFIG._serialized_start = 3635
    _SCENARIOLANEFOLLOWCONFIG._serialized_end = 3661
    _SCENARIOLEARNINGMODELSAMPLECONFIG._serialized_start = 3663
    _SCENARIOLEARNINGMODELSAMPLECONFIG._serialized_end = 3698
    _SCENARIONARROWSTREETUTURNCONFIG._serialized_start = 3700
    _SCENARIONARROWSTREETUTURNCONFIG._serialized_end = 3733
    _SCENARIOPARKANDGOCONFIG._serialized_start = 3736
    _SCENARIOPARKANDGOCONFIG._serialized_end = 3903
    _SCENARIOPULLOVERCONFIG._serialized_start = 3906
    _SCENARIOPULLOVERCONFIG._serialized_end = 4355
    _SCENARIOSTOPSIGNUNPROTECTEDCONFIG._serialized_start = 4358
    _SCENARIOSTOPSIGNUNPROTECTEDCONFIG._serialized_end = 4649
    _SCENARIOTRAFFICLIGHTPROTECTEDCONFIG._serialized_start = 4652
    _SCENARIOTRAFFICLIGHTPROTECTEDCONFIG._serialized_end = 4807
    _SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG._serialized_start = 4810
    _SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG._serialized_end = 5087
    _SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG._serialized_start = 5090
    _SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG._serialized_end = 5420
    _SCENARIOVALETPARKINGCONFIG._serialized_start = 5422
    _SCENARIOVALETPARKINGCONFIG._serialized_end = 5527
    _SCENARIODEADENDTURNAROUNDCONFIG._serialized_start = 5529
    _SCENARIODEADENDTURNAROUNDCONFIG._serialized_end = 5632
    _SCENARIOYIELDSIGNCONFIG._serialized_start = 5635
    _SCENARIOYIELDSIGNCONFIG._serialized_end = 5809
    _SCENARIOCONFIG._serialized_start = 5812
    _SCENARIOCONFIG._serialized_end = 9322
    _SCENARIOCONFIG_STAGECONFIG._serialized_start = 7361
    _SCENARIOCONFIG_STAGECONFIG._serialized_end = 7567
    _SCENARIOCONFIG_SCENARIOTYPE._serialized_start = 7570
    _SCENARIOCONFIG_SCENARIOTYPE._serialized_end = 7989
    _SCENARIOCONFIG_STAGETYPE._serialized_start = 7992
    _SCENARIOCONFIG_STAGETYPE._serialized_end = 9303
    _PLANNERPUBLICROADCONFIG._serialized_start = 9324
    _PLANNERPUBLICROADCONFIG._serialized_end = 9349
    _PLANNERNAVICONFIG._serialized_start = 9352
    _PLANNERNAVICONFIG._serialized_end = 9655
    _RTKPLANNINGCONFIG._serialized_start = 9657
    _RTKPLANNINGCONFIG._serialized_end = 9728
    _STANDARDPLANNINGCONFIG._serialized_start = 9731
    _STANDARDPLANNINGCONFIG._serialized_end = 9885
    _NAVIGATIONPLANNINGCONFIG._serialized_start = 9888
    _NAVIGATIONPLANNINGCONFIG._serialized_end = 10031
    _TOPICCONFIG._serialized_start = 10034
    _TOPICCONFIG._serialized_end = 10410
    _PLANNINGCONFIG._serialized_start = 10413
    _PLANNINGCONFIG._serialized_end = 10966
    _PLANNINGCONFIG_PLANNINGLEARNINGMODE._serialized_start = 10843
    _PLANNINGCONFIG_PLANNINGLEARNINGMODE._serialized_end = 10947