"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/drivers/gnss/proto/ins.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"V\n\x07InsStat\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x12\n\nins_status\x18\x02 \x01(\r\x12\x10\n\x08pos_type\x18\x03 \x01(\r"\xd6\x04\n\x03Ins\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12+\n\x04type\x18\x03 \x01(\x0e2\x1d.apollo.drivers.gnss.Ins.Type\x12)\n\x08position\x18\x04 \x01(\x0b2\x17.apollo.common.PointLLH\x12,\n\x0ceuler_angles\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x12/\n\x0flinear_velocity\x18\x06 \x01(\x0b2\x16.apollo.common.Point3D\x120\n\x10angular_velocity\x18\x07 \x01(\x0b2\x16.apollo.common.Point3D\x123\n\x13linear_acceleration\x18\x08 \x01(\x0b2\x16.apollo.common.Point3D\x12\x1f\n\x13position_covariance\x18\t \x03(\x02B\x02\x10\x01\x12#\n\x17euler_angles_covariance\x18\n \x03(\x02B\x02\x10\x01\x12&\n\x1alinear_velocity_covariance\x18\x0b \x03(\x02B\x02\x10\x01\x12\'\n\x1bangular_velocity_covariance\x18\x0c \x03(\x02B\x02\x10\x01\x12*\n\x1elinear_acceleration_covariance\x18\r \x03(\x02B\x02\x10\x01"-\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nCONVERGING\x10\x01\x12\x08\n\x04GOOD\x10\x02')
_INSSTAT = DESCRIPTOR.message_types_by_name['InsStat']
_INS = DESCRIPTOR.message_types_by_name['Ins']
_INS_TYPE = _INS.enum_types_by_name['Type']
InsStat = _reflection.GeneratedProtocolMessageType('InsStat', (_message.Message,), {'DESCRIPTOR': _INSSTAT, '__module__': 'modules.drivers.gnss.proto.ins_pb2'})
_sym_db.RegisterMessage(InsStat)
Ins = _reflection.GeneratedProtocolMessageType('Ins', (_message.Message,), {'DESCRIPTOR': _INS, '__module__': 'modules.drivers.gnss.proto.ins_pb2'})
_sym_db.RegisterMessage(Ins)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _INS.fields_by_name['position_covariance']._options = None
    _INS.fields_by_name['position_covariance']._serialized_options = b'\x10\x01'
    _INS.fields_by_name['euler_angles_covariance']._options = None
    _INS.fields_by_name['euler_angles_covariance']._serialized_options = b'\x10\x01'
    _INS.fields_by_name['linear_velocity_covariance']._options = None
    _INS.fields_by_name['linear_velocity_covariance']._serialized_options = b'\x10\x01'
    _INS.fields_by_name['angular_velocity_covariance']._options = None
    _INS.fields_by_name['angular_velocity_covariance']._serialized_options = b'\x10\x01'
    _INS.fields_by_name['linear_acceleration_covariance']._options = None
    _INS.fields_by_name['linear_acceleration_covariance']._serialized_options = b'\x10\x01'
    _INSSTAT._serialized_start = 133
    _INSSTAT._serialized_end = 219
    _INS._serialized_start = 222
    _INS._serialized_end = 820
    _INS_TYPE._serialized_start = 775
    _INS_TYPE._serialized_end = 820