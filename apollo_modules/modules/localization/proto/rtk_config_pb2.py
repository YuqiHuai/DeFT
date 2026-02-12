"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/localization/proto/rtk_config.proto\x12\x1eapollo.localization.rtk_config"\xcd\x02\n\x06Config\x12\x1a\n\x12localization_topic\x18\x01 \x01(\t\x12!\n\x19localization_status_topic\x18\x0b \x01(\t\x12\x11\n\timu_topic\x18\x02 \x01(\t\x12\x11\n\tgps_topic\x18\x03 \x01(\t\x12\x18\n\x10gps_status_topic\x18\x0c \x01(\t\x12\x1d\n\x15broadcast_tf_frame_id\x18\x04 \x01(\t\x12#\n\x1bbroadcast_tf_child_frame_id\x18\x05 \x01(\t\x12\x19\n\x11imu_list_max_size\x18\x06 \x01(\x05\x12#\n\x1bgps_imu_time_diff_threshold\x18\x07 \x01(\x01\x12\x14\n\x0cmap_offset_x\x18\x08 \x01(\x01\x12\x14\n\x0cmap_offset_y\x18\t \x01(\x01\x12\x14\n\x0cmap_offset_z\x18\n \x01(\x01')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.localization.proto.rtk_config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 80
    _CONFIG._serialized_end = 413