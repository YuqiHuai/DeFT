"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.v2x.proto import v2x_traffic_light_pb2 as modules_dot_v2x_dot_proto_dot_v2x__traffic__light__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/v2x/proto/v2x_obu_traffic_light.proto\x12\x0eapollo.v2x.obu\x1a!modules/common/proto/header.proto\x1a)modules/v2x/proto/v2x_traffic_light.proto"\x98\x03\n\x12SingleTrafficLight\x123\n\x05color\x18\x01 \x01(\x0e2$.apollo.v2x.SingleTrafficLight.Color\x12\x1a\n\x12traffic_light_type\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\t\x12\x1e\n\x16color_remaining_time_s\x18\x04 \x01(\x05\x12\x18\n\x10right_turn_light\x18\x05 \x01(\x08\x128\n\nnext_color\x18\x06 \x01(\x0e2$.apollo.v2x.SingleTrafficLight.Color\x12\x1b\n\x13next_remaining_time\x18\x07 \x01(\x01\x12<\n\x0enext_2nd_color\x18\x08 \x01(\x0e2$.apollo.v2x.SingleTrafficLight.Color\x12\x1f\n\x17next_2nd_remaining_time\x18\t \x01(\x01"5\n\x04Type\x12\x0c\n\x08STRAIGHT\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x03\x12\n\n\x06U_TURN\x10\x04"v\n\x10LaneTrafficLight\x12\x0f\n\x07gps_x_m\x18\x01 \x01(\x01\x12\x0f\n\x07gps_y_m\x18\x02 \x01(\x01\x12@\n\x14single_traffic_light\x18\x03 \x03(\x0b2".apollo.v2x.obu.SingleTrafficLight"h\n\x10RoadTrafficLight\x12<\n\x12lane_traffic_light\x18\x01 \x03(\x0b2 .apollo.v2x.obu.LaneTrafficLight\x12\x16\n\x0eroad_direction\x18\x02 \x01(\x05"\xaa\x01\n\x0fObuTrafficLight\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12<\n\x12road_traffic_light\x18\x02 \x03(\x0b2 .apollo.v2x.obu.RoadTrafficLight\x12\x17\n\x0fintersection_id\x18\x03 \x01(\x05\x12\x19\n\x11hdmap_junction_id\x18\x04 \x01(\x0c')
_SINGLETRAFFICLIGHT = DESCRIPTOR.message_types_by_name['SingleTrafficLight']
_LANETRAFFICLIGHT = DESCRIPTOR.message_types_by_name['LaneTrafficLight']
_ROADTRAFFICLIGHT = DESCRIPTOR.message_types_by_name['RoadTrafficLight']
_OBUTRAFFICLIGHT = DESCRIPTOR.message_types_by_name['ObuTrafficLight']
_SINGLETRAFFICLIGHT_TYPE = _SINGLETRAFFICLIGHT.enum_types_by_name['Type']
SingleTrafficLight = _reflection.GeneratedProtocolMessageType('SingleTrafficLight', (_message.Message,), {'DESCRIPTOR': _SINGLETRAFFICLIGHT, '__module__': 'modules.v2x.proto.v2x_obu_traffic_light_pb2'})
_sym_db.RegisterMessage(SingleTrafficLight)
LaneTrafficLight = _reflection.GeneratedProtocolMessageType('LaneTrafficLight', (_message.Message,), {'DESCRIPTOR': _LANETRAFFICLIGHT, '__module__': 'modules.v2x.proto.v2x_obu_traffic_light_pb2'})
_sym_db.RegisterMessage(LaneTrafficLight)
RoadTrafficLight = _reflection.GeneratedProtocolMessageType('RoadTrafficLight', (_message.Message,), {'DESCRIPTOR': _ROADTRAFFICLIGHT, '__module__': 'modules.v2x.proto.v2x_obu_traffic_light_pb2'})
_sym_db.RegisterMessage(RoadTrafficLight)
ObuTrafficLight = _reflection.GeneratedProtocolMessageType('ObuTrafficLight', (_message.Message,), {'DESCRIPTOR': _OBUTRAFFICLIGHT, '__module__': 'modules.v2x.proto.v2x_obu_traffic_light_pb2'})
_sym_db.RegisterMessage(ObuTrafficLight)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SINGLETRAFFICLIGHT._serialized_start = 144
    _SINGLETRAFFICLIGHT._serialized_end = 552
    _SINGLETRAFFICLIGHT_TYPE._serialized_start = 499
    _SINGLETRAFFICLIGHT_TYPE._serialized_end = 552
    _LANETRAFFICLIGHT._serialized_start = 554
    _LANETRAFFICLIGHT._serialized_end = 672
    _ROADTRAFFICLIGHT._serialized_start = 674
    _ROADTRAFFICLIGHT._serialized_end = 778
    _OBUTRAFFICLIGHT._serialized_start = 781
    _OBUTRAFFICLIGHT._serialized_end = 951