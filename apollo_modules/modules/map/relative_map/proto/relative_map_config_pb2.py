"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/map/relative_map/proto/relative_map_config.proto\x12\x13apollo.relative_map"\x7f\n\x12MapGenerationParam\x12 \n\x12default_left_width\x18\x01 \x01(\x01:\x041.75\x12!\n\x13default_right_width\x18\x02 \x01(\x01:\x041.75\x12$\n\x13default_speed_limit\x18\x03 \x01(\x01:\x0729.0576"\xaa\x04\n\x14NavigationLaneConfig\x12$\n\x17min_lane_marker_quality\x18\x01 \x01(\x01:\x030.5\x12I\n\x0blane_source\x18\x02 \x01(\x0e24.apollo.relative_map.NavigationLaneConfig.LaneSource\x12)\n\x1cmax_len_from_navigation_line\x18\x03 \x01(\x01:\x03250\x12(\n\x1bmin_len_for_navigation_lane\x18\x04 \x01(\x01:\x03150\x12(\n\x1bmax_len_for_navigation_lane\x18\x05 \x01(\x01:\x03250\x12-\n"ratio_navigation_lane_len_to_speed\x18\x06 \x01(\x01:\x018\x12+\n\x1fmax_distance_to_navigation_line\x18\x07 \x01(\x01:\x0215\x12.\n!min_view_range_to_use_lane_marker\x18\x08 \x01(\x01:\x030.5\x12 \n\x13min_lane_half_width\x18\t \x01(\x01:\x031.5\x12\x1e\n\x13max_lane_half_width\x18\n \x01(\x01:\x012\x12\x1f\n\x12lane_marker_weight\x18\x0b \x01(\x01:\x030.1"3\n\nLaneSource\x12\x0e\n\nPERCEPTION\x10\x01\x12\x15\n\x11OFFLINE_GENERATED\x10\x02"\x93\x01\n\x11RelativeMapConfig\x12:\n\tmap_param\x18\x01 \x01(\x0b2\'.apollo.relative_map.MapGenerationParam\x12B\n\x0fnavigation_lane\x18\x02 \x01(\x0b2).apollo.relative_map.NavigationLaneConfig')
_MAPGENERATIONPARAM = DESCRIPTOR.message_types_by_name['MapGenerationParam']
_NAVIGATIONLANECONFIG = DESCRIPTOR.message_types_by_name['NavigationLaneConfig']
_RELATIVEMAPCONFIG = DESCRIPTOR.message_types_by_name['RelativeMapConfig']
_NAVIGATIONLANECONFIG_LANESOURCE = _NAVIGATIONLANECONFIG.enum_types_by_name['LaneSource']
MapGenerationParam = _reflection.GeneratedProtocolMessageType('MapGenerationParam', (_message.Message,), {'DESCRIPTOR': _MAPGENERATIONPARAM, '__module__': 'modules.map.relative_map.proto.relative_map_config_pb2'})
_sym_db.RegisterMessage(MapGenerationParam)
NavigationLaneConfig = _reflection.GeneratedProtocolMessageType('NavigationLaneConfig', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONLANECONFIG, '__module__': 'modules.map.relative_map.proto.relative_map_config_pb2'})
_sym_db.RegisterMessage(NavigationLaneConfig)
RelativeMapConfig = _reflection.GeneratedProtocolMessageType('RelativeMapConfig', (_message.Message,), {'DESCRIPTOR': _RELATIVEMAPCONFIG, '__module__': 'modules.map.relative_map.proto.relative_map_config_pb2'})
_sym_db.RegisterMessage(RelativeMapConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MAPGENERATIONPARAM._serialized_start = 81
    _MAPGENERATIONPARAM._serialized_end = 208
    _NAVIGATIONLANECONFIG._serialized_start = 211
    _NAVIGATIONLANECONFIG._serialized_end = 765
    _NAVIGATIONLANECONFIG_LANESOURCE._serialized_start = 714
    _NAVIGATIONLANECONFIG_LANESOURCE._serialized_end = 765
    _RELATIVEMAPCONFIG._serialized_start = 768
    _RELATIVEMAPCONFIG._serialized_end = 915