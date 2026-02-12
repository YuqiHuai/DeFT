"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.localization.proto import pose_pb2 as modules_dot_localization_dot_proto_dot_pose__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/localization/proto/imu.proto\x12\x13apollo.localization\x1a!modules/common/proto/header.proto\x1a%modules/localization/proto/pose.proto"]\n\x0cCorrectedImu\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12&\n\x03imu\x18\x03 \x01(\x0b2\x19.apollo.localization.Pose')
_CORRECTEDIMU = DESCRIPTOR.message_types_by_name['CorrectedImu']
CorrectedImu = _reflection.GeneratedProtocolMessageType('CorrectedImu', (_message.Message,), {'DESCRIPTOR': _CORRECTEDIMU, '__module__': 'modules.localization.proto.imu_pb2'})
_sym_db.RegisterMessage(CorrectedImu)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CORRECTEDIMU._serialized_start = 135
    _CORRECTEDIMU._serialized_end = 228