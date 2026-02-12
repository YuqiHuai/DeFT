"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.canbus.proto import can_card_parameter_pb2 as modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHmodules/drivers/radar/ultrasonic_radar/proto/ultrasonic_radar_conf.proto\x12\x1fapollo.drivers.ultrasonic_radar\x1a5modules/drivers/canbus/proto/can_card_parameter.proto"\xb6\x01\n\x07CanConf\x12C\n\x12can_card_parameter\x18\x01 \x01(\x0b2\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11enable_debug_mode\x18\x02 \x01(\x08:\x05false\x12"\n\x13enable_receiver_log\x18\x03 \x01(\x08:\x05false\x12 \n\x11enable_sender_log\x18\x04 \x01(\x08:\x05false"g\n\x13UltrasonicRadarConf\x12:\n\x08can_conf\x18\x01 \x01(\x0b2(.apollo.drivers.ultrasonic_radar.CanConf\x12\x14\n\x0centrance_num\x18\x02 \x01(\x05')
_CANCONF = DESCRIPTOR.message_types_by_name['CanConf']
_ULTRASONICRADARCONF = DESCRIPTOR.message_types_by_name['UltrasonicRadarConf']
CanConf = _reflection.GeneratedProtocolMessageType('CanConf', (_message.Message,), {'DESCRIPTOR': _CANCONF, '__module__': 'modules.drivers.radar.ultrasonic_radar.proto.ultrasonic_radar_conf_pb2'})
_sym_db.RegisterMessage(CanConf)
UltrasonicRadarConf = _reflection.GeneratedProtocolMessageType('UltrasonicRadarConf', (_message.Message,), {'DESCRIPTOR': _ULTRASONICRADARCONF, '__module__': 'modules.drivers.radar.ultrasonic_radar.proto.ultrasonic_radar_conf_pb2'})
_sym_db.RegisterMessage(UltrasonicRadarConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CANCONF._serialized_start = 165
    _CANCONF._serialized_end = 347
    _ULTRASONICRADARCONF._serialized_start = 349
    _ULTRASONICRADARCONF._serialized_end = 452