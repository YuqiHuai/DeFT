"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n modules/map/proto/map_lane.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"\xcb\x01\n\x10LaneBoundaryType\x12\t\n\x01s\x18\x01 \x01(\x01\x122\n\x05types\x18\x02 \x03(\x0e2#.apollo.hdmap.LaneBoundaryType.Type"x\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rDOTTED_YELLOW\x10\x01\x12\x10\n\x0cDOTTED_WHITE\x10\x02\x12\x10\n\x0cSOLID_YELLOW\x10\x03\x12\x0f\n\x0bSOLID_WHITE\x10\x04\x12\x11\n\rDOUBLE_YELLOW\x10\x05\x12\x08\n\x04CURB\x10\x06"\x8a\x01\n\x0cLaneBoundary\x12"\n\x05curve\x18\x01 \x01(\x0b2\x13.apollo.hdmap.Curve\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0f\n\x07virtual\x18\x03 \x01(\x08\x125\n\rboundary_type\x18\x04 \x03(\x0b2\x1e.apollo.hdmap.LaneBoundaryType"1\n\x15LaneSampleAssociation\x12\t\n\x01s\x18\x01 \x01(\x01\x12\r\n\x05width\x18\x02 \x01(\x01"\xee\t\n\x04Lane\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12*\n\rcentral_curve\x18\x02 \x01(\x0b2\x13.apollo.hdmap.Curve\x121\n\rleft_boundary\x18\x03 \x01(\x0b2\x1a.apollo.hdmap.LaneBoundary\x122\n\x0eright_boundary\x18\x04 \x01(\x0b2\x1a.apollo.hdmap.LaneBoundary\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\x13\n\x0bspeed_limit\x18\x06 \x01(\x01\x12$\n\noverlap_id\x18\x07 \x03(\x0b2\x10.apollo.hdmap.Id\x12(\n\x0epredecessor_id\x18\x08 \x03(\x0b2\x10.apollo.hdmap.Id\x12&\n\x0csuccessor_id\x18\t \x03(\x0b2\x10.apollo.hdmap.Id\x127\n\x1dleft_neighbor_forward_lane_id\x18\n \x03(\x0b2\x10.apollo.hdmap.Id\x128\n\x1eright_neighbor_forward_lane_id\x18\x0b \x03(\x0b2\x10.apollo.hdmap.Id\x12)\n\x04type\x18\x0c \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneType\x12)\n\x04turn\x18\r \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneTurn\x127\n\x1dleft_neighbor_reverse_lane_id\x18\x0e \x03(\x0b2\x10.apollo.hdmap.Id\x128\n\x1eright_neighbor_reverse_lane_id\x18\x0f \x03(\x0b2\x10.apollo.hdmap.Id\x12%\n\x0bjunction_id\x18\x10 \x01(\x0b2\x10.apollo.hdmap.Id\x128\n\x0bleft_sample\x18\x11 \x03(\x0b2#.apollo.hdmap.LaneSampleAssociation\x129\n\x0cright_sample\x18\x12 \x03(\x0b2#.apollo.hdmap.LaneSampleAssociation\x123\n\tdirection\x18\x13 \x01(\x0e2 .apollo.hdmap.Lane.LaneDirection\x12=\n\x10left_road_sample\x18\x14 \x03(\x0b2#.apollo.hdmap.LaneSampleAssociation\x12>\n\x11right_road_sample\x18\x15 \x03(\x0b2#.apollo.hdmap.LaneSampleAssociation\x12.\n\x14self_reverse_lane_id\x18\x16 \x03(\x0b2\x10.apollo.hdmap.Id"[\n\x08LaneType\x12\x08\n\x04NONE\x10\x01\x12\x10\n\x0cCITY_DRIVING\x10\x02\x12\n\n\x06BIKING\x10\x03\x12\x0c\n\x08SIDEWALK\x10\x04\x12\x0b\n\x07PARKING\x10\x05\x12\x0c\n\x08SHOULDER\x10\x06"B\n\x08LaneTurn\x12\x0b\n\x07NO_TURN\x10\x01\x12\r\n\tLEFT_TURN\x10\x02\x12\x0e\n\nRIGHT_TURN\x10\x03\x12\n\n\x06U_TURN\x10\x04";\n\rLaneDirection\x12\x0b\n\x07FORWARD\x10\x01\x12\x0c\n\x08BACKWARD\x10\x02\x12\x0f\n\x0bBIDIRECTION\x10\x03')
_LANEBOUNDARYTYPE = DESCRIPTOR.message_types_by_name['LaneBoundaryType']
_LANEBOUNDARY = DESCRIPTOR.message_types_by_name['LaneBoundary']
_LANESAMPLEASSOCIATION = DESCRIPTOR.message_types_by_name['LaneSampleAssociation']
_LANE = DESCRIPTOR.message_types_by_name['Lane']
_LANEBOUNDARYTYPE_TYPE = _LANEBOUNDARYTYPE.enum_types_by_name['Type']
_LANE_LANETYPE = _LANE.enum_types_by_name['LaneType']
_LANE_LANETURN = _LANE.enum_types_by_name['LaneTurn']
_LANE_LANEDIRECTION = _LANE.enum_types_by_name['LaneDirection']
LaneBoundaryType = _reflection.GeneratedProtocolMessageType('LaneBoundaryType', (_message.Message,), {'DESCRIPTOR': _LANEBOUNDARYTYPE, '__module__': 'modules.map.proto.map_lane_pb2'})
_sym_db.RegisterMessage(LaneBoundaryType)
LaneBoundary = _reflection.GeneratedProtocolMessageType('LaneBoundary', (_message.Message,), {'DESCRIPTOR': _LANEBOUNDARY, '__module__': 'modules.map.proto.map_lane_pb2'})
_sym_db.RegisterMessage(LaneBoundary)
LaneSampleAssociation = _reflection.GeneratedProtocolMessageType('LaneSampleAssociation', (_message.Message,), {'DESCRIPTOR': _LANESAMPLEASSOCIATION, '__module__': 'modules.map.proto.map_lane_pb2'})
_sym_db.RegisterMessage(LaneSampleAssociation)
Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), {'DESCRIPTOR': _LANE, '__module__': 'modules.map.proto.map_lane_pb2'})
_sym_db.RegisterMessage(Lane)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANEBOUNDARYTYPE._serialized_start = 121
    _LANEBOUNDARYTYPE._serialized_end = 324
    _LANEBOUNDARYTYPE_TYPE._serialized_start = 204
    _LANEBOUNDARYTYPE_TYPE._serialized_end = 324
    _LANEBOUNDARY._serialized_start = 327
    _LANEBOUNDARY._serialized_end = 465
    _LANESAMPLEASSOCIATION._serialized_start = 467
    _LANESAMPLEASSOCIATION._serialized_end = 516
    _LANE._serialized_start = 519
    _LANE._serialized_end = 1781
    _LANE_LANETYPE._serialized_start = 1561
    _LANE_LANETYPE._serialized_end = 1652
    _LANE_LANETURN._serialized_start = 1654
    _LANE_LANETURN._serialized_end = 1720
    _LANE_LANEDIRECTION._serialized_start = 1722
    _LANE_LANEDIRECTION._serialized_end = 1781