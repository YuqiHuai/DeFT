"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/dreamview/proto/hmi_config.proto\x12\x10apollo.dreamview"\xc0\x02\n\tHMIConfig\x125\n\x05modes\x18\x01 \x03(\x0b2&.apollo.dreamview.HMIConfig.ModesEntry\x123\n\x04maps\x18\x02 \x03(\x0b2%.apollo.dreamview.HMIConfig.MapsEntry\x12;\n\x08vehicles\x18\x03 \x03(\x0b2).apollo.dreamview.HMIConfig.VehiclesEntry\x1a,\n\nModesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a+\n\tMapsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a/\n\rVehiclesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"}\n\x0bVehicleData\x12:\n\ndata_files\x18\x01 \x03(\x0b2&.apollo.dreamview.VehicleData.DataFile\x1a2\n\x08DataFile\x12\x13\n\x0bsource_path\x18\x01 \x01(\t\x12\x11\n\tdest_path\x18\x02 \x01(\t*\xb1\x01\n\tHMIAction\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nSETUP_MODE\x10\x01\x12\x0e\n\nRESET_MODE\x10\x02\x12\x13\n\x0fENTER_AUTO_MODE\x10\x03\x12\r\n\tDISENGAGE\x10\x04\x12\x0f\n\x0bCHANGE_MODE\x10\x05\x12\x0e\n\nCHANGE_MAP\x10\x06\x12\x12\n\x0eCHANGE_VEHICLE\x10\x07\x12\x10\n\x0cSTART_MODULE\x10\x08\x12\x0f\n\x0bSTOP_MODULE\x10\t')
_HMIACTION = DESCRIPTOR.enum_types_by_name['HMIAction']
HMIAction = enum_type_wrapper.EnumTypeWrapper(_HMIACTION)
NONE = 0
SETUP_MODE = 1
RESET_MODE = 2
ENTER_AUTO_MODE = 3
DISENGAGE = 4
CHANGE_MODE = 5
CHANGE_MAP = 6
CHANGE_VEHICLE = 7
START_MODULE = 8
STOP_MODULE = 9
_HMICONFIG = DESCRIPTOR.message_types_by_name['HMIConfig']
_HMICONFIG_MODESENTRY = _HMICONFIG.nested_types_by_name['ModesEntry']
_HMICONFIG_MAPSENTRY = _HMICONFIG.nested_types_by_name['MapsEntry']
_HMICONFIG_VEHICLESENTRY = _HMICONFIG.nested_types_by_name['VehiclesEntry']
_VEHICLEDATA = DESCRIPTOR.message_types_by_name['VehicleData']
_VEHICLEDATA_DATAFILE = _VEHICLEDATA.nested_types_by_name['DataFile']
HMIConfig = _reflection.GeneratedProtocolMessageType('HMIConfig', (_message.Message,), {'ModesEntry': _reflection.GeneratedProtocolMessageType('ModesEntry', (_message.Message,), {'DESCRIPTOR': _HMICONFIG_MODESENTRY, '__module__': 'modules.dreamview.proto.hmi_config_pb2'}), 'MapsEntry': _reflection.GeneratedProtocolMessageType('MapsEntry', (_message.Message,), {'DESCRIPTOR': _HMICONFIG_MAPSENTRY, '__module__': 'modules.dreamview.proto.hmi_config_pb2'}), 'VehiclesEntry': _reflection.GeneratedProtocolMessageType('VehiclesEntry', (_message.Message,), {'DESCRIPTOR': _HMICONFIG_VEHICLESENTRY, '__module__': 'modules.dreamview.proto.hmi_config_pb2'}), 'DESCRIPTOR': _HMICONFIG, '__module__': 'modules.dreamview.proto.hmi_config_pb2'})
_sym_db.RegisterMessage(HMIConfig)
_sym_db.RegisterMessage(HMIConfig.ModesEntry)
_sym_db.RegisterMessage(HMIConfig.MapsEntry)
_sym_db.RegisterMessage(HMIConfig.VehiclesEntry)
VehicleData = _reflection.GeneratedProtocolMessageType('VehicleData', (_message.Message,), {'DataFile': _reflection.GeneratedProtocolMessageType('DataFile', (_message.Message,), {'DESCRIPTOR': _VEHICLEDATA_DATAFILE, '__module__': 'modules.dreamview.proto.hmi_config_pb2'}), 'DESCRIPTOR': _VEHICLEDATA, '__module__': 'modules.dreamview.proto.hmi_config_pb2'})
_sym_db.RegisterMessage(VehicleData)
_sym_db.RegisterMessage(VehicleData.DataFile)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HMICONFIG_MODESENTRY._options = None
    _HMICONFIG_MODESENTRY._serialized_options = b'8\x01'
    _HMICONFIG_MAPSENTRY._options = None
    _HMICONFIG_MAPSENTRY._serialized_options = b'8\x01'
    _HMICONFIG_VEHICLESENTRY._options = None
    _HMICONFIG_VEHICLESENTRY._serialized_options = b'8\x01'
    _HMIACTION._serialized_start = 513
    _HMIACTION._serialized_end = 690
    _HMICONFIG._serialized_start = 63
    _HMICONFIG._serialized_end = 383
    _HMICONFIG_MODESENTRY._serialized_start = 245
    _HMICONFIG_MODESENTRY._serialized_end = 289
    _HMICONFIG_MAPSENTRY._serialized_start = 291
    _HMICONFIG_MAPSENTRY._serialized_end = 334
    _HMICONFIG_VEHICLESENTRY._serialized_start = 336
    _HMICONFIG_VEHICLESENTRY._serialized_end = 383
    _VEHICLEDATA._serialized_start = 385
    _VEHICLEDATA._serialized_end = 510
    _VEHICLEDATA_DATAFILE._serialized_start = 460
    _VEHICLEDATA_DATAFILE._serialized_end = 510