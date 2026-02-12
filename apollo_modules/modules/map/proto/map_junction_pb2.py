"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/map/proto/map_junction.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"\xff\x01\n\x08Junction\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x12)\n\x04type\x18\x04 \x01(\x0e2\x1b.apollo.hdmap.Junction.Type"\\\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02\x12\r\n\tFORK_ROAD\x10\x03\x12\r\n\tMAIN_SIDE\x10\x04\x12\x0c\n\x08DEAD_END\x10\x05')
_JUNCTION = DESCRIPTOR.message_types_by_name['Junction']
_JUNCTION_TYPE = _JUNCTION.enum_types_by_name['Type']
Junction = _reflection.GeneratedProtocolMessageType('Junction', (_message.Message,), {'DESCRIPTOR': _JUNCTION, '__module__': 'modules.map.proto.map_junction_pb2'})
_sym_db.RegisterMessage(Junction)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _JUNCTION._serialized_start = 125
    _JUNCTION._serialized_end = 380
    _JUNCTION_TYPE._serialized_start = 288
    _JUNCTION_TYPE._serialized_end = 380