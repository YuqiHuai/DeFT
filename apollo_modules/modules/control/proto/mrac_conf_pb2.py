"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/control/proto/mrac_conf.proto\x12\x0eapollo.control"\xef\x02\n\x08MracConf\x12\x1b\n\x10mrac_model_order\x18\x01 \x01(\x05:\x011\x12\x1f\n\x17reference_time_constant\x18\x02 \x01(\x01\x12#\n\x1breference_natural_frequency\x18\x03 \x01(\x01\x12\x1f\n\x17reference_damping_ratio\x18\x04 \x01(\x01\x12\x1b\n\x13adaption_state_gain\x18\x05 \x03(\x01\x12\x1d\n\x15adaption_desired_gain\x18\x06 \x01(\x01\x12\x1f\n\x17adaption_nonlinear_gain\x18\x07 \x01(\x01\x12\x19\n\x11adaption_matrix_p\x18\x08 \x03(\x01\x12 \n\x15mrac_saturation_level\x18\t \x01(\x01:\x011\x12%\n\x1danti_windup_compensation_gain\x18\n \x03(\x01\x12\x1e\n\x16clamping_time_constant\x18\x0b \x01(\x01')
_MRACCONF = DESCRIPTOR.message_types_by_name['MracConf']
MracConf = _reflection.GeneratedProtocolMessageType('MracConf', (_message.Message,), {'DESCRIPTOR': _MRACCONF, '__module__': 'modules.control.proto.mrac_conf_pb2'})
_sym_db.RegisterMessage(MracConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MRACCONF._serialized_start = 58
    _MRACCONF._serialized_end = 425