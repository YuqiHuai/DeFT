"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*modules/guardian/proto/guardian_conf.proto\x12\x0fapollo.guardian"\x91\x01\n\x0cGuardianConf\x12\x1e\n\x0fguardian_enable\x18\x01 \x01(\x08:\x05false\x122\n&guardian_cmd_emergency_stop_percentage\x18\x02 \x01(\x01:\x0250\x12-\n!guardian_cmd_soft_stop_percentage\x18\x03 \x01(\x01:\x0225')
_GUARDIANCONF = DESCRIPTOR.message_types_by_name['GuardianConf']
GuardianConf = _reflection.GeneratedProtocolMessageType('GuardianConf', (_message.Message,), {'DESCRIPTOR': _GUARDIANCONF, '__module__': 'modules.guardian.proto.guardian_conf_pb2'})
_sym_db.RegisterMessage(GuardianConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GUARDIANCONF._serialized_start = 64
    _GUARDIANCONF._serialized_end = 209