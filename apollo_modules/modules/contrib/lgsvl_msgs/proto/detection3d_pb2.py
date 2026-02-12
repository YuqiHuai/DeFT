"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from .....modules.contrib.lgsvl_msgs.proto import detection2d_pb2 as modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/contrib/lgsvl_msgs/proto/detection3d.proto\x12\x19apollo.contrib.lgsvl_msgs\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\x1a2modules/contrib/lgsvl_msgs/proto/detection2d.proto"`\n\x04Pose\x12(\n\x08position\x18\x01 \x01(\x0b2\x16.apollo.common.Point3D\x12.\n\x0borientation\x18\x02 \x01(\x0b2\x19.apollo.common.Quaternion"t\n\rBoundingBox3D\x121\n\x08position\x18\x01 \x01(\x0b2\x1f.apollo.contrib.lgsvl_msgs.Pose\x120\n\x04size\x18\x02 \x01(\x0b2".apollo.contrib.lgsvl_msgs.Vector3"\xca\x01\n\x0bDetection3D\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05label\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x01\x126\n\x04bbox\x18\x05 \x01(\x0b2(.apollo.contrib.lgsvl_msgs.BoundingBox3D\x122\n\x08velocity\x18\x06 \x01(\x0b2 .apollo.contrib.lgsvl_msgs.Twistb\x06proto3')
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_BOUNDINGBOX3D = DESCRIPTOR.message_types_by_name['BoundingBox3D']
_DETECTION3D = DESCRIPTOR.message_types_by_name['Detection3D']
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {'DESCRIPTOR': _POSE, '__module__': 'modules.contrib.lgsvl_msgs.proto.detection3d_pb2'})
_sym_db.RegisterMessage(Pose)
BoundingBox3D = _reflection.GeneratedProtocolMessageType('BoundingBox3D', (_message.Message,), {'DESCRIPTOR': _BOUNDINGBOX3D, '__module__': 'modules.contrib.lgsvl_msgs.proto.detection3d_pb2'})
_sym_db.RegisterMessage(BoundingBox3D)
Detection3D = _reflection.GeneratedProtocolMessageType('Detection3D', (_message.Message,), {'DESCRIPTOR': _DETECTION3D, '__module__': 'modules.contrib.lgsvl_msgs.proto.detection3d_pb2'})
_sym_db.RegisterMessage(Detection3D)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POSE._serialized_start = 205
    _POSE._serialized_end = 301
    _BOUNDINGBOX3D._serialized_start = 303
    _BOUNDINGBOX3D._serialized_end = 419
    _DETECTION3D._serialized_start = 422
    _DETECTION3D._serialized_end = 624