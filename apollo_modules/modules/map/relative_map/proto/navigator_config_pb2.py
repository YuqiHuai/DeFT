"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/map/relative_map/proto/navigator_config.proto\x12\x13apollo.relative_map"\x83\x02\n\x0bSampleParam\x12#\n\x18straight_sample_interval\x18\x01 \x01(\x01:\x013\x12&\n\x1bsmall_kappa_sample_interval\x18\x02 \x01(\x01:\x011\x12)\n\x1cmiddle_kappa_sample_interval\x18\x03 \x01(\x01:\x030.4\x12(\n\x1blarge_kappa_sample_interval\x18\x04 \x01(\x01:\x030.1\x12\x1a\n\x0bsmall_kappa\x18\x05 \x01(\x01:\x050.002\x12\x1b\n\x0cmiddle_kappa\x18\x06 \x01(\x01:\x050.008\x12\x19\n\x0blarge_kappa\x18\x07 \x01(\x01:\x040.02"t\n\x0fNavigatorConfig\x12)\n\x1benable_navigator_downsample\x18\x01 \x01(\x08:\x04true\x126\n\x0csample_param\x18\x02 \x01(\x0b2 .apollo.relative_map.SampleParam')
_SAMPLEPARAM = DESCRIPTOR.message_types_by_name['SampleParam']
_NAVIGATORCONFIG = DESCRIPTOR.message_types_by_name['NavigatorConfig']
SampleParam = _reflection.GeneratedProtocolMessageType('SampleParam', (_message.Message,), {'DESCRIPTOR': _SAMPLEPARAM, '__module__': 'modules.map.relative_map.proto.navigator_config_pb2'})
_sym_db.RegisterMessage(SampleParam)
NavigatorConfig = _reflection.GeneratedProtocolMessageType('NavigatorConfig', (_message.Message,), {'DESCRIPTOR': _NAVIGATORCONFIG, '__module__': 'modules.map.relative_map.proto.navigator_config_pb2'})
_sym_db.RegisterMessage(NavigatorConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SAMPLEPARAM._serialized_start = 79
    _SAMPLEPARAM._serialized_end = 338
    _NAVIGATORCONFIG._serialized_start = 340
    _NAVIGATORCONFIG._serialized_end = 456