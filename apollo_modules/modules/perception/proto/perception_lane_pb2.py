"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.perception.proto import perception_camera_pb2 as modules_dot_perception_dot_proto_dot_perception__camera__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/perception/proto/perception_lane.proto\x12\x11apollo.perception\x1a!modules/common/proto/header.proto\x1a0modules/perception/proto/perception_camera.proto"\xa3\x02\n\x0fPerceptionLanes\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x14\n\x0csource_topic\x18\x02 \x01(\t\x12I\n\nerror_code\x18\x03 \x01(\x0e2).apollo.perception.camera.CameraErrorCode:\nERROR_NONE\x12E\n\x11camera_calibrator\x18\x04 \x01(\x0b2*.apollo.perception.camera.CameraCalibrator\x12A\n\x0fcamera_laneline\x18\x05 \x03(\x0b2(.apollo.perception.camera.CameraLaneLine')
_PERCEPTIONLANES = DESCRIPTOR.message_types_by_name['PerceptionLanes']
PerceptionLanes = _reflection.GeneratedProtocolMessageType('PerceptionLanes', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONLANES, '__module__': 'modules.perception.proto.perception_lane_pb2'})
_sym_db.RegisterMessage(PerceptionLanes)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PERCEPTIONLANES._serialized_start = 155
    _PERCEPTIONLANES._serialized_end = 446