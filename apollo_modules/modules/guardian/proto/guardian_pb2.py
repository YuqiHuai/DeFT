"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.control.proto import control_cmd_pb2 as modules_dot_control_dot_proto_dot_control__cmd__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/guardian/proto/guardian.proto\x12\x0fapollo.guardian\x1a!modules/common/proto/header.proto\x1a\'modules/control/proto/control_cmd.proto"q\n\x0fGuardianCommand\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x127\n\x0fcontrol_command\x18\x02 \x01(\x0b2\x1e.apollo.control.ControlCommand')
_GUARDIANCOMMAND = DESCRIPTOR.message_types_by_name['GuardianCommand']
GuardianCommand = _reflection.GeneratedProtocolMessageType('GuardianCommand', (_message.Message,), {'DESCRIPTOR': _GUARDIANCOMMAND, '__module__': 'modules.guardian.proto.guardian_pb2'})
_sym_db.RegisterMessage(GuardianCommand)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GUARDIANCOMMAND._serialized_start = 134
    _GUARDIANCOMMAND._serialized_end = 247