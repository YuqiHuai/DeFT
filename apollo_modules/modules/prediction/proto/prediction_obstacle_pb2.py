"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import error_code_pb2 as modules_dot_common_dot_proto_dot_error__code__pb2
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.prediction.proto import scenario_pb2 as modules_dot_prediction_dot_proto_dot_scenario__pb2
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
from ....modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/prediction/proto/prediction_obstacle.proto\x12\x11apollo.prediction\x1a%modules/common/proto/error_code.proto\x1a!modules/common/proto/header.proto\x1a\'modules/prediction/proto/scenario.proto\x1a2modules/perception/proto/perception_obstacle.proto\x1a&modules/prediction/proto/feature.proto"\xf6\x01\n\x0eObstacleIntent\x12=\n\x04type\x18\x01 \x01(\x0e2&.apollo.prediction.ObstacleIntent.Type:\x07UNKNOWN"\xa4\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x0e\n\nSTATIONARY\x10\x02\x12\n\n\x06MOVING\x10\x03\x12\x0f\n\x0bCHANGE_LANE\x10\x04\x12\x14\n\x10LOW_ACCELERATION\x10\x05\x12\x15\n\x11HIGH_ACCELERATION\x10\x06\x12\x14\n\x10LOW_DECELERATION\x10\x07\x12\x15\n\x11HIGH_DECELERATION\x10\x08"{\n\x06Intent\x125\n\x04type\x18\x01 \x01(\x0e2\x1e.apollo.prediction.Intent.Type:\x07UNKNOWN":\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\n\n\x06CRUISE\x10\x02\x12\x0f\n\x0bCHANGE_LANE\x10\x03"\xad\x03\n\x12PredictionObstacle\x12B\n\x13perception_obstacle\x18\x01 \x01(\x0b2%.apollo.perception.PerceptionObstacle\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x18\n\x10predicted_period\x18\x03 \x01(\x01\x121\n\ntrajectory\x18\x04 \x03(\x0b2\x1d.apollo.prediction.Trajectory\x121\n\x06intent\x18\x05 \x01(\x0b2!.apollo.prediction.ObstacleIntent\x125\n\x08priority\x18\x06 \x01(\x0b2#.apollo.prediction.ObstaclePriority\x12B\n\x0finteractive_tag\x18\t \x01(\x0b2).apollo.prediction.ObstacleInteractiveTag\x12\x18\n\tis_static\x18\x07 \x01(\x08:\x05false\x12+\n\x07feature\x18\x08 \x03(\x0b2\x1a.apollo.prediction.Feature"\xc3\x02\n\x13PredictionObstacles\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12B\n\x13prediction_obstacle\x18\x02 \x03(\x0b2%.apollo.prediction.PredictionObstacle\x127\n\x15perception_error_code\x18\x03 \x01(\x0e2\x18.apollo.common.ErrorCode\x12\x17\n\x0fstart_timestamp\x18\x04 \x01(\x01\x12\x15\n\rend_timestamp\x18\x05 \x01(\x01\x12)\n\x06intent\x18\x06 \x01(\x0b2\x19.apollo.prediction.Intent\x12-\n\x08scenario\x18\x07 \x01(\x0b2\x1b.apollo.prediction.Scenario')
_OBSTACLEINTENT = DESCRIPTOR.message_types_by_name['ObstacleIntent']
_INTENT = DESCRIPTOR.message_types_by_name['Intent']
_PREDICTIONOBSTACLE = DESCRIPTOR.message_types_by_name['PredictionObstacle']
_PREDICTIONOBSTACLES = DESCRIPTOR.message_types_by_name['PredictionObstacles']
_OBSTACLEINTENT_TYPE = _OBSTACLEINTENT.enum_types_by_name['Type']
_INTENT_TYPE = _INTENT.enum_types_by_name['Type']
ObstacleIntent = _reflection.GeneratedProtocolMessageType('ObstacleIntent', (_message.Message,), {'DESCRIPTOR': _OBSTACLEINTENT, '__module__': 'modules.prediction.proto.prediction_obstacle_pb2'})
_sym_db.RegisterMessage(ObstacleIntent)
Intent = _reflection.GeneratedProtocolMessageType('Intent', (_message.Message,), {'DESCRIPTOR': _INTENT, '__module__': 'modules.prediction.proto.prediction_obstacle_pb2'})
_sym_db.RegisterMessage(Intent)
PredictionObstacle = _reflection.GeneratedProtocolMessageType('PredictionObstacle', (_message.Message,), {'DESCRIPTOR': _PREDICTIONOBSTACLE, '__module__': 'modules.prediction.proto.prediction_obstacle_pb2'})
_sym_db.RegisterMessage(PredictionObstacle)
PredictionObstacles = _reflection.GeneratedProtocolMessageType('PredictionObstacles', (_message.Message,), {'DESCRIPTOR': _PREDICTIONOBSTACLES, '__module__': 'modules.prediction.proto.prediction_obstacle_pb2'})
_sym_db.RegisterMessage(PredictionObstacles)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OBSTACLEINTENT._serialized_start = 281
    _OBSTACLEINTENT._serialized_end = 527
    _OBSTACLEINTENT_TYPE._serialized_start = 363
    _OBSTACLEINTENT_TYPE._serialized_end = 527
    _INTENT._serialized_start = 529
    _INTENT._serialized_end = 652
    _INTENT_TYPE._serialized_start = 594
    _INTENT_TYPE._serialized_end = 652
    _PREDICTIONOBSTACLE._serialized_start = 655
    _PREDICTIONOBSTACLE._serialized_end = 1084
    _PREDICTIONOBSTACLES._serialized_start = 1087
    _PREDICTIONOBSTACLES._serialized_end = 1410