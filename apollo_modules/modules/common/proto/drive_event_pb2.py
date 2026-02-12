"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.localization.proto import pose_pb2 as modules_dot_localization_dot_proto_dot_pose__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/common/proto/drive_event.proto\x12\rapollo.common\x1a!modules/common/proto/header.proto\x1a%modules/localization/proto/pose.proto"\xf6\x01\n\nDriveEvent\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\r\n\x05event\x18\x02 \x01(\t\x12+\n\x08location\x18\x03 \x01(\x0b2\x19.apollo.localization.Pose\x12,\n\x04type\x18\x04 \x03(\x0e2\x1e.apollo.common.DriveEvent.Type\x12\x15\n\ris_reportable\x18\x05 \x01(\x08"@\n\x04Type\x12\x0c\n\x08CRITICAL\x10\x00\x12\x0b\n\x07PROBLEM\x10\x01\x12\x0b\n\x07DESIRED\x10\x02\x12\x10\n\x0cOUT_OF_SCOPE\x10\x03')
_DRIVEEVENT = DESCRIPTOR.message_types_by_name['DriveEvent']
_DRIVEEVENT_TYPE = _DRIVEEVENT.enum_types_by_name['Type']
DriveEvent = _reflection.GeneratedProtocolMessageType('DriveEvent', (_message.Message,), {'DESCRIPTOR': _DRIVEEVENT, '__module__': 'modules.common.proto.drive_event_pb2'})
_sym_db.RegisterMessage(DriveEvent)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DRIVEEVENT._serialized_start = 132
    _DRIVEEVENT._serialized_end = 378
    _DRIVEEVENT_TYPE._serialized_start = 314
    _DRIVEEVENT_TYPE._serialized_end = 378