"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/drivers/lidar/proto/robosense.proto\x12\x18apollo.drivers.robosense\x1a!modules/common/proto/header.proto"2\n\x13RobosenseScanPacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\x9e\x01\n\rRobosenseScan\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\r\n\x05model\x18\x02 \x01(\t\x12B\n\x0bfiring_pkts\x18\x03 \x03(\x0b2-.apollo.drivers.robosense.RobosenseScanPacket\x12\x13\n\x08basetime\x18\x04 \x01(\x04:\x010')
_ROBOSENSESCANPACKET = DESCRIPTOR.message_types_by_name['RobosenseScanPacket']
_ROBOSENSESCAN = DESCRIPTOR.message_types_by_name['RobosenseScan']
RobosenseScanPacket = _reflection.GeneratedProtocolMessageType('RobosenseScanPacket', (_message.Message,), {'DESCRIPTOR': _ROBOSENSESCANPACKET, '__module__': 'modules.drivers.lidar.proto.robosense_pb2'})
_sym_db.RegisterMessage(RobosenseScanPacket)
RobosenseScan = _reflection.GeneratedProtocolMessageType('RobosenseScan', (_message.Message,), {'DESCRIPTOR': _ROBOSENSESCAN, '__module__': 'modules.drivers.lidar.proto.robosense_pb2'})
_sym_db.RegisterMessage(RobosenseScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ROBOSENSESCANPACKET._serialized_start = 108
    _ROBOSENSESCANPACKET._serialized_end = 158
    _ROBOSENSESCAN._serialized_start = 161
    _ROBOSENSESCAN._serialized_end = 319