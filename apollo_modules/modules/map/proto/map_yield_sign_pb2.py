"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/map/proto/map_yield_sign.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"w\n\tYieldSign\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\tstop_line\x18\x02 \x03(\x0b2\x13.apollo.hdmap.Curve\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id')
_YIELDSIGN = DESCRIPTOR.message_types_by_name['YieldSign']
YieldSign = _reflection.GeneratedProtocolMessageType('YieldSign', (_message.Message,), {'DESCRIPTOR': _YIELDSIGN, '__module__': 'modules.map.proto.map_yield_sign_pb2'})
_sym_db.RegisterMessage(YieldSign)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _YIELDSIGN._serialized_start = 126
    _YIELDSIGN._serialized_end = 245