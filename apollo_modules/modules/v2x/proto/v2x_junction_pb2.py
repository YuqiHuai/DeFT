"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/v2x/proto/v2x_junction.proto\x12\napollo.v2x\x1a#modules/common/proto/geometry.proto"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\x0c"\x8c\x03\n\x08Junction\x12\x1a\n\x02id\x18\x01 \x01(\x0b2\x0e.apollo.v2x.Id\x12\'\n\x07polygon\x18\x02 \x01(\x0b2\x16.apollo.common.Polygon\x12$\n\x0ccrosswalk_id\x18\x03 \x03(\x0b2\x0e.apollo.v2x.Id\x12"\n\noverlap_id\x18\x04 \x03(\x0b2\x0e.apollo.v2x.Id\x12\x1c\n\x11num_road_segments\x18\x05 \x01(\x05:\x014\x12\x1f\n\x07lane_id\x18\x06 \x03(\x0b2\x0e.apollo.v2x.Id\x12\'\n\x04type\x18\x07 \x01(\x0e2\x19.apollo.v2x.Junction.Type\x120\n\tedge_type\x18\x08 \x03(\x0e2\x1d.apollo.v2x.Junction.EdgeType"0\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02"%\n\x08EdgeType\x12\x0c\n\x08PHYSICAL\x10\x00\x12\x0b\n\x07VIRTUAL\x10\x01')
_ID = DESCRIPTOR.message_types_by_name['Id']
_JUNCTION = DESCRIPTOR.message_types_by_name['Junction']
_JUNCTION_TYPE = _JUNCTION.enum_types_by_name['Type']
_JUNCTION_EDGETYPE = _JUNCTION.enum_types_by_name['EdgeType']
Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {'DESCRIPTOR': _ID, '__module__': 'modules.v2x.proto.v2x_junction_pb2'})
_sym_db.RegisterMessage(Id)
Junction = _reflection.GeneratedProtocolMessageType('Junction', (_message.Message,), {'DESCRIPTOR': _JUNCTION, '__module__': 'modules.v2x.proto.v2x_junction_pb2'})
_sym_db.RegisterMessage(Junction)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ID._serialized_start = 89
    _ID._serialized_end = 105
    _JUNCTION._serialized_start = 108
    _JUNCTION._serialized_end = 504
    _JUNCTION_TYPE._serialized_start = 417
    _JUNCTION_TYPE._serialized_end = 465
    _JUNCTION_EDGETYPE._serialized_start = 467
    _JUNCTION_EDGETYPE._serialized_end = 504