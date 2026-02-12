"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/map/proto/map_geometry.proto\x12\x0capollo.hdmap\x1a#modules/common/proto/geometry.proto"1\n\x07Polygon\x12&\n\x05point\x18\x01 \x03(\x0b2\x17.apollo.common.PointENU"5\n\x0bLineSegment\x12&\n\x05point\x18\x01 \x03(\x0b2\x17.apollo.common.PointENU"\xac\x01\n\x0cCurveSegment\x121\n\x0cline_segment\x18\x01 \x01(\x0b2\x19.apollo.hdmap.LineSegmentH\x00\x12\t\n\x01s\x18\x06 \x01(\x01\x12/\n\x0estart_position\x18\x07 \x01(\x0b2\x17.apollo.common.PointENU\x12\x0f\n\x07heading\x18\x08 \x01(\x01\x12\x0e\n\x06length\x18\t \x01(\x01B\x0c\n\ncurve_type"4\n\x05Curve\x12+\n\x07segment\x18\x01 \x03(\x0b2\x1a.apollo.hdmap.CurveSegment')
_POLYGON = DESCRIPTOR.message_types_by_name['Polygon']
_LINESEGMENT = DESCRIPTOR.message_types_by_name['LineSegment']
_CURVESEGMENT = DESCRIPTOR.message_types_by_name['CurveSegment']
_CURVE = DESCRIPTOR.message_types_by_name['Curve']
Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {'DESCRIPTOR': _POLYGON, '__module__': 'modules.map.proto.map_geometry_pb2'})
_sym_db.RegisterMessage(Polygon)
LineSegment = _reflection.GeneratedProtocolMessageType('LineSegment', (_message.Message,), {'DESCRIPTOR': _LINESEGMENT, '__module__': 'modules.map.proto.map_geometry_pb2'})
_sym_db.RegisterMessage(LineSegment)
CurveSegment = _reflection.GeneratedProtocolMessageType('CurveSegment', (_message.Message,), {'DESCRIPTOR': _CURVESEGMENT, '__module__': 'modules.map.proto.map_geometry_pb2'})
_sym_db.RegisterMessage(CurveSegment)
Curve = _reflection.GeneratedProtocolMessageType('Curve', (_message.Message,), {'DESCRIPTOR': _CURVE, '__module__': 'modules.map.proto.map_geometry_pb2'})
_sym_db.RegisterMessage(Curve)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POLYGON._serialized_start = 91
    _POLYGON._serialized_end = 140
    _LINESEGMENT._serialized_start = 142
    _LINESEGMENT._serialized_end = 195
    _CURVESEGMENT._serialized_start = 198
    _CURVESEGMENT._serialized_end = 370
    _CURVE._serialized_start = 372
    _CURVE._serialized_end = 424