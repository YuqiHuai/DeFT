"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from .....modules.localization.proto import localization_pb2 as modules_dot_localization_dot_proto_dot_localization__pb2
from .....modules.map.proto import map_pb2 as modules_dot_map_dot_proto_dot_map__pb2
from .....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/map/relative_map/proto/navigation.proto\x12\x13apollo.relative_map\x1a!modules/common/proto/header.proto\x1a$modules/common/proto/pnc_point.proto\x1a-modules/localization/proto/localization.proto\x1a\x1bmodules/map/proto/map.proto\x1a2modules/perception/proto/perception_obstacle.proto"J\n\x0eNavigationPath\x12!\n\x04path\x18\x01 \x01(\x0b2\x13.apollo.common.Path\x12\x15\n\rpath_priority\x18\x02 \x01(\r"u\n\x0eNavigationInfo\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12<\n\x0fnavigation_path\x18\x02 \x03(\x0b2#.apollo.relative_map.NavigationPath"\xed\x02\n\x06MapMsg\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12 \n\x05hdmap\x18\x02 \x01(\x0b2\x11.apollo.hdmap.Map\x12H\n\x0fnavigation_path\x18\x03 \x03(\x0b2/.apollo.relative_map.MapMsg.NavigationPathEntry\x123\n\x0blane_marker\x18\x04 \x01(\x0b2\x1e.apollo.perception.LaneMarkers\x12?\n\x0clocalization\x18\x05 \x01(\x0b2).apollo.localization.LocalizationEstimate\x1aZ\n\x13NavigationPathEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x122\n\x05value\x18\x02 \x01(\x0b2#.apollo.relative_map.NavigationPath:\x028\x01')
_NAVIGATIONPATH = DESCRIPTOR.message_types_by_name['NavigationPath']
_NAVIGATIONINFO = DESCRIPTOR.message_types_by_name['NavigationInfo']
_MAPMSG = DESCRIPTOR.message_types_by_name['MapMsg']
_MAPMSG_NAVIGATIONPATHENTRY = _MAPMSG.nested_types_by_name['NavigationPathEntry']
NavigationPath = _reflection.GeneratedProtocolMessageType('NavigationPath', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONPATH, '__module__': 'modules.map.relative_map.proto.navigation_pb2'})
_sym_db.RegisterMessage(NavigationPath)
NavigationInfo = _reflection.GeneratedProtocolMessageType('NavigationInfo', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONINFO, '__module__': 'modules.map.relative_map.proto.navigation_pb2'})
_sym_db.RegisterMessage(NavigationInfo)
MapMsg = _reflection.GeneratedProtocolMessageType('MapMsg', (_message.Message,), {'NavigationPathEntry': _reflection.GeneratedProtocolMessageType('NavigationPathEntry', (_message.Message,), {'DESCRIPTOR': _MAPMSG_NAVIGATIONPATHENTRY, '__module__': 'modules.map.relative_map.proto.navigation_pb2'}), 'DESCRIPTOR': _MAPMSG, '__module__': 'modules.map.relative_map.proto.navigation_pb2'})
_sym_db.RegisterMessage(MapMsg)
_sym_db.RegisterMessage(MapMsg.NavigationPathEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MAPMSG_NAVIGATIONPATHENTRY._options = None
    _MAPMSG_NAVIGATIONPATHENTRY._serialized_options = b'8\x01'
    _NAVIGATIONPATH._serialized_start = 273
    _NAVIGATIONPATH._serialized_end = 347
    _NAVIGATIONINFO._serialized_start = 349
    _NAVIGATIONINFO._serialized_end = 466
    _MAPMSG._serialized_start = 469
    _MAPMSG._serialized_end = 834
    _MAPMSG_NAVIGATIONPATHENTRY._serialized_start = 744
    _MAPMSG_NAVIGATIONPATHENTRY._serialized_end = 834