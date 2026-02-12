"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2
from ....modules.prediction.proto import prediction_conf_pb2 as modules_dot_prediction_dot_proto_dot_prediction__conf__pb2
from ....modules.prediction.proto import scenario_pb2 as modules_dot_prediction_dot_proto_dot_scenario__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/prediction/proto/offline_features.proto\x12\x11apollo.prediction\x1a$modules/common/proto/pnc_point.proto\x1a&modules/prediction/proto/feature.proto\x1a.modules/prediction/proto/prediction_conf.proto\x1a\'modules/prediction/proto/scenario.proto"\xb1\x01\n\x0fDataForLearning\x12\x10\n\x08category\x18\x05 \x01(\t\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x1d\n\x15features_for_learning\x18\x03 \x03(\x01\x12$\n\x1cstring_features_for_learning\x18\x07 \x03(\t\x12\x0e\n\x06labels\x18\x04 \x03(\x01\x12\x18\n\x10lane_sequence_id\x18\x06 \x01(\x05"T\n\x13ListDataForLearning\x12=\n\x11data_for_learning\x18\x01 \x03(\x0b2".apollo.prediction.DataForLearning"\xcb\x01\n\x10PredictionResult\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x121\n\ntrajectory\x18\x03 \x03(\x0b2\x1d.apollo.prediction.Trajectory\x126\n\robstacle_conf\x18\x04 \x01(\x0b2\x1f.apollo.prediction.ObstacleConf\x12-\n\x08scenario\x18\x05 \x01(\x0b2\x1b.apollo.prediction.Scenario"V\n\x14ListPredictionResult\x12>\n\x11prediction_result\x18\x01 \x03(\x0b2#.apollo.prediction.PredictionResult">\n\x0cListFrameEnv\x12.\n\tframe_env\x18\x01 \x03(\x0b2\x1b.apollo.prediction.FrameEnv"\xcc\x01\n\rDataForTuning\x12\x10\n\x08category\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12\x19\n\x11values_for_tuning\x18\x04 \x03(\x01\x12\x17\n\x0freal_cost_value\x18\x05 \x03(\x01\x12\x18\n\x10lane_sequence_id\x18\x06 \x01(\x05\x12<\n\x14adc_trajectory_point\x18\x07 \x03(\x0b2\x1e.apollo.common.TrajectoryPoint"N\n\x11ListDataForTuning\x129\n\x0fdata_for_tuning\x18\x01 \x03(\x0b2 .apollo.prediction.DataForTuning"7\n\x08Features\x12+\n\x07feature\x18\x01 \x03(\x0b2\x1a.apollo.prediction.Feature')
_DATAFORLEARNING = DESCRIPTOR.message_types_by_name['DataForLearning']
_LISTDATAFORLEARNING = DESCRIPTOR.message_types_by_name['ListDataForLearning']
_PREDICTIONRESULT = DESCRIPTOR.message_types_by_name['PredictionResult']
_LISTPREDICTIONRESULT = DESCRIPTOR.message_types_by_name['ListPredictionResult']
_LISTFRAMEENV = DESCRIPTOR.message_types_by_name['ListFrameEnv']
_DATAFORTUNING = DESCRIPTOR.message_types_by_name['DataForTuning']
_LISTDATAFORTUNING = DESCRIPTOR.message_types_by_name['ListDataForTuning']
_FEATURES = DESCRIPTOR.message_types_by_name['Features']
DataForLearning = _reflection.GeneratedProtocolMessageType('DataForLearning', (_message.Message,), {'DESCRIPTOR': _DATAFORLEARNING, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(DataForLearning)
ListDataForLearning = _reflection.GeneratedProtocolMessageType('ListDataForLearning', (_message.Message,), {'DESCRIPTOR': _LISTDATAFORLEARNING, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(ListDataForLearning)
PredictionResult = _reflection.GeneratedProtocolMessageType('PredictionResult', (_message.Message,), {'DESCRIPTOR': _PREDICTIONRESULT, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(PredictionResult)
ListPredictionResult = _reflection.GeneratedProtocolMessageType('ListPredictionResult', (_message.Message,), {'DESCRIPTOR': _LISTPREDICTIONRESULT, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(ListPredictionResult)
ListFrameEnv = _reflection.GeneratedProtocolMessageType('ListFrameEnv', (_message.Message,), {'DESCRIPTOR': _LISTFRAMEENV, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(ListFrameEnv)
DataForTuning = _reflection.GeneratedProtocolMessageType('DataForTuning', (_message.Message,), {'DESCRIPTOR': _DATAFORTUNING, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(DataForTuning)
ListDataForTuning = _reflection.GeneratedProtocolMessageType('ListDataForTuning', (_message.Message,), {'DESCRIPTOR': _LISTDATAFORTUNING, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(ListDataForTuning)
Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {'DESCRIPTOR': _FEATURES, '__module__': 'modules.prediction.proto.offline_features_pb2'})
_sym_db.RegisterMessage(Features)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DATAFORLEARNING._serialized_start = 238
    _DATAFORLEARNING._serialized_end = 415
    _LISTDATAFORLEARNING._serialized_start = 417
    _LISTDATAFORLEARNING._serialized_end = 501
    _PREDICTIONRESULT._serialized_start = 504
    _PREDICTIONRESULT._serialized_end = 707
    _LISTPREDICTIONRESULT._serialized_start = 709
    _LISTPREDICTIONRESULT._serialized_end = 795
    _LISTFRAMEENV._serialized_start = 797
    _LISTFRAMEENV._serialized_end = 859
    _DATAFORTUNING._serialized_start = 862
    _DATAFORTUNING._serialized_end = 1066
    _LISTDATAFORTUNING._serialized_start = 1068
    _LISTDATAFORTUNING._serialized_end = 1146
    _FEATURES._serialized_start = 1148
    _FEATURES._serialized_end = 1203