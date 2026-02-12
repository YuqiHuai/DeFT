"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/map/proto/map_pnc_junction.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"\x92\x02\n\x07Passage\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12#\n\tsignal_id\x18\x02 \x03(\x0b2\x10.apollo.hdmap.Id\x12"\n\x08yield_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x12&\n\x0cstop_sign_id\x18\x04 \x03(\x0b2\x10.apollo.hdmap.Id\x12!\n\x07lane_id\x18\x05 \x03(\x0b2\x10.apollo.hdmap.Id\x12(\n\x04type\x18\x06 \x01(\x0e2\x1a.apollo.hdmap.Passage.Type"+\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08ENTRANCE\x10\x01\x12\x08\n\x04EXIT\x10\x02"T\n\x0cPassageGroup\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07passage\x18\x02 \x03(\x0b2\x15.apollo.hdmap.Passage"\xac\x01\n\x0bPNCJunction\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x121\n\rpassage_group\x18\x04 \x03(\x0b2\x1a.apollo.hdmap.PassageGroup')
_PASSAGE = DESCRIPTOR.message_types_by_name['Passage']
_PASSAGEGROUP = DESCRIPTOR.message_types_by_name['PassageGroup']
_PNCJUNCTION = DESCRIPTOR.message_types_by_name['PNCJunction']
_PASSAGE_TYPE = _PASSAGE.enum_types_by_name['Type']
Passage = _reflection.GeneratedProtocolMessageType('Passage', (_message.Message,), {'DESCRIPTOR': _PASSAGE, '__module__': 'modules.map.proto.map_pnc_junction_pb2'})
_sym_db.RegisterMessage(Passage)
PassageGroup = _reflection.GeneratedProtocolMessageType('PassageGroup', (_message.Message,), {'DESCRIPTOR': _PASSAGEGROUP, '__module__': 'modules.map.proto.map_pnc_junction_pb2'})
_sym_db.RegisterMessage(PassageGroup)
PNCJunction = _reflection.GeneratedProtocolMessageType('PNCJunction', (_message.Message,), {'DESCRIPTOR': _PNCJUNCTION, '__module__': 'modules.map.proto.map_pnc_junction_pb2'})
_sym_db.RegisterMessage(PNCJunction)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PASSAGE._serialized_start = 129
    _PASSAGE._serialized_end = 403
    _PASSAGE_TYPE._serialized_start = 360
    _PASSAGE_TYPE._serialized_end = 403
    _PASSAGEGROUP._serialized_start = 405
    _PASSAGEGROUP._serialized_end = 489
    _PNCJUNCTION._serialized_start = 492
    _PNCJUNCTION._serialized_end = 664