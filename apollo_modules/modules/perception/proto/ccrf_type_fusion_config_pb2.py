"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/perception/proto/ccrf_type_fusion_config.proto\x12\x17apollo.perception.lidar"\x8f\x01\n\x14CcrfTypeFusionConfig\x12(\n\x1eclassifiers_property_file_path\x18\x01 \x01(\t:\x00\x12\'\n\x1dtransition_property_file_path\x18\x02 \x01(\t:\x00\x12$\n\x17transition_matrix_alpha\x18\x03 \x01(\x02:\x031.8')
_CCRFTYPEFUSIONCONFIG = DESCRIPTOR.message_types_by_name['CcrfTypeFusionConfig']
CcrfTypeFusionConfig = _reflection.GeneratedProtocolMessageType('CcrfTypeFusionConfig', (_message.Message,), {'DESCRIPTOR': _CCRFTYPEFUSIONCONFIG, '__module__': 'modules.perception.proto.ccrf_type_fusion_config_pb2'})
_sym_db.RegisterMessage(CcrfTypeFusionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CCRFTYPEFUSIONCONFIG._serialized_start = 84
    _CCRFTYPEFUSIONCONFIG._serialized_end = 227