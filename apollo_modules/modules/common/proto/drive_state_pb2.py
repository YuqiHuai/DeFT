"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/common/proto/drive_state.proto\x12\rapollo.common"\xcd\x01\n\x0cEngageAdvice\x12C\n\x06advice\x18\x01 \x01(\x0e2".apollo.common.EngageAdvice.Advice:\x0fDISALLOW_ENGAGE\x12\x0e\n\x06reason\x18\x02 \x01(\t"h\n\x06Advice\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fDISALLOW_ENGAGE\x10\x01\x12\x13\n\x0fREADY_TO_ENGAGE\x10\x02\x12\x10\n\x0cKEEP_ENGAGED\x10\x03\x12\x15\n\x11PREPARE_DISENGAGE\x10\x04')
_ENGAGEADVICE = DESCRIPTOR.message_types_by_name['EngageAdvice']
_ENGAGEADVICE_ADVICE = _ENGAGEADVICE.enum_types_by_name['Advice']
EngageAdvice = _reflection.GeneratedProtocolMessageType('EngageAdvice', (_message.Message,), {'DESCRIPTOR': _ENGAGEADVICE, '__module__': 'modules.common.proto.drive_state_pb2'})
_sym_db.RegisterMessage(EngageAdvice)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ENGAGEADVICE._serialized_start = 58
    _ENGAGEADVICE._serialized_end = 263
    _ENGAGEADVICE_ADVICE._serialized_start = 159
    _ENGAGEADVICE_ADVICE._serialized_end = 263