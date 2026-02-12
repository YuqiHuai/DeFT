"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
from ....modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/prediction/proto/prediction_conf.proto\x12\x11apollo.prediction\x1a2modules/perception/proto/perception_obstacle.proto\x1a&modules/prediction/proto/feature.proto"\xae\t\n\x0cObstacleConf\x12A\n\robstacle_type\x18\x01 \x01(\x0e2*.apollo.perception.PerceptionObstacle.Type\x12S\n\x0fobstacle_status\x18\x02 \x01(\x0e2..apollo.prediction.ObstacleConf.ObstacleStatus:\nSTATIONARY\x12C\n\rpriority_type\x18\x05 \x01(\x0e2,.apollo.prediction.ObstaclePriority.Priority\x12Q\n\x0finteractive_tag\x18\x06 \x01(\x0e28.apollo.prediction.ObstacleInteractiveTag.InteractiveTag\x12E\n\x0eevaluator_type\x18\x03 \x01(\x0e2-.apollo.prediction.ObstacleConf.EvaluatorType\x12E\n\x0epredictor_type\x18\x04 \x01(\x0e2-.apollo.prediction.ObstacleConf.PredictorType"X\n\x0eObstacleStatus\x12\x0b\n\x07ON_LANE\x10\x00\x12\x0c\n\x08OFF_LANE\x10\x01\x12\x0e\n\nSTATIONARY\x10\x03\x12\n\n\x06MOVING\x10\x04\x12\x0f\n\x0bIN_JUNCTION\x10\x05"\x84\x03\n\rEvaluatorType\x12\x11\n\rMLP_EVALUATOR\x10\x00\x12\x15\n\rRNN_EVALUATOR\x10\x01\x1a\x02\x08\x01\x12\x12\n\x0eCOST_EVALUATOR\x10\x02\x12\x18\n\x14CRUISE_MLP_EVALUATOR\x10\x03\x12\x1a\n\x16JUNCTION_MLP_EVALUATOR\x10\x04\x12\x1f\n\x1bCYCLIST_KEEP_LANE_EVALUATOR\x10\x05\x12\x1b\n\x17LANE_SCANNING_EVALUATOR\x10\x06\x12$\n PEDESTRIAN_INTERACTION_EVALUATOR\x10\x07\x12\x1a\n\x16JUNCTION_MAP_EVALUATOR\x10\x08\x12\x1e\n\x1aLANE_AGGREGATING_EVALUATOR\x10\t\x12\x1b\n\x17SEMANTIC_LSTM_EVALUATOR\x10\n\x12)\n%JOINTLY_PREDICTION_PLANNING_EVALUATOR\x10\x0b\x12\x17\n\x13VECTORNET_EVALUATOR\x10\x0c"\xfe\x01\n\rPredictorType\x12\x1b\n\x17LANE_SEQUENCE_PREDICTOR\x10\x00\x12\x17\n\x13FREE_MOVE_PREDICTOR\x10\x01\x12\x1a\n\x12REGIONAL_PREDICTOR\x10\x02\x1a\x02\x08\x01\x12\x1b\n\x17MOVE_SEQUENCE_PREDICTOR\x10\x03\x12\x13\n\x0fEMPTY_PREDICTOR\x10\x04\x12\x19\n\x15SINGLE_LANE_PREDICTOR\x10\x05\x12\x16\n\x12JUNCTION_PREDICTOR\x10\x06\x12\x1b\n\x17EXTRAPOLATION_PREDICTOR\x10\x07\x12\x19\n\x15INTERACTION_PREDICTOR\x10\x08"\xa9\x02\n\tTopicConf\x12\x1f\n\x17adccontainer_topic_name\x18\x01 \x01(\t\x12\x1c\n\x14container_topic_name\x18\x02 \x01(\t\x12\x1c\n\x14evaluator_topic_name\x18\x03 \x01(\t\x12\x1a\n\x12localization_topic\x18\x04 \x01(\t\x12!\n\x19perception_obstacle_topic\x18\x05 \x01(\t\x12\'\n\x1fperception_obstacles_topic_name\x18\x06 \x01(\t\x12!\n\x19planning_trajectory_topic\x18\x07 \x01(\t\x12\x18\n\x10prediction_topic\x18\x08 \x01(\t\x12\x1a\n\x12storytelling_topic\x18\t \x01(\t"z\n\x0ePredictionConf\x120\n\ntopic_conf\x18\x01 \x01(\x0b2\x1c.apollo.prediction.TopicConf\x126\n\robstacle_conf\x18\x02 \x03(\x0b2\x1f.apollo.prediction.ObstacleConf')
_OBSTACLECONF = DESCRIPTOR.message_types_by_name['ObstacleConf']
_TOPICCONF = DESCRIPTOR.message_types_by_name['TopicConf']
_PREDICTIONCONF = DESCRIPTOR.message_types_by_name['PredictionConf']
_OBSTACLECONF_OBSTACLESTATUS = _OBSTACLECONF.enum_types_by_name['ObstacleStatus']
_OBSTACLECONF_EVALUATORTYPE = _OBSTACLECONF.enum_types_by_name['EvaluatorType']
_OBSTACLECONF_PREDICTORTYPE = _OBSTACLECONF.enum_types_by_name['PredictorType']
ObstacleConf = _reflection.GeneratedProtocolMessageType('ObstacleConf', (_message.Message,), {'DESCRIPTOR': _OBSTACLECONF, '__module__': 'modules.prediction.proto.prediction_conf_pb2'})
_sym_db.RegisterMessage(ObstacleConf)
TopicConf = _reflection.GeneratedProtocolMessageType('TopicConf', (_message.Message,), {'DESCRIPTOR': _TOPICCONF, '__module__': 'modules.prediction.proto.prediction_conf_pb2'})
_sym_db.RegisterMessage(TopicConf)
PredictionConf = _reflection.GeneratedProtocolMessageType('PredictionConf', (_message.Message,), {'DESCRIPTOR': _PREDICTIONCONF, '__module__': 'modules.prediction.proto.prediction_conf_pb2'})
_sym_db.RegisterMessage(PredictionConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OBSTACLECONF_EVALUATORTYPE.values_by_name['RNN_EVALUATOR']._options = None
    _OBSTACLECONF_EVALUATORTYPE.values_by_name['RNN_EVALUATOR']._serialized_options = b'\x08\x01'
    _OBSTACLECONF_PREDICTORTYPE.values_by_name['REGIONAL_PREDICTOR']._options = None
    _OBSTACLECONF_PREDICTORTYPE.values_by_name['REGIONAL_PREDICTOR']._serialized_options = b'\x08\x01'
    _OBSTACLECONF._serialized_start = 162
    _OBSTACLECONF._serialized_end = 1360
    _OBSTACLECONF_OBSTACLESTATUS._serialized_start = 624
    _OBSTACLECONF_OBSTACLESTATUS._serialized_end = 712
    _OBSTACLECONF_EVALUATORTYPE._serialized_start = 715
    _OBSTACLECONF_EVALUATORTYPE._serialized_end = 1103
    _OBSTACLECONF_PREDICTORTYPE._serialized_start = 1106
    _OBSTACLECONF_PREDICTORTYPE._serialized_end = 1360
    _TOPICCONF._serialized_start = 1363
    _TOPICCONF._serialized_end = 1660
    _PREDICTIONCONF._serialized_start = 1662
    _PREDICTIONCONF._serialized_end = 1784