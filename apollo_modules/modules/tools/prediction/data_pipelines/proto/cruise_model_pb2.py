"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/tools/prediction/data_pipelines/proto/cruise_model.proto"2\n\x0fTensorParameter\x12\x10\n\x04data\x18\x01 \x03(\x02B\x02\x10\x01\x12\r\n\x05shape\x18\x02 \x03(\x05"D\n\x0eInputParameter\x12\x13\n\x0binput_shape\x18\x01 \x03(\x05\x12\r\n\x05dtype\x18\x02 \x01(\t\x12\x0e\n\x06sparse\x18\x03 \x01(\x08"\x84\x01\n\x0fConv1dParameter\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\x10\n\x08use_bias\x18\x02 \x01(\x08\x12 \n\x06kernel\x18\x03 \x01(\x0b2\x10.TensorParameter\x12\x1e\n\x04bias\x18\x04 \x01(\x0b2\x10.TensorParameter\x12\x0e\n\x06stride\x18\x05 \x01(\x05"\x88\x01\n\x0eDenseParameter\x12\r\n\x05units\x18\x01 \x01(\x05\x12\x12\n\nactivation\x18\x02 \x01(\t\x12\x10\n\x08use_bias\x18\x03 \x01(\x08\x12!\n\x07weights\x18\x04 \x01(\x0b2\x10.TensorParameter\x12\x1e\n\x04bias\x18\x05 \x01(\x0b2\x10.TensorParameter")\n\x13ActivationParameter\x12\x12\n\nactivation\x18\x01 \x01(\t"9\n\x12MaxPool1dParameter\x12\x13\n\x0bkernel_size\x18\x01 \x01(\x05\x12\x0e\n\x06stride\x18\x02 \x01(\x05"9\n\x12AvgPool1dParameter\x12\x13\n\x0bkernel_size\x18\x01 \x01(\x05\x12\x0e\n\x06stride\x18\x02 \x01(\x05"\xde\x01\n\x18LaneFeatureConvParameter\x12"\n\x08conv1d_0\x18\x01 \x01(\x0b2\x10.Conv1dParameter\x12*\n\x0cactivation_1\x18\x02 \x01(\x0b2\x14.ActivationParameter\x12"\n\x08conv1d_2\x18\x03 \x01(\x0b2\x10.Conv1dParameter\x12*\n\x0cactivation_3\x18\x04 \x01(\x0b2\x14.ActivationParameter\x12"\n\x08conv1d_4\x18\x05 \x01(\x0b2\x10.Conv1dParameter"\xb5\x01\n\x15ObsFeatureFCParameter\x12!\n\x08linear_0\x18\x01 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_1\x18\x02 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_3\x18\x03 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_4\x18\x04 \x01(\x0b2\x14.ActivationParameter"\xd0\x02\n\x11ClassifyParameter\x12!\n\x08linear_0\x18\x01 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_1\x18\x02 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_3\x18\x03 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_4\x18\x04 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_6\x18\x05 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_7\x18\x06 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_9\x18\x07 \x01(\x0b2\x0f.DenseParameter\x12+\n\ractivation_10\x18\x08 \x01(\x0b2\x14.ActivationParameter"\xcf\x02\n\x10RegressParameter\x12!\n\x08linear_0\x18\x01 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_1\x18\x02 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_3\x18\x03 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_4\x18\x04 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_6\x18\x05 \x01(\x0b2\x0f.DenseParameter\x12*\n\x0cactivation_7\x18\x06 \x01(\x0b2\x14.ActivationParameter\x12!\n\x08linear_9\x18\x07 \x01(\x0b2\x0f.DenseParameter\x12+\n\ractivation_10\x18\x08 \x01(\x0b2\x14.ActivationParameter"\xac\x02\n\x14CruiseModelParameter\x124\n\x11lane_feature_conv\x18\x01 \x01(\x0b2\x19.LaneFeatureConvParameter\x121\n\x14lane_feature_maxpool\x18\x02 \x01(\x0b2\x13.MaxPool1dParameter\x121\n\x14lane_feature_avgpool\x18\x03 \x01(\x0b2\x13.AvgPool1dParameter\x12.\n\x0eobs_feature_fc\x18\x05 \x01(\x0b2\x16.ObsFeatureFCParameter\x12$\n\x08classify\x18\x06 \x01(\x0b2\x12.ClassifyParameter\x12"\n\x07regress\x18\x07 \x01(\x0b2\x11.RegressParameter')
_TENSORPARAMETER = DESCRIPTOR.message_types_by_name['TensorParameter']
_INPUTPARAMETER = DESCRIPTOR.message_types_by_name['InputParameter']
_CONV1DPARAMETER = DESCRIPTOR.message_types_by_name['Conv1dParameter']
_DENSEPARAMETER = DESCRIPTOR.message_types_by_name['DenseParameter']
_ACTIVATIONPARAMETER = DESCRIPTOR.message_types_by_name['ActivationParameter']
_MAXPOOL1DPARAMETER = DESCRIPTOR.message_types_by_name['MaxPool1dParameter']
_AVGPOOL1DPARAMETER = DESCRIPTOR.message_types_by_name['AvgPool1dParameter']
_LANEFEATURECONVPARAMETER = DESCRIPTOR.message_types_by_name['LaneFeatureConvParameter']
_OBSFEATUREFCPARAMETER = DESCRIPTOR.message_types_by_name['ObsFeatureFCParameter']
_CLASSIFYPARAMETER = DESCRIPTOR.message_types_by_name['ClassifyParameter']
_REGRESSPARAMETER = DESCRIPTOR.message_types_by_name['RegressParameter']
_CRUISEMODELPARAMETER = DESCRIPTOR.message_types_by_name['CruiseModelParameter']
TensorParameter = _reflection.GeneratedProtocolMessageType('TensorParameter', (_message.Message,), {'DESCRIPTOR': _TENSORPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(TensorParameter)
InputParameter = _reflection.GeneratedProtocolMessageType('InputParameter', (_message.Message,), {'DESCRIPTOR': _INPUTPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(InputParameter)
Conv1dParameter = _reflection.GeneratedProtocolMessageType('Conv1dParameter', (_message.Message,), {'DESCRIPTOR': _CONV1DPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(Conv1dParameter)
DenseParameter = _reflection.GeneratedProtocolMessageType('DenseParameter', (_message.Message,), {'DESCRIPTOR': _DENSEPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(DenseParameter)
ActivationParameter = _reflection.GeneratedProtocolMessageType('ActivationParameter', (_message.Message,), {'DESCRIPTOR': _ACTIVATIONPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(ActivationParameter)
MaxPool1dParameter = _reflection.GeneratedProtocolMessageType('MaxPool1dParameter', (_message.Message,), {'DESCRIPTOR': _MAXPOOL1DPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(MaxPool1dParameter)
AvgPool1dParameter = _reflection.GeneratedProtocolMessageType('AvgPool1dParameter', (_message.Message,), {'DESCRIPTOR': _AVGPOOL1DPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(AvgPool1dParameter)
LaneFeatureConvParameter = _reflection.GeneratedProtocolMessageType('LaneFeatureConvParameter', (_message.Message,), {'DESCRIPTOR': _LANEFEATURECONVPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(LaneFeatureConvParameter)
ObsFeatureFCParameter = _reflection.GeneratedProtocolMessageType('ObsFeatureFCParameter', (_message.Message,), {'DESCRIPTOR': _OBSFEATUREFCPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(ObsFeatureFCParameter)
ClassifyParameter = _reflection.GeneratedProtocolMessageType('ClassifyParameter', (_message.Message,), {'DESCRIPTOR': _CLASSIFYPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(ClassifyParameter)
RegressParameter = _reflection.GeneratedProtocolMessageType('RegressParameter', (_message.Message,), {'DESCRIPTOR': _REGRESSPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(RegressParameter)
CruiseModelParameter = _reflection.GeneratedProtocolMessageType('CruiseModelParameter', (_message.Message,), {'DESCRIPTOR': _CRUISEMODELPARAMETER, '__module__': 'modules.tools.prediction.data_pipelines.proto.cruise_model_pb2'})
_sym_db.RegisterMessage(CruiseModelParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TENSORPARAMETER.fields_by_name['data']._options = None
    _TENSORPARAMETER.fields_by_name['data']._serialized_options = b'\x10\x01'
    _TENSORPARAMETER._serialized_start = 68
    _TENSORPARAMETER._serialized_end = 118
    _INPUTPARAMETER._serialized_start = 120
    _INPUTPARAMETER._serialized_end = 188
    _CONV1DPARAMETER._serialized_start = 191
    _CONV1DPARAMETER._serialized_end = 323
    _DENSEPARAMETER._serialized_start = 326
    _DENSEPARAMETER._serialized_end = 462
    _ACTIVATIONPARAMETER._serialized_start = 464
    _ACTIVATIONPARAMETER._serialized_end = 505
    _MAXPOOL1DPARAMETER._serialized_start = 507
    _MAXPOOL1DPARAMETER._serialized_end = 564
    _AVGPOOL1DPARAMETER._serialized_start = 566
    _AVGPOOL1DPARAMETER._serialized_end = 623
    _LANEFEATURECONVPARAMETER._serialized_start = 626
    _LANEFEATURECONVPARAMETER._serialized_end = 848
    _OBSFEATUREFCPARAMETER._serialized_start = 851
    _OBSFEATUREFCPARAMETER._serialized_end = 1032
    _CLASSIFYPARAMETER._serialized_start = 1035
    _CLASSIFYPARAMETER._serialized_end = 1371
    _REGRESSPARAMETER._serialized_start = 1374
    _REGRESSPARAMETER._serialized_end = 1709
    _CRUISEMODELPARAMETER._serialized_start = 1712
    _CRUISEMODELPARAMETER._serialized_end = 2012