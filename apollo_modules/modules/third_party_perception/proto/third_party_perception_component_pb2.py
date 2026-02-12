"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKmodules/third_party_perception/proto/third_party_perception_component.proto\x12\x1dapollo.third_party_perception"p\n\x1aThirdPartyPerceptionDevice\x12R\n\x0bdevice_type\x18\x01 \x01(\x0e2=.apollo.third_party_perception.ThirdPartyPerceptionDeviceType*>\n\x1eThirdPartyPerceptionDeviceType\x12\x0e\n\nSMARTEREYE\x10\x00\x12\x0c\n\x08MOBILEYE\x10\x01')
_THIRDPARTYPERCEPTIONDEVICETYPE = DESCRIPTOR.enum_types_by_name['ThirdPartyPerceptionDeviceType']
ThirdPartyPerceptionDeviceType = enum_type_wrapper.EnumTypeWrapper(_THIRDPARTYPERCEPTIONDEVICETYPE)
SMARTEREYE = 0
MOBILEYE = 1
_THIRDPARTYPERCEPTIONDEVICE = DESCRIPTOR.message_types_by_name['ThirdPartyPerceptionDevice']
ThirdPartyPerceptionDevice = _reflection.GeneratedProtocolMessageType('ThirdPartyPerceptionDevice', (_message.Message,), {'DESCRIPTOR': _THIRDPARTYPERCEPTIONDEVICE, '__module__': 'modules.third_party_perception.proto.third_party_perception_component_pb2'})
_sym_db.RegisterMessage(ThirdPartyPerceptionDevice)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _THIRDPARTYPERCEPTIONDEVICETYPE._serialized_start = 224
    _THIRDPARTYPERCEPTIONDEVICETYPE._serialized_end = 286
    _THIRDPARTYPERCEPTIONDEVICE._serialized_start = 110
    _THIRDPARTYPERCEPTIONDEVICE._serialized_end = 222