"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/drivers/gnss/proto/imu.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\xca\x01\n\x03Imu\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x1b\n\x10measurement_span\x18\x03 \x01(\x02:\x010\x123\n\x13linear_acceleration\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x120\n\x10angular_velocity\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D')
_IMU = DESCRIPTOR.message_types_by_name['Imu']
Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), {'DESCRIPTOR': _IMU, '__module__': 'modules.drivers.gnss.proto.imu_pb2'})
_sym_db.RegisterMessage(Imu)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _IMU._serialized_start = 134
    _IMU._serialized_end = 336