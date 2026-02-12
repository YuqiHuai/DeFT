"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/control/proto/input_debug.proto\x12\x0eapollo.control\x1a!modules/common/proto/header.proto"\xe0\x01\n\nInputDebug\x122\n\x13localization_header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12,\n\rcanbus_header\x18\x02 \x01(\x0b2\x15.apollo.common.Header\x120\n\x11trajectory_header\x18\x03 \x01(\x0b2\x15.apollo.common.Header\x12>\n\x1flatest_replan_trajectory_header\x18\x04 \x01(\x0b2\x15.apollo.common.Header')
_INPUTDEBUG = DESCRIPTOR.message_types_by_name['InputDebug']
InputDebug = _reflection.GeneratedProtocolMessageType('InputDebug', (_message.Message,), {'DESCRIPTOR': _INPUTDEBUG, '__module__': 'modules.control.proto.input_debug_pb2'})
_sym_db.RegisterMessage(InputDebug)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _INPUTDEBUG._serialized_start = 95
    _INPUTDEBUG._serialized_end = 319