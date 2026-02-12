"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/perception/proto/perception_ultrasonic.proto\x12\x11apollo.perception\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"|\n\x16ImpendingCollisionEdge\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x0ccone_id_list\x18\x02 \x03(\x05B\x02\x18\x01\x12%\n\x05point\x18\x03 \x03(\x0b2\x16.apollo.common.Point3D\x12\x15\n\rtracking_time\x18\x04 \x01(\x01"\x8d\x01\n\x17ImpendingCollisionEdges\x12K\n\x18impending_collision_edge\x18\x01 \x03(\x0b2).apollo.perception.ImpendingCollisionEdge\x12%\n\x06header\x18\x02 \x01(\x0b2\x15.apollo.common.Header')
_IMPENDINGCOLLISIONEDGE = DESCRIPTOR.message_types_by_name['ImpendingCollisionEdge']
_IMPENDINGCOLLISIONEDGES = DESCRIPTOR.message_types_by_name['ImpendingCollisionEdges']
ImpendingCollisionEdge = _reflection.GeneratedProtocolMessageType('ImpendingCollisionEdge', (_message.Message,), {'DESCRIPTOR': _IMPENDINGCOLLISIONEDGE, '__module__': 'modules.perception.proto.perception_ultrasonic_pb2'})
_sym_db.RegisterMessage(ImpendingCollisionEdge)
ImpendingCollisionEdges = _reflection.GeneratedProtocolMessageType('ImpendingCollisionEdges', (_message.Message,), {'DESCRIPTOR': _IMPENDINGCOLLISIONEDGES, '__module__': 'modules.perception.proto.perception_ultrasonic_pb2'})
_sym_db.RegisterMessage(ImpendingCollisionEdges)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _IMPENDINGCOLLISIONEDGE.fields_by_name['cone_id_list']._options = None
    _IMPENDINGCOLLISIONEDGE.fields_by_name['cone_id_list']._serialized_options = b'\x18\x01'
    _IMPENDINGCOLLISIONEDGE._serialized_start = 147
    _IMPENDINGCOLLISIONEDGE._serialized_end = 271
    _IMPENDINGCOLLISIONEDGES._serialized_start = 274
    _IMPENDINGCOLLISIONEDGES._serialized_end = 415