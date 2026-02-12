"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/prediction/proto/network_layers.proto\x12\x11apollo.prediction"2\n\x0fTensorParameter\x12\x10\n\x04data\x18\x01 \x03(\x02B\x02\x10\x01\x12\r\n\x05shape\x18\x02 \x03(\x05"D\n\x0eInputParameter\x12\x13\n\x0binput_shape\x18\x01 \x03(\x05\x12\r\n\x05dtype\x18\x02 \x01(\t\x12\x0e\n\x06sparse\x18\x03 \x01(\x08"\xac\x01\n\x0eDenseParameter\x12\r\n\x05units\x18\x01 \x01(\x05\x12\x12\n\nactivation\x18\x02 \x01(\t\x12\x10\n\x08use_bias\x18\x03 \x01(\x08\x123\n\x07weights\x18\x04 \x01(\x0b2".apollo.prediction.TensorParameter\x120\n\x04bias\x18\x05 \x01(\x0b2".apollo.prediction.TensorParameter"\xa8\x01\n\x0fConv1dParameter\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\x10\n\x08use_bias\x18\x02 \x01(\x08\x122\n\x06kernel\x18\x03 \x01(\x0b2".apollo.prediction.TensorParameter\x120\n\x04bias\x18\x04 \x01(\x0b2".apollo.prediction.TensorParameter\x12\x0e\n\x06stride\x18\x05 \x01(\x05"9\n\x12MaxPool1dParameter\x12\x13\n\x0bkernel_size\x18\x01 \x01(\x05\x12\x0e\n\x06stride\x18\x02 \x01(\x05"9\n\x12AvgPool1dParameter\x12\x13\n\x0bkernel_size\x18\x01 \x01(\x05\x12\x0e\n\x06stride\x18\x02 \x01(\x05"\xbc\x02\n\x1bBatchNormalizationParameter\x12\x16\n\x07epsilon\x18\x01 \x01(\x01:\x051e-05\x12\x0c\n\x04axis\x18\x02 \x01(\x05\x12\x0e\n\x06center\x18\x03 \x01(\x08\x12\r\n\x05scale\x18\x04 \x01(\x08\x12\x10\n\x08momentum\x18\x05 \x01(\x02\x12.\n\x02mu\x18\x06 \x01(\x0b2".apollo.prediction.TensorParameter\x121\n\x05sigma\x18\x07 \x01(\x0b2".apollo.prediction.TensorParameter\x121\n\x05gamma\x18\x08 \x01(\x0b2".apollo.prediction.TensorParameter\x120\n\x04beta\x18\t \x01(\x0b2".apollo.prediction.TensorParameter"\xe0\x07\n\rLSTMParameter\x12\r\n\x05units\x18\x01 \x01(\x05\x12\x18\n\x10return_sequences\x18\x02 \x01(\x08\x12\x10\n\x08stateful\x18\x03 \x01(\x08\x12\x12\n\nactivation\x18\x04 \x01(\t\x12\x1c\n\x14recurrent_activation\x18\x05 \x01(\t\x12\x10\n\x08use_bias\x18\x06 \x01(\x08\x12\x1e\n\x10unit_forget_bias\x18\x07 \x01(\x08:\x04true\x12\x1b\n\x0cgo_backwards\x18\x08 \x01(\x08:\x05false\x12\x15\n\x06unroll\x18\t \x01(\x08:\x05false\x12\x19\n\x0eimplementation\x18\n \x01(\x05:\x010\x129\n\rweights_input\x18\x0f \x01(\x0b2".apollo.prediction.TensorParameter\x12:\n\x0eweights_forget\x18\x10 \x01(\x0b2".apollo.prediction.TensorParameter\x128\n\x0cweights_cell\x18\x11 \x01(\x0b2".apollo.prediction.TensorParameter\x12:\n\x0eweights_output\x18\x12 \x01(\x0b2".apollo.prediction.TensorParameter\x126\n\nbias_input\x18\x13 \x01(\x0b2".apollo.prediction.TensorParameter\x127\n\x0bbias_forget\x18\x14 \x01(\x0b2".apollo.prediction.TensorParameter\x125\n\tbias_cell\x18\x15 \x01(\x0b2".apollo.prediction.TensorParameter\x127\n\x0bbias_output\x18\x16 \x01(\x0b2".apollo.prediction.TensorParameter\x12C\n\x17recurrent_weights_input\x18\x19 \x01(\x0b2".apollo.prediction.TensorParameter\x12D\n\x18recurrent_weights_forget\x18\x1a \x01(\x0b2".apollo.prediction.TensorParameter\x12B\n\x16recurrent_weights_cell\x18\x1b \x01(\x0b2".apollo.prediction.TensorParameter\x12D\n\x18recurrent_weights_output\x18\x1c \x01(\x0b2".apollo.prediction.TensorParameter")\n\x13ActivationParameter\x12\x12\n\nactivation\x18\x01 \x01(\t"\x12\n\x10FlattenParameter"$\n\x14ConcatenateParameter\x12\x0c\n\x04axis\x18\x01 \x01(\x05"\x9f\x05\n\x0eLayerParameter\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0corder_number\x18\x03 \x01(\x05\x122\n\x05input\x18\x04 \x01(\x0b2!.apollo.prediction.InputParameterH\x00\x12<\n\nactivation\x18\x05 \x01(\x0b2&.apollo.prediction.ActivationParameterH\x00\x122\n\x05dense\x18\x06 \x01(\x0b2!.apollo.prediction.DenseParameterH\x00\x12M\n\x13batch_normalization\x18\x07 \x01(\x0b2..apollo.prediction.BatchNormalizationParameterH\x00\x120\n\x04lstm\x18\x08 \x01(\x0b2 .apollo.prediction.LSTMParameterH\x00\x126\n\x07flatten\x18\t \x01(\x0b2#.apollo.prediction.FlattenParameterH\x00\x12>\n\x0bconcatenate\x18\n \x01(\x0b2\'.apollo.prediction.ConcatenateParameterH\x00\x124\n\x06conv1d\x18\x0b \x01(\x0b2".apollo.prediction.Conv1dParameterH\x00\x12:\n\tmaxpool1d\x18\x0c \x01(\x0b2%.apollo.prediction.MaxPool1dParameterH\x00\x12:\n\tavgpool1d\x18\r \x01(\x0b2%.apollo.prediction.AvgPool1dParameterH\x00B\x0e\n\x0coneof_layers')
_TENSORPARAMETER = DESCRIPTOR.message_types_by_name['TensorParameter']
_INPUTPARAMETER = DESCRIPTOR.message_types_by_name['InputParameter']
_DENSEPARAMETER = DESCRIPTOR.message_types_by_name['DenseParameter']
_CONV1DPARAMETER = DESCRIPTOR.message_types_by_name['Conv1dParameter']
_MAXPOOL1DPARAMETER = DESCRIPTOR.message_types_by_name['MaxPool1dParameter']
_AVGPOOL1DPARAMETER = DESCRIPTOR.message_types_by_name['AvgPool1dParameter']
_BATCHNORMALIZATIONPARAMETER = DESCRIPTOR.message_types_by_name['BatchNormalizationParameter']
_LSTMPARAMETER = DESCRIPTOR.message_types_by_name['LSTMParameter']
_ACTIVATIONPARAMETER = DESCRIPTOR.message_types_by_name['ActivationParameter']
_FLATTENPARAMETER = DESCRIPTOR.message_types_by_name['FlattenParameter']
_CONCATENATEPARAMETER = DESCRIPTOR.message_types_by_name['ConcatenateParameter']
_LAYERPARAMETER = DESCRIPTOR.message_types_by_name['LayerParameter']
TensorParameter = _reflection.GeneratedProtocolMessageType('TensorParameter', (_message.Message,), {'DESCRIPTOR': _TENSORPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(TensorParameter)
InputParameter = _reflection.GeneratedProtocolMessageType('InputParameter', (_message.Message,), {'DESCRIPTOR': _INPUTPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(InputParameter)
DenseParameter = _reflection.GeneratedProtocolMessageType('DenseParameter', (_message.Message,), {'DESCRIPTOR': _DENSEPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(DenseParameter)
Conv1dParameter = _reflection.GeneratedProtocolMessageType('Conv1dParameter', (_message.Message,), {'DESCRIPTOR': _CONV1DPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(Conv1dParameter)
MaxPool1dParameter = _reflection.GeneratedProtocolMessageType('MaxPool1dParameter', (_message.Message,), {'DESCRIPTOR': _MAXPOOL1DPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(MaxPool1dParameter)
AvgPool1dParameter = _reflection.GeneratedProtocolMessageType('AvgPool1dParameter', (_message.Message,), {'DESCRIPTOR': _AVGPOOL1DPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(AvgPool1dParameter)
BatchNormalizationParameter = _reflection.GeneratedProtocolMessageType('BatchNormalizationParameter', (_message.Message,), {'DESCRIPTOR': _BATCHNORMALIZATIONPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(BatchNormalizationParameter)
LSTMParameter = _reflection.GeneratedProtocolMessageType('LSTMParameter', (_message.Message,), {'DESCRIPTOR': _LSTMPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(LSTMParameter)
ActivationParameter = _reflection.GeneratedProtocolMessageType('ActivationParameter', (_message.Message,), {'DESCRIPTOR': _ACTIVATIONPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(ActivationParameter)
FlattenParameter = _reflection.GeneratedProtocolMessageType('FlattenParameter', (_message.Message,), {'DESCRIPTOR': _FLATTENPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(FlattenParameter)
ConcatenateParameter = _reflection.GeneratedProtocolMessageType('ConcatenateParameter', (_message.Message,), {'DESCRIPTOR': _CONCATENATEPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(ConcatenateParameter)
LayerParameter = _reflection.GeneratedProtocolMessageType('LayerParameter', (_message.Message,), {'DESCRIPTOR': _LAYERPARAMETER, '__module__': 'modules.prediction.proto.network_layers_pb2'})
_sym_db.RegisterMessage(LayerParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TENSORPARAMETER.fields_by_name['data']._options = None
    _TENSORPARAMETER.fields_by_name['data']._serialized_options = b'\x10\x01'
    _TENSORPARAMETER._serialized_start = 68
    _TENSORPARAMETER._serialized_end = 118
    _INPUTPARAMETER._serialized_start = 120
    _INPUTPARAMETER._serialized_end = 188
    _DENSEPARAMETER._serialized_start = 191
    _DENSEPARAMETER._serialized_end = 363
    _CONV1DPARAMETER._serialized_start = 366
    _CONV1DPARAMETER._serialized_end = 534
    _MAXPOOL1DPARAMETER._serialized_start = 536
    _MAXPOOL1DPARAMETER._serialized_end = 593
    _AVGPOOL1DPARAMETER._serialized_start = 595
    _AVGPOOL1DPARAMETER._serialized_end = 652
    _BATCHNORMALIZATIONPARAMETER._serialized_start = 655
    _BATCHNORMALIZATIONPARAMETER._serialized_end = 971
    _LSTMPARAMETER._serialized_start = 974
    _LSTMPARAMETER._serialized_end = 1966
    _ACTIVATIONPARAMETER._serialized_start = 1968
    _ACTIVATIONPARAMETER._serialized_end = 2009
    _FLATTENPARAMETER._serialized_start = 2011
    _FLATTENPARAMETER._serialized_end = 2029
    _CONCATENATEPARAMETER._serialized_start = 2031
    _CONCATENATEPARAMETER._serialized_end = 2067
    _LAYERPARAMETER._serialized_start = 2070
    _LAYERPARAMETER._serialized_end = 2741