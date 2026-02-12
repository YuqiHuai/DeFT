"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/storytelling/proto/storytelling_config.proto\x12\x13apollo.storytelling"L\n\x0bTopicConfig\x12!\n\x19planning_trajectory_topic\x18\x01 \x01(\t\x12\x1a\n\x12storytelling_topic\x18\x02 \x01(\t"L\n\x12StorytellingConfig\x126\n\x0ctopic_config\x18\x01 \x01(\x0b2 .apollo.storytelling.TopicConfig')
_TOPICCONFIG = DESCRIPTOR.message_types_by_name['TopicConfig']
_STORYTELLINGCONFIG = DESCRIPTOR.message_types_by_name['StorytellingConfig']
TopicConfig = _reflection.GeneratedProtocolMessageType('TopicConfig', (_message.Message,), {'DESCRIPTOR': _TOPICCONFIG, '__module__': 'modules.storytelling.proto.storytelling_config_pb2'})
_sym_db.RegisterMessage(TopicConfig)
StorytellingConfig = _reflection.GeneratedProtocolMessageType('StorytellingConfig', (_message.Message,), {'DESCRIPTOR': _STORYTELLINGCONFIG, '__module__': 'modules.storytelling.proto.storytelling_config_pb2'})
_sym_db.RegisterMessage(StorytellingConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TOPICCONFIG._serialized_start = 77
    _TOPICCONFIG._serialized_end = 153
    _STORYTELLINGCONFIG._serialized_start = 155
    _STORYTELLINGCONFIG._serialized_end = 231