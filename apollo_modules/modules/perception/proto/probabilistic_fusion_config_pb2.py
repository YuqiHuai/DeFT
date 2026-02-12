"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/perception/proto/probabilistic_fusion_config.proto\x12\x18apollo.perception.fusion"\xa3\x03\n\x19ProbabilisticFusionConfig\x12\x17\n\tuse_lidar\x18\x01 \x01(\x08:\x04true\x12\x17\n\tuse_radar\x18\x02 \x01(\x08:\x04true\x12\x18\n\nuse_camera\x18\x03 \x01(\x08:\x04true\x12"\n\x0etracker_method\x18\x04 \x01(\t:\nPbfTracker\x12.\n\x17data_association_method\x18\x05 \x01(\t:\rHMAssociation\x12)\n\x12gate_keeper_method\x18\x06 \x01(\t:\rPbfGatekeeper\x12\x1b\n\x13prohibition_sensors\x18\x07 \x03(\t\x12(\n\x1amax_lidar_invisible_period\x18\x08 \x01(\x01:\x040.25\x12\'\n\x1amax_radar_invisible_period\x18\t \x01(\x01:\x030.5\x12)\n\x1bmax_camera_invisible_period\x18\n \x01(\x01:\x040.75\x12 \n\x14max_cached_frame_num\x18\x0b \x01(\x03:\x0250')
_PROBABILISTICFUSIONCONFIG = DESCRIPTOR.message_types_by_name['ProbabilisticFusionConfig']
ProbabilisticFusionConfig = _reflection.GeneratedProtocolMessageType('ProbabilisticFusionConfig', (_message.Message,), {'DESCRIPTOR': _PROBABILISTICFUSIONCONFIG, '__module__': 'modules.perception.proto.probabilistic_fusion_config_pb2'})
_sym_db.RegisterMessage(ProbabilisticFusionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PROBABILISTICFUSIONCONFIG._serialized_start = 89
    _PROBABILISTICFUSIONCONFIG._serialized_end = 508