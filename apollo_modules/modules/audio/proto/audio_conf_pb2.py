"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/audio/proto/audio_conf.proto\x12\x0capollo.audio"\xae\x01\n\tTopicConf\x12\x1d\n\x15audio_data_topic_name\x18\x01 \x01(\t\x12"\n\x1aaudio_detection_topic_name\x18\x02 \x01(\t\x12\x1f\n\x17localization_topic_name\x18\x03 \x01(\t\x12\x1e\n\x16audio_event_topic_name\x18\x04 \x01(\t\x12\x1d\n\x15perception_topic_name\x18\x05 \x01(\t"[\n\tAudioConf\x12+\n\ntopic_conf\x18\x01 \x01(\x0b2\x17.apollo.audio.TopicConf\x12!\n\x19respeaker_extrinsics_path\x18\x02 \x01(\t')
_TOPICCONF = DESCRIPTOR.message_types_by_name['TopicConf']
_AUDIOCONF = DESCRIPTOR.message_types_by_name['AudioConf']
TopicConf = _reflection.GeneratedProtocolMessageType('TopicConf', (_message.Message,), {'DESCRIPTOR': _TOPICCONF, '__module__': 'modules.audio.proto.audio_conf_pb2'})
_sym_db.RegisterMessage(TopicConf)
AudioConf = _reflection.GeneratedProtocolMessageType('AudioConf', (_message.Message,), {'DESCRIPTOR': _AUDIOCONF, '__module__': 'modules.audio.proto.audio_conf_pb2'})
_sym_db.RegisterMessage(AudioConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TOPICCONF._serialized_start = 55
    _TOPICCONF._serialized_end = 229
    _AUDIOCONF._serialized_start = 231
    _AUDIOCONF._serialized_end = 322