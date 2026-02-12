"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.drivers.lidar.proto import hesai_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2
from .....modules.drivers.lidar.proto import velodyne_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2
from .....modules.drivers.lidar.proto import lidar_parameter_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2
from .....modules.drivers.lidar.proto import robosense_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/drivers/lidar/proto/config.proto\x12\x14apollo.drivers.lidar\x1a.modules/drivers/lidar/proto/hesai_config.proto\x1a1modules/drivers/lidar/proto/velodyne_config.proto\x1a1modules/drivers/lidar/proto/lidar_parameter.proto\x1a2modules/drivers/lidar/proto/robosense_config.proto"\xdd\x01\n\x06config\x12>\n\x05brand\x18\x01 \x01(\x0e2/.apollo.drivers.lidar.LidarParameter.LidarBrand\x12+\n\x05hesai\x18\x02 \x01(\x0b2\x1c.apollo.drivers.hesai.Config\x123\n\trobosense\x18\x03 \x01(\x0b2 .apollo.drivers.robosense.Config\x121\n\x08velodyne\x18\x04 \x01(\x0b2\x1f.apollo.drivers.velodyne.Config')
_CONFIG = DESCRIPTOR.message_types_by_name['config']
config = _reflection.GeneratedProtocolMessageType('config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.proto.config_pb2'})
_sym_db.RegisterMessage(config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 269
    _CONFIG._serialized_end = 490