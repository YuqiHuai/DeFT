"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/map/proto/map_speed_control.proto\x12\x0capollo.hdmap\x1a$modules/map/proto/map_geometry.proto"Y\n\x0cSpeedControl\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12\x13\n\x0bspeed_limit\x18\x03 \x01(\x01"B\n\rSpeedControls\x121\n\rspeed_control\x18\x01 \x03(\x0b2\x1a.apollo.hdmap.SpeedControl')
_SPEEDCONTROL = DESCRIPTOR.message_types_by_name['SpeedControl']
_SPEEDCONTROLS = DESCRIPTOR.message_types_by_name['SpeedControls']
SpeedControl = _reflection.GeneratedProtocolMessageType('SpeedControl', (_message.Message,), {'DESCRIPTOR': _SPEEDCONTROL, '__module__': 'modules.map.proto.map_speed_control_pb2'})
_sym_db.RegisterMessage(SpeedControl)
SpeedControls = _reflection.GeneratedProtocolMessageType('SpeedControls', (_message.Message,), {'DESCRIPTOR': _SPEEDCONTROLS, '__module__': 'modules.map.proto.map_speed_control_pb2'})
_sym_db.RegisterMessage(SpeedControls)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SPEEDCONTROL._serialized_start = 97
    _SPEEDCONTROL._serialized_end = 186
    _SPEEDCONTROLS._serialized_start = 188
    _SPEEDCONTROLS._serialized_end = 254