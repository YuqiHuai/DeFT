"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCmodules/map/tools/map_datachecker/proto/collection_error_code.proto\x12\x0capollo.hdmap*\xab\x05\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x11\n\rERROR_REQUEST\x10\x02\x12\x1d\n\x19ERROR_SERVICE_NO_RESPONSE\x10\x03\x12\x18\n\x14ERROR_REPEATED_START\x10\x04\x12\x1c\n\x18ERROR_CHECK_BEFORE_START\x10\x05\x12\x15\n\x11ERROR_GPSBIN_LACK\x10e\x12\x18\n\x14ERROR_DISKINFO_ERROR\x10f\x12\x16\n\x12ERROR_DISK_UNMOUNT\x10g\x12\x14\n\x10ERROR_SPEED_LACK\x10i\x12\x19\n\x15WARNING_ODOMETER_LACK\x10j\x12\x19\n\x15ERROR_RTKSTATUS_EMPTY\x10k\x12\x1e\n\x19ERROR_MAPGRPC_NOT_CONNECT\x10\xc9\x01\x12\x19\n\x14WARNING_NOT_STRAIGHT\x10\xd4\x01\x12\x1e\n\x19WARNING_PROGRESS_ROLLBACK\x10\xd5\x01\x12\x1a\n\x15ERROR_NOT_EIGHT_ROUTE\x10\xdd\x01\x12$\n\x1fERROR_CHANNEL_VERIFY_TOPIC_LACK\x10\xe7\x01\x12(\n#ERROR_CHANNEL_VERIFY_RATES_ABNORMAL\x10\xe8\x01\x12\x1e\n\x19ERROR_VERIFY_NO_RECORDERS\x10\xe9\x01\x12\x1c\n\x17ERROR_LOOPS_NOT_REACHED\x10\xea\x01\x12\x1c\n\x17ERROR_VERIFY_NO_GNSSPOS\x10\xeb\x01\x12\x15\n\x10ERROR_NOT_STATIC\x10\xf1\x01\x12\x1b\n\x16ERROR_GNSS_SIGNAL_FAIL\x10\xf2\x01\x12\x17\n\x12SUCCESS_TASK_EMPTY\x10\xad\x02\x12\x17\n\x12SUCCESS_TASK_STOCK\x10\xae\x02')
_ERRORCODE = DESCRIPTOR.enum_types_by_name['ErrorCode']
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
SUCCESS = 0
ERROR = 1
ERROR_REQUEST = 2
ERROR_SERVICE_NO_RESPONSE = 3
ERROR_REPEATED_START = 4
ERROR_CHECK_BEFORE_START = 5
ERROR_GPSBIN_LACK = 101
ERROR_DISKINFO_ERROR = 102
ERROR_DISK_UNMOUNT = 103
ERROR_SPEED_LACK = 105
WARNING_ODOMETER_LACK = 106
ERROR_RTKSTATUS_EMPTY = 107
ERROR_MAPGRPC_NOT_CONNECT = 201
WARNING_NOT_STRAIGHT = 212
WARNING_PROGRESS_ROLLBACK = 213
ERROR_NOT_EIGHT_ROUTE = 221
ERROR_CHANNEL_VERIFY_TOPIC_LACK = 231
ERROR_CHANNEL_VERIFY_RATES_ABNORMAL = 232
ERROR_VERIFY_NO_RECORDERS = 233
ERROR_LOOPS_NOT_REACHED = 234
ERROR_VERIFY_NO_GNSSPOS = 235
ERROR_NOT_STATIC = 241
ERROR_GNSS_SIGNAL_FAIL = 242
SUCCESS_TASK_EMPTY = 301
SUCCESS_TASK_STOCK = 302
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ERRORCODE._serialized_start = 86
    _ERRORCODE._serialized_end = 769