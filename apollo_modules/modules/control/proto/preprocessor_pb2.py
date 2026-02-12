"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import drive_state_pb2 as modules_dot_common_dot_proto_dot_drive__state__pb2
from ....modules.control.proto import input_debug_pb2 as modules_dot_control_dot_proto_dot_input__debug__pb2
from ....modules.control.proto import local_view_pb2 as modules_dot_control_dot_proto_dot_local__view__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/control/proto/preprocessor.proto\x12\x0eapollo.control\x1a!modules/common/proto/header.proto\x1a&modules/common/proto/drive_state.proto\x1a\'modules/control/proto/input_debug.proto\x1a&modules/control/proto/local_view.proto"\x96\x02\n\x0cPreprocessor\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12-\n\nlocal_view\x18\x02 \x01(\x0b2\x19.apollo.control.LocalView\x122\n\rengage_advice\x18\x04 \x01(\x0b2\x1b.apollo.common.EngageAdvice\x12/\n\x0binput_debug\x18\x05 \x01(\x0b2\x1a.apollo.control.InputDebug\x12\x1f\n\x10received_pad_msg\x18\x06 \x01(\x08:\x05false\x12\x14\n\x05estop\x18\x07 \x01(\x08:\x05false\x12\x14\n\x0cestop_reason\x18\x08 \x01(\t')
_PREPROCESSOR = DESCRIPTOR.message_types_by_name['Preprocessor']
Preprocessor = _reflection.GeneratedProtocolMessageType('Preprocessor', (_message.Message,), {'DESCRIPTOR': _PREPROCESSOR, '__module__': 'modules.control.proto.preprocessor_pb2'})
_sym_db.RegisterMessage(Preprocessor)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PREPROCESSOR._serialized_start = 217
    _PREPROCESSOR._serialized_end = 495