"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.map.proto import map_lane_pb2 as modules_dot_map_dot_proto_dot_map__lane__pb2
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
from ....modules.prediction.proto import lane_graph_pb2 as modules_dot_prediction_dot_proto_dot_lane__graph__pb2
from ....modules.prediction.proto import prediction_point_pb2 as modules_dot_prediction_dot_proto_dot_prediction__point__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/prediction/proto/feature.proto\x12\x11apollo.prediction\x1a#modules/common/proto/geometry.proto\x1a$modules/common/proto/pnc_point.proto\x1a modules/map/proto/map_lane.proto\x1a2modules/perception/proto/perception_obstacle.proto\x1a)modules/prediction/proto/lane_graph.proto\x1a/modules/prediction/proto/prediction_point.proto"\xc4\x02\n\x04Lane\x12<\n\x14current_lane_feature\x18\x01 \x03(\x0b2\x1e.apollo.prediction.LaneFeature\x124\n\x0clane_feature\x18\x02 \x01(\x0b2\x1e.apollo.prediction.LaneFeature\x12;\n\x13nearby_lane_feature\x18\x03 \x03(\x0b2\x1e.apollo.prediction.LaneFeature\x120\n\nlane_graph\x18\x04 \x01(\x0b2\x1c.apollo.prediction.LaneGraph\x128\n\x12lane_graph_ordered\x18\x05 \x01(\x0b2\x1c.apollo.prediction.LaneGraph\x12\x1f\n\x17label_update_time_delta\x18\x1a \x01(\x01"\xef\x01\n\x0bLaneFeature\x12\x0f\n\x07lane_id\x18\x01 \x01(\t\x12\x16\n\x0elane_turn_type\x18\x02 \x01(\r\x12\x0e\n\x06lane_s\x18\x03 \x01(\x01\x12\x0e\n\x06lane_l\x18\x04 \x01(\x01\x12\x12\n\nangle_diff\x18\x05 \x01(\x01\x12\x1d\n\x15dist_to_left_boundary\x18\x06 \x01(\x01\x12\x1e\n\x16dist_to_right_boundary\x18\x07 \x01(\x01\x12\x14\n\x0clane_heading\x18\x08 \x01(\x01\x12.\n\tlane_type\x18\t \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneType"}\n\x0cJunctionExit\x12\x14\n\x0cexit_lane_id\x18\x01 \x01(\t\x12-\n\rexit_position\x18\x02 \x01(\x0b2\x16.apollo.common.Point3D\x12\x14\n\x0cexit_heading\x18\x03 \x01(\x01\x12\x12\n\nexit_width\x18\x04 \x01(\x01"\x9d\x02\n\x0fJunctionFeature\x12\x13\n\x0bjunction_id\x18\x01 \x01(\t\x12\x16\n\x0ejunction_range\x18\x02 \x01(\x01\x122\n\nenter_lane\x18\x03 \x01(\x0b2\x1e.apollo.prediction.LaneFeature\x126\n\rjunction_exit\x18\x04 \x03(\x0b2\x1f.apollo.prediction.JunctionExit\x12\x1c\n\x14junction_mlp_feature\x18\x05 \x03(\x01\x12\x1a\n\x12junction_mlp_label\x18\x06 \x03(\x05\x12 \n\x18junction_mlp_probability\x18\x07 \x03(\x01\x12\x15\n\rstart_lane_id\x18\x08 \x03(\t"\x8b\x01\n\x10ObstaclePriority\x12F\n\x08priority\x18\x19 \x01(\x0e2,.apollo.prediction.ObstaclePriority.Priority:\x06NORMAL"/\n\x08Priority\x12\x0b\n\x07CAUTION\x10\x01\x12\n\n\x06NORMAL\x10\x02\x12\n\n\x06IGNORE\x10\x03"\xb2\x01\n\x16ObstacleInteractiveTag\x12a\n\x0finteractive_tag\x18% \x01(\x0e28.apollo.prediction.ObstacleInteractiveTag.InteractiveTag:\x0eNONINTERACTION"5\n\x0eInteractiveTag\x12\x0f\n\x0bINTERACTION\x10\x01\x12\x12\n\x0eNONINTERACTION\x10\x02"[\n\nTrajectory\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x128\n\x10trajectory_point\x18\x02 \x03(\x0b2\x1e.apollo.common.TrajectoryPoint"\xb7\x0b\n\x07Feature\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\rpolygon_point\x18\x1e \x03(\x0b2\x16.apollo.common.Point3D\x12(\n\x08position\x18\x02 \x01(\x0b2\x16.apollo.common.Point3D\x12.\n\x0efront_position\x18\x1b \x01(\x0b2\x16.apollo.common.Point3D\x12(\n\x08velocity\x18\x03 \x01(\x0b2\x16.apollo.common.Point3D\x12,\n\x0craw_velocity\x18\x1c \x01(\x0b2\x16.apollo.common.Point3D\x12,\n\x0cacceleration\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12\x18\n\x10velocity_heading\x18\x05 \x01(\x01\x12\r\n\x05speed\x18\x06 \x01(\x01\x12\x0b\n\x03acc\x18\x07 \x01(\x01\x12\r\n\x05theta\x18\x08 \x01(\x01\x12\x0e\n\x06length\x18\t \x01(\x01\x12\r\n\x05width\x18\n \x01(\x01\x12\x0e\n\x06height\x18\x0b \x01(\x01\x12\x15\n\rtracking_time\x18\x0c \x01(\x01\x12\x11\n\ttimestamp\x18\r \x01(\x01\x12%\n\x04lane\x18\x0e \x01(\x0b2\x17.apollo.prediction.Lane\x12<\n\x10junction_feature\x18\x1a \x01(\x0b2".apollo.prediction.JunctionFeature\x12*\n\nt_position\x18\x10 \x01(\x0b2\x16.apollo.common.Point3D\x12.\n\nt_velocity\x18\x11 \x01(\x0b2\x16.apollo.common.Point3DB\x02\x18\x01\x12\x1e\n\x12t_velocity_heading\x18\x12 \x01(\x01B\x02\x18\x01\x12\x13\n\x07t_speed\x18\x13 \x01(\x01B\x02\x18\x01\x122\n\x0et_acceleration\x18\x14 \x01(\x0b2\x16.apollo.common.Point3DB\x02\x18\x01\x12\x11\n\x05t_acc\x18\x15 \x01(\x01B\x02\x18\x01\x12\x17\n\x08is_still\x18\x16 \x01(\x08:\x05false\x128\n\x04type\x18\x17 \x01(\x0e2*.apollo.perception.PerceptionObstacle.Type\x12\x1f\n\x17label_update_time_delta\x18\x18 \x01(\x01\x125\n\x08priority\x18\x19 \x01(\x0b2#.apollo.prediction.ObstaclePriority\x12B\n\x0finteractive_tag\x18% \x01(\x0b2).apollo.prediction.ObstacleInteractiveTag\x12\x1f\n\x10is_near_junction\x18\x1d \x01(\x08:\x05false\x12N\n\x18future_trajectory_points\x18\x1f \x03(\x0b2,.apollo.prediction.PredictionTrajectoryPoint\x12N\n&short_term_predicted_trajectory_points\x18  \x03(\x0b2\x1e.apollo.common.TrajectoryPoint\x12;\n\x14predicted_trajectory\x18! \x03(\x0b2\x1d.apollo.prediction.Trajectory\x12<\n\x14adc_trajectory_point\x18" \x03(\x0b2\x1e.apollo.common.TrajectoryPoint\x12\x15\n\radc_timestamp\x18& \x01(\x01\x12?\n\x10adc_localization\x18\' \x01(\x0b2%.apollo.perception.PerceptionObstacle\x12\x1b\n\x13surrounding_lane_id\x18# \x03(\t\x12\x16\n\x0ewithin_lane_id\x18$ \x03(\t"[\n\x0fObstacleHistory\x12+\n\x07feature\x18\x01 \x03(\x0b2\x1a.apollo.prediction.Feature\x12\x1b\n\x0cis_trainable\x18\x02 \x01(\x08:\x05false"\x95\x01\n\x08FrameEnv\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x127\n\x0bego_history\x18\x02 \x01(\x0b2".apollo.prediction.ObstacleHistory\x12=\n\x11obstacles_history\x18\x03 \x03(\x0b2".apollo.prediction.ObstacleHistory')
_LANE = DESCRIPTOR.message_types_by_name['Lane']
_LANEFEATURE = DESCRIPTOR.message_types_by_name['LaneFeature']
_JUNCTIONEXIT = DESCRIPTOR.message_types_by_name['JunctionExit']
_JUNCTIONFEATURE = DESCRIPTOR.message_types_by_name['JunctionFeature']
_OBSTACLEPRIORITY = DESCRIPTOR.message_types_by_name['ObstaclePriority']
_OBSTACLEINTERACTIVETAG = DESCRIPTOR.message_types_by_name['ObstacleInteractiveTag']
_TRAJECTORY = DESCRIPTOR.message_types_by_name['Trajectory']
_FEATURE = DESCRIPTOR.message_types_by_name['Feature']
_OBSTACLEHISTORY = DESCRIPTOR.message_types_by_name['ObstacleHistory']
_FRAMEENV = DESCRIPTOR.message_types_by_name['FrameEnv']
_OBSTACLEPRIORITY_PRIORITY = _OBSTACLEPRIORITY.enum_types_by_name['Priority']
_OBSTACLEINTERACTIVETAG_INTERACTIVETAG = _OBSTACLEINTERACTIVETAG.enum_types_by_name['InteractiveTag']
Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), {'DESCRIPTOR': _LANE, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(Lane)
LaneFeature = _reflection.GeneratedProtocolMessageType('LaneFeature', (_message.Message,), {'DESCRIPTOR': _LANEFEATURE, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(LaneFeature)
JunctionExit = _reflection.GeneratedProtocolMessageType('JunctionExit', (_message.Message,), {'DESCRIPTOR': _JUNCTIONEXIT, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(JunctionExit)
JunctionFeature = _reflection.GeneratedProtocolMessageType('JunctionFeature', (_message.Message,), {'DESCRIPTOR': _JUNCTIONFEATURE, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(JunctionFeature)
ObstaclePriority = _reflection.GeneratedProtocolMessageType('ObstaclePriority', (_message.Message,), {'DESCRIPTOR': _OBSTACLEPRIORITY, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(ObstaclePriority)
ObstacleInteractiveTag = _reflection.GeneratedProtocolMessageType('ObstacleInteractiveTag', (_message.Message,), {'DESCRIPTOR': _OBSTACLEINTERACTIVETAG, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(ObstacleInteractiveTag)
Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), {'DESCRIPTOR': _TRAJECTORY, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(Trajectory)
Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {'DESCRIPTOR': _FEATURE, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(Feature)
ObstacleHistory = _reflection.GeneratedProtocolMessageType('ObstacleHistory', (_message.Message,), {'DESCRIPTOR': _OBSTACLEHISTORY, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(ObstacleHistory)
FrameEnv = _reflection.GeneratedProtocolMessageType('FrameEnv', (_message.Message,), {'DESCRIPTOR': _FRAMEENV, '__module__': 'modules.prediction.proto.feature_pb2'})
_sym_db.RegisterMessage(FrameEnv)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FEATURE.fields_by_name['t_velocity']._options = None
    _FEATURE.fields_by_name['t_velocity']._serialized_options = b'\x18\x01'
    _FEATURE.fields_by_name['t_velocity_heading']._options = None
    _FEATURE.fields_by_name['t_velocity_heading']._serialized_options = b'\x18\x01'
    _FEATURE.fields_by_name['t_speed']._options = None
    _FEATURE.fields_by_name['t_speed']._serialized_options = b'\x18\x01'
    _FEATURE.fields_by_name['t_acceleration']._options = None
    _FEATURE.fields_by_name['t_acceleration']._serialized_options = b'\x18\x01'
    _FEATURE.fields_by_name['t_acc']._options = None
    _FEATURE.fields_by_name['t_acc']._serialized_options = b'\x18\x01'
    _LANE._serialized_start = 315
    _LANE._serialized_end = 639
    _LANEFEATURE._serialized_start = 642
    _LANEFEATURE._serialized_end = 881
    _JUNCTIONEXIT._serialized_start = 883
    _JUNCTIONEXIT._serialized_end = 1008
    _JUNCTIONFEATURE._serialized_start = 1011
    _JUNCTIONFEATURE._serialized_end = 1296
    _OBSTACLEPRIORITY._serialized_start = 1299
    _OBSTACLEPRIORITY._serialized_end = 1438
    _OBSTACLEPRIORITY_PRIORITY._serialized_start = 1391
    _OBSTACLEPRIORITY_PRIORITY._serialized_end = 1438
    _OBSTACLEINTERACTIVETAG._serialized_start = 1441
    _OBSTACLEINTERACTIVETAG._serialized_end = 1619
    _OBSTACLEINTERACTIVETAG_INTERACTIVETAG._serialized_start = 1566
    _OBSTACLEINTERACTIVETAG_INTERACTIVETAG._serialized_end = 1619
    _TRAJECTORY._serialized_start = 1621
    _TRAJECTORY._serialized_end = 1712
    _FEATURE._serialized_start = 1715
    _FEATURE._serialized_end = 3178
    _OBSTACLEHISTORY._serialized_start = 3180
    _OBSTACLEHISTORY._serialized_end = 3271
    _FRAMEENV._serialized_start = 3274
    _FRAMEENV._serialized_end = 3423