"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/perception/onboard/proto/lidar_component_config.proto\x12\x19apollo.perception.onboard"\xc7\x01\n\x1dLidarDetectionComponentConfig\x12\x13\n\x0bsensor_name\x18\x01 \x01(\t\x12\x15\n\rdetector_name\x18\x02 \x01(\t\x12\x14\n\x0cenable_hdmap\x18\x03 \x01(\x08\x12\x1d\n\x15lidar_query_tf_offset\x18\x04 \x01(\x01\x12(\n lidar2novatel_tf2_child_frame_id\x18\x05 \x01(\t\x12\x1b\n\x13output_channel_name\x18\x06 \x01(\t"X\n\x1fLidarRecognitionComponentConfig\x12\x18\n\x10main_sensor_name\x18\x01 \x01(\t\x12\x1b\n\x13output_channel_name\x18\x02 \x01(\t')
_LIDARDETECTIONCOMPONENTCONFIG = DESCRIPTOR.message_types_by_name['LidarDetectionComponentConfig']
_LIDARRECOGNITIONCOMPONENTCONFIG = DESCRIPTOR.message_types_by_name['LidarRecognitionComponentConfig']
LidarDetectionComponentConfig = _reflection.GeneratedProtocolMessageType('LidarDetectionComponentConfig', (_message.Message,), {'DESCRIPTOR': _LIDARDETECTIONCOMPONENTCONFIG, '__module__': 'modules.perception.onboard.proto.lidar_component_config_pb2'})
_sym_db.RegisterMessage(LidarDetectionComponentConfig)
LidarRecognitionComponentConfig = _reflection.GeneratedProtocolMessageType('LidarRecognitionComponentConfig', (_message.Message,), {'DESCRIPTOR': _LIDARRECOGNITIONCOMPONENTCONFIG, '__module__': 'modules.perception.onboard.proto.lidar_component_config_pb2'})
_sym_db.RegisterMessage(LidarRecognitionComponentConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LIDARDETECTIONCOMPONENTCONFIG._serialized_start = 93
    _LIDARDETECTIONCOMPONENTCONFIG._serialized_end = 292
    _LIDARRECOGNITIONCOMPONENTCONFIG._serialized_start = 294
    _LIDARRECOGNITIONCOMPONENTCONFIG._serialized_end = 382