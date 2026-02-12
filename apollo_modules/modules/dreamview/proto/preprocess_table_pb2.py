"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/dreamview/proto/preprocess_table.proto\x12\x10apollo.dreamview".\n\x0bTranslation\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02"V\n\x0bLidarConfig\x12\x13\n\x0bsensor_name\x18\x01 \x01(\t\x122\n\x0btranslation\x18\x02 \x01(\x0b2\x1d.apollo.dreamview.Translation"X\n\x0cCameraConfig\x122\n\x0btranslation\x18\x01 \x01(\x0b2\x1d.apollo.dreamview.Translation\x12\t\n\x01D\x18\x02 \x03(\x02\x12\t\n\x01K\x18\x03 \x03(\x02"\\\n\x08Progress\x12\x12\n\npercentage\x18\x01 \x01(\x02\x12\x12\n\nlog_string\x18\x02 \x01(\t\x12(\n\x06status\x18\x03 \x01(\x0e2\x18.apollo.dreamview.Status"\xc0\x01\n\x0fPreprocessTable\x123\n\x0clidar_config\x18\x01 \x03(\x0b2\x1d.apollo.dreamview.LidarConfig\x125\n\rcamera_config\x18\x02 \x01(\x0b2\x1e.apollo.dreamview.CameraConfig\x12\x13\n\x0bmain_sensor\x18\x03 \x01(\t\x12,\n\x08progress\x18\x04 \x01(\x0b2\x1a.apollo.dreamview.Progress*,\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04FAIL\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02')
_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
SUCCESS = 0
FAIL = 1
UNKNOWN = 2
_TRANSLATION = DESCRIPTOR.message_types_by_name['Translation']
_LIDARCONFIG = DESCRIPTOR.message_types_by_name['LidarConfig']
_CAMERACONFIG = DESCRIPTOR.message_types_by_name['CameraConfig']
_PROGRESS = DESCRIPTOR.message_types_by_name['Progress']
_PREPROCESSTABLE = DESCRIPTOR.message_types_by_name['PreprocessTable']
Translation = _reflection.GeneratedProtocolMessageType('Translation', (_message.Message,), {'DESCRIPTOR': _TRANSLATION, '__module__': 'modules.dreamview.proto.preprocess_table_pb2'})
_sym_db.RegisterMessage(Translation)
LidarConfig = _reflection.GeneratedProtocolMessageType('LidarConfig', (_message.Message,), {'DESCRIPTOR': _LIDARCONFIG, '__module__': 'modules.dreamview.proto.preprocess_table_pb2'})
_sym_db.RegisterMessage(LidarConfig)
CameraConfig = _reflection.GeneratedProtocolMessageType('CameraConfig', (_message.Message,), {'DESCRIPTOR': _CAMERACONFIG, '__module__': 'modules.dreamview.proto.preprocess_table_pb2'})
_sym_db.RegisterMessage(CameraConfig)
Progress = _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), {'DESCRIPTOR': _PROGRESS, '__module__': 'modules.dreamview.proto.preprocess_table_pb2'})
_sym_db.RegisterMessage(Progress)
PreprocessTable = _reflection.GeneratedProtocolMessageType('PreprocessTable', (_message.Message,), {'DESCRIPTOR': _PREPROCESSTABLE, '__module__': 'modules.dreamview.proto.preprocess_table_pb2'})
_sym_db.RegisterMessage(PreprocessTable)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STATUS._serialized_start = 583
    _STATUS._serialized_end = 627
    _TRANSLATION._serialized_start = 68
    _TRANSLATION._serialized_end = 114
    _LIDARCONFIG._serialized_start = 116
    _LIDARCONFIG._serialized_end = 202
    _CAMERACONFIG._serialized_start = 204
    _CAMERACONFIG._serialized_end = 292
    _PROGRESS._serialized_start = 294
    _PROGRESS._serialized_end = 386
    _PREPROCESSTABLE._serialized_start = 389
    _PREPROCESSTABLE._serialized_end = 581