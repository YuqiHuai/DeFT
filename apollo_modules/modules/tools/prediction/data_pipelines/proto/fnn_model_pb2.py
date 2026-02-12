"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/tools/prediction/data_pipelines/proto/fnn_model.proto"\x19\n\x06Vector\x12\x0f\n\x07columns\x18\x01 \x03(\x01"\x1f\n\x06Matrix\x12\x15\n\x04rows\x18\x01 \x03(\x0b2\x07.Vector"\xf2\x01\n\x05Layer\x12\x17\n\x0flayer_input_dim\x18\x01 \x01(\x05\x12\x18\n\x10layer_output_dim\x18\x02 \x01(\x05\x12#\n\x12layer_input_weight\x18\x03 \x01(\x0b2\x07.Matrix\x12\x1b\n\nlayer_bias\x18\x04 \x01(\x0b2\x07.Vector\x124\n\x15layer_activation_func\x18\x05 \x01(\x0e2\x15.Layer.ActivationFunc">\n\x0eActivationFunc\x12\x08\n\x04RELU\x10\x00\x12\x08\n\x04TANH\x10\x01\x12\x0b\n\x07SIGMOID\x10\x02\x12\x0b\n\x07SOFTMAX\x10\x03"\x98\x01\n\x08FnnModel\x12\x11\n\tdim_input\x18\x01 \x01(\x05\x12\x1d\n\x0csamples_mean\x18\x02 \x01(\x0b2\x07.Vector\x12\x1c\n\x0bsamples_std\x18\x03 \x01(\x0b2\x07.Vector\x12\x11\n\tnum_layer\x18\x04 \x01(\x05\x12\x15\n\x05layer\x18\x05 \x03(\x0b2\x06.Layer\x12\x12\n\ndim_output\x18\x06 \x01(\x05')
_VECTOR = DESCRIPTOR.message_types_by_name['Vector']
_MATRIX = DESCRIPTOR.message_types_by_name['Matrix']
_LAYER = DESCRIPTOR.message_types_by_name['Layer']
_FNNMODEL = DESCRIPTOR.message_types_by_name['FnnModel']
_LAYER_ACTIVATIONFUNC = _LAYER.enum_types_by_name['ActivationFunc']
Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {'DESCRIPTOR': _VECTOR, '__module__': 'modules.tools.prediction.data_pipelines.proto.fnn_model_pb2'})
_sym_db.RegisterMessage(Vector)
Matrix = _reflection.GeneratedProtocolMessageType('Matrix', (_message.Message,), {'DESCRIPTOR': _MATRIX, '__module__': 'modules.tools.prediction.data_pipelines.proto.fnn_model_pb2'})
_sym_db.RegisterMessage(Matrix)
Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), {'DESCRIPTOR': _LAYER, '__module__': 'modules.tools.prediction.data_pipelines.proto.fnn_model_pb2'})
_sym_db.RegisterMessage(Layer)
FnnModel = _reflection.GeneratedProtocolMessageType('FnnModel', (_message.Message,), {'DESCRIPTOR': _FNNMODEL, '__module__': 'modules.tools.prediction.data_pipelines.proto.fnn_model_pb2'})
_sym_db.RegisterMessage(FnnModel)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VECTOR._serialized_start = 65
    _VECTOR._serialized_end = 90
    _MATRIX._serialized_start = 92
    _MATRIX._serialized_end = 123
    _LAYER._serialized_start = 126
    _LAYER._serialized_end = 368
    _LAYER_ACTIVATIONFUNC._serialized_start = 306
    _LAYER_ACTIVATIONFUNC._serialized_end = 368
    _FNNMODEL._serialized_start = 371
    _FNNMODEL._serialized_end = 523