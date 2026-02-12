"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/common/monitor_log/proto/monitor_log.proto\x12\x15apollo.common.monitor\x1a!modules/common/proto/header.proto"\xc1\x04\n\x12MonitorMessageItem\x12P\n\x06source\x18\x01 \x01(\x0e27.apollo.common.monitor.MonitorMessageItem.MessageSource:\x07UNKNOWN\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12K\n\tlog_level\x18\x03 \x01(\x0e22.apollo.common.monitor.MonitorMessageItem.LogLevel:\x04INFO"\xc8\x02\n\rMessageSource\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06CANBUS\x10\x02\x12\x0b\n\x07CONTROL\x10\x03\x12\x0c\n\x08DECISION\x10\x04\x12\x10\n\x0cLOCALIZATION\x10\x05\x12\x0c\n\x08PLANNING\x10\x06\x12\x0e\n\nPREDICTION\x10\x07\x12\r\n\tSIMULATOR\x10\x08\x12\t\n\x05HWSYS\x10\t\x12\x0b\n\x07ROUTING\x10\n\x12\x0b\n\x07MONITOR\x10\x0b\x12\x07\n\x03HMI\x10\x0c\x12\x10\n\x0cRELATIVE_MAP\x10\r\x12\x08\n\x04GNSS\x10\x0e\x12\x0f\n\x0bCONTI_RADAR\x10\x0f\x12\x11\n\rRACOBIT_RADAR\x10\x10\x12\x14\n\x10ULTRASONIC_RADAR\x10\x11\x12\x0c\n\x08MOBILEYE\x10\x12\x12\x0e\n\nDELPHI_ESR\x10\x13\x12\x10\n\x0cSTORYTELLING\x10\x14\x12\x10\n\x0cTASK_MANAGER\x10\x15"4\n\x08LogLevel\x12\x08\n\x04INFO\x10\x00\x12\x08\n\x04WARN\x10\x01\x12\t\n\x05ERROR\x10\x02\x12\t\n\x05FATAL\x10\x03"p\n\x0eMonitorMessage\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x127\n\x04item\x18\x02 \x03(\x0b2).apollo.common.monitor.MonitorMessageItem')
_MONITORMESSAGEITEM = DESCRIPTOR.message_types_by_name['MonitorMessageItem']
_MONITORMESSAGE = DESCRIPTOR.message_types_by_name['MonitorMessage']
_MONITORMESSAGEITEM_MESSAGESOURCE = _MONITORMESSAGEITEM.enum_types_by_name['MessageSource']
_MONITORMESSAGEITEM_LOGLEVEL = _MONITORMESSAGEITEM.enum_types_by_name['LogLevel']
MonitorMessageItem = _reflection.GeneratedProtocolMessageType('MonitorMessageItem', (_message.Message,), {'DESCRIPTOR': _MONITORMESSAGEITEM, '__module__': 'modules.common.monitor_log.proto.monitor_log_pb2'})
_sym_db.RegisterMessage(MonitorMessageItem)
MonitorMessage = _reflection.GeneratedProtocolMessageType('MonitorMessage', (_message.Message,), {'DESCRIPTOR': _MONITORMESSAGE, '__module__': 'modules.common.monitor_log.proto.monitor_log_pb2'})
_sym_db.RegisterMessage(MonitorMessage)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MONITORMESSAGEITEM._serialized_start = 113
    _MONITORMESSAGEITEM._serialized_end = 690
    _MONITORMESSAGEITEM_MESSAGESOURCE._serialized_start = 308
    _MONITORMESSAGEITEM_MESSAGESOURCE._serialized_end = 636
    _MONITORMESSAGEITEM_LOGLEVEL._serialized_start = 638
    _MONITORMESSAGEITEM_LOGLEVEL._serialized_end = 690
    _MONITORMESSAGE._serialized_start = 692
    _MONITORMESSAGE._serialized_end = 804