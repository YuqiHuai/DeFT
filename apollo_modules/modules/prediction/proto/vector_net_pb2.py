"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/prediction/proto/vector_net.proto\x12\x11apollo.prediction"\x1b\n\x08VNVector\x12\x0f\n\x07element\x18\x01 \x03(\x01"W\n\x08Polyline\x12+\n\x06vector\x18\x01 \x03(\x0b2\x1b.apollo.prediction.VNVector\x12\x0e\n\x06p_id_x\x18\x02 \x01(\x01\x12\x0e\n\x06p_id_y\x18\x03 \x01(\x01"<\n\x0bCarPosition\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0b\n\x03phi\x18\x03 \x01(\x01\x12\n\n\x02id\x18\x04 \x01(\t"w\n\x10VectorNetFeature\x124\n\x0ccar_position\x18\x01 \x01(\x0b2\x1e.apollo.prediction.CarPosition\x12-\n\x08polyline\x18\x02 \x03(\x0b2\x1b.apollo.prediction.Polyline":\n\nWorldCoord\x12,\n\x04pose\x18\x01 \x03(\x0b2\x1e.apollo.prediction.CarPosition')
_VNVECTOR = DESCRIPTOR.message_types_by_name['VNVector']
_POLYLINE = DESCRIPTOR.message_types_by_name['Polyline']
_CARPOSITION = DESCRIPTOR.message_types_by_name['CarPosition']
_VECTORNETFEATURE = DESCRIPTOR.message_types_by_name['VectorNetFeature']
_WORLDCOORD = DESCRIPTOR.message_types_by_name['WorldCoord']
VNVector = _reflection.GeneratedProtocolMessageType('VNVector', (_message.Message,), {'DESCRIPTOR': _VNVECTOR, '__module__': 'modules.prediction.proto.vector_net_pb2'})
_sym_db.RegisterMessage(VNVector)
Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), {'DESCRIPTOR': _POLYLINE, '__module__': 'modules.prediction.proto.vector_net_pb2'})
_sym_db.RegisterMessage(Polyline)
CarPosition = _reflection.GeneratedProtocolMessageType('CarPosition', (_message.Message,), {'DESCRIPTOR': _CARPOSITION, '__module__': 'modules.prediction.proto.vector_net_pb2'})
_sym_db.RegisterMessage(CarPosition)
VectorNetFeature = _reflection.GeneratedProtocolMessageType('VectorNetFeature', (_message.Message,), {'DESCRIPTOR': _VECTORNETFEATURE, '__module__': 'modules.prediction.proto.vector_net_pb2'})
_sym_db.RegisterMessage(VectorNetFeature)
WorldCoord = _reflection.GeneratedProtocolMessageType('WorldCoord', (_message.Message,), {'DESCRIPTOR': _WORLDCOORD, '__module__': 'modules.prediction.proto.vector_net_pb2'})
_sym_db.RegisterMessage(WorldCoord)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VNVECTOR._serialized_start = 64
    _VNVECTOR._serialized_end = 91
    _POLYLINE._serialized_start = 93
    _POLYLINE._serialized_end = 180
    _CARPOSITION._serialized_start = 182
    _CARPOSITION._serialized_end = 242
    _VECTORNETFEATURE._serialized_start = 244
    _VECTORNETFEATURE._serialized_end = 363
    _WORLDCOORD._serialized_start = 365
    _WORLDCOORD._serialized_end = 423