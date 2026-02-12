"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/tools/sensor_calibration/proto/extractor_config.proto"\xa2\x01\n\x08IoConfig\x12\x16\n\ttask_name\x18\x01 \x02(\t:\x03tmp\x12#\n\x0boutput_path\x18\x02 \x02(\t:\x0eextracted_data\x12"\n\x0fstart_timestamp\x18\x03 \x01(\t:\tFLOAT_MIN\x12 \n\rend_timestamp\x18\x04 \x01(\t:\tFLOAT_MAX\x12\x13\n\x0bmain_sensor\x18\x05 \x01(\t"P\n\rChannelConfig\x12\x15\n\x0bdescription\x18\x01 \x01(\t:\x00\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x1a\n\x0fextraction_rate\x18\x03 \x02(\r:\x011"+\n\x08Channels\x12\x1f\n\x07channel\x18\x01 \x03(\x0b2\x0e.ChannelConfig"\x1e\n\x07Records\x12\x13\n\x0brecord_path\x18\x01 \x03(\t"l\n\x14DataExtractionConfig\x12\x1c\n\tio_config\x18\x01 \x02(\x0b2\t.IoConfig\x12\x1b\n\x08channels\x18\x02 \x02(\x0b2\t.Channels\x12\x19\n\x07records\x18\x03 \x02(\x0b2\x08.Records')
_IOCONFIG = DESCRIPTOR.message_types_by_name['IoConfig']
_CHANNELCONFIG = DESCRIPTOR.message_types_by_name['ChannelConfig']
_CHANNELS = DESCRIPTOR.message_types_by_name['Channels']
_RECORDS = DESCRIPTOR.message_types_by_name['Records']
_DATAEXTRACTIONCONFIG = DESCRIPTOR.message_types_by_name['DataExtractionConfig']
IoConfig = _reflection.GeneratedProtocolMessageType('IoConfig', (_message.Message,), {'DESCRIPTOR': _IOCONFIG, '__module__': 'modules.tools.sensor_calibration.proto.extractor_config_pb2'})
_sym_db.RegisterMessage(IoConfig)
ChannelConfig = _reflection.GeneratedProtocolMessageType('ChannelConfig', (_message.Message,), {'DESCRIPTOR': _CHANNELCONFIG, '__module__': 'modules.tools.sensor_calibration.proto.extractor_config_pb2'})
_sym_db.RegisterMessage(ChannelConfig)
Channels = _reflection.GeneratedProtocolMessageType('Channels', (_message.Message,), {'DESCRIPTOR': _CHANNELS, '__module__': 'modules.tools.sensor_calibration.proto.extractor_config_pb2'})
_sym_db.RegisterMessage(Channels)
Records = _reflection.GeneratedProtocolMessageType('Records', (_message.Message,), {'DESCRIPTOR': _RECORDS, '__module__': 'modules.tools.sensor_calibration.proto.extractor_config_pb2'})
_sym_db.RegisterMessage(Records)
DataExtractionConfig = _reflection.GeneratedProtocolMessageType('DataExtractionConfig', (_message.Message,), {'DESCRIPTOR': _DATAEXTRACTIONCONFIG, '__module__': 'modules.tools.sensor_calibration.proto.extractor_config_pb2'})
_sym_db.RegisterMessage(DataExtractionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _IOCONFIG._serialized_start = 66
    _IOCONFIG._serialized_end = 228
    _CHANNELCONFIG._serialized_start = 230
    _CHANNELCONFIG._serialized_end = 310
    _CHANNELS._serialized_start = 312
    _CHANNELS._serialized_end = 355
    _RECORDS._serialized_start = 357
    _RECORDS._serialized_end = 387
    _DATAEXTRACTIONCONFIG._serialized_start = 389
    _DATAEXTRACTIONCONFIG._serialized_end = 497