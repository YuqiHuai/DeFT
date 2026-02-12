"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import error_code_pb2 as modules_dot_common_dot_proto_dot_error__code__pb2
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/v2x/proto/v2x_obstacles.proto\x12\napollo.v2x\x1a!modules/common/proto/header.proto\x1a%modules/common/proto/error_code.proto\x1a2modules/perception/proto/perception_obstacle.proto"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01"\x9f\x01\n\x0bMiniAreaMap\x12\x0f\n\x07rscu_id\x18\x01 \x01(\x0c\x12+\n\x10feature_position\x18\x02 \x01(\x0b2\x11.apollo.v2x.Point\x12)\n\x0estart_position\x18\x03 \x01(\x0b2\x11.apollo.v2x.Point\x12\'\n\x0cend_position\x18\x04 \x01(\x0b2\x11.apollo.v2x.Point"E\n\x13AbnormalInformation\x12\x15\n\raverage_speed\x18\x01 \x01(\x01\x12\x17\n\x0fvehicle_density\x18\x02 \x01(\x01"\xfc\x02\n\x0eV2XInformation\x124\n\x08v2x_type\x18\x01 \x03(\x0e2".apollo.v2x.V2XInformation.V2XType\x12.\n\x13traffic_event_start\x18\x03 \x01(\x0b2\x11.apollo.v2x.Point\x124\n\x19traffic_event_start_error\x18\x04 \x01(\x0b2\x11.apollo.v2x.Point\x12,\n\x11traffic_event_end\x18\x05 \x01(\x0b2\x11.apollo.v2x.Point\x122\n\x17traffic_event_end_error\x18\x06 \x01(\x0b2\x11.apollo.v2x.Point\x126\n\rabnormal_info\x18\x07 \x01(\x0b2\x1f.apollo.v2x.AbnormalInformation"4\n\x07V2XType\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bZOMBIES_CAR\x10\x01\x12\x0e\n\nBLIND_ZONE\x10\x02"\x7f\n\x0bV2XObstacle\x12B\n\x13perception_obstacle\x18\x01 \x01(\x0b2%.apollo.perception.PerceptionObstacle\x12,\n\x08v2x_info\x18\x02 \x01(\x0b2\x1a.apollo.v2x.V2XInformation"\xd7\x01\n\x0cV2XObstacles\x12-\n\x0cv2x_obstacle\x18\x01 \x03(\x0b2\x17.apollo.v2x.V2XObstacle\x12)\n\x08area_map\x18\x02 \x01(\x0b2\x17.apollo.v2x.MiniAreaMap\x12\x14\n\x0ctraffic_flow\x18\x03 \x01(\x01\x12%\n\x06header\x18\x04 \x01(\x0b2\x15.apollo.common.Header\x120\n\nerror_code\x18\x05 \x01(\x0e2\x18.apollo.common.ErrorCode:\x02OK')
_POINT = DESCRIPTOR.message_types_by_name['Point']
_MINIAREAMAP = DESCRIPTOR.message_types_by_name['MiniAreaMap']
_ABNORMALINFORMATION = DESCRIPTOR.message_types_by_name['AbnormalInformation']
_V2XINFORMATION = DESCRIPTOR.message_types_by_name['V2XInformation']
_V2XOBSTACLE = DESCRIPTOR.message_types_by_name['V2XObstacle']
_V2XOBSTACLES = DESCRIPTOR.message_types_by_name['V2XObstacles']
_V2XINFORMATION_V2XTYPE = _V2XINFORMATION.enum_types_by_name['V2XType']
Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {'DESCRIPTOR': _POINT, '__module__': 'modules.v2x.proto.v2x_obstacles_pb2'})
_sym_db.RegisterMessage(Point)
MiniAreaMap = _reflection.GeneratedProtocolMessageType('MiniAreaMap', (_message.Message,), {'DESCRIPTOR': _MINIAREAMAP, '__module__': 'modules.v2x.proto.v2x_obstacles_pb2'})
_sym_db.RegisterMessage(MiniAreaMap)
AbnormalInformation = _reflection.GeneratedProtocolMessageType('AbnormalInformation', (_message.Message,), {'DESCRIPTOR': _ABNORMALINFORMATION, '__module__': 'modules.v2x.proto.v2x_obstacles_pb2'})
_sym_db.RegisterMessage(AbnormalInformation)
V2XInformation = _reflection.GeneratedProtocolMessageType('V2XInformation', (_message.Message,), {'DESCRIPTOR': _V2XINFORMATION, '__module__': 'modules.v2x.proto.v2x_obstacles_pb2'})
_sym_db.RegisterMessage(V2XInformation)
V2XObstacle = _reflection.GeneratedProtocolMessageType('V2XObstacle', (_message.Message,), {'DESCRIPTOR': _V2XOBSTACLE, '__module__': 'modules.v2x.proto.v2x_obstacles_pb2'})
_sym_db.RegisterMessage(V2XObstacle)
V2XObstacles = _reflection.GeneratedProtocolMessageType('V2XObstacles', (_message.Message,), {'DESCRIPTOR': _V2XOBSTACLES, '__module__': 'modules.v2x.proto.v2x_obstacles_pb2'})
_sym_db.RegisterMessage(V2XObstacles)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POINT._serialized_start = 179
    _POINT._serialized_end = 219
    _MINIAREAMAP._serialized_start = 222
    _MINIAREAMAP._serialized_end = 381
    _ABNORMALINFORMATION._serialized_start = 383
    _ABNORMALINFORMATION._serialized_end = 452
    _V2XINFORMATION._serialized_start = 455
    _V2XINFORMATION._serialized_end = 835
    _V2XINFORMATION_V2XTYPE._serialized_start = 783
    _V2XINFORMATION_V2XTYPE._serialized_end = 835
    _V2XOBSTACLE._serialized_start = 837
    _V2XOBSTACLE._serialized_end = 964
    _V2XOBSTACLES._serialized_start = 967
    _V2XOBSTACLES._serialized_end = 1182