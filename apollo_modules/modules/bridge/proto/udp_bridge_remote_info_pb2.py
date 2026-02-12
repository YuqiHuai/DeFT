"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/bridge/proto/udp_bridge_remote_info.proto\x12\rapollo.bridge"v\n\x19UDPBridgeSenderRemoteInfo\x12\x1c\n\tremote_ip\x18\x01 \x01(\t:\t127.0.0.1\x12\x19\n\x0bremote_port\x18\x02 \x01(\x05:\x048900\x12 \n\nproto_name\x18\x03 \x01(\t:\x0cProtoMsgName"\x8c\x01\n\x1bUDPBridgeReceiverRemoteInfo\x12\x14\n\ntopic_name\x18\x01 \x01(\t:\x00\x12\x17\n\tbind_port\x18\x02 \x01(\x05:\x048500\x12 \n\nproto_name\x18\x03 \x01(\t:\x0cProtoMsgName\x12\x1c\n\x0eenable_timeout\x18\x04 \x01(\x08:\x04true')
_UDPBRIDGESENDERREMOTEINFO = DESCRIPTOR.message_types_by_name['UDPBridgeSenderRemoteInfo']
_UDPBRIDGERECEIVERREMOTEINFO = DESCRIPTOR.message_types_by_name['UDPBridgeReceiverRemoteInfo']
UDPBridgeSenderRemoteInfo = _reflection.GeneratedProtocolMessageType('UDPBridgeSenderRemoteInfo', (_message.Message,), {'DESCRIPTOR': _UDPBRIDGESENDERREMOTEINFO, '__module__': 'modules.bridge.proto.udp_bridge_remote_info_pb2'})
_sym_db.RegisterMessage(UDPBridgeSenderRemoteInfo)
UDPBridgeReceiverRemoteInfo = _reflection.GeneratedProtocolMessageType('UDPBridgeReceiverRemoteInfo', (_message.Message,), {'DESCRIPTOR': _UDPBRIDGERECEIVERREMOTEINFO, '__module__': 'modules.bridge.proto.udp_bridge_remote_info_pb2'})
_sym_db.RegisterMessage(UDPBridgeReceiverRemoteInfo)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _UDPBRIDGESENDERREMOTEINFO._serialized_start = 68
    _UDPBRIDGESENDERREMOTEINFO._serialized_end = 186
    _UDPBRIDGERECEIVERREMOTEINFO._serialized_start = 189
    _UDPBRIDGERECEIVERREMOTEINFO._serialized_end = 329