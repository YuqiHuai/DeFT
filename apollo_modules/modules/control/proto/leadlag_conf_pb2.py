"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/control/proto/leadlag_conf.proto\x12\x0eapollo.control"l\n\x0bLeadlagConf\x12(\n\x1binnerstate_saturation_level\x18\x01 \x01(\x01:\x03300\x12\x12\n\x05alpha\x18\x02 \x01(\x01:\x030.1\x12\x0f\n\x04beta\x18\x03 \x01(\x01:\x011\x12\x0e\n\x03tau\x18\x04 \x01(\x01:\x010')
_LEADLAGCONF = DESCRIPTOR.message_types_by_name['LeadlagConf']
LeadlagConf = _reflection.GeneratedProtocolMessageType('LeadlagConf', (_message.Message,), {'DESCRIPTOR': _LEADLAGCONF, '__module__': 'modules.control.proto.leadlag_conf_pb2'})
_sym_db.RegisterMessage(LeadlagConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LEADLAGCONF._serialized_start = 60
    _LEADLAGCONF._serialized_end = 168