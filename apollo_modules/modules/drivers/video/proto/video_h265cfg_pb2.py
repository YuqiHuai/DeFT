"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/drivers/video/proto/video_h265cfg.proto\x12\x1bapollo.drivers.video.config"\xf0\x05\n\x10CameraH265Config\x12\x10\n\x08udp_port\x18\x01 \x02(\r\x12\x10\n\x08frame_id\x18\x02 \x02(\t\x12\x1a\n\x0cpixel_format\x18\x03 \x02(\t:\x04yuyv\x12\x0e\n\x06record\x18\x04 \x02(\r\x12\r\n\x05width\x18\x05 \x02(\r\x12\x0e\n\x06height\x18\x06 \x02(\r\x12\x12\n\nframe_rate\x18\x07 \x02(\r\x12\x19\n\nmonochrome\x18\x08 \x02(\x08:\x05false\x12\x16\n\nbrightness\x18\t \x02(\x05:\x02-1\x12\x14\n\x08contrast\x18\n \x02(\x05:\x02-1\x12\x16\n\nsaturation\x18\x0b \x02(\x05:\x02-1\x12\x15\n\tsharpness\x18\x0c \x02(\x05:\x02-1\x12\x10\n\x04gain\x18\r \x02(\x05:\x02-1\x12\x19\n\nauto_focus\x18\x0e \x02(\x08:\x05false\x12\x11\n\x05focus\x18\x0f \x02(\x05:\x02-1\x12\x1b\n\rauto_exposure\x18\x10 \x02(\x08:\x04true\x12\x15\n\x08exposure\x18\x11 \x02(\x05:\x03100\x12 \n\x12auto_white_balance\x18\x12 \x02(\x08:\x04true\x12\x1b\n\rwhite_balance\x18\x13 \x02(\x05:\x044000\x12\x1a\n\x0fbytes_per_pixel\x18\x14 \x02(\r:\x013\x12\x1b\n\rtrigger_param\x18\x15 \x02(\t:\x04f2ff\x12\x1d\n\x11metric_error_code\x18\x16 \x02(\r:\x0211\x12\x1b\n\x0ffpga_dev_number\x18\x17 \x02(\x05:\x02-1\x12\x1d\n\x11camera_seq_number\x18\x18 \x02(\x05:\x02-1\x12S\n\rcompress_conf\x18\x19 \x01(\x0b2<.apollo.drivers.video.config.CameraH265Config.CompressConfig\x1aE\n\x0eCompressConfig\x12\x16\n\x0eoutput_channel\x18\x01 \x01(\t\x12\x1b\n\x0fimage_pool_size\x18\x02 \x01(\r:\x0220')
_CAMERAH265CONFIG = DESCRIPTOR.message_types_by_name['CameraH265Config']
_CAMERAH265CONFIG_COMPRESSCONFIG = _CAMERAH265CONFIG.nested_types_by_name['CompressConfig']
CameraH265Config = _reflection.GeneratedProtocolMessageType('CameraH265Config', (_message.Message,), {'CompressConfig': _reflection.GeneratedProtocolMessageType('CompressConfig', (_message.Message,), {'DESCRIPTOR': _CAMERAH265CONFIG_COMPRESSCONFIG, '__module__': 'modules.drivers.video.proto.video_h265cfg_pb2'}), 'DESCRIPTOR': _CAMERAH265CONFIG, '__module__': 'modules.drivers.video.proto.video_h265cfg_pb2'})
_sym_db.RegisterMessage(CameraH265Config)
_sym_db.RegisterMessage(CameraH265Config.CompressConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CAMERAH265CONFIG._serialized_start = 81
    _CAMERAH265CONFIG._serialized_end = 833
    _CAMERAH265CONFIG_COMPRESSCONFIG._serialized_start = 764
    _CAMERAH265CONFIG_COMPRESSCONFIG._serialized_end = 833