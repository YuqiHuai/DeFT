"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/planning/proto/planning_semantic_map_config.proto\x12\x0fapollo.planning"\xc8\x02\n\x19PlanningSemanticMapConfig\x12\x12\n\nresolution\x18\x01 \x01(\x01\x12\x0e\n\x06height\x18d \x01(\x05\x12\r\n\x05width\x18e \x01(\x05\x12\x11\n\tego_idx_x\x18f \x01(\x05\x12\x11\n\tego_idx_y\x18g \x01(\x05\x12\x1a\n\x12max_rand_delta_phi\x18h \x01(\x01\x12\x1e\n\x16max_ego_future_horizon\x18i \x01(\x01\x12\x1c\n\x14max_ego_past_horizon\x18j \x01(\x01\x12\x1e\n\x16max_obs_future_horizon\x18k \x01(\x01\x12\x1c\n\x14max_obs_past_horizon\x18l \x01(\x01\x12\x19\n\x10base_map_padding\x18\xc8\x01 \x01(\x05\x12\x1f\n\x16city_driving_max_speed\x18\xc9\x01 \x01(\x01')
_PLANNINGSEMANTICMAPCONFIG = DESCRIPTOR.message_types_by_name['PlanningSemanticMapConfig']
PlanningSemanticMapConfig = _reflection.GeneratedProtocolMessageType('PlanningSemanticMapConfig', (_message.Message,), {'DESCRIPTOR': _PLANNINGSEMANTICMAPCONFIG, '__module__': 'modules.planning.proto.planning_semantic_map_config_pb2'})
_sym_db.RegisterMessage(PlanningSemanticMapConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PLANNINGSEMANTICMAPCONFIG._serialized_start = 79
    _PLANNINGSEMANTICMAPCONFIG._serialized_end = 407