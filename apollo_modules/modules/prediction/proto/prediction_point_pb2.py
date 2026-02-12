"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/prediction/proto/prediction_point.proto\x12\x11apollo.prediction"E\n\x13PredictionPathPoint\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\x18\n\x10velocity_heading\x18\x03 \x01(\x01"j\n\x19PredictionTrajectoryPoint\x12:\n\npath_point\x18\x01 \x02(\x0b2&.apollo.prediction.PredictionPathPoint\x12\x11\n\ttimestamp\x18\x02 \x02(\x01')
_PREDICTIONPATHPOINT = DESCRIPTOR.message_types_by_name['PredictionPathPoint']
_PREDICTIONTRAJECTORYPOINT = DESCRIPTOR.message_types_by_name['PredictionTrajectoryPoint']
PredictionPathPoint = _reflection.GeneratedProtocolMessageType('PredictionPathPoint', (_message.Message,), {'DESCRIPTOR': _PREDICTIONPATHPOINT, '__module__': 'modules.prediction.proto.prediction_point_pb2'})
_sym_db.RegisterMessage(PredictionPathPoint)
PredictionTrajectoryPoint = _reflection.GeneratedProtocolMessageType('PredictionTrajectoryPoint', (_message.Message,), {'DESCRIPTOR': _PREDICTIONTRAJECTORYPOINT, '__module__': 'modules.prediction.proto.prediction_point_pb2'})
_sym_db.RegisterMessage(PredictionTrajectoryPoint)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PREDICTIONPATHPOINT._serialized_start = 70
    _PREDICTIONPATHPOINT._serialized_end = 139
    _PREDICTIONTRAJECTORYPOINT._serialized_start = 141
    _PREDICTIONTRAJECTORYPOINT._serialized_end = 247