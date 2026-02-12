"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/monitor/proto/system_status.proto\x12\x0eapollo.monitor\x1a!modules/common/proto/header.proto"\xa2\x01\n\x0fComponentStatus\x12?\n\x06status\x18\x01 \x01(\x0e2&.apollo.monitor.ComponentStatus.Status:\x07UNKNOWN\x12\x0f\n\x07message\x18\x02 \x01(\t"=\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x08\n\x04WARN\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\t\n\x05FATAL\x10\x04"\xd8\x02\n\tComponent\x120\n\x07summary\x18\x01 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus\x127\n\x0eprocess_status\x18\x02 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus\x127\n\x0echannel_status\x18\x03 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus\x128\n\x0fresource_status\x18\x04 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus\x125\n\x0cother_status\x18\x05 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus\x126\n\rmodule_status\x18\x06 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus"\x8a\x05\n\x0cSystemStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12A\n\x0bhmi_modules\x18\x07 \x03(\x0b2,.apollo.monitor.SystemStatus.HmiModulesEntry\x12@\n\ncomponents\x18\x08 \x03(\x0b2,.apollo.monitor.SystemStatus.ComponentsEntry\x12\x15\n\rpassenger_msg\x18\x04 \x01(\t\x12 \n\x18safety_mode_trigger_time\x18\x05 \x01(\x01\x12\x1e\n\x16require_emergency_stop\x18\x06 \x01(\x08\x12!\n\x19is_realtime_in_simulation\x18\t \x01(\x08\x12K\n\x10other_components\x18\n \x03(\x0b21.apollo.monitor.SystemStatus.OtherComponentsEntry\x1aR\n\x0fHmiModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus:\x028\x01\x1aL\n\x0fComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b2\x19.apollo.monitor.Component:\x028\x01\x1aW\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus:\x028\x01J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04')
_COMPONENTSTATUS = DESCRIPTOR.message_types_by_name['ComponentStatus']
_COMPONENT = DESCRIPTOR.message_types_by_name['Component']
_SYSTEMSTATUS = DESCRIPTOR.message_types_by_name['SystemStatus']
_SYSTEMSTATUS_HMIMODULESENTRY = _SYSTEMSTATUS.nested_types_by_name['HmiModulesEntry']
_SYSTEMSTATUS_COMPONENTSENTRY = _SYSTEMSTATUS.nested_types_by_name['ComponentsEntry']
_SYSTEMSTATUS_OTHERCOMPONENTSENTRY = _SYSTEMSTATUS.nested_types_by_name['OtherComponentsEntry']
_COMPONENTSTATUS_STATUS = _COMPONENTSTATUS.enum_types_by_name['Status']
ComponentStatus = _reflection.GeneratedProtocolMessageType('ComponentStatus', (_message.Message,), {'DESCRIPTOR': _COMPONENTSTATUS, '__module__': 'modules.monitor.proto.system_status_pb2'})
_sym_db.RegisterMessage(ComponentStatus)
Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), {'DESCRIPTOR': _COMPONENT, '__module__': 'modules.monitor.proto.system_status_pb2'})
_sym_db.RegisterMessage(Component)
SystemStatus = _reflection.GeneratedProtocolMessageType('SystemStatus', (_message.Message,), {'HmiModulesEntry': _reflection.GeneratedProtocolMessageType('HmiModulesEntry', (_message.Message,), {'DESCRIPTOR': _SYSTEMSTATUS_HMIMODULESENTRY, '__module__': 'modules.monitor.proto.system_status_pb2'}), 'ComponentsEntry': _reflection.GeneratedProtocolMessageType('ComponentsEntry', (_message.Message,), {'DESCRIPTOR': _SYSTEMSTATUS_COMPONENTSENTRY, '__module__': 'modules.monitor.proto.system_status_pb2'}), 'OtherComponentsEntry': _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), {'DESCRIPTOR': _SYSTEMSTATUS_OTHERCOMPONENTSENTRY, '__module__': 'modules.monitor.proto.system_status_pb2'}), 'DESCRIPTOR': _SYSTEMSTATUS, '__module__': 'modules.monitor.proto.system_status_pb2'})
_sym_db.RegisterMessage(SystemStatus)
_sym_db.RegisterMessage(SystemStatus.HmiModulesEntry)
_sym_db.RegisterMessage(SystemStatus.ComponentsEntry)
_sym_db.RegisterMessage(SystemStatus.OtherComponentsEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SYSTEMSTATUS_HMIMODULESENTRY._options = None
    _SYSTEMSTATUS_HMIMODULESENTRY._serialized_options = b'8\x01'
    _SYSTEMSTATUS_COMPONENTSENTRY._options = None
    _SYSTEMSTATUS_COMPONENTSENTRY._serialized_options = b'8\x01'
    _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._options = None
    _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._serialized_options = b'8\x01'
    _COMPONENTSTATUS._serialized_start = 97
    _COMPONENTSTATUS._serialized_end = 259
    _COMPONENTSTATUS_STATUS._serialized_start = 198
    _COMPONENTSTATUS_STATUS._serialized_end = 259
    _COMPONENT._serialized_start = 262
    _COMPONENT._serialized_end = 606
    _SYSTEMSTATUS._serialized_start = 609
    _SYSTEMSTATUS._serialized_end = 1259
    _SYSTEMSTATUS_HMIMODULESENTRY._serialized_start = 998
    _SYSTEMSTATUS_HMIMODULESENTRY._serialized_end = 1080
    _SYSTEMSTATUS_COMPONENTSENTRY._serialized_start = 1082
    _SYSTEMSTATUS_COMPONENTSENTRY._serialized_end = 1158
    _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._serialized_start = 1160
    _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._serialized_end = 1247