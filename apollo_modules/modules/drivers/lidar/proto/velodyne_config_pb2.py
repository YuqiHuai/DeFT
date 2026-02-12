"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.drivers.lidar.proto import velodyne_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/drivers/lidar/proto/velodyne_config.proto\x12\x17apollo.drivers.velodyne\x1a*modules/drivers/lidar/proto/velodyne.proto"\xc9\x04\n\x06Config\x12\x10\n\x08frame_id\x18\x01 \x01(\t\x12\x14\n\x0cscan_channel\x18\x02 \x01(\t\x12\x10\n\x03rpm\x18\x03 \x01(\x01:\x03600\x12-\n\x05model\x18\x04 \x01(\x0e2\x1e.apollo.drivers.velodyne.Model\x12+\n\x04mode\x18\x15 \x01(\x0e2\x1d.apollo.drivers.velodyne.Mode\x12\x0c\n\x04pcap\x18\x05 \x01(\t\x12\x14\n\x0cprefix_angle\x18\x06 \x01(\x05\x12\x18\n\x10firing_data_port\x18\x07 \x01(\x05\x12\x1d\n\x15positioning_data_port\x18\x08 \x01(\x05\x12\x17\n\x0fuse_sensor_sync\x18\t \x01(\x08\x12\x11\n\tmax_range\x18\n \x01(\x01\x12\x11\n\tmin_range\x18\x0b \x01(\x01\x12\x11\n\tmax_angle\x18\x0c \x01(\x01\x12\x11\n\tmin_angle\x18\r \x01(\x01\x12\x16\n\x0eview_direction\x18\x0e \x01(\x01\x12\x12\n\nview_width\x18\x0f \x01(\x01\x12\x1a\n\x12calibration_online\x18\x10 \x01(\x08\x12\x18\n\x10calibration_file\x18\x11 \x01(\t\x12\x11\n\torganized\x18\x12 \x01(\x08\x12\x1c\n\x14convert_channel_name\x18\x13 \x01(\t\x12\x10\n\x08npackets\x18\x14 \x01(\x05\x12\x14\n\x0cuse_gps_time\x18\x17 \x01(\x08\x12\x15\n\ruse_poll_sync\x18\x18 \x01(\x08\x12\x15\n\ris_main_frame\x18\x19 \x01(\x08"\x86\x01\n\x0cFusionConfig\x12\x17\n\x0fmax_interval_ms\x18\x01 \x01(\r\x12\x19\n\x11drop_expired_data\x18\x02 \x01(\x08\x12\x16\n\x0efusion_channel\x18\x03 \x01(\t\x12\x15\n\rinput_channel\x18\x04 \x03(\t\x12\x13\n\x0bwait_time_s\x18\x05 \x01(\x02"\xa4\x01\n\x11CompensatorConfig\x12\x16\n\x0eoutput_channel\x18\x01 \x01(\t\x12%\n\x17transform_query_timeout\x18\x02 \x01(\x02:\x040.02\x12\x1d\n\x0eworld_frame_id\x18\x03 \x01(\t:\x05world\x12\x17\n\x0ftarget_frame_id\x18\x04 \x01(\t\x12\x18\n\x10point_cloud_size\x18\x05 \x01(\r')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_FUSIONCONFIG = DESCRIPTOR.message_types_by_name['FusionConfig']
_COMPENSATORCONFIG = DESCRIPTOR.message_types_by_name['CompensatorConfig']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.proto.velodyne_config_pb2'})
_sym_db.RegisterMessage(Config)
FusionConfig = _reflection.GeneratedProtocolMessageType('FusionConfig', (_message.Message,), {'DESCRIPTOR': _FUSIONCONFIG, '__module__': 'modules.drivers.lidar.proto.velodyne_config_pb2'})
_sym_db.RegisterMessage(FusionConfig)
CompensatorConfig = _reflection.GeneratedProtocolMessageType('CompensatorConfig', (_message.Message,), {'DESCRIPTOR': _COMPENSATORCONFIG, '__module__': 'modules.drivers.lidar.proto.velodyne_config_pb2'})
_sym_db.RegisterMessage(CompensatorConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 123
    _CONFIG._serialized_end = 708
    _FUSIONCONFIG._serialized_start = 711
    _FUSIONCONFIG._serialized_end = 845
    _COMPENSATORCONFIG._serialized_start = 848
    _COMPENSATORCONFIG._serialized_end = 1012