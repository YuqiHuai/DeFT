"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/dreamview/proto/camera_update.proto\x12\x10apollo.dreamview"o\n\x0cCameraUpdate\x12\x14\n\x0clocalization\x18\x01 \x03(\x01\x12\x1e\n\x16localization2camera_tf\x18\x02 \x03(\x01\x12\r\n\x05image\x18\x03 \x01(\x0c\x12\x1a\n\x12image_aspect_ratio\x18\x04 \x01(\x01')
_CAMERAUPDATE = DESCRIPTOR.message_types_by_name['CameraUpdate']
CameraUpdate = _reflection.GeneratedProtocolMessageType('CameraUpdate', (_message.Message,), {'DESCRIPTOR': _CAMERAUPDATE, '__module__': 'modules.dreamview.proto.camera_update_pb2'})
_sym_db.RegisterMessage(CameraUpdate)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CAMERAUPDATE._serialized_start = 65
    _CAMERAUPDATE._serialized_end = 176