"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/drivers/proto/pointcloud.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto"h\n\nPointXYZIT\x12\x0e\n\x01x\x18\x01 \x01(\x02:\x03nan\x12\x0e\n\x01y\x18\x02 \x01(\x02:\x03nan\x12\x0e\n\x01z\x18\x03 \x01(\x02:\x03nan\x12\x14\n\tintensity\x18\x04 \x01(\r:\x010\x12\x14\n\ttimestamp\x18\x05 \x01(\x04:\x010"\xbb\x01\n\nPointCloud\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08frame_id\x18\x02 \x01(\t\x12\x10\n\x08is_dense\x18\x03 \x01(\x08\x12)\n\x05point\x18\x04 \x03(\x0b2\x1a.apollo.drivers.PointXYZIT\x12\x18\n\x10measurement_time\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\r\x12\x0e\n\x06height\x18\x07 \x01(\r')
_POINTXYZIT = DESCRIPTOR.message_types_by_name['PointXYZIT']
_POINTCLOUD = DESCRIPTOR.message_types_by_name['PointCloud']
PointXYZIT = _reflection.GeneratedProtocolMessageType('PointXYZIT', (_message.Message,), {'DESCRIPTOR': _POINTXYZIT, '__module__': 'modules.drivers.proto.pointcloud_pb2'})
_sym_db.RegisterMessage(PointXYZIT)
PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), {'DESCRIPTOR': _POINTCLOUD, '__module__': 'modules.drivers.proto.pointcloud_pb2'})
_sym_db.RegisterMessage(PointCloud)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POINTXYZIT._serialized_start = 93
    _POINTXYZIT._serialized_end = 197
    _POINTCLOUD._serialized_start = 200
    _POINTCLOUD._serialized_end = 387