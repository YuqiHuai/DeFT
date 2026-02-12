"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/drivers/lidar/proto/robosense_config.proto\x12\x18apollo.drivers.robosense"\xbb\x02\n\x06Config\x12\r\n\x05model\x18\x01 \x01(\t\x12\x10\n\x08frame_id\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x11\n\tmsop_port\x18\x04 \x01(\r\x12\x12\n\ndifop_port\x18\x05 \x01(\r\x12\x11\n\techo_mode\x18\x06 \x01(\r\x12\x13\n\x0bstart_angle\x18\x08 \x01(\r\x12\x11\n\tend_angle\x18\t \x01(\r\x12\x14\n\x0cmin_distance\x18\n \x01(\r\x12\x14\n\x0cmax_distance\x18\x0b \x01(\r\x12\x11\n\tcut_angle\x18\x0c \x01(\r\x12\x1a\n\x12pointcloud_channel\x18\r \x01(\t\x12\x14\n\x0cscan_channel\x18\x0e \x01(\t\x12\x18\n\x10calibration_file\x18\x0f \x01(\t\x12\x17\n\x0fuse_lidar_clock\x18\x10 \x01(\x08')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.proto.robosense_config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 81
    _CONFIG._serialized_end = 396