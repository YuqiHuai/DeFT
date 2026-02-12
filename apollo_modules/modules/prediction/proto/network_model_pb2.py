"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.prediction.proto import network_layers_pb2 as modules_dot_prediction_dot_proto_dot_network__layers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/prediction/proto/network_model.proto\x12\x11apollo.prediction\x1a-modules/prediction/proto/network_layers.proto"q\n\x12VerificationSample\x124\n\x08features\x18\x01 \x03(\x0b2".apollo.prediction.TensorParameter\x12\x13\n\x0bprobability\x18\x02 \x01(\x02\x12\x10\n\x08distance\x18\x03 \x01(\x02"B\n\x0bPerformance\x12\x10\n\x08accuracy\x18\x01 \x03(\x02\x12\x0e\n\x06recall\x18\x02 \x03(\x02\x12\x11\n\tprecision\x18\x03 \x03(\x02"\xea\x01\n\x0cNetParameter\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x121\n\x06layers\x18\x03 \x03(\x0b2!.apollo.prediction.LayerParameter\x12C\n\x14verification_samples\x18\x04 \x03(\x0b2%.apollo.prediction.VerificationSample\x123\n\x0bperformance\x18\x05 \x01(\x0b2\x1e.apollo.prediction.Performance\x12\x13\n\x0btime_dumped\x18\x06 \x01(\x02')
_VERIFICATIONSAMPLE = DESCRIPTOR.message_types_by_name['VerificationSample']
_PERFORMANCE = DESCRIPTOR.message_types_by_name['Performance']
_NETPARAMETER = DESCRIPTOR.message_types_by_name['NetParameter']
VerificationSample = _reflection.GeneratedProtocolMessageType('VerificationSample', (_message.Message,), {'DESCRIPTOR': _VERIFICATIONSAMPLE, '__module__': 'modules.prediction.proto.network_model_pb2'})
_sym_db.RegisterMessage(VerificationSample)
Performance = _reflection.GeneratedProtocolMessageType('Performance', (_message.Message,), {'DESCRIPTOR': _PERFORMANCE, '__module__': 'modules.prediction.proto.network_model_pb2'})
_sym_db.RegisterMessage(Performance)
NetParameter = _reflection.GeneratedProtocolMessageType('NetParameter', (_message.Message,), {'DESCRIPTOR': _NETPARAMETER, '__module__': 'modules.prediction.proto.network_model_pb2'})
_sym_db.RegisterMessage(NetParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VERIFICATIONSAMPLE._serialized_start = 114
    _VERIFICATIONSAMPLE._serialized_end = 227
    _PERFORMANCE._serialized_start = 229
    _PERFORMANCE._serialized_end = 295
    _NETPARAMETER._serialized_start = 298
    _NETPARAMETER._serialized_end = 532