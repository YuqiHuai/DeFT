"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/perception/proto/dst_type_fusion_config.proto\x12\x18apollo.perception.fusion"}\n\x18CameraDstTypeFusionParam\x12\x0e\n\x04name\x18\x01 \x01(\t:\x00\x12\x15\n\nvalid_dist\x18\x02 \x01(\x01:\x010\x12\x16\n\x0breliability\x18\x03 \x01(\x01:\x010\x12"\n\x17reliability_for_unknown\x18\x04 \x01(\x01:\x010"e\n\x17LidarDstTypeFusionParam\x12\x0e\n\x04name\x18\x01 \x01(\t:\x00\x12\x16\n\x0breliability\x18\x02 \x01(\x01:\x010\x12"\n\x17reliability_for_unknown\x18\x03 \x01(\x01:\x010"\xa9\x01\n\x13DstTypeFusionConfig\x12I\n\rcamera_params\x18\x01 \x03(\x0b22.apollo.perception.fusion.CameraDstTypeFusionParam\x12G\n\x0clidar_params\x18\x02 \x03(\x0b21.apollo.perception.fusion.LidarDstTypeFusionParam')
_CAMERADSTTYPEFUSIONPARAM = DESCRIPTOR.message_types_by_name['CameraDstTypeFusionParam']
_LIDARDSTTYPEFUSIONPARAM = DESCRIPTOR.message_types_by_name['LidarDstTypeFusionParam']
_DSTTYPEFUSIONCONFIG = DESCRIPTOR.message_types_by_name['DstTypeFusionConfig']
CameraDstTypeFusionParam = _reflection.GeneratedProtocolMessageType('CameraDstTypeFusionParam', (_message.Message,), {'DESCRIPTOR': _CAMERADSTTYPEFUSIONPARAM, '__module__': 'modules.perception.proto.dst_type_fusion_config_pb2'})
_sym_db.RegisterMessage(CameraDstTypeFusionParam)
LidarDstTypeFusionParam = _reflection.GeneratedProtocolMessageType('LidarDstTypeFusionParam', (_message.Message,), {'DESCRIPTOR': _LIDARDSTTYPEFUSIONPARAM, '__module__': 'modules.perception.proto.dst_type_fusion_config_pb2'})
_sym_db.RegisterMessage(LidarDstTypeFusionParam)
DstTypeFusionConfig = _reflection.GeneratedProtocolMessageType('DstTypeFusionConfig', (_message.Message,), {'DESCRIPTOR': _DSTTYPEFUSIONCONFIG, '__module__': 'modules.perception.proto.dst_type_fusion_config_pb2'})
_sym_db.RegisterMessage(DstTypeFusionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CAMERADSTTYPEFUSIONPARAM._serialized_start = 83
    _CAMERADSTTYPEFUSIONPARAM._serialized_end = 208
    _LIDARDSTTYPEFUSIONPARAM._serialized_start = 210
    _LIDARDSTTYPEFUSIONPARAM._serialized_end = 311
    _DSTTYPEFUSIONCONFIG._serialized_start = 314
    _DSTTYPEFUSIONCONFIG._serialized_end = 483