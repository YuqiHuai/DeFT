"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/localization/proto/measure.proto\x12\x13apollo.localization\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\xd6\x04\n\x0cIntegMeasure\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12C\n\x0cmeasure_type\x18\x02 \x01(\x0e2-.apollo.localization.IntegMeasure.MeasureType\x12?\n\nframe_type\x18\x03 \x01(\x0e2+.apollo.localization.IntegMeasure.FrameType\x12(\n\x08position\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12(\n\x08velocity\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x12\x0b\n\x03yaw\x18\x06 \x01(\x01\x12\x0f\n\x07zone_id\x18\x07 \x01(\x05\x12\x18\n\x10is_have_variance\x18\x08 \x01(\x08\x12\x1e\n\x16is_gnss_double_antenna\x18\t \x01(\x08\x12\x19\n\rmeasure_covar\x18\n \x03(\x01B\x02\x10\x01"\x9a\x01\n\x0bMeasureType\x12\x11\n\rGNSS_POS_ONLY\x10\x00\x12\x10\n\x0cGNSS_POS_VEL\x10\x01\x12\x0f\n\x0bGNSS_POS_XY\x10\x02\x12\x11\n\rGNSS_VEL_ONLY\x10\x03\x12\x13\n\x0fPOINT_CLOUD_POS\x10\x04\x12\x15\n\x11ODOMETER_VEL_ONLY\x10\x05\x12\x16\n\x12VEHICLE_CONSTRAINT\x10\x06"5\n\tFrameType\x12\x07\n\x03ENU\x10\x00\x12\x08\n\x04ECEF\x10\x01\x12\x07\n\x03UTM\x10\x02\x12\x0c\n\x08ODOMETER\x10\x03')
_INTEGMEASURE = DESCRIPTOR.message_types_by_name['IntegMeasure']
_INTEGMEASURE_MEASURETYPE = _INTEGMEASURE.enum_types_by_name['MeasureType']
_INTEGMEASURE_FRAMETYPE = _INTEGMEASURE.enum_types_by_name['FrameType']
IntegMeasure = _reflection.GeneratedProtocolMessageType('IntegMeasure', (_message.Message,), {'DESCRIPTOR': _INTEGMEASURE, '__module__': 'modules.localization.proto.measure_pb2'})
_sym_db.RegisterMessage(IntegMeasure)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _INTEGMEASURE.fields_by_name['measure_covar']._options = None
    _INTEGMEASURE.fields_by_name['measure_covar']._serialized_options = b'\x10\x01'
    _INTEGMEASURE._serialized_start = 138
    _INTEGMEASURE._serialized_end = 736
    _INTEGMEASURE_MEASURETYPE._serialized_start = 527
    _INTEGMEASURE_MEASURETYPE._serialized_end = 681
    _INTEGMEASURE_FRAMETYPE._serialized_start = 683
    _INTEGMEASURE_FRAMETYPE._serialized_end = 736