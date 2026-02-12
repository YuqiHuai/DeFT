"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.routing.proto import routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmodules/routing/proto/poi.proto\x12\x0eapollo.routing\x1a#modules/routing/proto/routing.proto"\x99\x01\n\x08Landmark\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x08waypoint\x18\x02 \x03(\x0b2\x1c.apollo.routing.LaneWaypoint\x12\x1c\n\x10parking_space_id\x18\x03 \x01(\tB\x02\x18\x01\x121\n\x0cparking_info\x18\x04 \x01(\x0b2\x1b.apollo.routing.ParkingInfo"1\n\x03POI\x12*\n\x08landmark\x18\x01 \x03(\x0b2\x18.apollo.routing.Landmark')
_LANDMARK = DESCRIPTOR.message_types_by_name['Landmark']
_POI = DESCRIPTOR.message_types_by_name['POI']
Landmark = _reflection.GeneratedProtocolMessageType('Landmark', (_message.Message,), {'DESCRIPTOR': _LANDMARK, '__module__': 'modules.routing.proto.poi_pb2'})
_sym_db.RegisterMessage(Landmark)
POI = _reflection.GeneratedProtocolMessageType('POI', (_message.Message,), {'DESCRIPTOR': _POI, '__module__': 'modules.routing.proto.poi_pb2'})
_sym_db.RegisterMessage(POI)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANDMARK.fields_by_name['parking_space_id']._options = None
    _LANDMARK.fields_by_name['parking_space_id']._serialized_options = b'\x18\x01'
    _LANDMARK._serialized_start = 89
    _LANDMARK._serialized_end = 242
    _POI._serialized_start = 244
    _POI._serialized_end = 293