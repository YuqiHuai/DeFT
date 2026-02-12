"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/localization/proto/pose.proto\x12\x13apollo.localization\x1a#modules/common/proto/geometry.proto"\xa7\x03\n\x04Pose\x12)\n\x08position\x18\x01 \x01(\x0b2\x17.apollo.common.PointENU\x12.\n\x0borientation\x18\x02 \x01(\x0b2\x19.apollo.common.Quaternion\x12/\n\x0flinear_velocity\x18\x03 \x01(\x0b2\x16.apollo.common.Point3D\x123\n\x13linear_acceleration\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x120\n\x10angular_velocity\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x12\x0f\n\x07heading\x18\x06 \x01(\x01\x127\n\x17linear_acceleration_vrf\x18\x07 \x01(\x0b2\x16.apollo.common.Point3D\x124\n\x14angular_velocity_vrf\x18\x08 \x01(\x0b2\x16.apollo.common.Point3D\x12,\n\x0ceuler_angles\x18\t \x01(\x0b2\x16.apollo.common.Point3D')
_POSE = DESCRIPTOR.message_types_by_name['Pose']
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {'DESCRIPTOR': _POSE, '__module__': 'modules.localization.proto.pose_pb2'})
_sym_db.RegisterMessage(Pose)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POSE._serialized_start = 100
    _POSE._serialized_end = 523