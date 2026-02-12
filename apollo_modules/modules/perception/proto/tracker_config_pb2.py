"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/perception/proto/tracker_config.proto"R\n\rMatcherConfig\x12\x1f\n\x12max_match_distance\x18\x01 \x01(\x01:\x032.5\x12 \n\x14bound_match_distance\x18\x02 \x01(\x01:\x0210')
_MATCHERCONFIG = DESCRIPTOR.message_types_by_name['MatcherConfig']
MatcherConfig = _reflection.GeneratedProtocolMessageType('MatcherConfig', (_message.Message,), {'DESCRIPTOR': _MATCHERCONFIG, '__module__': 'modules.perception.proto.tracker_config_pb2'})
_sym_db.RegisterMessage(MatcherConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MATCHERCONFIG._serialized_start = 49
    _MATCHERCONFIG._serialized_end = 131