"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/perception/proto/traffic_light_detection.proto\x12\x11apollo.perception\x1a!modules/common/proto/header.proto"\xa3\x01\n\x0fTrafficLightBox\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x124\n\x05color\x18\x05 \x01(\x0e2%.apollo.perception.TrafficLight.Color\x12\x10\n\x08selected\x18\x06 \x01(\x08\x12\x13\n\x0bcamera_name\x18\x07 \x01(\t"\xfa\x03\n\x11TrafficLightDebug\x123\n\x07cropbox\x18\x01 \x01(\x0b2".apollo.perception.TrafficLightBox\x12/\n\x03box\x18\x02 \x03(\x0b2".apollo.perception.TrafficLightBox\x12\x12\n\nsignal_num\x18\x03 \x01(\x05\x12\x11\n\tvalid_pos\x18\x04 \x01(\x05\x12\x13\n\x0bts_diff_pos\x18\x05 \x01(\x01\x12\x13\n\x0bts_diff_sys\x18\x06 \x01(\x01\x12\x15\n\rproject_error\x18\x07 \x01(\x05\x12\x1d\n\x15distance_to_stop_line\x18\x08 \x01(\x01\x12\x15\n\tcamera_id\x18\t \x01(\x05B\x02\x18\x01\x124\n\x08crop_roi\x18\n \x03(\x0b2".apollo.perception.TrafficLightBox\x129\n\rprojected_roi\x18\x0b \x03(\x0b2".apollo.perception.TrafficLightBox\x129\n\rrectified_roi\x18\x0c \x03(\x0b2".apollo.perception.TrafficLightBox\x125\n\tdebug_roi\x18\r \x03(\x0b2".apollo.perception.TrafficLightBox"\xe6\x01\n\x0cTrafficLight\x124\n\x05color\x18\x01 \x01(\x0e2%.apollo.perception.TrafficLight.Color\x12\n\n\x02id\x18\x02 \x01(\t\x12\x15\n\nconfidence\x18\x03 \x01(\x01:\x011\x12\x15\n\rtracking_time\x18\x04 \x01(\x01\x12\r\n\x05blink\x18\x05 \x01(\x08\x12\x16\n\x0eremaining_time\x18\x06 \x01(\x01"?\n\x05Color\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\t\n\x05BLACK\x10\x04"\x82\x03\n\x15TrafficLightDetection\x12%\n\x06header\x18\x02 \x01(\x0b2\x15.apollo.common.Header\x126\n\rtraffic_light\x18\x01 \x03(\x0b2\x1f.apollo.perception.TrafficLight\x12A\n\x13traffic_light_debug\x18\x03 \x01(\x0b2$.apollo.perception.TrafficLightDebug\x12\x16\n\x0econtain_lights\x18\x04 \x01(\x08\x12D\n\tcamera_id\x18\x05 \x01(\x0e21.apollo.perception.TrafficLightDetection.CameraID"i\n\x08CameraID\x12\x15\n\x11CAMERA_FRONT_LONG\x10\x00\x12\x17\n\x13CAMERA_FRONT_NARROW\x10\x01\x12\x16\n\x12CAMERA_FRONT_SHORT\x10\x02\x12\x15\n\x11CAMERA_FRONT_WIDE\x10\x03')
_TRAFFICLIGHTBOX = DESCRIPTOR.message_types_by_name['TrafficLightBox']
_TRAFFICLIGHTDEBUG = DESCRIPTOR.message_types_by_name['TrafficLightDebug']
_TRAFFICLIGHT = DESCRIPTOR.message_types_by_name['TrafficLight']
_TRAFFICLIGHTDETECTION = DESCRIPTOR.message_types_by_name['TrafficLightDetection']
_TRAFFICLIGHT_COLOR = _TRAFFICLIGHT.enum_types_by_name['Color']
_TRAFFICLIGHTDETECTION_CAMERAID = _TRAFFICLIGHTDETECTION.enum_types_by_name['CameraID']
TrafficLightBox = _reflection.GeneratedProtocolMessageType('TrafficLightBox', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTBOX, '__module__': 'modules.perception.proto.traffic_light_detection_pb2'})
_sym_db.RegisterMessage(TrafficLightBox)
TrafficLightDebug = _reflection.GeneratedProtocolMessageType('TrafficLightDebug', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTDEBUG, '__module__': 'modules.perception.proto.traffic_light_detection_pb2'})
_sym_db.RegisterMessage(TrafficLightDebug)
TrafficLight = _reflection.GeneratedProtocolMessageType('TrafficLight', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHT, '__module__': 'modules.perception.proto.traffic_light_detection_pb2'})
_sym_db.RegisterMessage(TrafficLight)
TrafficLightDetection = _reflection.GeneratedProtocolMessageType('TrafficLightDetection', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTDETECTION, '__module__': 'modules.perception.proto.traffic_light_detection_pb2'})
_sym_db.RegisterMessage(TrafficLightDetection)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TRAFFICLIGHTDEBUG.fields_by_name['camera_id']._options = None
    _TRAFFICLIGHTDEBUG.fields_by_name['camera_id']._serialized_options = b'\x18\x01'
    _TRAFFICLIGHTBOX._serialized_start = 113
    _TRAFFICLIGHTBOX._serialized_end = 276
    _TRAFFICLIGHTDEBUG._serialized_start = 279
    _TRAFFICLIGHTDEBUG._serialized_end = 785
    _TRAFFICLIGHT._serialized_start = 788
    _TRAFFICLIGHT._serialized_end = 1018
    _TRAFFICLIGHT_COLOR._serialized_start = 955
    _TRAFFICLIGHT_COLOR._serialized_end = 1018
    _TRAFFICLIGHTDETECTION._serialized_start = 1021
    _TRAFFICLIGHTDETECTION._serialized_end = 1407
    _TRAFFICLIGHTDETECTION_CAMERAID._serialized_start = 1302
    _TRAFFICLIGHTDETECTION_CAMERAID._serialized_end = 1407