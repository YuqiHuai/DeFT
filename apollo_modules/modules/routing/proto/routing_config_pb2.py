"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*modules/routing/proto/routing_config.proto\x12\x0eapollo.routing"U\n\x0bTopicConfig\x12\x1e\n\x16routing_response_topic\x18\x01 \x01(\t\x12&\n\x1erouting_response_history_topic\x18\x02 \x01(\t"\xda\x01\n\rRoutingConfig\x12\x12\n\nbase_speed\x18\x01 \x01(\x01\x12\x19\n\x11left_turn_penalty\x18\x02 \x01(\x01\x12\x1a\n\x12right_turn_penalty\x18\x03 \x01(\x01\x12\x15\n\ruturn_penalty\x18\x04 \x01(\x01\x12\x16\n\x0echange_penalty\x18\x05 \x01(\x01\x12\x1c\n\x14base_changing_length\x18\x06 \x01(\x01\x121\n\x0ctopic_config\x18\x07 \x01(\x0b2\x1b.apollo.routing.TopicConfig')
_TOPICCONFIG = DESCRIPTOR.message_types_by_name['TopicConfig']
_ROUTINGCONFIG = DESCRIPTOR.message_types_by_name['RoutingConfig']
TopicConfig = _reflection.GeneratedProtocolMessageType('TopicConfig', (_message.Message,), {'DESCRIPTOR': _TOPICCONFIG, '__module__': 'modules.routing.proto.routing_config_pb2'})
_sym_db.RegisterMessage(TopicConfig)
RoutingConfig = _reflection.GeneratedProtocolMessageType('RoutingConfig', (_message.Message,), {'DESCRIPTOR': _ROUTINGCONFIG, '__module__': 'modules.routing.proto.routing_config_pb2'})
_sym_db.RegisterMessage(RoutingConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TOPICCONFIG._serialized_start = 62
    _TOPICCONFIG._serialized_end = 147
    _ROUTINGCONFIG._serialized_start = 150
    _ROUTINGCONFIG._serialized_end = 368