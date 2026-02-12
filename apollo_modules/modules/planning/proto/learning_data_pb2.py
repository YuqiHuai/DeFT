"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.map.proto import map_lane_pb2 as modules_dot_map_dot_proto_dot_map__lane__pb2
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
from ....modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2
from ....modules.prediction.proto import prediction_obstacle_pb2 as modules_dot_prediction_dot_proto_dot_prediction__obstacle__pb2
from ....modules.perception.proto import traffic_light_detection_pb2 as modules_dot_perception_dot_proto_dot_traffic__light__detection__pb2
from ....modules.routing.proto import routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*modules/planning/proto/learning_data.proto\x12\x0fapollo.planning\x1a"modules/canbus/proto/chassis.proto\x1a#modules/common/proto/geometry.proto\x1a!modules/common/proto/header.proto\x1a$modules/common/proto/pnc_point.proto\x1a modules/map/proto/map_lane.proto\x1a2modules/perception/proto/perception_obstacle.proto\x1a&modules/prediction/proto/feature.proto\x1a2modules/prediction/proto/prediction_obstacle.proto\x1a6modules/perception/proto/traffic_light_detection.proto\x1a#modules/routing/proto/routing.proto".\n\x0eOverlapFeature\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08distance\x18\x02 \x01(\x01"\xf7\x02\n\x0bPlanningTag\x12.\n\tlane_turn\x18\x01 \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneTurn\x123\n\nclear_area\x18\x02 \x01(\x0b2\x1f.apollo.planning.OverlapFeature\x122\n\tcrosswalk\x18\x03 \x01(\x0b2\x1f.apollo.planning.OverlapFeature\x125\n\x0cpnc_junction\x18\x04 \x01(\x0b2\x1f.apollo.planning.OverlapFeature\x12/\n\x06signal\x18\x05 \x01(\x0b2\x1f.apollo.planning.OverlapFeature\x122\n\tstop_sign\x18\x06 \x01(\x0b2\x1f.apollo.planning.OverlapFeature\x123\n\nyield_sign\x18\x07 \x01(\x0b2\x1f.apollo.planning.OverlapFeature"\xd2\x01\n\x0eChassisFeature\x12\x1d\n\x15message_timestamp_sec\x18\x01 \x01(\x01\x12\x11\n\tspeed_mps\x18\x02 \x01(\x02\x12\x1b\n\x13throttle_percentage\x18\x03 \x01(\x02\x12\x18\n\x10brake_percentage\x18\x04 \x01(\x02\x12\x1b\n\x13steering_percentage\x18\x05 \x01(\x02\x12:\n\rgear_location\x18\x06 \x01(\x0e2#.apollo.canbus.Chassis.GearPosition"\x88\x02\n\x13LocalizationFeature\x12\x1d\n\x15message_timestamp_sec\x18\x01 \x01(\x01\x12)\n\x08position\x18\x02 \x01(\x0b2\x17.apollo.common.PointENU\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12/\n\x0flinear_velocity\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x123\n\x13linear_acceleration\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x120\n\x10angular_velocity\x18\x06 \x01(\x0b2\x16.apollo.common.Point3D"d\n\x16CommonPathPointFeature\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\r\n\x05theta\x18\x04 \x01(\x01\x12\t\n\x01s\x18\x05 \x01(\x01\x12\x0f\n\x07lane_id\x18\x06 \x01(\t"\xbc\x01\n\x1cCommonTrajectoryPointFeature\x12;\n\npath_point\x18\x01 \x01(\x0b2\'.apollo.planning.CommonPathPointFeature\x12\t\n\x01v\x18\x02 \x01(\x01\x12\t\n\x01a\x18\x03 \x01(\x01\x12\x15\n\rrelative_time\x18\x04 \x01(\x01\x122\n\rgaussian_info\x18\x05 \x01(\x0b2\x1b.apollo.common.GaussianInfo"x\n\x16TrajectoryPointFeature\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12G\n\x10trajectory_point\x18\x02 \x01(\x0b2-.apollo.planning.CommonTrajectoryPointFeature"\xf2\x01\n\x19PerceptionObstacleFeature\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12(\n\x08position\x18\x02 \x01(\x0b2\x16.apollo.common.Point3D\x12\r\n\x05theta\x18\x03 \x01(\x01\x12(\n\x08velocity\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12,\n\x0cacceleration\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x12-\n\rpolygon_point\x18\x06 \x03(\x0b2\x16.apollo.common.Point3D"\xb9\x01\n\x19ObstacleTrajectoryFeature\x12O\n\x1bperception_obstacle_history\x18\x01 \x03(\x0b2*.apollo.planning.PerceptionObstacleFeature\x12K\n\x1aevaluated_trajectory_point\x18\x02 \x03(\x0b2\'.apollo.planning.TrajectoryPointFeature"u\n\x1bPredictionTrajectoryFeature\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12A\n\x10trajectory_point\x18\x02 \x03(\x0b2\'.apollo.planning.TrajectoryPointFeature"\x92\x02\n\x19PredictionObstacleFeature\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x18\n\x10predicted_period\x18\x02 \x01(\x01\x121\n\x06intent\x18\x03 \x01(\x0b2!.apollo.prediction.ObstacleIntent\x125\n\x08priority\x18\x04 \x01(\x0b2#.apollo.prediction.ObstaclePriority\x12\x18\n\tis_static\x18\x05 \x01(\x08:\x05false\x12@\n\ntrajectory\x18\x06 \x03(\x0b2,.apollo.planning.PredictionTrajectoryFeature"\x98\x02\n\x0fObstacleFeature\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\x01\x128\n\x04type\x18\x05 \x01(\x0e2*.apollo.perception.PerceptionObstacle.Type\x12G\n\x13obstacle_trajectory\x18\x06 \x01(\x0b2*.apollo.planning.ObstacleTrajectoryFeature\x12G\n\x13obstacle_prediction\x18\x07 \x01(\x0b2*.apollo.planning.PredictionObstacleFeature"u\n\x16RoutingResponseFeature\x12)\n\x04road\x18\x01 \x03(\x0b2\x1b.apollo.routing.RoadSegment\x120\n\x0bmeasurement\x18\x02 \x01(\x0b2\x1b.apollo.routing.Measurement"\xb2\x01\n\x0eRoutingFeature\x12A\n\x10routing_response\x18\x01 \x01(\x0b2\'.apollo.planning.RoutingResponseFeature\x12\x1d\n\x15local_routing_lane_id\x18\x02 \x03(\t\x12>\n\rlocal_routing\x18\x03 \x01(\x0b2\'.apollo.planning.RoutingResponseFeature"\xac\x01\n\x13TrafficLightFeature\x124\n\x05color\x18\x01 \x01(\x0e2%.apollo.perception.TrafficLight.Color\x12\n\n\x02id\x18\x02 \x01(\t\x12\x15\n\nconfidence\x18\x03 \x01(\x01:\x011\x12\x15\n\rtracking_time\x18\x04 \x01(\x01\x12\r\n\x05blink\x18\x05 \x01(\x08\x12\x16\n\x0eremaining_time\x18\x06 \x01(\x01"z\n\x1cTrafficLightDetectionFeature\x12\x1d\n\x15message_timestamp_sec\x18\x01 \x01(\x01\x12;\n\rtraffic_light\x18\x02 \x03(\x0b2$.apollo.planning.TrafficLightFeature"\xa8\x01\n\x12ADCTrajectoryPoint\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x122\n\x0cplanning_tag\x18\x02 \x01(\x0b2\x1c.apollo.planning.PlanningTag\x12G\n\x10trajectory_point\x18\x03 \x01(\x0b2-.apollo.planning.CommonTrajectoryPointFeature"^\n\x0eLearningOutput\x12L\n\x1badc_future_trajectory_point\x18\x01 \x03(\x0b2\'.apollo.planning.TrajectoryPointFeature"\xa3\x04\n\x11LearningDataFrame\x12\x1d\n\x15message_timestamp_sec\x18\x01 \x01(\x01\x12\x11\n\tframe_num\x18\x02 \x01(\r\x12\x10\n\x08map_name\x18\x03 \x01(\t\x122\n\x0cplanning_tag\x18\x04 \x01(\x0b2\x1c.apollo.planning.PlanningTag\x120\n\x07chassis\x18\x05 \x01(\x0b2\x1f.apollo.planning.ChassisFeature\x12:\n\x0clocalization\x18\x06 \x01(\x0b2$.apollo.planning.LocalizationFeature\x122\n\x08obstacle\x18\x07 \x03(\x0b2 .apollo.planning.ObstacleFeature\x120\n\x07routing\x18\x08 \x01(\x0b2\x1f.apollo.planning.RoutingFeature\x12N\n\x17traffic_light_detection\x18\t \x01(\x0b2-.apollo.planning.TrafficLightDetectionFeature\x12A\n\x14adc_trajectory_point\x18\n \x03(\x0b2#.apollo.planning.ADCTrajectoryPoint\x12/\n\x06output\x18\x0b \x01(\x0b2\x1f.apollo.planning.LearningOutput"O\n\x0cLearningData\x12?\n\x13learning_data_frame\x18\x01 \x03(\x0b2".apollo.planning.LearningDataFrame"~\n\x14PlanningLearningData\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12?\n\x13learning_data_frame\x18\x02 \x01(\x0b2".apollo.planning.LearningDataFrame')
_OVERLAPFEATURE = DESCRIPTOR.message_types_by_name['OverlapFeature']
_PLANNINGTAG = DESCRIPTOR.message_types_by_name['PlanningTag']
_CHASSISFEATURE = DESCRIPTOR.message_types_by_name['ChassisFeature']
_LOCALIZATIONFEATURE = DESCRIPTOR.message_types_by_name['LocalizationFeature']
_COMMONPATHPOINTFEATURE = DESCRIPTOR.message_types_by_name['CommonPathPointFeature']
_COMMONTRAJECTORYPOINTFEATURE = DESCRIPTOR.message_types_by_name['CommonTrajectoryPointFeature']
_TRAJECTORYPOINTFEATURE = DESCRIPTOR.message_types_by_name['TrajectoryPointFeature']
_PERCEPTIONOBSTACLEFEATURE = DESCRIPTOR.message_types_by_name['PerceptionObstacleFeature']
_OBSTACLETRAJECTORYFEATURE = DESCRIPTOR.message_types_by_name['ObstacleTrajectoryFeature']
_PREDICTIONTRAJECTORYFEATURE = DESCRIPTOR.message_types_by_name['PredictionTrajectoryFeature']
_PREDICTIONOBSTACLEFEATURE = DESCRIPTOR.message_types_by_name['PredictionObstacleFeature']
_OBSTACLEFEATURE = DESCRIPTOR.message_types_by_name['ObstacleFeature']
_ROUTINGRESPONSEFEATURE = DESCRIPTOR.message_types_by_name['RoutingResponseFeature']
_ROUTINGFEATURE = DESCRIPTOR.message_types_by_name['RoutingFeature']
_TRAFFICLIGHTFEATURE = DESCRIPTOR.message_types_by_name['TrafficLightFeature']
_TRAFFICLIGHTDETECTIONFEATURE = DESCRIPTOR.message_types_by_name['TrafficLightDetectionFeature']
_ADCTRAJECTORYPOINT = DESCRIPTOR.message_types_by_name['ADCTrajectoryPoint']
_LEARNINGOUTPUT = DESCRIPTOR.message_types_by_name['LearningOutput']
_LEARNINGDATAFRAME = DESCRIPTOR.message_types_by_name['LearningDataFrame']
_LEARNINGDATA = DESCRIPTOR.message_types_by_name['LearningData']
_PLANNINGLEARNINGDATA = DESCRIPTOR.message_types_by_name['PlanningLearningData']
OverlapFeature = _reflection.GeneratedProtocolMessageType('OverlapFeature', (_message.Message,), {'DESCRIPTOR': _OVERLAPFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(OverlapFeature)
PlanningTag = _reflection.GeneratedProtocolMessageType('PlanningTag', (_message.Message,), {'DESCRIPTOR': _PLANNINGTAG, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(PlanningTag)
ChassisFeature = _reflection.GeneratedProtocolMessageType('ChassisFeature', (_message.Message,), {'DESCRIPTOR': _CHASSISFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(ChassisFeature)
LocalizationFeature = _reflection.GeneratedProtocolMessageType('LocalizationFeature', (_message.Message,), {'DESCRIPTOR': _LOCALIZATIONFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(LocalizationFeature)
CommonPathPointFeature = _reflection.GeneratedProtocolMessageType('CommonPathPointFeature', (_message.Message,), {'DESCRIPTOR': _COMMONPATHPOINTFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(CommonPathPointFeature)
CommonTrajectoryPointFeature = _reflection.GeneratedProtocolMessageType('CommonTrajectoryPointFeature', (_message.Message,), {'DESCRIPTOR': _COMMONTRAJECTORYPOINTFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(CommonTrajectoryPointFeature)
TrajectoryPointFeature = _reflection.GeneratedProtocolMessageType('TrajectoryPointFeature', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYPOINTFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(TrajectoryPointFeature)
PerceptionObstacleFeature = _reflection.GeneratedProtocolMessageType('PerceptionObstacleFeature', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONOBSTACLEFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(PerceptionObstacleFeature)
ObstacleTrajectoryFeature = _reflection.GeneratedProtocolMessageType('ObstacleTrajectoryFeature', (_message.Message,), {'DESCRIPTOR': _OBSTACLETRAJECTORYFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(ObstacleTrajectoryFeature)
PredictionTrajectoryFeature = _reflection.GeneratedProtocolMessageType('PredictionTrajectoryFeature', (_message.Message,), {'DESCRIPTOR': _PREDICTIONTRAJECTORYFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(PredictionTrajectoryFeature)
PredictionObstacleFeature = _reflection.GeneratedProtocolMessageType('PredictionObstacleFeature', (_message.Message,), {'DESCRIPTOR': _PREDICTIONOBSTACLEFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(PredictionObstacleFeature)
ObstacleFeature = _reflection.GeneratedProtocolMessageType('ObstacleFeature', (_message.Message,), {'DESCRIPTOR': _OBSTACLEFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(ObstacleFeature)
RoutingResponseFeature = _reflection.GeneratedProtocolMessageType('RoutingResponseFeature', (_message.Message,), {'DESCRIPTOR': _ROUTINGRESPONSEFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(RoutingResponseFeature)
RoutingFeature = _reflection.GeneratedProtocolMessageType('RoutingFeature', (_message.Message,), {'DESCRIPTOR': _ROUTINGFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(RoutingFeature)
TrafficLightFeature = _reflection.GeneratedProtocolMessageType('TrafficLightFeature', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(TrafficLightFeature)
TrafficLightDetectionFeature = _reflection.GeneratedProtocolMessageType('TrafficLightDetectionFeature', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTDETECTIONFEATURE, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(TrafficLightDetectionFeature)
ADCTrajectoryPoint = _reflection.GeneratedProtocolMessageType('ADCTrajectoryPoint', (_message.Message,), {'DESCRIPTOR': _ADCTRAJECTORYPOINT, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(ADCTrajectoryPoint)
LearningOutput = _reflection.GeneratedProtocolMessageType('LearningOutput', (_message.Message,), {'DESCRIPTOR': _LEARNINGOUTPUT, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(LearningOutput)
LearningDataFrame = _reflection.GeneratedProtocolMessageType('LearningDataFrame', (_message.Message,), {'DESCRIPTOR': _LEARNINGDATAFRAME, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(LearningDataFrame)
LearningData = _reflection.GeneratedProtocolMessageType('LearningData', (_message.Message,), {'DESCRIPTOR': _LEARNINGDATA, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(LearningData)
PlanningLearningData = _reflection.GeneratedProtocolMessageType('PlanningLearningData', (_message.Message,), {'DESCRIPTOR': _PLANNINGLEARNINGDATA, '__module__': 'modules.planning.proto.learning_data_pb2'})
_sym_db.RegisterMessage(PlanningLearningData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OVERLAPFEATURE._serialized_start = 480
    _OVERLAPFEATURE._serialized_end = 526
    _PLANNINGTAG._serialized_start = 529
    _PLANNINGTAG._serialized_end = 904
    _CHASSISFEATURE._serialized_start = 907
    _CHASSISFEATURE._serialized_end = 1117
    _LOCALIZATIONFEATURE._serialized_start = 1120
    _LOCALIZATIONFEATURE._serialized_end = 1384
    _COMMONPATHPOINTFEATURE._serialized_start = 1386
    _COMMONPATHPOINTFEATURE._serialized_end = 1486
    _COMMONTRAJECTORYPOINTFEATURE._serialized_start = 1489
    _COMMONTRAJECTORYPOINTFEATURE._serialized_end = 1677
    _TRAJECTORYPOINTFEATURE._serialized_start = 1679
    _TRAJECTORYPOINTFEATURE._serialized_end = 1799
    _PERCEPTIONOBSTACLEFEATURE._serialized_start = 1802
    _PERCEPTIONOBSTACLEFEATURE._serialized_end = 2044
    _OBSTACLETRAJECTORYFEATURE._serialized_start = 2047
    _OBSTACLETRAJECTORYFEATURE._serialized_end = 2232
    _PREDICTIONTRAJECTORYFEATURE._serialized_start = 2234
    _PREDICTIONTRAJECTORYFEATURE._serialized_end = 2351
    _PREDICTIONOBSTACLEFEATURE._serialized_start = 2354
    _PREDICTIONOBSTACLEFEATURE._serialized_end = 2628
    _OBSTACLEFEATURE._serialized_start = 2631
    _OBSTACLEFEATURE._serialized_end = 2911
    _ROUTINGRESPONSEFEATURE._serialized_start = 2913
    _ROUTINGRESPONSEFEATURE._serialized_end = 3030
    _ROUTINGFEATURE._serialized_start = 3033
    _ROUTINGFEATURE._serialized_end = 3211
    _TRAFFICLIGHTFEATURE._serialized_start = 3214
    _TRAFFICLIGHTFEATURE._serialized_end = 3386
    _TRAFFICLIGHTDETECTIONFEATURE._serialized_start = 3388
    _TRAFFICLIGHTDETECTIONFEATURE._serialized_end = 3510
    _ADCTRAJECTORYPOINT._serialized_start = 3513
    _ADCTRAJECTORYPOINT._serialized_end = 3681
    _LEARNINGOUTPUT._serialized_start = 3683
    _LEARNINGOUTPUT._serialized_end = 3777
    _LEARNINGDATAFRAME._serialized_start = 3780
    _LEARNINGDATAFRAME._serialized_end = 4327
    _LEARNINGDATA._serialized_start = 4329
    _LEARNINGDATA._serialized_end = 4408
    _PLANNINGLEARNINGDATA._serialized_start = 4410
    _PLANNINGLEARNINGDATA._serialized_end = 4536