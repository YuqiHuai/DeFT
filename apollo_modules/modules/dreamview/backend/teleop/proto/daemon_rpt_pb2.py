"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7modules/dreamview/backend/teleop/proto/daemon_rpt.proto\x12\x15modules.teleop.daemon\x1a!modules/common/proto/header.proto"D\n\tDaemonRpt\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08services\x18\x02 \x03(\t')
_DAEMONRPT = DESCRIPTOR.message_types_by_name['DaemonRpt']
DaemonRpt = _reflection.GeneratedProtocolMessageType('DaemonRpt', (_message.Message,), {'DESCRIPTOR': _DAEMONRPT, '__module__': 'modules.dreamview.backend.teleop.proto.daemon_rpt_pb2'})
_sym_db.RegisterMessage(DaemonRpt)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DAEMONRPT._serialized_start = 117
    _DAEMONRPT._serialized_end = 185