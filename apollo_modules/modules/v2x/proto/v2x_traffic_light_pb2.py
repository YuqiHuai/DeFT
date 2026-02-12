"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import direction_pb2 as modules_dot_common_dot_proto_dot_direction__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/v2x/proto/v2x_traffic_light.proto\x12\napollo.v2x\x1a!modules/common/proto/header.proto\x1a$modules/common/proto/direction.proto"\xb2\x03\n\x12SingleTrafficLight\x123\n\x05color\x18\x01 \x01(\x0e2$.apollo.v2x.SingleTrafficLight.Color\x12?\n\x12traffic_light_type\x18\x02 \x03(\x0e2#.apollo.v2x.SingleTrafficLight.Type\x12\n\n\x02id\x18\x03 \x01(\t\x12\x1e\n\x16color_remaining_time_s\x18\x04 \x01(\x05\x12\x18\n\x10right_turn_light\x18\x05 \x01(\x08\x128\n\nnext_color\x18\x06 \x01(\x0e2$.apollo.v2x.SingleTrafficLight.Color\x12\x1d\n\x15next_remaining_time_s\x18\x07 \x01(\x01"P\n\x05Color\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\t\n\x05BLACK\x10\x04\x12\x0f\n\x0bFLASH_GREEN\x10\x05"5\n\x04Type\x12\x0c\n\x08STRAIGHT\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\n\n\x06U_TURN\x10\x03"\xa4\x01\n\x10RoadTrafficLight\x12\x0f\n\x07gps_x_m\x18\x01 \x01(\x01\x12\x0f\n\x07gps_y_m\x18\x02 \x01(\x01\x12<\n\x14single_traffic_light\x18\x03 \x03(\x0b2\x1e.apollo.v2x.SingleTrafficLight\x120\n\x0eroad_attribute\x18\x04 \x01(\x0e2\x18.apollo.common.Direction"\xac\x01\n\x1cIntersectionTrafficLightData\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x128\n\x12road_traffic_light\x18\x02 \x03(\x0b2\x1c.apollo.v2x.RoadTrafficLight\x12\x17\n\x0fintersection_id\x18\x03 \x01(\x05\x12\x12\n\nconfidence\x18\x04 \x01(\x01')
_SINGLETRAFFICLIGHT = DESCRIPTOR.message_types_by_name['SingleTrafficLight']
_ROADTRAFFICLIGHT = DESCRIPTOR.message_types_by_name['RoadTrafficLight']
_INTERSECTIONTRAFFICLIGHTDATA = DESCRIPTOR.message_types_by_name['IntersectionTrafficLightData']
_SINGLETRAFFICLIGHT_COLOR = _SINGLETRAFFICLIGHT.enum_types_by_name['Color']
_SINGLETRAFFICLIGHT_TYPE = _SINGLETRAFFICLIGHT.enum_types_by_name['Type']
SingleTrafficLight = _reflection.GeneratedProtocolMessageType('SingleTrafficLight', (_message.Message,), {'DESCRIPTOR': _SINGLETRAFFICLIGHT, '__module__': 'modules.v2x.proto.v2x_traffic_light_pb2'})
_sym_db.RegisterMessage(SingleTrafficLight)
RoadTrafficLight = _reflection.GeneratedProtocolMessageType('RoadTrafficLight', (_message.Message,), {'DESCRIPTOR': _ROADTRAFFICLIGHT, '__module__': 'modules.v2x.proto.v2x_traffic_light_pb2'})
_sym_db.RegisterMessage(RoadTrafficLight)
IntersectionTrafficLightData = _reflection.GeneratedProtocolMessageType('IntersectionTrafficLightData', (_message.Message,), {'DESCRIPTOR': _INTERSECTIONTRAFFICLIGHTDATA, '__module__': 'modules.v2x.proto.v2x_traffic_light_pb2'})
_sym_db.RegisterMessage(IntersectionTrafficLightData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SINGLETRAFFICLIGHT._serialized_start = 131
    _SINGLETRAFFICLIGHT._serialized_end = 565
    _SINGLETRAFFICLIGHT_COLOR._serialized_start = 430
    _SINGLETRAFFICLIGHT_COLOR._serialized_end = 510
    _SINGLETRAFFICLIGHT_TYPE._serialized_start = 512
    _SINGLETRAFFICLIGHT_TYPE._serialized_end = 565
    _ROADTRAFFICLIGHT._serialized_start = 568
    _ROADTRAFFICLIGHT._serialized_end = 732
    _INTERSECTIONTRAFFICLIGHTDATA._serialized_start = 735
    _INTERSECTIONTRAFFICLIGHTDATA._serialized_end = 907