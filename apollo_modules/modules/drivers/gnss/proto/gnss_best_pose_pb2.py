"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/drivers/gnss/proto/gnss_best_pose.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto"\xaa\x05\n\x0cGnssBestPose\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x127\n\nsol_status\x18\x03 \x01(\x0e2#.apollo.drivers.gnss.SolutionStatus\x123\n\x08sol_type\x18\x04 \x01(\x0e2!.apollo.drivers.gnss.SolutionType\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01\x12\x12\n\nheight_msl\x18\x07 \x01(\x01\x12\x12\n\nundulation\x18\x08 \x01(\x02\x12.\n\x08datum_id\x18\t \x01(\x0e2\x1c.apollo.drivers.gnss.DatumId\x12\x18\n\x10latitude_std_dev\x18\n \x01(\x02\x12\x19\n\x11longitude_std_dev\x18\x0b \x01(\x02\x12\x16\n\x0eheight_std_dev\x18\x0c \x01(\x02\x12\x17\n\x0fbase_station_id\x18\r \x01(\x0c\x12\x18\n\x10differential_age\x18\x0e \x01(\x02\x12\x14\n\x0csolution_age\x18\x0f \x01(\x02\x12\x18\n\x10num_sats_tracked\x18\x10 \x01(\r\x12\x1c\n\x14num_sats_in_solution\x18\x11 \x01(\r\x12\x13\n\x0bnum_sats_l1\x18\x12 \x01(\r\x12\x16\n\x0enum_sats_multi\x18\x13 \x01(\r\x12\x10\n\x08reserved\x18\x14 \x01(\r\x12 \n\x18extended_solution_status\x18\x15 \x01(\r\x12 \n\x18galileo_beidou_used_mask\x18\x16 \x01(\r\x12\x1d\n\x15gps_glonass_used_mask\x18\x17 \x01(\r*\x90\x02\n\x0eSolutionStatus\x12\x10\n\x0cSOL_COMPUTED\x10\x00\x12\x14\n\x10INSUFFICIENT_OBS\x10\x01\x12\x12\n\x0eNO_CONVERGENCE\x10\x02\x12\x0f\n\x0bSINGULARITY\x10\x03\x12\r\n\tCOV_TRACE\x10\x04\x12\r\n\tTEST_DIST\x10\x05\x12\x0e\n\nCOLD_START\x10\x06\x12\r\n\tV_H_LIMIT\x10\x07\x12\x0c\n\x08VARIANCE\x10\x08\x12\r\n\tRESIDUALS\x10\t\x12\x15\n\x11INTEGRITY_WARNING\x10\r\x12\x0b\n\x07PENDING\x10\x12\x12\x0f\n\x0bINVALID_FIX\x10\x13\x12\x10\n\x0cUNAUTHORIZED\x10\x14\x12\x10\n\x0cINVALID_RATE\x10\x16*\x9f\x04\n\x0cSolutionType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08FIXEDPOS\x10\x01\x12\x0f\n\x0bFIXEDHEIGHT\x10\x02\x12\r\n\tFLOATCONV\x10\x04\x12\x0c\n\x08WIDELANE\x10\x05\x12\x0e\n\nNARROWLANE\x10\x06\x12\x14\n\x10DOPPLER_VELOCITY\x10\x08\x12\n\n\x06SINGLE\x10\x10\x12\x0b\n\x07PSRDIFF\x10\x11\x12\x08\n\x04WAAS\x10\x12\x12\x0e\n\nPROPOGATED\x10\x13\x12\x0c\n\x08OMNISTAR\x10\x14\x12\x0c\n\x08L1_FLOAT\x10 \x12\x12\n\x0eIONOFREE_FLOAT\x10!\x12\x10\n\x0cNARROW_FLOAT\x10"\x12\n\n\x06L1_INT\x100\x12\x0c\n\x08WIDE_INT\x101\x12\x0e\n\nNARROW_INT\x102\x12\x12\n\x0eRTK_DIRECT_INS\x103\x12\x0c\n\x08INS_SBAS\x104\x12\r\n\tINS_PSRSP\x105\x12\x0f\n\x0bINS_PSRDIFF\x106\x12\x10\n\x0cINS_RTKFLOAT\x107\x12\x10\n\x0cINS_RTKFIXED\x108\x12\x10\n\x0cINS_OMNISTAR\x109\x12\x13\n\x0fINS_OMNISTAR_HP\x10:\x12\x13\n\x0fINS_OMNISTAR_XP\x10;\x12\x0f\n\x0bOMNISTAR_HP\x10@\x12\x0f\n\x0bOMNISTAR_XP\x10A\x12\x12\n\x0ePPP_CONVERGING\x10D\x12\x07\n\x03PPP\x10E\x12\x16\n\x12INS_PPP_CONVERGING\x10I\x12\x0b\n\x07INS_PPP\x10J*\x14\n\x07DatumId\x12\t\n\x05WGS84\x10=')
_SOLUTIONSTATUS = DESCRIPTOR.enum_types_by_name['SolutionStatus']
SolutionStatus = enum_type_wrapper.EnumTypeWrapper(_SOLUTIONSTATUS)
_SOLUTIONTYPE = DESCRIPTOR.enum_types_by_name['SolutionType']
SolutionType = enum_type_wrapper.EnumTypeWrapper(_SOLUTIONTYPE)
_DATUMID = DESCRIPTOR.enum_types_by_name['DatumId']
DatumId = enum_type_wrapper.EnumTypeWrapper(_DATUMID)
SOL_COMPUTED = 0
INSUFFICIENT_OBS = 1
NO_CONVERGENCE = 2
SINGULARITY = 3
COV_TRACE = 4
TEST_DIST = 5
COLD_START = 6
V_H_LIMIT = 7
VARIANCE = 8
RESIDUALS = 9
INTEGRITY_WARNING = 13
PENDING = 18
INVALID_FIX = 19
UNAUTHORIZED = 20
INVALID_RATE = 22
NONE = 0
FIXEDPOS = 1
FIXEDHEIGHT = 2
FLOATCONV = 4
WIDELANE = 5
NARROWLANE = 6
DOPPLER_VELOCITY = 8
SINGLE = 16
PSRDIFF = 17
WAAS = 18
PROPOGATED = 19
OMNISTAR = 20
L1_FLOAT = 32
IONOFREE_FLOAT = 33
NARROW_FLOAT = 34
L1_INT = 48
WIDE_INT = 49
NARROW_INT = 50
RTK_DIRECT_INS = 51
INS_SBAS = 52
INS_PSRSP = 53
INS_PSRDIFF = 54
INS_RTKFLOAT = 55
INS_RTKFIXED = 56
INS_OMNISTAR = 57
INS_OMNISTAR_HP = 58
INS_OMNISTAR_XP = 59
OMNISTAR_HP = 64
OMNISTAR_XP = 65
PPP_CONVERGING = 68
PPP = 69
INS_PPP_CONVERGING = 73
INS_PPP = 74
WGS84 = 61
_GNSSBESTPOSE = DESCRIPTOR.message_types_by_name['GnssBestPose']
GnssBestPose = _reflection.GeneratedProtocolMessageType('GnssBestPose', (_message.Message,), {'DESCRIPTOR': _GNSSBESTPOSE, '__module__': 'modules.drivers.gnss.proto.gnss_best_pose_pb2'})
_sym_db.RegisterMessage(GnssBestPose)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SOLUTIONSTATUS._serialized_start = 793
    _SOLUTIONSTATUS._serialized_end = 1065
    _SOLUTIONTYPE._serialized_start = 1068
    _SOLUTIONTYPE._serialized_end = 1611
    _DATUMID._serialized_start = 1613
    _DATUMID._serialized_end = 1633
    _GNSSBESTPOSE._serialized_start = 108
    _GNSSBESTPOSE._serialized_end = 790