"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/map/proto/map_stop_sign.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"\x82\x02\n\x08StopSign\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\tstop_line\x18\x02 \x03(\x0b2\x13.apollo.hdmap.Curve\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x12-\n\x04type\x18\x04 \x01(\x0e2\x1f.apollo.hdmap.StopSign.StopType"[\n\x08StopType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07ONE_WAY\x10\x01\x12\x0b\n\x07TWO_WAY\x10\x02\x12\r\n\tTHREE_WAY\x10\x03\x12\x0c\n\x08FOUR_WAY\x10\x04\x12\x0b\n\x07ALL_WAY\x10\x05')
_STOPSIGN = DESCRIPTOR.message_types_by_name['StopSign']
_STOPSIGN_STOPTYPE = _STOPSIGN.enum_types_by_name['StopType']
StopSign = _reflection.GeneratedProtocolMessageType('StopSign', (_message.Message,), {'DESCRIPTOR': _STOPSIGN, '__module__': 'modules.map.proto.map_stop_sign_pb2'})
_sym_db.RegisterMessage(StopSign)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STOPSIGN._serialized_start = 126
    _STOPSIGN._serialized_end = 384
    _STOPSIGN_STOPTYPE._serialized_start = 293
    _STOPSIGN_STOPTYPE._serialized_end = 384