"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/perception/onboard/proto/motion_service.proto\x12\x19apollo.perception.onboard"\x85\x02\n\rMotionService\x12\x1f\n\x0ccamera_names\x18\x01 \x01(\t:\tfront_6mm\x12I\n\x1ainput_camera_channel_names\x18\x02 \x01(\t:%/apollo/sensor/camera/front_6mm/image\x12B\n\x1finput_localization_channel_name\x18\x03 \x01(\t:\x19/apollo/localization/pose\x12D\n\x19output_topic_channel_name\x18\x04 \x01(\t:!/apollo/perception/motion_service')
_MOTIONSERVICE = DESCRIPTOR.message_types_by_name['MotionService']
MotionService = _reflection.GeneratedProtocolMessageType('MotionService', (_message.Message,), {'DESCRIPTOR': _MOTIONSERVICE, '__module__': 'modules.perception.onboard.proto.motion_service_pb2'})
_sym_db.RegisterMessage(MotionService)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MOTIONSERVICE._serialized_start = 85
    _MOTIONSERVICE._serialized_end = 346