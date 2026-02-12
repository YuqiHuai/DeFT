"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/drivers/camera/proto/config.proto\x12\x1capollo.drivers.camera.config"\xd3\x06\n\x06Config\x12\x12\n\ncamera_dev\x18\x01 \x01(\t\x12\x10\n\x08frame_id\x18\x02 \x01(\t\x12\x1a\n\x0cpixel_format\x18\x03 \x01(\t:\x04yuyv\x129\n\tio_method\x18\x04 \x01(\x0e2&.apollo.drivers.camera.config.IOMethod\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0e\n\x06height\x18\x06 \x01(\r\x12\x12\n\nframe_rate\x18\x07 \x01(\r\x12\x19\n\nmonochrome\x18\x08 \x01(\x08:\x05false\x12\x16\n\nbrightness\x18\t \x01(\x05:\x02-1\x12\x14\n\x08contrast\x18\n \x01(\x05:\x02-1\x12\x16\n\nsaturation\x18\x0b \x01(\x05:\x02-1\x12\x15\n\tsharpness\x18\x0c \x01(\x05:\x02-1\x12\x10\n\x04gain\x18\r \x01(\x05:\x02-1\x12\x19\n\nauto_focus\x18\x0e \x01(\x08:\x05false\x12\x11\n\x05focus\x18\x0f \x01(\x05:\x02-1\x12\x1b\n\rauto_exposure\x18\x10 \x01(\x08:\x04true\x12\x15\n\x08exposure\x18\x11 \x01(\x05:\x03100\x12 \n\x12auto_white_balance\x18\x12 \x01(\x08:\x04true\x12\x1b\n\rwhite_balance\x18\x13 \x01(\x05:\x044000\x12\x1a\n\x0fbytes_per_pixel\x18\x14 \x01(\r:\x013\x12\x1b\n\x10trigger_internal\x18\x15 \x01(\r:\x010\x12\x17\n\x0btrigger_fps\x18\x16 \x01(\r:\x0230\x12\x14\n\x0cchannel_name\x18\x17 \x01(\t\x12\x1c\n\x0edevice_wait_ms\x18\x18 \x01(\r:\x042000\x12\x16\n\tspin_rate\x18\x19 \x01(\r:\x03200\x12=\n\x0boutput_type\x18\x1a \x01(\x0e2(.apollo.drivers.camera.config.OutputType\x12J\n\rcompress_conf\x18\x1b \x01(\x0b23.apollo.drivers.camera.config.Config.CompressConfig\x1aE\n\x0eCompressConfig\x12\x16\n\x0eoutput_channel\x18\x01 \x01(\t\x12\x1b\n\x0fimage_pool_size\x18\x02 \x01(\r:\x0220*`\n\x08IOMethod\x12\x15\n\x11IO_METHOD_UNKNOWN\x10\x00\x12\x12\n\x0eIO_METHOD_READ\x10\x01\x12\x12\n\x0eIO_METHOD_MMAP\x10\x02\x12\x15\n\x11IO_METHOD_USERPTR\x10\x03*\x1f\n\nOutputType\x12\x08\n\x04YUYV\x10\x00\x12\x07\n\x03RGB\x10\x01')
_IOMETHOD = DESCRIPTOR.enum_types_by_name['IOMethod']
IOMethod = enum_type_wrapper.EnumTypeWrapper(_IOMETHOD)
_OUTPUTTYPE = DESCRIPTOR.enum_types_by_name['OutputType']
OutputType = enum_type_wrapper.EnumTypeWrapper(_OUTPUTTYPE)
IO_METHOD_UNKNOWN = 0
IO_METHOD_READ = 1
IO_METHOD_MMAP = 2
IO_METHOD_USERPTR = 3
YUYV = 0
RGB = 1
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CONFIG_COMPRESSCONFIG = _CONFIG.nested_types_by_name['CompressConfig']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'CompressConfig': _reflection.GeneratedProtocolMessageType('CompressConfig', (_message.Message,), {'DESCRIPTOR': _CONFIG_COMPRESSCONFIG, '__module__': 'modules.drivers.camera.proto.config_pb2'}), 'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.camera.proto.config_pb2'})
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.CompressConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _IOMETHOD._serialized_start = 929
    _IOMETHOD._serialized_end = 1025
    _OUTPUTTYPE._serialized_start = 1027
    _OUTPUTTYPE._serialized_end = 1058
    _CONFIG._serialized_start = 76
    _CONFIG._serialized_end = 927
    _CONFIG_COMPRESSCONFIG._serialized_start = 858
    _CONFIG_COMPRESSCONFIG._serialized_end = 927