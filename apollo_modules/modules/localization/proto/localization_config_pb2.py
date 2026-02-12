"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/localization/proto/localization_config.proto\x12\x13apollo.localization"\x94\x01\n\x12LocalizationConfig\x12X\n\x11localization_type\x18\x01 \x01(\x0e28.apollo.localization.LocalizationConfig.LocalizationType:\x03RTK"$\n\x10LocalizationType\x12\x07\n\x03RTK\x10\x00\x12\x07\n\x03MSF\x10\x01')
_LOCALIZATIONCONFIG = DESCRIPTOR.message_types_by_name['LocalizationConfig']
_LOCALIZATIONCONFIG_LOCALIZATIONTYPE = _LOCALIZATIONCONFIG.enum_types_by_name['LocalizationType']
LocalizationConfig = _reflection.GeneratedProtocolMessageType('LocalizationConfig', (_message.Message,), {'DESCRIPTOR': _LOCALIZATIONCONFIG, '__module__': 'modules.localization.proto.localization_config_pb2'})
_sym_db.RegisterMessage(LocalizationConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LOCALIZATIONCONFIG._serialized_start = 78
    _LOCALIZATIONCONFIG._serialized_end = 226
    _LOCALIZATIONCONFIG_LOCALIZATIONTYPE._serialized_start = 190
    _LOCALIZATIONCONFIG_LOCALIZATIONTYPE._serialized_end = 226