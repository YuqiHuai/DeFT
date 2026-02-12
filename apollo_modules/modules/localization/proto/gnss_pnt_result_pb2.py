"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.drivers.gnss.proto import gnss_raw_observation_pb2 as modules_dot_drivers_dot_gnss_dot_proto_dot_gnss__raw__observation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/localization/proto/gnss_pnt_result.proto\x12\x13apollo.localization\x1a5modules/drivers/gnss/proto/gnss_raw_observation.proto"f\n\x0cSatDirCosine\x12\x0f\n\x07sat_prn\x18\x01 \x01(\r\x12\x0f\n\x07sat_sys\x18\x02 \x01(\r\x12\x10\n\x08cosine_x\x18\x03 \x01(\x01\x12\x10\n\x08cosine_y\x18\x04 \x01(\x01\x12\x10\n\x08cosine_z\x18\x05 \x01(\x01"\xac\x04\n\rGnssPntResult\x12\x13\n\x0breceiver_id\x18\x01 \x01(\r\x12>\n\ttime_type\x18\x02 \x01(\x0e2!.apollo.drivers.gnss.GnssTimeType:\x08GPS_TIME\x12\x11\n\tgnss_week\x18\x03 \x01(\r\x12\x15\n\rgnss_second_s\x18\x04 \x01(\x01\x12;\n\x08pnt_type\x18\x05 \x01(\x0e2\x1c.apollo.localization.PntType:\x0bPNT_INVALID\x12\x0f\n\x07pos_x_m\x18\x06 \x01(\x01\x12\x0f\n\x07pos_y_m\x18\x07 \x01(\x01\x12\x0f\n\x07pos_z_m\x18\x08 \x01(\x01\x12\x13\n\x0bstd_pos_x_m\x18\t \x01(\x01\x12\x13\n\x0bstd_pos_y_m\x18\n \x01(\x01\x12\x13\n\x0bstd_pos_z_m\x18\x0b \x01(\x01\x12\x0f\n\x07vel_x_m\x18\x0c \x01(\x01\x12\x0f\n\x07vel_y_m\x18\r \x01(\x01\x12\x0f\n\x07vel_z_m\x18\x0e \x01(\x01\x12\x13\n\x0bstd_vel_x_m\x18\x0f \x01(\x01\x12\x13\n\x0bstd_vel_y_m\x18\x10 \x01(\x01\x12\x13\n\x0bstd_vel_z_m\x18\x11 \x01(\x01\x12\x16\n\x0esovled_sat_num\x18\x12 \x01(\r\x129\n\x0esat_dir_cosine\x18\x13 \x03(\x0b2!.apollo.localization.SatDirCosine\x12\x0c\n\x04pdop\x18\x14 \x01(\x01\x12\x0c\n\x04hdop\x18\x15 \x01(\x01\x12\x0c\n\x04vdop\x18\x16 \x01(\x01*r\n\x07PntType\x12\x0f\n\x0bPNT_INVALID\x10\x00\x12\x0b\n\x07PNT_SPP\x10\x01\x12\x10\n\x0cPNT_PHASE_TD\x10\x02\x12\x11\n\rPNT_CODE_DIFF\x10\x03\x12\x11\n\rPNT_RTK_FLOAT\x10\x04\x12\x11\n\rPNT_RTK_FIXED\x10\x05')
_PNTTYPE = DESCRIPTOR.enum_types_by_name['PntType']
PntType = enum_type_wrapper.EnumTypeWrapper(_PNTTYPE)
PNT_INVALID = 0
PNT_SPP = 1
PNT_PHASE_TD = 2
PNT_CODE_DIFF = 3
PNT_RTK_FLOAT = 4
PNT_RTK_FIXED = 5
_SATDIRCOSINE = DESCRIPTOR.message_types_by_name['SatDirCosine']
_GNSSPNTRESULT = DESCRIPTOR.message_types_by_name['GnssPntResult']
SatDirCosine = _reflection.GeneratedProtocolMessageType('SatDirCosine', (_message.Message,), {'DESCRIPTOR': _SATDIRCOSINE, '__module__': 'modules.localization.proto.gnss_pnt_result_pb2'})
_sym_db.RegisterMessage(SatDirCosine)
GnssPntResult = _reflection.GeneratedProtocolMessageType('GnssPntResult', (_message.Message,), {'DESCRIPTOR': _GNSSPNTRESULT, '__module__': 'modules.localization.proto.gnss_pnt_result_pb2'})
_sym_db.RegisterMessage(GnssPntResult)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PNTTYPE._serialized_start = 791
    _PNTTYPE._serialized_end = 905
    _SATDIRCOSINE._serialized_start = 128
    _SATDIRCOSINE._serialized_end = 230
    _GNSSPNTRESULT._serialized_start = 233
    _GNSSPNTRESULT._serialized_end = 789