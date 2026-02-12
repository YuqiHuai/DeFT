"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/planning/proto/auto_tuning_model_input.proto\x12\x1aapollo.planning.autotuning"\xf9\x04\n\x14PathPointwiseFeature\x12\t\n\x01l\x18\x01 \x01(\x01\x12\n\n\x02dl\x18\x02 \x01(\x01\x12\x0b\n\x03ddl\x18\x03 \x01(\x01\x12\r\n\x05kappa\x18\x04 \x01(\x01\x12W\n\robstacle_info\x18\x05 \x03(\x0b2@.apollo.planning.autotuning.PathPointwiseFeature.ObstacleFeature\x12`\n\x12left_bound_feature\x18\x06 \x01(\x0b2D.apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature\x12a\n\x13right_bound_feature\x18\x07 \x01(\x0b2D.apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature\x1a+\n\x0fObstacleFeature\x12\x18\n\x10lateral_distance\x18\x01 \x01(\x01\x1a\xe2\x01\n\x13BoundRelatedFeature\x12\x16\n\x0ebound_distance\x18\x01 \x01(\x01\x12l\n\x0fcrossable_level\x18\x02 \x01(\x0e2S.apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature.CrossableLevel"E\n\x0eCrossableLevel\x12\x0e\n\nCROSS_FREE\x10\x00\x12\x0e\n\nCROSS_ABLE\x10\x01\x12\x13\n\x0fCROSS_FORBIDDEN\x10\x02"\x87\x08\n\x15SpeedPointwiseFeature\x12\x0c\n\x01s\x18\x01 \x01(\x01:\x010\x12\x0c\n\x01t\x18\x02 \x01(\x01:\x010\x12\x0c\n\x01v\x18\x03 \x01(\x01:\x010\x12\x16\n\x0bspeed_limit\x18\x04 \x01(\x01:\x010\x12\x0e\n\x03acc\x18\x05 \x01(\x01:\x010\x12\x0f\n\x04jerk\x18\x06 \x01(\x01:\x010\x12]\n\x12follow_obs_feature\x18\x07 \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12_\n\x14overtake_obs_feature\x18\x08 \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\\\n\x11nudge_obs_feature\x18\t \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12[\n\x10stop_obs_feature\x18\n \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\x1a\n\x0fcollision_times\x18\x0b \x01(\x05:\x010\x12^\n\x13virtual_obs_feature\x18\x0c \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\x16\n\x0blateral_acc\x18\r \x01(\x01:\x010\x12\x1d\n\x12path_curvature_abs\x18\x0e \x01(\x01:\x010\x12e\n\x1asidepass_front_obs_feature\x18\x0f \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12d\n\x19sidepass_rear_obs_feature\x18\x10 \x03(\x0b2A.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x1a\x8f\x01\n\x0fObstacleFeature\x12\x1d\n\x15longitudinal_distance\x18\x01 \x01(\x01\x12\x16\n\x0eobstacle_speed\x18\x02 \x01(\x01\x12\x1c\n\x10lateral_distance\x18\x03 \x01(\x01:\x0210\x12\x13\n\x0bprobability\x18\x04 \x01(\x01\x12\x12\n\nrelative_v\x18\x05 \x01(\x01"\xba\x01\n\x1aTrajectoryPointwiseFeature\x12L\n\x12path_input_feature\x18\x01 \x01(\x0b20.apollo.planning.autotuning.PathPointwiseFeature\x12N\n\x13speed_input_feature\x18\x02 \x01(\x0b21.apollo.planning.autotuning.SpeedPointwiseFeature"b\n\x11TrajectoryFeature\x12M\n\rpoint_feature\x18\x01 \x03(\x0b26.apollo.planning.autotuning.TrajectoryPointwiseFeature')
_PATHPOINTWISEFEATURE = DESCRIPTOR.message_types_by_name['PathPointwiseFeature']
_PATHPOINTWISEFEATURE_OBSTACLEFEATURE = _PATHPOINTWISEFEATURE.nested_types_by_name['ObstacleFeature']
_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE = _PATHPOINTWISEFEATURE.nested_types_by_name['BoundRelatedFeature']
_SPEEDPOINTWISEFEATURE = DESCRIPTOR.message_types_by_name['SpeedPointwiseFeature']
_SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE = _SPEEDPOINTWISEFEATURE.nested_types_by_name['ObstacleFeature']
_TRAJECTORYPOINTWISEFEATURE = DESCRIPTOR.message_types_by_name['TrajectoryPointwiseFeature']
_TRAJECTORYFEATURE = DESCRIPTOR.message_types_by_name['TrajectoryFeature']
_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL = _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE.enum_types_by_name['CrossableLevel']
PathPointwiseFeature = _reflection.GeneratedProtocolMessageType('PathPointwiseFeature', (_message.Message,), {'ObstacleFeature': _reflection.GeneratedProtocolMessageType('ObstacleFeature', (_message.Message,), {'DESCRIPTOR': _PATHPOINTWISEFEATURE_OBSTACLEFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'}), 'BoundRelatedFeature': _reflection.GeneratedProtocolMessageType('BoundRelatedFeature', (_message.Message,), {'DESCRIPTOR': _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'}), 'DESCRIPTOR': _PATHPOINTWISEFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'})
_sym_db.RegisterMessage(PathPointwiseFeature)
_sym_db.RegisterMessage(PathPointwiseFeature.ObstacleFeature)
_sym_db.RegisterMessage(PathPointwiseFeature.BoundRelatedFeature)
SpeedPointwiseFeature = _reflection.GeneratedProtocolMessageType('SpeedPointwiseFeature', (_message.Message,), {'ObstacleFeature': _reflection.GeneratedProtocolMessageType('ObstacleFeature', (_message.Message,), {'DESCRIPTOR': _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'}), 'DESCRIPTOR': _SPEEDPOINTWISEFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'})
_sym_db.RegisterMessage(SpeedPointwiseFeature)
_sym_db.RegisterMessage(SpeedPointwiseFeature.ObstacleFeature)
TrajectoryPointwiseFeature = _reflection.GeneratedProtocolMessageType('TrajectoryPointwiseFeature', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYPOINTWISEFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'})
_sym_db.RegisterMessage(TrajectoryPointwiseFeature)
TrajectoryFeature = _reflection.GeneratedProtocolMessageType('TrajectoryFeature', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYFEATURE, '__module__': 'modules.planning.proto.auto_tuning_model_input_pb2'})
_sym_db.RegisterMessage(TrajectoryFeature)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PATHPOINTWISEFEATURE._serialized_start = 85
    _PATHPOINTWISEFEATURE._serialized_end = 718
    _PATHPOINTWISEFEATURE_OBSTACLEFEATURE._serialized_start = 446
    _PATHPOINTWISEFEATURE_OBSTACLEFEATURE._serialized_end = 489
    _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE._serialized_start = 492
    _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE._serialized_end = 718
    _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL._serialized_start = 649
    _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL._serialized_end = 718
    _SPEEDPOINTWISEFEATURE._serialized_start = 721
    _SPEEDPOINTWISEFEATURE._serialized_end = 1752
    _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE._serialized_start = 1609
    _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE._serialized_end = 1752
    _TRAJECTORYPOINTWISEFEATURE._serialized_start = 1755
    _TRAJECTORYPOINTWISEFEATURE._serialized_end = 1941
    _TRAJECTORYFEATURE._serialized_start = 1943
    _TRAJECTORYFEATURE._serialized_end = 2041