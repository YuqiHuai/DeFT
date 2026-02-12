"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"modules/map/proto/map_signal.proto\x12\x0capollo.hdmap\x1a#modules/common/proto/geometry.proto\x1a$modules/map/proto/map_geometry.proto\x1a\x1emodules/map/proto/map_id.proto"\xa1\x02\n\tSubsignal\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12*\n\x04type\x18\x02 \x01(\x0e2\x1c.apollo.hdmap.Subsignal.Type\x12)\n\x08location\x18\x03 \x01(\x0b2\x17.apollo.common.PointENU"\x9e\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06CIRCLE\x10\x02\x12\x0e\n\nARROW_LEFT\x10\x03\x12\x11\n\rARROW_FORWARD\x10\x04\x12\x0f\n\x0bARROW_RIGHT\x10\x05\x12\x1a\n\x16ARROW_LEFT_AND_FORWARD\x10\x06\x12\x1b\n\x17ARROW_RIGHT_AND_FORWARD\x10\x07\x12\x10\n\x0cARROW_U_TURN\x10\x08"a\n\x08SignInfo\x12)\n\x04type\x18\x01 \x01(\x0e2\x1b.apollo.hdmap.SignInfo.Type"*\n\x04Type\x12\x08\n\x04None\x10\x00\x12\x18\n\x14NO_RIGHT_TURN_ON_RED\x10\x01"\x92\x03\n\x06Signal\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12\'\n\x08boundary\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12*\n\tsubsignal\x18\x03 \x03(\x0b2\x17.apollo.hdmap.Subsignal\x12$\n\noverlap_id\x18\x04 \x03(\x0b2\x10.apollo.hdmap.Id\x12\'\n\x04type\x18\x05 \x01(\x0e2\x19.apollo.hdmap.Signal.Type\x12&\n\tstop_line\x18\x06 \x03(\x0b2\x13.apollo.hdmap.Curve\x12)\n\tsign_info\x18\x07 \x03(\x0b2\x16.apollo.hdmap.SignInfo"s\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x14\n\x10MIX_2_HORIZONTAL\x10\x02\x12\x12\n\x0eMIX_2_VERTICAL\x10\x03\x12\x14\n\x10MIX_3_HORIZONTAL\x10\x04\x12\x12\n\x0eMIX_3_VERTICAL\x10\x05\x12\n\n\x06SINGLE\x10\x06')
_SUBSIGNAL = DESCRIPTOR.message_types_by_name['Subsignal']
_SIGNINFO = DESCRIPTOR.message_types_by_name['SignInfo']
_SIGNAL = DESCRIPTOR.message_types_by_name['Signal']
_SUBSIGNAL_TYPE = _SUBSIGNAL.enum_types_by_name['Type']
_SIGNINFO_TYPE = _SIGNINFO.enum_types_by_name['Type']
_SIGNAL_TYPE = _SIGNAL.enum_types_by_name['Type']
Subsignal = _reflection.GeneratedProtocolMessageType('Subsignal', (_message.Message,), {'DESCRIPTOR': _SUBSIGNAL, '__module__': 'modules.map.proto.map_signal_pb2'})
_sym_db.RegisterMessage(Subsignal)
SignInfo = _reflection.GeneratedProtocolMessageType('SignInfo', (_message.Message,), {'DESCRIPTOR': _SIGNINFO, '__module__': 'modules.map.proto.map_signal_pb2'})
_sym_db.RegisterMessage(SignInfo)
Signal = _reflection.GeneratedProtocolMessageType('Signal', (_message.Message,), {'DESCRIPTOR': _SIGNAL, '__module__': 'modules.map.proto.map_signal_pb2'})
_sym_db.RegisterMessage(Signal)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SUBSIGNAL._serialized_start = 160
    _SUBSIGNAL._serialized_end = 449
    _SUBSIGNAL_TYPE._serialized_start = 291
    _SUBSIGNAL_TYPE._serialized_end = 449
    _SIGNINFO._serialized_start = 451
    _SIGNINFO._serialized_end = 548
    _SIGNINFO_TYPE._serialized_start = 506
    _SIGNINFO_TYPE._serialized_end = 548
    _SIGNAL._serialized_start = 551
    _SIGNAL._serialized_end = 953
    _SIGNAL_TYPE._serialized_start = 838
    _SIGNAL_TYPE._serialized_end = 953