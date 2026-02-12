"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/tools/navigator/dbmap/proto/dbmap.proto\x12\x0capollo.dbmap"F\n\x07DBPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01s\x18\x04 \x01(\x01\x12\x0f\n\x07heading\x18\x05 \x01(\x01".\n\x06DBLine\x12$\n\x05point\x18\x01 \x03(\x0b2\x15.apollo.dbmap.DBPoint"o\n\x12DBNeighbourSegment\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05end_s\x18\x02 \x01(\x01\x12\x0f\n\x07path_id\x18\x03 \x01(\t\x12\x14\n\x0cpath_start_s\x18\x04 \x01(\x01\x12\x12\n\npath_end_s\x18\x05 \x01(\x01"D\n\x0fDBNeighbourPath\x121\n\x07segment\x18\x01 \x03(\x0b2 .apollo.dbmap.DBNeighbourSegment"\xad\x02\n\x06DBPath\x12\n\n\x02id\x18\x01 \x01(\t\x12"\n\x04path\x18\x02 \x03(\x0b2\x14.apollo.dbmap.DBLine\x12*\n\x0cleft_bounday\x18\x03 \x03(\x0b2\x14.apollo.dbmap.DBLine\x12+\n\rright_bounday\x18\x04 \x03(\x0b2\x14.apollo.dbmap.DBLine\x120\n\tleft_path\x18\x05 \x03(\x0b2\x1d.apollo.dbmap.DBNeighbourPath\x121\n\nright_path\x18\x06 \x03(\x0b2\x1d.apollo.dbmap.DBNeighbourPath\x125\n\x0eduplicate_path\x18\x07 \x03(\x0b2\x1d.apollo.dbmap.DBNeighbourPath",\n\x05DBMap\x12#\n\x05paths\x18\x01 \x03(\x0b2\x14.apollo.dbmap.DBPath')
_DBPOINT = DESCRIPTOR.message_types_by_name['DBPoint']
_DBLINE = DESCRIPTOR.message_types_by_name['DBLine']
_DBNEIGHBOURSEGMENT = DESCRIPTOR.message_types_by_name['DBNeighbourSegment']
_DBNEIGHBOURPATH = DESCRIPTOR.message_types_by_name['DBNeighbourPath']
_DBPATH = DESCRIPTOR.message_types_by_name['DBPath']
_DBMAP = DESCRIPTOR.message_types_by_name['DBMap']
DBPoint = _reflection.GeneratedProtocolMessageType('DBPoint', (_message.Message,), {'DESCRIPTOR': _DBPOINT, '__module__': 'modules.tools.navigator.dbmap.proto.dbmap_pb2'})
_sym_db.RegisterMessage(DBPoint)
DBLine = _reflection.GeneratedProtocolMessageType('DBLine', (_message.Message,), {'DESCRIPTOR': _DBLINE, '__module__': 'modules.tools.navigator.dbmap.proto.dbmap_pb2'})
_sym_db.RegisterMessage(DBLine)
DBNeighbourSegment = _reflection.GeneratedProtocolMessageType('DBNeighbourSegment', (_message.Message,), {'DESCRIPTOR': _DBNEIGHBOURSEGMENT, '__module__': 'modules.tools.navigator.dbmap.proto.dbmap_pb2'})
_sym_db.RegisterMessage(DBNeighbourSegment)
DBNeighbourPath = _reflection.GeneratedProtocolMessageType('DBNeighbourPath', (_message.Message,), {'DESCRIPTOR': _DBNEIGHBOURPATH, '__module__': 'modules.tools.navigator.dbmap.proto.dbmap_pb2'})
_sym_db.RegisterMessage(DBNeighbourPath)
DBPath = _reflection.GeneratedProtocolMessageType('DBPath', (_message.Message,), {'DESCRIPTOR': _DBPATH, '__module__': 'modules.tools.navigator.dbmap.proto.dbmap_pb2'})
_sym_db.RegisterMessage(DBPath)
DBMap = _reflection.GeneratedProtocolMessageType('DBMap', (_message.Message,), {'DESCRIPTOR': _DBMAP, '__module__': 'modules.tools.navigator.dbmap.proto.dbmap_pb2'})
_sym_db.RegisterMessage(DBMap)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DBPOINT._serialized_start = 65
    _DBPOINT._serialized_end = 135
    _DBLINE._serialized_start = 137
    _DBLINE._serialized_end = 183
    _DBNEIGHBOURSEGMENT._serialized_start = 185
    _DBNEIGHBOURSEGMENT._serialized_end = 296
    _DBNEIGHBOURPATH._serialized_start = 298
    _DBNEIGHBOURPATH._serialized_end = 366
    _DBPATH._serialized_start = 369
    _DBPATH._serialized_end = 670
    _DBMAP._serialized_start = 672
    _DBMAP._serialized_end = 716