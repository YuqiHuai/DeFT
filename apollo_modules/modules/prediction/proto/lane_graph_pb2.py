"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.map.proto import map_lane_pb2 as modules_dot_map_dot_proto_dot_map__lane__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/prediction/proto/lane_graph.proto\x12\x11apollo.prediction\x1a#modules/common/proto/geometry.proto\x1a$modules/common/proto/pnc_point.proto\x1a modules/map/proto/map_lane.proto"\xc4\x02\n\tLanePoint\x12(\n\x08position\x18\x01 \x01(\x0b2\x16.apollo.common.Point3D\x12\x12\n\x07heading\x18\x02 \x01(\x01:\x010\x12\x10\n\x05width\x18\x03 \x01(\x01:\x010\x12\x15\n\nrelative_s\x18\x04 \x01(\x01:\x010\x12\x15\n\nrelative_l\x18\x05 \x01(\x01:\x010\x12\x15\n\nangle_diff\x18\x06 \x01(\x01:\x010\x12\x10\n\x05kappa\x18\x07 \x01(\x01:\x010\x12@\n\rscenario_type\x18\x08 \x01(\x0e2).apollo.prediction.LanePoint.ScenarioType\x12\x13\n\x0bspeed_limit\x18\t \x01(\x01"9\n\x0cScenarioType\x12\x0e\n\nURBAN_ROAD\x10\x00\x12\x0c\n\x08JUNCTION\x10\x01\x12\x0b\n\x07HIGHWAY\x10\x02"\xdb\x01\n\x0bLaneSegment\x12\x0f\n\x07lane_id\x18\x01 \x01(\t\x12\x12\n\x07start_s\x18\x02 \x01(\x01:\x010\x12\x10\n\x05end_s\x18\x03 \x01(\x01:\x010\x12\x19\n\x0elane_turn_type\x18\x04 \x01(\r:\x010\x120\n\nlane_point\x18\x05 \x03(\x0b2\x1c.apollo.prediction.LanePoint\x12\x10\n\x05adc_s\x18\x07 \x01(\x01:\x010\x12\x1d\n\x12adc_lane_point_idx\x18\x08 \x01(\x05:\x010\x12\x17\n\x0ctotal_length\x18\x06 \x01(\x01:\x010"2\n\x0eNearbyObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01s\x18\x02 \x01(\x01\x12\t\n\x01l\x18\x03 \x01(\x01"Z\n\x08StopSign\x12\x14\n\x0cstop_sign_id\x18\x01 \x01(\t\x12\x0f\n\x07lane_id\x18\x02 \x01(\t\x12\x0e\n\x06lane_s\x18\x03 \x01(\x01\x12\x17\n\x0flane_sequence_s\x18\x04 \x01(\x01"\xff\x08\n\x0cLaneSequence\x12\x18\n\x10lane_sequence_id\x18\x01 \x01(\x05\x124\n\x0clane_segment\x18\x02 \x03(\x0b2\x1e.apollo.prediction.LaneSegment\x12\x1f\n\x14adc_lane_segment_idx\x18\x17 \x01(\x05:\x010\x12,\n\npath_point\x18\x08 \x03(\x0b2\x18.apollo.common.PathPoint\x12.\n\tlane_type\x18\x16 \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneType\x12\x0e\n\x06lane_s\x18\x11 \x01(\x01\x12\x0e\n\x06lane_l\x18\x12 \x01(\x01\x12\x17\n\x0fvehicle_on_lane\x18\n \x01(\x08\x12:\n\x0fnearby_obstacle\x18\x03 \x03(\x0b2!.apollo.prediction.NearbyObstacle\x12.\n\tstop_sign\x18\x14 \x01(\x0b2\x1b.apollo.prediction.StopSign\x12\x14\n\x0cright_of_way\x18\x15 \x01(\x05\x12:\n\x08features\x18\x04 \x01(\x0b2(.apollo.prediction.LaneSequence.Features\x12\x10\n\x05label\x18\x05 \x01(\x05:\x010\x12\x16\n\x0bprobability\x18\x06 \x01(\x01:\x010\x12\x17\n\x0cacceleration\x18\x07 \x01(\x01:\x010\x12\x1b\n\x13time_to_lane_center\x18\x10 \x01(\x01\x12\x19\n\x11time_to_lane_edge\x18\x13 \x01(\x01\x12C\n\rbehavior_type\x18\t \x01(\x0e2,.apollo.prediction.LaneSequence.BehaviorType\x125\n\x0fcurr_lane_point\x18\x0b \x03(\x0b2\x1c.apollo.prediction.LanePoint\x129\n\x13left_neighbor_point\x18\x0c \x03(\x0b2\x1c.apollo.prediction.LanePoint\x12:\n\x14right_neighbor_point\x18\r \x03(\x0b2\x1c.apollo.prediction.LanePoint\x12?\n\x14left_nearby_obstacle\x18\x0e \x03(\x0b2!.apollo.prediction.NearbyObstacle\x12@\n\x15right_nearby_obstacle\x18\x0f \x03(\x0b2!.apollo.prediction.NearbyObstacle\x1a \n\x08Features\x12\x14\n\x0cmlp_features\x18\x01 \x03(\x01"\x95\x01\n\x0cBehaviorType\x12\x11\n\rNOT_GOTO_LANE\x10\x01\x12\x12\n\x0eCONSTANT_SPEED\x10\x02\x12\x16\n\x12SMALL_ACCELERATION\x10\x03\x12\x16\n\x12LARGE_ACCELERATION\x10\x04\x12\x16\n\x12SMALL_DECELERATION\x10\x05\x12\x16\n\x12LARGE_DECELERATION\x10\x06"C\n\tLaneGraph\x126\n\rlane_sequence\x18\x01 \x03(\x0b2\x1f.apollo.prediction.LaneSequence"T\n\x0cLaneObstacle\x12\x13\n\x0bobstacle_id\x18\x01 \x01(\x05\x12\x0f\n\x07lane_id\x18\x02 \x01(\t\x12\x0e\n\x06lane_s\x18\x03 \x01(\x01\x12\x0e\n\x06lane_l\x18\x04 \x01(\x01')
_LANEPOINT = DESCRIPTOR.message_types_by_name['LanePoint']
_LANESEGMENT = DESCRIPTOR.message_types_by_name['LaneSegment']
_NEARBYOBSTACLE = DESCRIPTOR.message_types_by_name['NearbyObstacle']
_STOPSIGN = DESCRIPTOR.message_types_by_name['StopSign']
_LANESEQUENCE = DESCRIPTOR.message_types_by_name['LaneSequence']
_LANESEQUENCE_FEATURES = _LANESEQUENCE.nested_types_by_name['Features']
_LANEGRAPH = DESCRIPTOR.message_types_by_name['LaneGraph']
_LANEOBSTACLE = DESCRIPTOR.message_types_by_name['LaneObstacle']
_LANEPOINT_SCENARIOTYPE = _LANEPOINT.enum_types_by_name['ScenarioType']
_LANESEQUENCE_BEHAVIORTYPE = _LANESEQUENCE.enum_types_by_name['BehaviorType']
LanePoint = _reflection.GeneratedProtocolMessageType('LanePoint', (_message.Message,), {'DESCRIPTOR': _LANEPOINT, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(LanePoint)
LaneSegment = _reflection.GeneratedProtocolMessageType('LaneSegment', (_message.Message,), {'DESCRIPTOR': _LANESEGMENT, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(LaneSegment)
NearbyObstacle = _reflection.GeneratedProtocolMessageType('NearbyObstacle', (_message.Message,), {'DESCRIPTOR': _NEARBYOBSTACLE, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(NearbyObstacle)
StopSign = _reflection.GeneratedProtocolMessageType('StopSign', (_message.Message,), {'DESCRIPTOR': _STOPSIGN, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(StopSign)
LaneSequence = _reflection.GeneratedProtocolMessageType('LaneSequence', (_message.Message,), {'Features': _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {'DESCRIPTOR': _LANESEQUENCE_FEATURES, '__module__': 'modules.prediction.proto.lane_graph_pb2'}), 'DESCRIPTOR': _LANESEQUENCE, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(LaneSequence)
_sym_db.RegisterMessage(LaneSequence.Features)
LaneGraph = _reflection.GeneratedProtocolMessageType('LaneGraph', (_message.Message,), {'DESCRIPTOR': _LANEGRAPH, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(LaneGraph)
LaneObstacle = _reflection.GeneratedProtocolMessageType('LaneObstacle', (_message.Message,), {'DESCRIPTOR': _LANEOBSTACLE, '__module__': 'modules.prediction.proto.lane_graph_pb2'})
_sym_db.RegisterMessage(LaneObstacle)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANEPOINT._serialized_start = 174
    _LANEPOINT._serialized_end = 498
    _LANEPOINT_SCENARIOTYPE._serialized_start = 441
    _LANEPOINT_SCENARIOTYPE._serialized_end = 498
    _LANESEGMENT._serialized_start = 501
    _LANESEGMENT._serialized_end = 720
    _NEARBYOBSTACLE._serialized_start = 722
    _NEARBYOBSTACLE._serialized_end = 772
    _STOPSIGN._serialized_start = 774
    _STOPSIGN._serialized_end = 864
    _LANESEQUENCE._serialized_start = 867
    _LANESEQUENCE._serialized_end = 2018
    _LANESEQUENCE_FEATURES._serialized_start = 1834
    _LANESEQUENCE_FEATURES._serialized_end = 1866
    _LANESEQUENCE_BEHAVIORTYPE._serialized_start = 1869
    _LANESEQUENCE_BEHAVIORTYPE._serialized_end = 2018
    _LANEGRAPH._serialized_start = 2020
    _LANEGRAPH._serialized_end = 2087
    _LANEOBSTACLE._serialized_start = 2089
    _LANEOBSTACLE._serialized_end = 2173