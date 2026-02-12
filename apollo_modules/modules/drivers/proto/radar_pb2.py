"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import error_code_pb2 as modules_dot_common_dot_proto_dot_error__code__pb2
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!modules/drivers/proto/radar.proto\x12\x0eapollo.drivers\x1a%modules/common/proto/error_code.proto\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\xcc\x05\n\rRadarObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x121\n\x11relative_position\x18\x02 \x01(\x0b2\x16.apollo.common.Point2D\x121\n\x11relative_velocity\x18\x03 \x01(\x0b2\x16.apollo.common.Point2D\x12\x0b\n\x03rcs\x18\x04 \x01(\x01\x12A\n\rmoving_status\x18\x05 \x01(\x0e2*.apollo.drivers.RadarObstacle.MovingStatus\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06length\x18\x07 \x01(\x01\x12\x0e\n\x06height\x18\x08 \x01(\x01\x12\r\n\x05theta\x18\t \x01(\x01\x121\n\x11absolute_position\x18\n \x01(\x0b2\x16.apollo.common.Point2D\x121\n\x11absolute_velocity\x18\x0b \x01(\x0b2\x16.apollo.common.Point2D\x12\r\n\x05count\x18\x0c \x01(\x05\x12\x1b\n\x13moving_frames_count\x18\r \x01(\x05\x124\n\x06status\x18\x0e \x01(\x0e2$.apollo.drivers.RadarObstacle.Status"\xae\x01\n\x06Status\x12\r\n\tNO_TARGET\x10\x00\x12\x0e\n\nNEW_TARGET\x10\x01\x12\x16\n\x12NEW_UPDATED_TARGET\x10\x02\x12\x12\n\x0eUPDATED_TARGET\x10\x03\x12\x12\n\x0eCOASTED_TARGET\x10\x04\x12\x11\n\rMERGED_TARGET\x10\x05\x12\x1a\n\x16INVALID_COASTED_TARGET\x10\x06\x12\x16\n\x12NEW_COASTED_TARGET\x10\x07"B\n\x0cMovingStatus\x12\x0e\n\nSTATIONARY\x10\x00\x12\x0b\n\x07NEARING\x10\x01\x12\x0b\n\x07AWAYING\x10\x02\x12\x08\n\x04NONE\x10\x03"\x89\x02\n\x0eRadarObstacles\x12I\n\x0eradar_obstacle\x18\x01 \x03(\x0b21.apollo.drivers.RadarObstacles.RadarObstacleEntry\x12%\n\x06header\x18\x02 \x01(\x0b2\x15.apollo.common.Header\x120\n\nerror_code\x18\x03 \x01(\x0e2\x18.apollo.common.ErrorCode:\x02OK\x1aS\n\x12RadarObstacleEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12,\n\x05value\x18\x02 \x01(\x0b2\x1d.apollo.drivers.RadarObstacle:\x028\x01')
_RADAROBSTACLE = DESCRIPTOR.message_types_by_name['RadarObstacle']
_RADAROBSTACLES = DESCRIPTOR.message_types_by_name['RadarObstacles']
_RADAROBSTACLES_RADAROBSTACLEENTRY = _RADAROBSTACLES.nested_types_by_name['RadarObstacleEntry']
_RADAROBSTACLE_STATUS = _RADAROBSTACLE.enum_types_by_name['Status']
_RADAROBSTACLE_MOVINGSTATUS = _RADAROBSTACLE.enum_types_by_name['MovingStatus']
RadarObstacle = _reflection.GeneratedProtocolMessageType('RadarObstacle', (_message.Message,), {'DESCRIPTOR': _RADAROBSTACLE, '__module__': 'modules.drivers.proto.radar_pb2'})
_sym_db.RegisterMessage(RadarObstacle)
RadarObstacles = _reflection.GeneratedProtocolMessageType('RadarObstacles', (_message.Message,), {'RadarObstacleEntry': _reflection.GeneratedProtocolMessageType('RadarObstacleEntry', (_message.Message,), {'DESCRIPTOR': _RADAROBSTACLES_RADAROBSTACLEENTRY, '__module__': 'modules.drivers.proto.radar_pb2'}), 'DESCRIPTOR': _RADAROBSTACLES, '__module__': 'modules.drivers.proto.radar_pb2'})
_sym_db.RegisterMessage(RadarObstacles)
_sym_db.RegisterMessage(RadarObstacles.RadarObstacleEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _RADAROBSTACLES_RADAROBSTACLEENTRY._options = None
    _RADAROBSTACLES_RADAROBSTACLEENTRY._serialized_options = b'8\x01'
    _RADAROBSTACLE._serialized_start = 165
    _RADAROBSTACLE._serialized_end = 881
    _RADAROBSTACLE_STATUS._serialized_start = 639
    _RADAROBSTACLE_STATUS._serialized_end = 813
    _RADAROBSTACLE_MOVINGSTATUS._serialized_start = 815
    _RADAROBSTACLE_MOVINGSTATUS._serialized_end = 881
    _RADAROBSTACLES._serialized_start = 884
    _RADAROBSTACLES._serialized_end = 1149
    _RADAROBSTACLES_RADAROBSTACLEENTRY._serialized_start = 1066
    _RADAROBSTACLES_RADAROBSTACLEENTRY._serialized_end = 1149