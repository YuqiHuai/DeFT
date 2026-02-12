"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/drivers/gnss/proto/gnss.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\x82\x04\n\x04Gnss\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x1b\n\x10velocity_latency\x18\x03 \x01(\x02:\x010\x12)\n\x08position\x18\x04 \x01(\x0b2\x17.apollo.common.PointLLH\x120\n\x10position_std_dev\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x12/\n\x0flinear_velocity\x18\x06 \x01(\x0b2\x16.apollo.common.Point3D\x127\n\x17linear_velocity_std_dev\x18\x07 \x01(\x0b2\x16.apollo.common.Point3D\x12\x10\n\x08num_sats\x18\x08 \x01(\x05\x12,\n\x04type\x18\t \x01(\x0e2\x1e.apollo.drivers.gnss.Gnss.Type\x12\x17\n\x0fsolution_status\x18\n \x01(\r\x12\x15\n\rposition_type\x18\x0b \x01(\r"e\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nPROPAGATED\x10\x01\x12\n\n\x06SINGLE\x10\x02\x12\x0b\n\x07PSRDIFF\x10\x03\x12\x07\n\x03PPP\x10\x04\x12\r\n\tRTK_FLOAT\x10\x05\x12\x0f\n\x0bRTK_INTEGER\x10\x06">\n\x07RawData\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x0c\n\x04data\x18\x02 \x01(\x0c')
_GNSS = DESCRIPTOR.message_types_by_name['Gnss']
_RAWDATA = DESCRIPTOR.message_types_by_name['RawData']
_GNSS_TYPE = _GNSS.enum_types_by_name['Type']
Gnss = _reflection.GeneratedProtocolMessageType('Gnss', (_message.Message,), {'DESCRIPTOR': _GNSS, '__module__': 'modules.drivers.gnss.proto.gnss_pb2'})
_sym_db.RegisterMessage(Gnss)
RawData = _reflection.GeneratedProtocolMessageType('RawData', (_message.Message,), {'DESCRIPTOR': _RAWDATA, '__module__': 'modules.drivers.gnss.proto.gnss_pb2'})
_sym_db.RegisterMessage(RawData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GNSS._serialized_start = 135
    _GNSS._serialized_end = 649
    _GNSS_TYPE._serialized_start = 548
    _GNSS_TYPE._serialized_end = 649
    _RAWDATA._serialized_start = 651
    _RAWDATA._serialized_end = 713