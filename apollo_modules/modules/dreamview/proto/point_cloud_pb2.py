"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/dreamview/proto/point_cloud.proto\x12\x10apollo.dreamview"\x1d\n\nPointCloud\x12\x0f\n\x03num\x18\x01 \x03(\x02B\x02\x10\x01')
_POINTCLOUD = DESCRIPTOR.message_types_by_name['PointCloud']
PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), {'DESCRIPTOR': _POINTCLOUD, '__module__': 'modules.dreamview.proto.point_cloud_pb2'})
_sym_db.RegisterMessage(PointCloud)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POINTCLOUD.fields_by_name['num']._options = None
    _POINTCLOUD.fields_by_name['num']._serialized_options = b'\x10\x01'
    _POINTCLOUD._serialized_start = 63
    _POINTCLOUD._serialized_end = 92