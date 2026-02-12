"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/planning/proto/auto_tuning_raw_feature.proto\x12\x1aapollo.planning.autotuning\x1a$modules/common/proto/pnc_point.proto"\x7f\n\x13PathPointRawFeature\x121\n\x0fcartesian_coord\x18\x01 \x01(\x0b2\x18.apollo.common.PathPoint\x125\n\x0cfrenet_coord\x18\x02 \x01(\x0b2\x1f.apollo.common.FrenetFramePoint"\x89\x08\n\x14SpeedPointRawFeature\x12\t\n\x01s\x18\x01 \x01(\x01\x12\t\n\x01t\x18\x02 \x01(\x01\x12\t\n\x01v\x18\x03 \x01(\x01\x12\t\n\x01a\x18\x04 \x01(\x01\x12\t\n\x01j\x18\x05 \x01(\x01\x12\x13\n\x0bspeed_limit\x18\x06 \x01(\x01\x12V\n\x06follow\x18\n \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12X\n\x08overtake\x18\x0b \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12`\n\x10virtual_decision\x18\r \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12T\n\x04stop\x18\x0e \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12Y\n\tcollision\x18\x0f \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12U\n\x05nudge\x18\x0c \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12^\n\x0esidepass_front\x18\x10 \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12]\n\rsidepass_rear\x18\x11 \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12Z\n\nkeep_clear\x18\x12 \x03(\x0b2F.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x1an\n\x15ObjectDecisionFeature\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nrelative_s\x18\x02 \x01(\x01\x12\x12\n\nrelative_l\x18\x03 \x01(\x01\x12\x12\n\nrelative_v\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x01"\xdf\x04\n\x11ObstacleSTRawData\x12V\n\x10obstacle_st_data\x18\x01 \x03(\x0b2<.apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData\x12W\n\x11obstacle_st_nudge\x18\x02 \x03(\x0b2<.apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData\x12Z\n\x14obstacle_st_sidepass\x18\x03 \x03(\x0b2<.apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData\x1aI\n\x0bSTPointPair\x12\x0f\n\x07s_lower\x18\x01 \x01(\x01\x12\x0f\n\x07s_upper\x18\x02 \x01(\x01\x12\t\n\x01t\x18\x03 \x01(\x01\x12\r\n\x01l\x18\x04 \x01(\x01:\x0210\x1a\xf1\x01\n\x0eObstacleSTData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05speed\x18\x02 \x01(\x01\x12\x12\n\nis_virtual\x18\x03 \x01(\x08\x12\x13\n\x0bprobability\x18\x04 \x01(\x01\x12J\n\x07polygon\x18\x08 \x03(\x0b29.apollo.planning.autotuning.ObstacleSTRawData.STPointPair\x12O\n\x0cdistribution\x18\t \x03(\x0b29.apollo.planning.autotuning.ObstacleSTRawData.STPointPair"\xab\x01\n\x19TrajectoryPointRawFeature\x12E\n\x0cpath_feature\x18\x01 \x01(\x0b2/.apollo.planning.autotuning.PathPointRawFeature\x12G\n\rspeed_feature\x18\x02 \x01(\x0b20.apollo.planning.autotuning.SpeedPointRawFeature"\xa8\x01\n\x14TrajectoryRawFeature\x12L\n\rpoint_feature\x18\x01 \x03(\x0b25.apollo.planning.autotuning.TrajectoryPointRawFeature\x12B\n\x0bst_raw_data\x18\x02 \x01(\x0b2-.apollo.planning.autotuning.ObstacleSTRawData')
_PATHPOINTRAWFEATURE = DESCRIPTOR.message_types_by_name['PathPointRawFeature']
_SPEEDPOINTRAWFEATURE = DESCRIPTOR.message_types_by_name['SpeedPointRawFeature']
_SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE = _SPEEDPOINTRAWFEATURE.nested_types_by_name['ObjectDecisionFeature']
_OBSTACLESTRAWDATA = DESCRIPTOR.message_types_by_name['ObstacleSTRawData']
_OBSTACLESTRAWDATA_STPOINTPAIR = _OBSTACLESTRAWDATA.nested_types_by_name['STPointPair']
_OBSTACLESTRAWDATA_OBSTACLESTDATA = _OBSTACLESTRAWDATA.nested_types_by_name['ObstacleSTData']
_TRAJECTORYPOINTRAWFEATURE = DESCRIPTOR.message_types_by_name['TrajectoryPointRawFeature']
_TRAJECTORYRAWFEATURE = DESCRIPTOR.message_types_by_name['TrajectoryRawFeature']
PathPointRawFeature = _reflection.GeneratedProtocolMessageType('PathPointRawFeature', (_message.Message,), {'DESCRIPTOR': _PATHPOINTRAWFEATURE, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'})
_sym_db.RegisterMessage(PathPointRawFeature)
SpeedPointRawFeature = _reflection.GeneratedProtocolMessageType('SpeedPointRawFeature', (_message.Message,), {'ObjectDecisionFeature': _reflection.GeneratedProtocolMessageType('ObjectDecisionFeature', (_message.Message,), {'DESCRIPTOR': _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'}), 'DESCRIPTOR': _SPEEDPOINTRAWFEATURE, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'})
_sym_db.RegisterMessage(SpeedPointRawFeature)
_sym_db.RegisterMessage(SpeedPointRawFeature.ObjectDecisionFeature)
ObstacleSTRawData = _reflection.GeneratedProtocolMessageType('ObstacleSTRawData', (_message.Message,), {'STPointPair': _reflection.GeneratedProtocolMessageType('STPointPair', (_message.Message,), {'DESCRIPTOR': _OBSTACLESTRAWDATA_STPOINTPAIR, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'}), 'ObstacleSTData': _reflection.GeneratedProtocolMessageType('ObstacleSTData', (_message.Message,), {'DESCRIPTOR': _OBSTACLESTRAWDATA_OBSTACLESTDATA, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'}), 'DESCRIPTOR': _OBSTACLESTRAWDATA, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'})
_sym_db.RegisterMessage(ObstacleSTRawData)
_sym_db.RegisterMessage(ObstacleSTRawData.STPointPair)
_sym_db.RegisterMessage(ObstacleSTRawData.ObstacleSTData)
TrajectoryPointRawFeature = _reflection.GeneratedProtocolMessageType('TrajectoryPointRawFeature', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYPOINTRAWFEATURE, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'})
_sym_db.RegisterMessage(TrajectoryPointRawFeature)
TrajectoryRawFeature = _reflection.GeneratedProtocolMessageType('TrajectoryRawFeature', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYRAWFEATURE, '__module__': 'modules.planning.proto.auto_tuning_raw_feature_pb2'})
_sym_db.RegisterMessage(TrajectoryRawFeature)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PATHPOINTRAWFEATURE._serialized_start = 122
    _PATHPOINTRAWFEATURE._serialized_end = 249
    _SPEEDPOINTRAWFEATURE._serialized_start = 252
    _SPEEDPOINTRAWFEATURE._serialized_end = 1285
    _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE._serialized_start = 1175
    _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE._serialized_end = 1285
    _OBSTACLESTRAWDATA._serialized_start = 1288
    _OBSTACLESTRAWDATA._serialized_end = 1895
    _OBSTACLESTRAWDATA_STPOINTPAIR._serialized_start = 1578
    _OBSTACLESTRAWDATA_STPOINTPAIR._serialized_end = 1651
    _OBSTACLESTRAWDATA_OBSTACLESTDATA._serialized_start = 1654
    _OBSTACLESTRAWDATA_OBSTACLESTDATA._serialized_end = 1895
    _TRAJECTORYPOINTRAWFEATURE._serialized_start = 1898
    _TRAJECTORYPOINTRAWFEATURE._serialized_end = 2069
    _TRAJECTORYRAWFEATURE._serialized_start = 2072
    _TRAJECTORYRAWFEATURE._serialized_end = 2240