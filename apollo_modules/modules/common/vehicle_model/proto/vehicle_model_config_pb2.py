"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/common/vehicle_model/proto/vehicle_model_config.proto\x12\rapollo.common"\xab\x03\n\x12VehicleModelConfig\x12?\n\nmodel_type\x18\x01 \x01(\x0e2+.apollo.common.VehicleModelConfig.ModelType\x12Z\n\x1arc_kinematic_bicycle_model\x18\x02 \x01(\x0b26.apollo.common.RearCenteredKinematicBicycleModelConfig\x12W\n\x1acomc_dynamic_bicycle_model\x18\x03 \x01(\x0b23.apollo.common.ComCenteredDynamicBicycleModelConfig\x120\n\tmlp_model\x18\x04 \x01(\x0b2\x1d.apollo.common.MlpModelConfig"m\n\tModelType\x12)\n%REAR_CENTERED_KINEMATIC_BICYCLE_MODEL\x10\x00\x12&\n"COM_CENTERED_DYNAMIC_BICYCLE_MODEL\x10\x01\x12\r\n\tMLP_MODEL\x10\x02"5\n\'RearCenteredKinematicBicycleModelConfig\x12\n\n\x02dt\x18\x01 \x01(\x01"2\n$ComCenteredDynamicBicycleModelConfig\x12\n\n\x02dt\x18\x01 \x01(\x01"\x1c\n\x0eMlpModelConfig\x12\n\n\x02dt\x18\x01 \x01(\x01')
_VEHICLEMODELCONFIG = DESCRIPTOR.message_types_by_name['VehicleModelConfig']
_REARCENTEREDKINEMATICBICYCLEMODELCONFIG = DESCRIPTOR.message_types_by_name['RearCenteredKinematicBicycleModelConfig']
_COMCENTEREDDYNAMICBICYCLEMODELCONFIG = DESCRIPTOR.message_types_by_name['ComCenteredDynamicBicycleModelConfig']
_MLPMODELCONFIG = DESCRIPTOR.message_types_by_name['MlpModelConfig']
_VEHICLEMODELCONFIG_MODELTYPE = _VEHICLEMODELCONFIG.enum_types_by_name['ModelType']
VehicleModelConfig = _reflection.GeneratedProtocolMessageType('VehicleModelConfig', (_message.Message,), {'DESCRIPTOR': _VEHICLEMODELCONFIG, '__module__': 'modules.common.vehicle_model.proto.vehicle_model_config_pb2'})
_sym_db.RegisterMessage(VehicleModelConfig)
RearCenteredKinematicBicycleModelConfig = _reflection.GeneratedProtocolMessageType('RearCenteredKinematicBicycleModelConfig', (_message.Message,), {'DESCRIPTOR': _REARCENTEREDKINEMATICBICYCLEMODELCONFIG, '__module__': 'modules.common.vehicle_model.proto.vehicle_model_config_pb2'})
_sym_db.RegisterMessage(RearCenteredKinematicBicycleModelConfig)
ComCenteredDynamicBicycleModelConfig = _reflection.GeneratedProtocolMessageType('ComCenteredDynamicBicycleModelConfig', (_message.Message,), {'DESCRIPTOR': _COMCENTEREDDYNAMICBICYCLEMODELCONFIG, '__module__': 'modules.common.vehicle_model.proto.vehicle_model_config_pb2'})
_sym_db.RegisterMessage(ComCenteredDynamicBicycleModelConfig)
MlpModelConfig = _reflection.GeneratedProtocolMessageType('MlpModelConfig', (_message.Message,), {'DESCRIPTOR': _MLPMODELCONFIG, '__module__': 'modules.common.vehicle_model.proto.vehicle_model_config_pb2'})
_sym_db.RegisterMessage(MlpModelConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VEHICLEMODELCONFIG._serialized_start = 81
    _VEHICLEMODELCONFIG._serialized_end = 508
    _VEHICLEMODELCONFIG_MODELTYPE._serialized_start = 399
    _VEHICLEMODELCONFIG_MODELTYPE._serialized_end = 508
    _REARCENTEREDKINEMATICBICYCLEMODELCONFIG._serialized_start = 510
    _REARCENTEREDKINEMATICBICYCLEMODELCONFIG._serialized_end = 563
    _COMCENTEREDDYNAMICBICYCLEMODELCONFIG._serialized_start = 565
    _COMCENTEREDDYNAMICBICYCLEMODELCONFIG._serialized_end = 615
    _MLPMODELCONFIG._serialized_start = 617
    _MLPMODELCONFIG._serialized_end = 645