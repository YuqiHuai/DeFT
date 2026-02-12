"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/task_manager/proto/task_manager_config.proto\x12\x13apollo.task_manager"\x85\x01\n\x0bTopicConfig\x12\x1d\n\x15routing_request_topic\x18\x01 \x01(\t\x12\x1e\n\x16routing_response_topic\x18\x02 \x01(\t\x12\x1f\n\x17localization_pose_topic\x18\x03 \x01(\t\x12\x16\n\x0eplanning_topic\x18\x04 \x01(\t"K\n\x11TaskManagerConfig\x126\n\x0ctopic_config\x18\x01 \x01(\x0b2 .apollo.task_manager.TopicConfig')
_TOPICCONFIG = DESCRIPTOR.message_types_by_name['TopicConfig']
_TASKMANAGERCONFIG = DESCRIPTOR.message_types_by_name['TaskManagerConfig']
TopicConfig = _reflection.GeneratedProtocolMessageType('TopicConfig', (_message.Message,), {'DESCRIPTOR': _TOPICCONFIG, '__module__': 'modules.task_manager.proto.task_manager_config_pb2'})
_sym_db.RegisterMessage(TopicConfig)
TaskManagerConfig = _reflection.GeneratedProtocolMessageType('TaskManagerConfig', (_message.Message,), {'DESCRIPTOR': _TASKMANAGERCONFIG, '__module__': 'modules.task_manager.proto.task_manager_config_pb2'})
_sym_db.RegisterMessage(TaskManagerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TOPICCONFIG._serialized_start = 78
    _TOPICCONFIG._serialized_end = 211
    _TASKMANAGERCONFIG._serialized_start = 213
    _TASKMANAGERCONFIG._serialized_end = 288