"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.drivers.canbus.proto import can_card_parameter_pb2 as modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/drivers/canbus/proto/sensor_canbus_conf.proto\x12\x15apollo.drivers.canbus\x1a5modules/drivers/canbus/proto/can_card_parameter.proto"\x9d\x01\n\x10SensorCanbusConf\x12C\n\x12can_card_parameter\x18\x01 \x01(\x0b2\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11enable_debug_mode\x18\x02 \x01(\x08:\x05false\x12"\n\x13enable_receiver_log\x18\x03 \x01(\x08:\x05false')
_SENSORCANBUSCONF = DESCRIPTOR.message_types_by_name['SensorCanbusConf']
SensorCanbusConf = _reflection.GeneratedProtocolMessageType('SensorCanbusConf', (_message.Message,), {'DESCRIPTOR': _SENSORCANBUSCONF, '__module__': 'modules.drivers.canbus.proto.sensor_canbus_conf_pb2'})
_sym_db.RegisterMessage(SensorCanbusConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SENSORCANBUSCONF._serialized_start = 136
    _SENSORCANBUSCONF._serialized_end = 293