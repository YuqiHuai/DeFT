"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/perception/proto/dst_existence_fusion_config.proto\x12\x11apollo.perception"?\n\x0fCameraValidDist\x12\x15\n\x0bcamera_name\x18\x01 \x01(\t:\x00\x12\x15\n\nvalid_dist\x18\x02 \x01(\x01:\x010"\x85\x01\n\x18DstExistenceFusionConfig\x12*\n\x1ftrack_object_max_match_distance\x18\x01 \x01(\x01:\x014\x12=\n\x11camera_valid_dist\x18\x02 \x03(\x0b2".apollo.perception.CameraValidDist')
_CAMERAVALIDDIST = DESCRIPTOR.message_types_by_name['CameraValidDist']
_DSTEXISTENCEFUSIONCONFIG = DESCRIPTOR.message_types_by_name['DstExistenceFusionConfig']
CameraValidDist = _reflection.GeneratedProtocolMessageType('CameraValidDist', (_message.Message,), {'DESCRIPTOR': _CAMERAVALIDDIST, '__module__': 'modules.perception.proto.dst_existence_fusion_config_pb2'})
_sym_db.RegisterMessage(CameraValidDist)
DstExistenceFusionConfig = _reflection.GeneratedProtocolMessageType('DstExistenceFusionConfig', (_message.Message,), {'DESCRIPTOR': _DSTEXISTENCEFUSIONCONFIG, '__module__': 'modules.perception.proto.dst_existence_fusion_config_pb2'})
_sym_db.RegisterMessage(DstExistenceFusionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CAMERAVALIDDIST._serialized_start = 81
    _CAMERAVALIDDIST._serialized_end = 144
    _DSTEXISTENCEFUSIONCONFIG._serialized_start = 147
    _DSTEXISTENCEFUSIONCONFIG._serialized_end = 280