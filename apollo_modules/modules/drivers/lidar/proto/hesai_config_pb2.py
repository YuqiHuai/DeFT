"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.drivers.lidar.proto import hesai_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/drivers/lidar/proto/hesai_config.proto\x12\x14apollo.drivers.hesai\x1a\'modules/drivers/lidar/proto/hesai.proto"\xc6\x02\n\x06Config\x12*\n\x05model\x18\x01 \x01(\x0e2\x1b.apollo.drivers.hesai.Model\x12\x19\n\x02ip\x18\x02 \x01(\t:\r192.168.20.13\x12\x17\n\x0flidar_recv_port\x18\x03 \x01(\r\x12\x15\n\rgps_recv_port\x18\x04 \x01(\r\x12\x13\n\x0bstart_angle\x18\x05 \x01(\r\x12\x1a\n\x12pointcloud_channel\x18\x06 \x01(\t\x12\x11\n\ttime_zone\x18\x07 \x01(\r\x12\x10\n\x08frame_id\x18\x08 \x01(\t\x12\x14\n\x0cscan_channel\x18\t \x01(\t\x12#\n\x15is_online_calibration\x18\x0b \x01(\x08:\x04true\x12\x18\n\x10calibration_file\x18\x0c \x01(\t\x12\x1a\n\x0ctcp_cmd_port\x18\r \x01(\r:\x049347')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.proto.hesai_config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 114
    _CONFIG._serialized_end = 440