"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/planning/proto/ipopt_return_status.proto\x12\x0fapollo.planning*\xeb\x04\n\x11IpoptReturnStatus\x12\x13\n\x0fSOLVE_SUCCEEDED\x10\x00\x12\x1e\n\x1aSOLVED_TO_ACCEPTABLE_LEVEL\x10\x01\x12\x1f\n\x1bINFEASIBLE_PROBLEM_DETECTED\x10\x02\x12&\n"SEARCH_DIRECTION_BECOMES_TOO_SMALL\x10\x03\x12\x15\n\x11DIVERGIN_ITERATES\x10\x04\x12\x17\n\x13USER_REQUESTED_STOP\x10\x05\x12\x18\n\x14FEASIBLE_POINT_FOUND\x10\x06\x12(\n\x1bMAXIMUM_ITERATIONS_EXCEEDED\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12RESTORATION_FAILED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12&\n\x19ERROR_IN_STEP_COMPUTATION\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12*\n\x1dNOT_ENOUGH_DEGREES_OF_FREEDOM\x10\xf6\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\'\n\x1aINVALID_PROGRAM_DEFINITION\x10\xf5\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1b\n\x0eINVALID_OPTION\x10\xf4\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17INVALID_NUMBER_DETECTED\x10\xf3\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17UNRECOVERABLE_EXCEPTION\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12&\n\x19NONIPOPT_EXCEPTION_THROWN\x10\x9b\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13INSUFFICIENT_MEMORY\x10\x9a\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x13\n\x0eINTERNAL_ERROR\x10\xc7\x01')
_IPOPTRETURNSTATUS = DESCRIPTOR.enum_types_by_name['IpoptReturnStatus']
IpoptReturnStatus = enum_type_wrapper.EnumTypeWrapper(_IPOPTRETURNSTATUS)
SOLVE_SUCCEEDED = 0
SOLVED_TO_ACCEPTABLE_LEVEL = 1
INFEASIBLE_PROBLEM_DETECTED = 2
SEARCH_DIRECTION_BECOMES_TOO_SMALL = 3
DIVERGIN_ITERATES = 4
USER_REQUESTED_STOP = 5
FEASIBLE_POINT_FOUND = 6
MAXIMUM_ITERATIONS_EXCEEDED = -1
RESTORATION_FAILED = -2
ERROR_IN_STEP_COMPUTATION = -3
NOT_ENOUGH_DEGREES_OF_FREEDOM = -10
INVALID_PROGRAM_DEFINITION = -11
INVALID_OPTION = -12
INVALID_NUMBER_DETECTED = -13
UNRECOVERABLE_EXCEPTION = -100
NONIPOPT_EXCEPTION_THROWN = -101
INSUFFICIENT_MEMORY = -102
INTERNAL_ERROR = 199
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _IPOPTRETURNSTATUS._serialized_start = 70
    _IPOPTRETURNSTATUS._serialized_end = 689