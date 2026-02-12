"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.map.tools.map_datachecker.proto import collection_check_message_pb2 as modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/map/tools/map_datachecker/proto/collection_service.proto\x12\x0capollo.hdmap\x1aFmodules/map/tools/map_datachecker/proto/collection_check_message.proto2\xf1\x03\n\x18CollectionCheckerService\x12^\n\x13ServiceDynamicAlign\x12!.apollo.hdmap.DynamicAlignRequest\x1a".apollo.hdmap.DynamicAlignResponse"\x00\x12[\n\x12ServiceStaticAlign\x12 .apollo.hdmap.StaticAlignRequest\x1a!.apollo.hdmap.StaticAlignResponse"\x00\x12X\n\x11ServiceEightRoute\x12\x1f.apollo.hdmap.EightRouteRequest\x1a .apollo.hdmap.EightRouteResponse"\x00\x12a\n\x14ServiceChannelVerify\x12".apollo.hdmap.ChannelVerifyRequest\x1a#.apollo.hdmap.ChannelVerifyResponse"\x00\x12[\n\x12ServiceLoopsVerify\x12 .apollo.hdmap.LoopsVerifyRequest\x1a!.apollo.hdmap.LoopsVerifyResponse"\x00')
_COLLECTIONCHECKERSERVICE = DESCRIPTOR.services_by_name['CollectionCheckerService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _COLLECTIONCHECKERSERVICE._serialized_start = 155
    _COLLECTIONCHECKERSERVICE._serialized_end = 652