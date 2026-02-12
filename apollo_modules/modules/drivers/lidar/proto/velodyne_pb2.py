"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*modules/drivers/lidar/proto/velodyne.proto\x12\x17apollo.drivers.velodyne\x1a!modules/common/proto/header.proto"-\n\x0eVelodynePacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\xb3\x02\n\x0cVelodyneScan\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12-\n\x05model\x18\x02 \x01(\x0e2\x1e.apollo.drivers.velodyne.Model\x12+\n\x04mode\x18\x03 \x01(\x0e2\x1d.apollo.drivers.velodyne.Mode\x12<\n\x0bfiring_pkts\x18\x04 \x03(\x0b2\'.apollo.drivers.velodyne.VelodynePacket\x12A\n\x10positioning_pkts\x18\x05 \x03(\x0b2\'.apollo.drivers.velodyne.VelodynePacket\x12\n\n\x02sn\x18\x06 \x01(\t\x12\x13\n\x08basetime\x18\x07 \x01(\x04:\x010*r\n\x05Model\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nHDL64E_S3S\x10\x01\x12\x0e\n\nHDL64E_S3D\x10\x02\x12\r\n\tHDL64E_S2\x10\x03\x12\n\n\x06HDL32E\x10\x04\x12\t\n\x05VLP16\x10\x05\x12\n\n\x06VLP32C\x10\x06\x12\n\n\x06VLS128\x10\x07*)\n\x04Mode\x12\r\n\tSTRONGEST\x10\x01\x12\x08\n\x04LAST\x10\x02\x12\x08\n\x04DUAL\x10\x03')
_MODEL = DESCRIPTOR.enum_types_by_name['Model']
Model = enum_type_wrapper.EnumTypeWrapper(_MODEL)
_MODE = DESCRIPTOR.enum_types_by_name['Mode']
Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
UNKNOWN = 0
HDL64E_S3S = 1
HDL64E_S3D = 2
HDL64E_S2 = 3
HDL32E = 4
VLP16 = 5
VLP32C = 6
VLS128 = 7
STRONGEST = 1
LAST = 2
DUAL = 3
_VELODYNEPACKET = DESCRIPTOR.message_types_by_name['VelodynePacket']
_VELODYNESCAN = DESCRIPTOR.message_types_by_name['VelodyneScan']
VelodynePacket = _reflection.GeneratedProtocolMessageType('VelodynePacket', (_message.Message,), {'DESCRIPTOR': _VELODYNEPACKET, '__module__': 'modules.drivers.lidar.proto.velodyne_pb2'})
_sym_db.RegisterMessage(VelodynePacket)
VelodyneScan = _reflection.GeneratedProtocolMessageType('VelodyneScan', (_message.Message,), {'DESCRIPTOR': _VELODYNESCAN, '__module__': 'modules.drivers.lidar.proto.velodyne_pb2'})
_sym_db.RegisterMessage(VelodyneScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MODEL._serialized_start = 463
    _MODEL._serialized_end = 577
    _MODE._serialized_start = 579
    _MODE._serialized_end = 620
    _VELODYNEPACKET._serialized_start = 106
    _VELODYNEPACKET._serialized_end = 151
    _VELODYNESCAN._serialized_start = 154
    _VELODYNESCAN._serialized_end = 461