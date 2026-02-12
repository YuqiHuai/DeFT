"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n modules/map/proto/map_road.proto\x12\x0capollo.hdmap\x1a$modules/map/proto/map_geometry.proto\x1a\x1emodules/map/proto/map_id.proto"\xa9\x01\n\x0cBoundaryEdge\x12"\n\x05curve\x18\x01 \x01(\x0b2\x13.apollo.hdmap.Curve\x12-\n\x04type\x18\x02 \x01(\x0e2\x1f.apollo.hdmap.BoundaryEdge.Type"F\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x11\n\rLEFT_BOUNDARY\x10\x02\x12\x12\n\x0eRIGHT_BOUNDARY\x10\x03";\n\x0fBoundaryPolygon\x12(\n\x04edge\x18\x01 \x03(\x0b2\x1a.apollo.hdmap.BoundaryEdge"q\n\x0cRoadBoundary\x124\n\router_polygon\x18\x01 \x01(\x0b2\x1d.apollo.hdmap.BoundaryPolygon\x12+\n\x04hole\x18\x02 \x03(\x0b2\x1d.apollo.hdmap.BoundaryPolygon"d\n\x0fRoadROIBoundary\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x123\n\x0froad_boundaries\x18\x02 \x03(\x0b2\x1a.apollo.hdmap.RoadBoundary"|\n\x0bRoadSection\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12!\n\x07lane_id\x18\x02 \x03(\x0b2\x10.apollo.hdmap.Id\x12,\n\x08boundary\x18\x03 \x01(\x0b2\x1a.apollo.hdmap.RoadBoundary"\xd9\x01\n\x04Road\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12*\n\x07section\x18\x02 \x03(\x0b2\x19.apollo.hdmap.RoadSection\x12%\n\x0bjunction_id\x18\x03 \x01(\x0b2\x10.apollo.hdmap.Id\x12%\n\x04type\x18\x04 \x01(\x0e2\x17.apollo.hdmap.Road.Type"9\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07HIGHWAY\x10\x01\x12\r\n\tCITY_ROAD\x10\x02\x12\x08\n\x04PARK\x10\x03')
_BOUNDARYEDGE = DESCRIPTOR.message_types_by_name['BoundaryEdge']
_BOUNDARYPOLYGON = DESCRIPTOR.message_types_by_name['BoundaryPolygon']
_ROADBOUNDARY = DESCRIPTOR.message_types_by_name['RoadBoundary']
_ROADROIBOUNDARY = DESCRIPTOR.message_types_by_name['RoadROIBoundary']
_ROADSECTION = DESCRIPTOR.message_types_by_name['RoadSection']
_ROAD = DESCRIPTOR.message_types_by_name['Road']
_BOUNDARYEDGE_TYPE = _BOUNDARYEDGE.enum_types_by_name['Type']
_ROAD_TYPE = _ROAD.enum_types_by_name['Type']
BoundaryEdge = _reflection.GeneratedProtocolMessageType('BoundaryEdge', (_message.Message,), {'DESCRIPTOR': _BOUNDARYEDGE, '__module__': 'modules.map.proto.map_road_pb2'})
_sym_db.RegisterMessage(BoundaryEdge)
BoundaryPolygon = _reflection.GeneratedProtocolMessageType('BoundaryPolygon', (_message.Message,), {'DESCRIPTOR': _BOUNDARYPOLYGON, '__module__': 'modules.map.proto.map_road_pb2'})
_sym_db.RegisterMessage(BoundaryPolygon)
RoadBoundary = _reflection.GeneratedProtocolMessageType('RoadBoundary', (_message.Message,), {'DESCRIPTOR': _ROADBOUNDARY, '__module__': 'modules.map.proto.map_road_pb2'})
_sym_db.RegisterMessage(RoadBoundary)
RoadROIBoundary = _reflection.GeneratedProtocolMessageType('RoadROIBoundary', (_message.Message,), {'DESCRIPTOR': _ROADROIBOUNDARY, '__module__': 'modules.map.proto.map_road_pb2'})
_sym_db.RegisterMessage(RoadROIBoundary)
RoadSection = _reflection.GeneratedProtocolMessageType('RoadSection', (_message.Message,), {'DESCRIPTOR': _ROADSECTION, '__module__': 'modules.map.proto.map_road_pb2'})
_sym_db.RegisterMessage(RoadSection)
Road = _reflection.GeneratedProtocolMessageType('Road', (_message.Message,), {'DESCRIPTOR': _ROAD, '__module__': 'modules.map.proto.map_road_pb2'})
_sym_db.RegisterMessage(Road)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BOUNDARYEDGE._serialized_start = 121
    _BOUNDARYEDGE._serialized_end = 290
    _BOUNDARYEDGE_TYPE._serialized_start = 220
    _BOUNDARYEDGE_TYPE._serialized_end = 290
    _BOUNDARYPOLYGON._serialized_start = 292
    _BOUNDARYPOLYGON._serialized_end = 351
    _ROADBOUNDARY._serialized_start = 353
    _ROADBOUNDARY._serialized_end = 466
    _ROADROIBOUNDARY._serialized_start = 468
    _ROADROIBOUNDARY._serialized_end = 568
    _ROADSECTION._serialized_start = 570
    _ROADSECTION._serialized_end = 694
    _ROAD._serialized_start = 697
    _ROAD._serialized_end = 914
    _ROAD_TYPE._serialized_start = 857
    _ROAD_TYPE._serialized_end = 914