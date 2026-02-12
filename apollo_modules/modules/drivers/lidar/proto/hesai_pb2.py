"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/drivers/lidar/proto/hesai.proto\x12\x14apollo.drivers.hesai\x1a!modules/common/proto/header.proto".\n\x0fHesaiScanPacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\xaf\x01\n\tHesaiScan\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12*\n\x05model\x18\x02 \x01(\x0e2\x1b.apollo.drivers.hesai.Model\x12:\n\x0bfiring_pkts\x18\x03 \x03(\x0b2%.apollo.drivers.hesai.HesaiScanPacket\x12\x13\n\x08basetime\x18\x04 \x01(\x04:\x010*/\n\x05Model\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08HESAI40P\x10\x01\x12\x0b\n\x07HESAI64\x10\x02')
_MODEL = DESCRIPTOR.enum_types_by_name['Model']
Model = enum_type_wrapper.EnumTypeWrapper(_MODEL)
UNKNOWN = 0
HESAI40P = 1
HESAI64 = 2
_HESAISCANPACKET = DESCRIPTOR.message_types_by_name['HesaiScanPacket']
_HESAISCAN = DESCRIPTOR.message_types_by_name['HesaiScan']
HesaiScanPacket = _reflection.GeneratedProtocolMessageType('HesaiScanPacket', (_message.Message,), {'DESCRIPTOR': _HESAISCANPACKET, '__module__': 'modules.drivers.lidar.proto.hesai_pb2'})
_sym_db.RegisterMessage(HesaiScanPacket)
HesaiScan = _reflection.GeneratedProtocolMessageType('HesaiScan', (_message.Message,), {'DESCRIPTOR': _HESAISCAN, '__module__': 'modules.drivers.lidar.proto.hesai_pb2'})
_sym_db.RegisterMessage(HesaiScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MODEL._serialized_start = 326
    _MODEL._serialized_end = 373
    _HESAISCANPACKET._serialized_start = 100
    _HESAISCANPACKET._serialized_end = 146
    _HESAISCAN._serialized_start = 149
    _HESAISCAN._serialized_end = 324