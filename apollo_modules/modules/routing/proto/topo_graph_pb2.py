"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/routing/proto/topo_graph.proto\x12\x0eapollo.routing\x1a$modules/map/proto/map_geometry.proto"\x17\n\nCurvePoint\x12\t\n\x01s\x18\x01 \x01(\x01"`\n\nCurveRange\x12)\n\x05start\x18\x01 \x01(\x0b2\x1a.apollo.routing.CurvePoint\x12\'\n\x03end\x18\x02 \x01(\x0b2\x1a.apollo.routing.CurvePoint"\xe9\x01\n\x04Node\x12\x0f\n\x07lane_id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12,\n\x08left_out\x18\x03 \x03(\x0b2\x1a.apollo.routing.CurveRange\x12-\n\tright_out\x18\x04 \x03(\x0b2\x1a.apollo.routing.CurveRange\x12\x0c\n\x04cost\x18\x05 \x01(\x01\x12*\n\rcentral_curve\x18\x06 \x01(\x0b2\x13.apollo.hdmap.Curve\x12\x18\n\nis_virtual\x18\x07 \x01(\x08:\x04true\x12\x0f\n\x07road_id\x18\x08 \x01(\t"\xad\x01\n\x04Edge\x12\x14\n\x0cfrom_lane_id\x18\x01 \x01(\t\x12\x12\n\nto_lane_id\x18\x02 \x01(\t\x12\x0c\n\x04cost\x18\x03 \x01(\x01\x12:\n\x0edirection_type\x18\x04 \x01(\x0e2".apollo.routing.Edge.DirectionType"1\n\rDirectionType\x12\x0b\n\x07FORWARD\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02"~\n\x05Graph\x12\x15\n\rhdmap_version\x18\x01 \x01(\t\x12\x16\n\x0ehdmap_district\x18\x02 \x01(\t\x12"\n\x04node\x18\x03 \x03(\x0b2\x14.apollo.routing.Node\x12"\n\x04edge\x18\x04 \x03(\x0b2\x14.apollo.routing.Edge')
_CURVEPOINT = DESCRIPTOR.message_types_by_name['CurvePoint']
_CURVERANGE = DESCRIPTOR.message_types_by_name['CurveRange']
_NODE = DESCRIPTOR.message_types_by_name['Node']
_EDGE = DESCRIPTOR.message_types_by_name['Edge']
_GRAPH = DESCRIPTOR.message_types_by_name['Graph']
_EDGE_DIRECTIONTYPE = _EDGE.enum_types_by_name['DirectionType']
CurvePoint = _reflection.GeneratedProtocolMessageType('CurvePoint', (_message.Message,), {'DESCRIPTOR': _CURVEPOINT, '__module__': 'modules.routing.proto.topo_graph_pb2'})
_sym_db.RegisterMessage(CurvePoint)
CurveRange = _reflection.GeneratedProtocolMessageType('CurveRange', (_message.Message,), {'DESCRIPTOR': _CURVERANGE, '__module__': 'modules.routing.proto.topo_graph_pb2'})
_sym_db.RegisterMessage(CurveRange)
Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {'DESCRIPTOR': _NODE, '__module__': 'modules.routing.proto.topo_graph_pb2'})
_sym_db.RegisterMessage(Node)
Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), {'DESCRIPTOR': _EDGE, '__module__': 'modules.routing.proto.topo_graph_pb2'})
_sym_db.RegisterMessage(Edge)
Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), {'DESCRIPTOR': _GRAPH, '__module__': 'modules.routing.proto.topo_graph_pb2'})
_sym_db.RegisterMessage(Graph)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CURVEPOINT._serialized_start = 96
    _CURVEPOINT._serialized_end = 119
    _CURVERANGE._serialized_start = 121
    _CURVERANGE._serialized_end = 217
    _NODE._serialized_start = 220
    _NODE._serialized_end = 453
    _EDGE._serialized_start = 456
    _EDGE._serialized_end = 629
    _EDGE_DIRECTIONTYPE._serialized_start = 580
    _EDGE_DIRECTIONTYPE._serialized_end = 629
    _GRAPH._serialized_start = 631
    _GRAPH._serialized_end = 757