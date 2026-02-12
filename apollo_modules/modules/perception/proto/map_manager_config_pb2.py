"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/perception/proto/map_manager_config.proto\x12\x17apollo.perception.lidar"v\n\x10MapManagerConfig\x12\x1a\n\x0bupdate_pose\x18\x01 \x01(\x08:\x05false\x12\x1f\n\x13roi_search_distance\x18\x02 \x01(\x01:\x0280\x12\x12\n\nlane_range\x18\x03 \x01(\x01\x12\x11\n\tmax_depth\x18\x04 \x01(\x01')
_MAPMANAGERCONFIG = DESCRIPTOR.message_types_by_name['MapManagerConfig']
MapManagerConfig = _reflection.GeneratedProtocolMessageType('MapManagerConfig', (_message.Message,), {'DESCRIPTOR': _MAPMANAGERCONFIG, '__module__': 'modules.perception.proto.map_manager_config_pb2'})
_sym_db.RegisterMessage(MapManagerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MAPMANAGERCONFIG._serialized_start = 78
    _MAPMANAGERCONFIG._serialized_end = 196