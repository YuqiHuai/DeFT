"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/v2x/proto/v2x_monitor.proto\x12\napollo.v2x"Y\n\x08ObuAlarm\x12\x10\n\x08mode_num\x18\x01 \x02(\x01\x12(\n\terror_num\x18\x02 \x02(\x0e2\x15.apollo.v2x.ErrorCode\x12\x11\n\terror_msg\x18\x03 \x02(\t*_\n\tErrorCode\x12\t\n\x04LTEV\x10\xf4\x03\x12\x08\n\x03NET\x10\xf5\x03\x12\x08\n\x03CPU\x10\xf6\x03\x12\x08\n\x03MEM\x10\xf7\x03\x12\x08\n\x03GPS\x10\xf8\x03\x12\x08\n\x03MAP\x10\xfe\x03\x12\t\n\x04SPAT\x10\xff\x03\x12\n\n\x05OBUID\x10\xe7\x07')
_ERRORCODE = DESCRIPTOR.enum_types_by_name['ErrorCode']
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
LTEV = 500
NET = 501
CPU = 502
MEM = 503
GPS = 504
MAP = 510
SPAT = 511
OBUID = 999
_OBUALARM = DESCRIPTOR.message_types_by_name['ObuAlarm']
ObuAlarm = _reflection.GeneratedProtocolMessageType('ObuAlarm', (_message.Message,), {'DESCRIPTOR': _OBUALARM, '__module__': 'modules.v2x.proto.v2x_monitor_pb2'})
_sym_db.RegisterMessage(ObuAlarm)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ERRORCODE._serialized_start = 142
    _ERRORCODE._serialized_end = 237
    _OBUALARM._serialized_start = 51
    _OBUALARM._serialized_end = 140