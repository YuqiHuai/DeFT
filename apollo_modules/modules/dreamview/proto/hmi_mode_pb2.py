"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/dreamview/proto/hmi_mode.proto\x12\x10apollo.dreamview"0\n\x14ProcessMonitorConfig\x12\x18\n\x10command_keywords\x18\x01 \x03(\t"(\n\x13ModuleMonitorConfig\x12\x11\n\tnode_name\x18\x01 \x03(\t"\x9d\x01\n\x14ChannelMonitorConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0bdelay_fatal\x18\x02 \x01(\x01:\x013\x12\x18\n\x10mandatory_fields\x18\x03 \x03(\t\x12 \n\x15min_frequency_allowed\x18\x04 \x01(\x01:\x010\x12#\n\x15max_frequency_allowed\x18\x05 \x01(\x01:\x041000"\xce\x05\n\x15ResourceMonitorConfig\x12F\n\x0bdisk_spaces\x18\x01 \x03(\x0b21.apollo.dreamview.ResourceMonitorConfig.DiskSpace\x12D\n\ncpu_usages\x18\x02 \x03(\x0b20.apollo.dreamview.ResourceMonitorConfig.CPUUsage\x12J\n\rmemory_usages\x18\x03 \x03(\x0b23.apollo.dreamview.ResourceMonitorConfig.MemoryUsage\x12J\n\x10disk_load_usages\x18\x04 \x03(\x0b20.apollo.dreamview.ResourceMonitorConfig.DiskLoad\x1a_\n\tDiskSpace\x12\x0c\n\x04path\x18\x01 \x01(\t\x12"\n\x1ainsufficient_space_warning\x18\x02 \x01(\x05\x12 \n\x18insufficient_space_error\x18\x03 \x01(\x05\x1ab\n\x08CPUUsage\x12\x1e\n\x16high_cpu_usage_warning\x18\x01 \x01(\x02\x12\x1c\n\x14high_cpu_usage_error\x18\x02 \x01(\x02\x12\x18\n\x10process_dag_path\x18\x03 \x01(\t\x1ak\n\x0bMemoryUsage\x12!\n\x19high_memory_usage_warning\x18\x01 \x01(\x05\x12\x1f\n\x17high_memory_usage_error\x18\x02 \x01(\x05\x12\x18\n\x10process_dag_path\x18\x03 \x01(\t\x1a]\n\x08DiskLoad\x12\x1e\n\x16high_disk_load_warning\x18\x01 \x01(\x05\x12\x1c\n\x14high_disk_load_error\x18\x02 \x01(\x05\x12\x13\n\x0bdevice_name\x18\x03 \x01(\t"\x9b\x02\n\x12MonitoredComponent\x127\n\x07process\x18\x01 \x01(\x0b2&.apollo.dreamview.ProcessMonitorConfig\x127\n\x07channel\x18\x02 \x01(\x0b2&.apollo.dreamview.ChannelMonitorConfig\x129\n\x08resource\x18\x03 \x01(\x0b2\'.apollo.dreamview.ResourceMonitorConfig\x12!\n\x13required_for_safety\x18\x04 \x01(\x08:\x04true\x125\n\x06module\x18\x05 \x01(\x0b2%.apollo.dreamview.ModuleMonitorConfig"\xa0\x01\n\x06Module\x12\x15\n\rstart_command\x18\x01 \x01(\t\x12\x14\n\x0cstop_command\x18\x02 \x01(\t\x12F\n\x16process_monitor_config\x18\x03 \x01(\x0b2&.apollo.dreamview.ProcessMonitorConfig\x12!\n\x13required_for_safety\x18\x04 \x01(\x08:\x04true"Z\n\x0bCyberModule\x12\x11\n\tdag_files\x18\x01 \x03(\t\x12!\n\x13required_for_safety\x18\x02 \x01(\x08:\x04true\x12\x15\n\rprocess_group\x18\x03 \x01(\t"\x82\x05\n\x07HMIMode\x12B\n\rcyber_modules\x18\x01 \x03(\x0b2+.apollo.dreamview.HMIMode.CyberModulesEntry\x127\n\x07modules\x18\x02 \x03(\x0b2&.apollo.dreamview.HMIMode.ModulesEntry\x12P\n\x14monitored_components\x18\x03 \x03(\x0b22.apollo.dreamview.HMIMode.MonitoredComponentsEntry\x12H\n\x10other_components\x18\x04 \x03(\x0b2..apollo.dreamview.HMIMode.OtherComponentsEntry\x1aR\n\x11CyberModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b2\x1d.apollo.dreamview.CyberModule:\x028\x01\x1aH\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b2\x18.apollo.dreamview.Module:\x028\x01\x1a`\n\x18MonitoredComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x123\n\x05value\x18\x02 \x01(\x0b2$.apollo.dreamview.MonitoredComponent:\x028\x01\x1a^\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.apollo.dreamview.ProcessMonitorConfig:\x028\x01')
_PROCESSMONITORCONFIG = DESCRIPTOR.message_types_by_name['ProcessMonitorConfig']
_MODULEMONITORCONFIG = DESCRIPTOR.message_types_by_name['ModuleMonitorConfig']
_CHANNELMONITORCONFIG = DESCRIPTOR.message_types_by_name['ChannelMonitorConfig']
_RESOURCEMONITORCONFIG = DESCRIPTOR.message_types_by_name['ResourceMonitorConfig']
_RESOURCEMONITORCONFIG_DISKSPACE = _RESOURCEMONITORCONFIG.nested_types_by_name['DiskSpace']
_RESOURCEMONITORCONFIG_CPUUSAGE = _RESOURCEMONITORCONFIG.nested_types_by_name['CPUUsage']
_RESOURCEMONITORCONFIG_MEMORYUSAGE = _RESOURCEMONITORCONFIG.nested_types_by_name['MemoryUsage']
_RESOURCEMONITORCONFIG_DISKLOAD = _RESOURCEMONITORCONFIG.nested_types_by_name['DiskLoad']
_MONITOREDCOMPONENT = DESCRIPTOR.message_types_by_name['MonitoredComponent']
_MODULE = DESCRIPTOR.message_types_by_name['Module']
_CYBERMODULE = DESCRIPTOR.message_types_by_name['CyberModule']
_HMIMODE = DESCRIPTOR.message_types_by_name['HMIMode']
_HMIMODE_CYBERMODULESENTRY = _HMIMODE.nested_types_by_name['CyberModulesEntry']
_HMIMODE_MODULESENTRY = _HMIMODE.nested_types_by_name['ModulesEntry']
_HMIMODE_MONITOREDCOMPONENTSENTRY = _HMIMODE.nested_types_by_name['MonitoredComponentsEntry']
_HMIMODE_OTHERCOMPONENTSENTRY = _HMIMODE.nested_types_by_name['OtherComponentsEntry']
ProcessMonitorConfig = _reflection.GeneratedProtocolMessageType('ProcessMonitorConfig', (_message.Message,), {'DESCRIPTOR': _PROCESSMONITORCONFIG, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(ProcessMonitorConfig)
ModuleMonitorConfig = _reflection.GeneratedProtocolMessageType('ModuleMonitorConfig', (_message.Message,), {'DESCRIPTOR': _MODULEMONITORCONFIG, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(ModuleMonitorConfig)
ChannelMonitorConfig = _reflection.GeneratedProtocolMessageType('ChannelMonitorConfig', (_message.Message,), {'DESCRIPTOR': _CHANNELMONITORCONFIG, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(ChannelMonitorConfig)
ResourceMonitorConfig = _reflection.GeneratedProtocolMessageType('ResourceMonitorConfig', (_message.Message,), {'DiskSpace': _reflection.GeneratedProtocolMessageType('DiskSpace', (_message.Message,), {'DESCRIPTOR': _RESOURCEMONITORCONFIG_DISKSPACE, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'CPUUsage': _reflection.GeneratedProtocolMessageType('CPUUsage', (_message.Message,), {'DESCRIPTOR': _RESOURCEMONITORCONFIG_CPUUSAGE, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'MemoryUsage': _reflection.GeneratedProtocolMessageType('MemoryUsage', (_message.Message,), {'DESCRIPTOR': _RESOURCEMONITORCONFIG_MEMORYUSAGE, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'DiskLoad': _reflection.GeneratedProtocolMessageType('DiskLoad', (_message.Message,), {'DESCRIPTOR': _RESOURCEMONITORCONFIG_DISKLOAD, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'DESCRIPTOR': _RESOURCEMONITORCONFIG, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(ResourceMonitorConfig)
_sym_db.RegisterMessage(ResourceMonitorConfig.DiskSpace)
_sym_db.RegisterMessage(ResourceMonitorConfig.CPUUsage)
_sym_db.RegisterMessage(ResourceMonitorConfig.MemoryUsage)
_sym_db.RegisterMessage(ResourceMonitorConfig.DiskLoad)
MonitoredComponent = _reflection.GeneratedProtocolMessageType('MonitoredComponent', (_message.Message,), {'DESCRIPTOR': _MONITOREDCOMPONENT, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(MonitoredComponent)
Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {'DESCRIPTOR': _MODULE, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(Module)
CyberModule = _reflection.GeneratedProtocolMessageType('CyberModule', (_message.Message,), {'DESCRIPTOR': _CYBERMODULE, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(CyberModule)
HMIMode = _reflection.GeneratedProtocolMessageType('HMIMode', (_message.Message,), {'CyberModulesEntry': _reflection.GeneratedProtocolMessageType('CyberModulesEntry', (_message.Message,), {'DESCRIPTOR': _HMIMODE_CYBERMODULESENTRY, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'ModulesEntry': _reflection.GeneratedProtocolMessageType('ModulesEntry', (_message.Message,), {'DESCRIPTOR': _HMIMODE_MODULESENTRY, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'MonitoredComponentsEntry': _reflection.GeneratedProtocolMessageType('MonitoredComponentsEntry', (_message.Message,), {'DESCRIPTOR': _HMIMODE_MONITOREDCOMPONENTSENTRY, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'OtherComponentsEntry': _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), {'DESCRIPTOR': _HMIMODE_OTHERCOMPONENTSENTRY, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'}), 'DESCRIPTOR': _HMIMODE, '__module__': 'modules.dreamview.proto.hmi_mode_pb2'})
_sym_db.RegisterMessage(HMIMode)
_sym_db.RegisterMessage(HMIMode.CyberModulesEntry)
_sym_db.RegisterMessage(HMIMode.ModulesEntry)
_sym_db.RegisterMessage(HMIMode.MonitoredComponentsEntry)
_sym_db.RegisterMessage(HMIMode.OtherComponentsEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HMIMODE_CYBERMODULESENTRY._options = None
    _HMIMODE_CYBERMODULESENTRY._serialized_options = b'8\x01'
    _HMIMODE_MODULESENTRY._options = None
    _HMIMODE_MODULESENTRY._serialized_options = b'8\x01'
    _HMIMODE_MONITOREDCOMPONENTSENTRY._options = None
    _HMIMODE_MONITOREDCOMPONENTSENTRY._serialized_options = b'8\x01'
    _HMIMODE_OTHERCOMPONENTSENTRY._options = None
    _HMIMODE_OTHERCOMPONENTSENTRY._serialized_options = b'8\x01'
    _PROCESSMONITORCONFIG._serialized_start = 60
    _PROCESSMONITORCONFIG._serialized_end = 108
    _MODULEMONITORCONFIG._serialized_start = 110
    _MODULEMONITORCONFIG._serialized_end = 150
    _CHANNELMONITORCONFIG._serialized_start = 153
    _CHANNELMONITORCONFIG._serialized_end = 310
    _RESOURCEMONITORCONFIG._serialized_start = 313
    _RESOURCEMONITORCONFIG._serialized_end = 1031
    _RESOURCEMONITORCONFIG_DISKSPACE._serialized_start = 632
    _RESOURCEMONITORCONFIG_DISKSPACE._serialized_end = 727
    _RESOURCEMONITORCONFIG_CPUUSAGE._serialized_start = 729
    _RESOURCEMONITORCONFIG_CPUUSAGE._serialized_end = 827
    _RESOURCEMONITORCONFIG_MEMORYUSAGE._serialized_start = 829
    _RESOURCEMONITORCONFIG_MEMORYUSAGE._serialized_end = 936
    _RESOURCEMONITORCONFIG_DISKLOAD._serialized_start = 938
    _RESOURCEMONITORCONFIG_DISKLOAD._serialized_end = 1031
    _MONITOREDCOMPONENT._serialized_start = 1034
    _MONITOREDCOMPONENT._serialized_end = 1317
    _MODULE._serialized_start = 1320
    _MODULE._serialized_end = 1480
    _CYBERMODULE._serialized_start = 1482
    _CYBERMODULE._serialized_end = 1572
    _HMIMODE._serialized_start = 1575
    _HMIMODE._serialized_end = 2217
    _HMIMODE_CYBERMODULESENTRY._serialized_start = 1867
    _HMIMODE_CYBERMODULESENTRY._serialized_end = 1949
    _HMIMODE_MODULESENTRY._serialized_start = 1951
    _HMIMODE_MODULESENTRY._serialized_end = 2023
    _HMIMODE_MONITOREDCOMPONENTSENTRY._serialized_start = 2025
    _HMIMODE_MONITOREDCOMPONENTSENTRY._serialized_end = 2121
    _HMIMODE_OTHERCOMPONENTSENTRY._serialized_start = 2123
    _HMIMODE_OTHERCOMPONENTSENTRY._serialized_end = 2217