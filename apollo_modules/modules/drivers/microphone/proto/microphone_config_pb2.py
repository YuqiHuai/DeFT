"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/drivers/microphone/proto/microphone_config.proto\x12 apollo.drivers.microphone.config"\xf4\x02\n\x10MicrophoneConfig\x12\\\n\x10microphone_model\x18\x02 \x01(\x0e2B.apollo.drivers.microphone.config.MicrophoneConfig.MicrophoneModel\x12\r\n\x05chunk\x18\x03 \x01(\x05\x12\x13\n\x0bsample_rate\x18\x04 \x01(\x02\x12\x16\n\x0erecord_seconds\x18\x05 \x01(\x02\x12\x14\n\x0csample_width\x18\x06 \x01(\x05\x12\x14\n\x0cchannel_name\x18\x07 \x01(\t\x12\x10\n\x08frame_id\x18\x08 \x01(\t\x12\x14\n\x0cmic_distance\x18\t \x01(\x02\x12C\n\x0cchannel_type\x18\x01 \x03(\x0e2-.apollo.drivers.microphone.config.ChannelType"-\n\x0fMicrophoneModel\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tRESPEAKER\x10\x01*:\n\x0bChannelType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03ASR\x10\x01\x12\x07\n\x03RAW\x10\x02\x12\x0c\n\x08PLAYBACK\x10\x03')
_CHANNELTYPE = DESCRIPTOR.enum_types_by_name['ChannelType']
ChannelType = enum_type_wrapper.EnumTypeWrapper(_CHANNELTYPE)
UNKNOWN = 0
ASR = 1
RAW = 2
PLAYBACK = 3
_MICROPHONECONFIG = DESCRIPTOR.message_types_by_name['MicrophoneConfig']
_MICROPHONECONFIG_MICROPHONEMODEL = _MICROPHONECONFIG.enum_types_by_name['MicrophoneModel']
MicrophoneConfig = _reflection.GeneratedProtocolMessageType('MicrophoneConfig', (_message.Message,), {'DESCRIPTOR': _MICROPHONECONFIG, '__module__': 'modules.drivers.microphone.proto.microphone_config_pb2'})
_sym_db.RegisterMessage(MicrophoneConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CHANNELTYPE._serialized_start = 469
    _CHANNELTYPE._serialized_end = 527
    _MICROPHONECONFIG._serialized_start = 95
    _MICROPHONECONFIG._serialized_end = 467
    _MICROPHONECONFIG_MICROPHONEMODEL._serialized_start = 422
    _MICROPHONECONFIG_MICROPHONEMODEL._serialized_end = 467