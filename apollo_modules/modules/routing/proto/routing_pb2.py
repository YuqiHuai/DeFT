"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import error_code_pb2 as modules_dot_common_dot_proto_dot_error__code__pb2
from ....modules.map.proto import map_parking_space_pb2 as modules_dot_map_dot_proto_dot_map__parking__space__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/routing/proto/routing.proto\x12\x0eapollo.routing\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\x1a%modules/common/proto/error_code.proto\x1a)modules/map/proto/map_parking_space.proto\x1a$modules/map/proto/map_geometry.proto"]\n\x0cLaneWaypoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\x01\x12%\n\x04pose\x18\x03 \x01(\x0b2\x17.apollo.common.PointENU\x12\x0f\n\x07heading\x18\x04 \x01(\x01"9\n\x0bLaneSegment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07start_s\x18\x02 \x01(\x01\x12\r\n\x05end_s\x18\x03 \x01(\x01"\xc2\x01\n\x0bParkingInfo\x12\x18\n\x10parking_space_id\x18\x01 \x01(\t\x12.\n\rparking_point\x18\x02 \x01(\x0b2\x17.apollo.common.PointENU\x12<\n\x12parking_space_type\x18\x03 \x01(\x0e2 .apollo.routing.ParkingSpaceType\x12+\n\x0ccorner_point\x18\x04 \x01(\x0b2\x15.apollo.hdmap.Polygon"\x7f\n\x0bDeadEndInfo\x12A\n\x15dead_end_routing_type\x18\x01 \x01(\x0e2".apollo.routing.DeadEndRoutingType\x12-\n\x0ctarget_point\x18\x02 \x01(\x0b2\x17.apollo.common.PointENU"\xef\x02\n\x0eRoutingRequest\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12.\n\x08waypoint\x18\x02 \x03(\x0b2\x1c.apollo.routing.LaneWaypoint\x125\n\x10blacklisted_lane\x18\x03 \x03(\x0b2\x1b.apollo.routing.LaneSegment\x12\x18\n\x10blacklisted_road\x18\x04 \x03(\t\x12\x17\n\tbroadcast\x18\x05 \x01(\x08:\x04true\x125\n\rparking_space\x18\x06 \x01(\x0b2\x1a.apollo.hdmap.ParkingSpaceB\x02\x18\x01\x121\n\x0cparking_info\x18\x07 \x01(\x0b2\x1b.apollo.routing.ParkingInfo\x122\n\rdead_end_info\x18\x08 \x01(\x0b2\x1b.apollo.routing.DeadEndInfo"\x1f\n\x0bMeasurement\x12\x10\n\x08distance\x18\x01 \x01(\x01"\x8c\x01\n\x07Passage\x12,\n\x07segment\x18\x01 \x03(\x0b2\x1b.apollo.routing.LaneSegment\x12\x10\n\x08can_exit\x18\x02 \x01(\x08\x12A\n\x10change_lane_type\x18\x03 \x01(\x0e2\x1e.apollo.routing.ChangeLaneType:\x07FORWARD"C\n\x0bRoadSegment\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x07passage\x18\x02 \x03(\x0b2\x17.apollo.routing.Passage"\x8c\x02\n\x0fRoutingResponse\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12)\n\x04road\x18\x02 \x03(\x0b2\x1b.apollo.routing.RoadSegment\x120\n\x0bmeasurement\x18\x03 \x01(\x0b2\x1b.apollo.routing.Measurement\x127\n\x0frouting_request\x18\x04 \x01(\x0b2\x1e.apollo.routing.RoutingRequest\x12\x13\n\x0bmap_version\x18\x05 \x01(\x0c\x12\'\n\x06status\x18\x06 \x01(\x0b2\x17.apollo.common.StatusPb*;\n\x10ParkingSpaceType\x12\x11\n\rVERTICAL_PLOT\x10\x00\x12\x14\n\x10PARALLEL_PARKING\x10\x01*H\n\x12DeadEndRoutingType\x12\x11\n\rROUTING_OTHER\x10\x00\x12\x0e\n\nROUTING_IN\x10\x01\x12\x0f\n\x0bROUTING_OUT\x10\x02*2\n\x0eChangeLaneType\x12\x0b\n\x07FORWARD\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02')
_PARKINGSPACETYPE = DESCRIPTOR.enum_types_by_name['ParkingSpaceType']
ParkingSpaceType = enum_type_wrapper.EnumTypeWrapper(_PARKINGSPACETYPE)
_DEADENDROUTINGTYPE = DESCRIPTOR.enum_types_by_name['DeadEndRoutingType']
DeadEndRoutingType = enum_type_wrapper.EnumTypeWrapper(_DEADENDROUTINGTYPE)
_CHANGELANETYPE = DESCRIPTOR.enum_types_by_name['ChangeLaneType']
ChangeLaneType = enum_type_wrapper.EnumTypeWrapper(_CHANGELANETYPE)
VERTICAL_PLOT = 0
PARALLEL_PARKING = 1
ROUTING_OTHER = 0
ROUTING_IN = 1
ROUTING_OUT = 2
FORWARD = 0
LEFT = 1
RIGHT = 2
_LANEWAYPOINT = DESCRIPTOR.message_types_by_name['LaneWaypoint']
_LANESEGMENT = DESCRIPTOR.message_types_by_name['LaneSegment']
_PARKINGINFO = DESCRIPTOR.message_types_by_name['ParkingInfo']
_DEADENDINFO = DESCRIPTOR.message_types_by_name['DeadEndInfo']
_ROUTINGREQUEST = DESCRIPTOR.message_types_by_name['RoutingRequest']
_MEASUREMENT = DESCRIPTOR.message_types_by_name['Measurement']
_PASSAGE = DESCRIPTOR.message_types_by_name['Passage']
_ROADSEGMENT = DESCRIPTOR.message_types_by_name['RoadSegment']
_ROUTINGRESPONSE = DESCRIPTOR.message_types_by_name['RoutingResponse']
LaneWaypoint = _reflection.GeneratedProtocolMessageType('LaneWaypoint', (_message.Message,), {'DESCRIPTOR': _LANEWAYPOINT, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(LaneWaypoint)
LaneSegment = _reflection.GeneratedProtocolMessageType('LaneSegment', (_message.Message,), {'DESCRIPTOR': _LANESEGMENT, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(LaneSegment)
ParkingInfo = _reflection.GeneratedProtocolMessageType('ParkingInfo', (_message.Message,), {'DESCRIPTOR': _PARKINGINFO, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(ParkingInfo)
DeadEndInfo = _reflection.GeneratedProtocolMessageType('DeadEndInfo', (_message.Message,), {'DESCRIPTOR': _DEADENDINFO, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(DeadEndInfo)
RoutingRequest = _reflection.GeneratedProtocolMessageType('RoutingRequest', (_message.Message,), {'DESCRIPTOR': _ROUTINGREQUEST, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(RoutingRequest)
Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), {'DESCRIPTOR': _MEASUREMENT, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(Measurement)
Passage = _reflection.GeneratedProtocolMessageType('Passage', (_message.Message,), {'DESCRIPTOR': _PASSAGE, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(Passage)
RoadSegment = _reflection.GeneratedProtocolMessageType('RoadSegment', (_message.Message,), {'DESCRIPTOR': _ROADSEGMENT, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(RoadSegment)
RoutingResponse = _reflection.GeneratedProtocolMessageType('RoutingResponse', (_message.Message,), {'DESCRIPTOR': _ROUTINGRESPONSE, '__module__': 'modules.routing.proto.routing_pb2'})
_sym_db.RegisterMessage(RoutingResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ROUTINGREQUEST.fields_by_name['parking_space']._options = None
    _ROUTINGREQUEST.fields_by_name['parking_space']._serialized_options = b'\x18\x01'
    _PARKINGSPACETYPE._serialized_start = 1613
    _PARKINGSPACETYPE._serialized_end = 1672
    _DEADENDROUTINGTYPE._serialized_start = 1674
    _DEADENDROUTINGTYPE._serialized_end = 1746
    _CHANGELANETYPE._serialized_start = 1748
    _CHANGELANETYPE._serialized_end = 1798
    _LANEWAYPOINT._serialized_start = 247
    _LANEWAYPOINT._serialized_end = 340
    _LANESEGMENT._serialized_start = 342
    _LANESEGMENT._serialized_end = 399
    _PARKINGINFO._serialized_start = 402
    _PARKINGINFO._serialized_end = 596
    _DEADENDINFO._serialized_start = 598
    _DEADENDINFO._serialized_end = 725
    _ROUTINGREQUEST._serialized_start = 728
    _ROUTINGREQUEST._serialized_end = 1095
    _MEASUREMENT._serialized_start = 1097
    _MEASUREMENT._serialized_end = 1128
    _PASSAGE._serialized_start = 1131
    _PASSAGE._serialized_end = 1271
    _ROADSEGMENT._serialized_start = 1273
    _ROADSEGMENT._serialized_end = 1340
    _ROUTINGRESPONSE._serialized_start = 1343
    _ROUTINGRESPONSE._serialized_end = 1611