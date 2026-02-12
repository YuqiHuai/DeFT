"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/v2x/proto/v2x_traffic_light_policy.proto\x12\napollo.v2x""\n\nPosition2D\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01"\x92\x01\n\nConnection\x12;\n\x16allow_driving_behavior\x18\x01 \x01(\x0e2\x1b.apollo.v2x.Connection.Type\x12\x10\n\x08phase_id\x18\x02 \x01(\x05"5\n\x04Type\x12\x0c\n\x08STRAIGHT\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\n\n\x06U_TURN\x10\x03"u\n\x04Lane\x12\x0f\n\x07lane_id\x18\x01 \x01(\x05\x12/\n\x0fposition_offset\x18\x02 \x03(\x0b2\x16.apollo.v2x.Position2D\x12+\n\x0bconnections\x18\x03 \x03(\x0b2\x16.apollo.v2x.Connection"i\n\x04Road\x12\x18\n\x10upstream_node_id\x18\x01 \x01(\x05\x12&\n\x06points\x18\x02 \x01(\x0b2\x16.apollo.v2x.Position2D\x12\x1f\n\x05lanes\x18\x03 \x03(\x0b2\x10.apollo.v2x.Lane"e\n\x0cIntersection\x12\n\n\x02id\x18\x01 \x01(\x05\x12(\n\x08position\x18\x02 \x01(\x0b2\x16.apollo.v2x.Position2D\x12\x1f\n\x05roads\x18\x03 \x03(\x0b2\x10.apollo.v2x.Road"[\n\x03Map\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x0f\n\x07msg_cnt\x18\x02 \x01(\x05\x12/\n\rintersections\x18\x03 \x03(\x0b2\x18.apollo.v2x.Intersection"\xad\x01\n\x05Phase\x12\n\n\x02id\x18\x01 \x01(\x05\x12&\n\x05color\x18\x02 \x01(\x0e2\x17.apollo.v2x.Phase.Color\x12\x1e\n\x16color_remaining_time_s\x18\x03 \x01(\x05"P\n\x05Color\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\t\n\x05BLACK\x10\x04\x12\x0f\n\x0bFLASH_GREEN\x10\x05"x\n\x11IntersectionState\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\x12!\n\x06Phases\x18\x02 \x03(\x0b2\x11.apollo.v2x.Phase\x12\x0b\n\x03moy\x18\x03 \x01(\x05\x12\x1a\n\x12time_stamp_dsecond\x18\x04 \x01(\x05"a\n\x04Spat\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x0f\n\x07msg_cnt\x18\x02 \x01(\x05\x124\n\rintersections\x18\x03 \x03(\x0b2\x1d.apollo.v2x.IntersectionState"J\n\nPolicyData\x12\x1c\n\x03map\x18\x01 \x01(\x0b2\x0f.apollo.v2x.Map\x12\x1e\n\x04spat\x18\x02 \x01(\x0b2\x10.apollo.v2x.Spat')
_POSITION2D = DESCRIPTOR.message_types_by_name['Position2D']
_CONNECTION = DESCRIPTOR.message_types_by_name['Connection']
_LANE = DESCRIPTOR.message_types_by_name['Lane']
_ROAD = DESCRIPTOR.message_types_by_name['Road']
_INTERSECTION = DESCRIPTOR.message_types_by_name['Intersection']
_MAP = DESCRIPTOR.message_types_by_name['Map']
_PHASE = DESCRIPTOR.message_types_by_name['Phase']
_INTERSECTIONSTATE = DESCRIPTOR.message_types_by_name['IntersectionState']
_SPAT = DESCRIPTOR.message_types_by_name['Spat']
_POLICYDATA = DESCRIPTOR.message_types_by_name['PolicyData']
_CONNECTION_TYPE = _CONNECTION.enum_types_by_name['Type']
_PHASE_COLOR = _PHASE.enum_types_by_name['Color']
Position2D = _reflection.GeneratedProtocolMessageType('Position2D', (_message.Message,), {'DESCRIPTOR': _POSITION2D, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Position2D)
Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {'DESCRIPTOR': _CONNECTION, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Connection)
Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), {'DESCRIPTOR': _LANE, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Lane)
Road = _reflection.GeneratedProtocolMessageType('Road', (_message.Message,), {'DESCRIPTOR': _ROAD, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Road)
Intersection = _reflection.GeneratedProtocolMessageType('Intersection', (_message.Message,), {'DESCRIPTOR': _INTERSECTION, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Intersection)
Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {'DESCRIPTOR': _MAP, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Map)
Phase = _reflection.GeneratedProtocolMessageType('Phase', (_message.Message,), {'DESCRIPTOR': _PHASE, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Phase)
IntersectionState = _reflection.GeneratedProtocolMessageType('IntersectionState', (_message.Message,), {'DESCRIPTOR': _INTERSECTIONSTATE, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(IntersectionState)
Spat = _reflection.GeneratedProtocolMessageType('Spat', (_message.Message,), {'DESCRIPTOR': _SPAT, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(Spat)
PolicyData = _reflection.GeneratedProtocolMessageType('PolicyData', (_message.Message,), {'DESCRIPTOR': _POLICYDATA, '__module__': 'modules.v2x.proto.v2x_traffic_light_policy_pb2'})
_sym_db.RegisterMessage(PolicyData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POSITION2D._serialized_start = 64
    _POSITION2D._serialized_end = 98
    _CONNECTION._serialized_start = 101
    _CONNECTION._serialized_end = 247
    _CONNECTION_TYPE._serialized_start = 194
    _CONNECTION_TYPE._serialized_end = 247
    _LANE._serialized_start = 249
    _LANE._serialized_end = 366
    _ROAD._serialized_start = 368
    _ROAD._serialized_end = 473
    _INTERSECTION._serialized_start = 475
    _INTERSECTION._serialized_end = 576
    _MAP._serialized_start = 578
    _MAP._serialized_end = 669
    _PHASE._serialized_start = 672
    _PHASE._serialized_end = 845
    _PHASE_COLOR._serialized_start = 765
    _PHASE_COLOR._serialized_end = 845
    _INTERSECTIONSTATE._serialized_start = 847
    _INTERSECTIONSTATE._serialized_end = 967
    _SPAT._serialized_start = 969
    _SPAT._serialized_end = 1066
    _POLICYDATA._serialized_start = 1068
    _POLICYDATA._serialized_end = 1142