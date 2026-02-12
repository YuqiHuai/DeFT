"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGmodules/perception/lidar/app/proto/lidar_obstacle_tracking_config.proto\x12\x17apollo.perception.lidar"\xab\x01\n\x1bLidarObstacleTrackingConfig\x125\n\x14multi_target_tracker\x18\x01 \x01(\t:\x17DummyMultiTargetTracker\x12)\n\x10frame_classifier\x18\x02 \x01(\t:\x0fDummyClassifier\x12*\n\x11fusion_classifier\x18\x03 \x01(\t:\x0fDummyClassifier')
_LIDAROBSTACLETRACKINGCONFIG = DESCRIPTOR.message_types_by_name['LidarObstacleTrackingConfig']
LidarObstacleTrackingConfig = _reflection.GeneratedProtocolMessageType('LidarObstacleTrackingConfig', (_message.Message,), {'DESCRIPTOR': _LIDAROBSTACLETRACKINGCONFIG, '__module__': 'modules.perception.lidar.app.proto.lidar_obstacle_tracking_config_pb2'})
_sym_db.RegisterMessage(LidarObstacleTrackingConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LIDAROBSTACLETRACKINGCONFIG._serialized_start = 101
    _LIDAROBSTACLETRACKINGCONFIG._serialized_end = 272