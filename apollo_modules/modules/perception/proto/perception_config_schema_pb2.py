"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7modules/perception/proto/perception_config_schema.proto\x12\x11apollo.perception"*\n\x0bKeyValueInt\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05"-\n\x0eKeyValueString\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c"-\n\x0eKeyValueDouble\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01",\n\rKeyValueFloat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02"+\n\x0cKeyValueBool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08"0\n\x10KeyValueArrayInt\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x05"3\n\x13KeyValueArrayString\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x0c"3\n\x13KeyValueArrayDouble\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x01"2\n\x12KeyValueArrayFloat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x02"1\n\x11KeyValueArrayBool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x08"\x9c\x05\n\x10ModelConfigProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x126\n\x0einteger_params\x18\x03 \x03(\x0b2\x1e.apollo.perception.KeyValueInt\x128\n\rstring_params\x18\x04 \x03(\x0b2!.apollo.perception.KeyValueString\x128\n\rdouble_params\x18\x05 \x03(\x0b2!.apollo.perception.KeyValueDouble\x126\n\x0cfloat_params\x18\x06 \x03(\x0b2 .apollo.perception.KeyValueFloat\x124\n\x0bbool_params\x18\x07 \x03(\x0b2\x1f.apollo.perception.KeyValueBool\x12A\n\x14array_integer_params\x18\x08 \x03(\x0b2#.apollo.perception.KeyValueArrayInt\x12C\n\x13array_string_params\x18\t \x03(\x0b2&.apollo.perception.KeyValueArrayString\x12C\n\x13array_double_params\x18\n \x03(\x0b2&.apollo.perception.KeyValueArrayDouble\x12A\n\x12array_float_params\x18\x0b \x03(\x0b2%.apollo.perception.KeyValueArrayFloat\x12?\n\x11array_bool_params\x18\x0c \x03(\x0b2$.apollo.perception.KeyValueArrayBool"S\n\x15MultiModelConfigProto\x12:\n\rmodel_configs\x18\x01 \x03(\x0b2#.apollo.perception.ModelConfigProto"5\n\x18ModelConfigFileListProto\x12\x19\n\x11model_config_path\x18\x01 \x03(\t')
_KEYVALUEINT = DESCRIPTOR.message_types_by_name['KeyValueInt']
_KEYVALUESTRING = DESCRIPTOR.message_types_by_name['KeyValueString']
_KEYVALUEDOUBLE = DESCRIPTOR.message_types_by_name['KeyValueDouble']
_KEYVALUEFLOAT = DESCRIPTOR.message_types_by_name['KeyValueFloat']
_KEYVALUEBOOL = DESCRIPTOR.message_types_by_name['KeyValueBool']
_KEYVALUEARRAYINT = DESCRIPTOR.message_types_by_name['KeyValueArrayInt']
_KEYVALUEARRAYSTRING = DESCRIPTOR.message_types_by_name['KeyValueArrayString']
_KEYVALUEARRAYDOUBLE = DESCRIPTOR.message_types_by_name['KeyValueArrayDouble']
_KEYVALUEARRAYFLOAT = DESCRIPTOR.message_types_by_name['KeyValueArrayFloat']
_KEYVALUEARRAYBOOL = DESCRIPTOR.message_types_by_name['KeyValueArrayBool']
_MODELCONFIGPROTO = DESCRIPTOR.message_types_by_name['ModelConfigProto']
_MULTIMODELCONFIGPROTO = DESCRIPTOR.message_types_by_name['MultiModelConfigProto']
_MODELCONFIGFILELISTPROTO = DESCRIPTOR.message_types_by_name['ModelConfigFileListProto']
KeyValueInt = _reflection.GeneratedProtocolMessageType('KeyValueInt', (_message.Message,), {'DESCRIPTOR': _KEYVALUEINT, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueInt)
KeyValueString = _reflection.GeneratedProtocolMessageType('KeyValueString', (_message.Message,), {'DESCRIPTOR': _KEYVALUESTRING, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueString)
KeyValueDouble = _reflection.GeneratedProtocolMessageType('KeyValueDouble', (_message.Message,), {'DESCRIPTOR': _KEYVALUEDOUBLE, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueDouble)
KeyValueFloat = _reflection.GeneratedProtocolMessageType('KeyValueFloat', (_message.Message,), {'DESCRIPTOR': _KEYVALUEFLOAT, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueFloat)
KeyValueBool = _reflection.GeneratedProtocolMessageType('KeyValueBool', (_message.Message,), {'DESCRIPTOR': _KEYVALUEBOOL, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueBool)
KeyValueArrayInt = _reflection.GeneratedProtocolMessageType('KeyValueArrayInt', (_message.Message,), {'DESCRIPTOR': _KEYVALUEARRAYINT, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueArrayInt)
KeyValueArrayString = _reflection.GeneratedProtocolMessageType('KeyValueArrayString', (_message.Message,), {'DESCRIPTOR': _KEYVALUEARRAYSTRING, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueArrayString)
KeyValueArrayDouble = _reflection.GeneratedProtocolMessageType('KeyValueArrayDouble', (_message.Message,), {'DESCRIPTOR': _KEYVALUEARRAYDOUBLE, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueArrayDouble)
KeyValueArrayFloat = _reflection.GeneratedProtocolMessageType('KeyValueArrayFloat', (_message.Message,), {'DESCRIPTOR': _KEYVALUEARRAYFLOAT, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueArrayFloat)
KeyValueArrayBool = _reflection.GeneratedProtocolMessageType('KeyValueArrayBool', (_message.Message,), {'DESCRIPTOR': _KEYVALUEARRAYBOOL, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(KeyValueArrayBool)
ModelConfigProto = _reflection.GeneratedProtocolMessageType('ModelConfigProto', (_message.Message,), {'DESCRIPTOR': _MODELCONFIGPROTO, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(ModelConfigProto)
MultiModelConfigProto = _reflection.GeneratedProtocolMessageType('MultiModelConfigProto', (_message.Message,), {'DESCRIPTOR': _MULTIMODELCONFIGPROTO, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(MultiModelConfigProto)
ModelConfigFileListProto = _reflection.GeneratedProtocolMessageType('ModelConfigFileListProto', (_message.Message,), {'DESCRIPTOR': _MODELCONFIGFILELISTPROTO, '__module__': 'modules.perception.proto.perception_config_schema_pb2'})
_sym_db.RegisterMessage(ModelConfigFileListProto)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _KEYVALUEINT._serialized_start = 78
    _KEYVALUEINT._serialized_end = 120
    _KEYVALUESTRING._serialized_start = 122
    _KEYVALUESTRING._serialized_end = 167
    _KEYVALUEDOUBLE._serialized_start = 169
    _KEYVALUEDOUBLE._serialized_end = 214
    _KEYVALUEFLOAT._serialized_start = 216
    _KEYVALUEFLOAT._serialized_end = 260
    _KEYVALUEBOOL._serialized_start = 262
    _KEYVALUEBOOL._serialized_end = 305
    _KEYVALUEARRAYINT._serialized_start = 307
    _KEYVALUEARRAYINT._serialized_end = 355
    _KEYVALUEARRAYSTRING._serialized_start = 357
    _KEYVALUEARRAYSTRING._serialized_end = 408
    _KEYVALUEARRAYDOUBLE._serialized_start = 410
    _KEYVALUEARRAYDOUBLE._serialized_end = 461
    _KEYVALUEARRAYFLOAT._serialized_start = 463
    _KEYVALUEARRAYFLOAT._serialized_end = 513
    _KEYVALUEARRAYBOOL._serialized_start = 515
    _KEYVALUEARRAYBOOL._serialized_end = 564
    _MODELCONFIGPROTO._serialized_start = 567
    _MODELCONFIGPROTO._serialized_end = 1235
    _MULTIMODELCONFIGPROTO._serialized_start = 1237
    _MULTIMODELCONFIGPROTO._serialized_end = 1320
    _MODELCONFIGFILELISTPROTO._serialized_start = 1322
    _MODELCONFIGFILELISTPROTO._serialized_end = 1375