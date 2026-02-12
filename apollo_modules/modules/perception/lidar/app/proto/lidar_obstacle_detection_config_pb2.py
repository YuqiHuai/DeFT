"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHmodules/perception/lidar/app/proto/lidar_obstacle_detection_config.proto\x12\x17apollo.perception.lidar"\xba\x01\n\x1cLidarObstacleDetectionConfig\x12,\n\x0cpreprocessor\x18\x01 \x01(\t:\x16PointCloudPreprocessor\x12\'\n\x08detector\x18\x02 \x01(\t:\x15PointPillarsDetection\x12\x1d\n\x0fuse_map_manager\x18\x03 \x01(\x08:\x04true\x12$\n\x16use_object_filter_bank\x18\x04 \x01(\x08:\x04true')
_LIDAROBSTACLEDETECTIONCONFIG = DESCRIPTOR.message_types_by_name['LidarObstacleDetectionConfig']
LidarObstacleDetectionConfig = _reflection.GeneratedProtocolMessageType('LidarObstacleDetectionConfig', (_message.Message,), {'DESCRIPTOR': _LIDAROBSTACLEDETECTIONCONFIG, '__module__': 'modules.perception.lidar.app.proto.lidar_obstacle_detection_config_pb2'})
_sym_db.RegisterMessage(LidarObstacleDetectionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LIDAROBSTACLEDETECTIONCONFIG._serialized_start = 102
    _LIDAROBSTACLEDETECTIONCONFIG._serialized_end = 288