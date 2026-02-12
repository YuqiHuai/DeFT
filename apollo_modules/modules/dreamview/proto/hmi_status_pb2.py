"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.monitor.proto import system_status_pb2 as modules_dot_monitor_dot_proto_dot_system__status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/dreamview/proto/hmi_status.proto\x12\x10apollo.dreamview\x1a!modules/common/proto/header.proto\x1a)modules/monitor/proto/system_status.proto"\xa8\x05\n\tHMIStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\r\n\x05modes\x18\x02 \x03(\t\x12\x14\n\x0ccurrent_mode\x18\x03 \x01(\t\x12\x0c\n\x04maps\x18\x04 \x03(\t\x12\x13\n\x0bcurrent_map\x18\x05 \x01(\t\x12\x10\n\x08vehicles\x18\x06 \x03(\t\x12\x17\n\x0fcurrent_vehicle\x18\x07 \x01(\t\x129\n\x07modules\x18\x08 \x03(\x0b2(.apollo.dreamview.HMIStatus.ModulesEntry\x12R\n\x14monitored_components\x18\t \x03(\x0b24.apollo.dreamview.HMIStatus.MonitoredComponentsEntry\x12\x14\n\x0cdocker_image\x18\n \x01(\t\x12\x13\n\x0butm_zone_id\x18\x0b \x01(\x05\x12\x15\n\rpassenger_msg\x18\x0c \x01(\t\x12J\n\x10other_components\x18\r \x03(\x0b20.apollo.dreamview.HMIStatus.OtherComponentsEntry\x1a.\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x028\x01\x1a[\n\x18MonitoredComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus:\x028\x01\x1aW\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b2\x1f.apollo.monitor.ComponentStatus:\x028\x01')
_HMISTATUS = DESCRIPTOR.message_types_by_name['HMIStatus']
_HMISTATUS_MODULESENTRY = _HMISTATUS.nested_types_by_name['ModulesEntry']
_HMISTATUS_MONITOREDCOMPONENTSENTRY = _HMISTATUS.nested_types_by_name['MonitoredComponentsEntry']
_HMISTATUS_OTHERCOMPONENTSENTRY = _HMISTATUS.nested_types_by_name['OtherComponentsEntry']
HMIStatus = _reflection.GeneratedProtocolMessageType('HMIStatus', (_message.Message,), {'ModulesEntry': _reflection.GeneratedProtocolMessageType('ModulesEntry', (_message.Message,), {'DESCRIPTOR': _HMISTATUS_MODULESENTRY, '__module__': 'modules.dreamview.proto.hmi_status_pb2'}), 'MonitoredComponentsEntry': _reflection.GeneratedProtocolMessageType('MonitoredComponentsEntry', (_message.Message,), {'DESCRIPTOR': _HMISTATUS_MONITOREDCOMPONENTSENTRY, '__module__': 'modules.dreamview.proto.hmi_status_pb2'}), 'OtherComponentsEntry': _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), {'DESCRIPTOR': _HMISTATUS_OTHERCOMPONENTSENTRY, '__module__': 'modules.dreamview.proto.hmi_status_pb2'}), 'DESCRIPTOR': _HMISTATUS, '__module__': 'modules.dreamview.proto.hmi_status_pb2'})
_sym_db.RegisterMessage(HMIStatus)
_sym_db.RegisterMessage(HMIStatus.ModulesEntry)
_sym_db.RegisterMessage(HMIStatus.MonitoredComponentsEntry)
_sym_db.RegisterMessage(HMIStatus.OtherComponentsEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HMISTATUS_MODULESENTRY._options = None
    _HMISTATUS_MODULESENTRY._serialized_options = b'8\x01'
    _HMISTATUS_MONITOREDCOMPONENTSENTRY._options = None
    _HMISTATUS_MONITOREDCOMPONENTSENTRY._serialized_options = b'8\x01'
    _HMISTATUS_OTHERCOMPONENTSENTRY._options = None
    _HMISTATUS_OTHERCOMPONENTSENTRY._serialized_options = b'8\x01'
    _HMISTATUS._serialized_start = 141
    _HMISTATUS._serialized_end = 821
    _HMISTATUS_MODULESENTRY._serialized_start = 593
    _HMISTATUS_MODULESENTRY._serialized_end = 639
    _HMISTATUS_MONITOREDCOMPONENTSENTRY._serialized_start = 641
    _HMISTATUS_MONITOREDCOMPONENTSENTRY._serialized_end = 732
    _HMISTATUS_OTHERCOMPONENTSENTRY._serialized_start = 734
    _HMISTATUS_OTHERCOMPONENTSENTRY._serialized_end = 821