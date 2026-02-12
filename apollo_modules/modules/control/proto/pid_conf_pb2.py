"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/control/proto/pid_conf.proto\x12\x0eapollo.control"\x9e\x01\n\x07PidConf\x12\x19\n\x11integrator_enable\x18\x01 \x01(\x08\x12#\n\x1bintegrator_saturation_level\x18\x02 \x01(\x01\x12\n\n\x02kp\x18\x03 \x01(\x01\x12\n\n\x02ki\x18\x04 \x01(\x01\x12\n\n\x02kd\x18\x05 \x01(\x01\x12\x0e\n\x03kaw\x18\x06 \x01(\x01:\x010\x12\x1f\n\x17output_saturation_level\x18\x07 \x01(\x01')
_PIDCONF = DESCRIPTOR.message_types_by_name['PidConf']
PidConf = _reflection.GeneratedProtocolMessageType('PidConf', (_message.Message,), {'DESCRIPTOR': _PIDCONF, '__module__': 'modules.control.proto.pid_conf_pb2'})
_sym_db.RegisterMessage(PidConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PIDCONF._serialized_start = 57
    _PIDCONF._serialized_end = 215