"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/perception/proto/perception_camera.proto\x12\x18apollo.perception.camera\x1a#modules/common/proto/geometry.proto\x1a!modules/common/proto/header.proto\x1a2modules/perception/proto/perception_obstacle.proto"n\n\x12LaneLineCubicCurve\x12\x15\n\rlongitude_min\x18\x01 \x01(\x02\x12\x15\n\rlongitude_max\x18\x02 \x01(\x02\x12\t\n\x01a\x18\x03 \x01(\x02\x12\t\n\x01b\x18\x04 \x01(\x02\x12\t\n\x01c\x18\x05 \x01(\x02\x12\t\n\x01d\x18\x06 \x01(\x02"W\n\tEndPoints\x12%\n\x05start\x18\x01 \x01(\x0b2\x16.apollo.common.Point2D\x12#\n\x03end\x18\x02 \x01(\x0b2\x16.apollo.common.Point2D"\xaf\x04\n\x0eCameraLaneLine\x124\n\x04type\x18\x01 \x01(\x0e2&.apollo.perception.camera.LaneLineType\x12@\n\x08pos_type\x18\x02 \x01(\x0e2..apollo.perception.camera.LaneLinePositionType\x12H\n\x12curve_camera_coord\x18\x03 \x01(\x0b2,.apollo.perception.camera.LaneLineCubicCurve\x12G\n\x11curve_image_coord\x18\x04 \x01(\x0b2,.apollo.perception.camera.LaneLineCubicCurve\x126\n\x16curve_camera_point_set\x18\x05 \x03(\x0b2\x16.apollo.common.Point3D\x125\n\x15curve_image_point_set\x18\x06 \x03(\x0b2\x16.apollo.common.Point2D\x12@\n\x13image_end_point_set\x18\x07 \x03(\x0b2#.apollo.perception.camera.EndPoints\x12\x10\n\x08track_id\x18\x08 \x01(\x05\x12\x12\n\nconfidence\x18\t \x01(\x02\x12;\n\x08use_type\x18\n \x01(\x0e2).apollo.perception.camera.LaneLineUseType">\n\x10CameraCalibrator\x12\x13\n\x0bpitch_angle\x18\x01 \x01(\x02\x12\x15\n\rcamera_height\x18\x02 \x01(\x02"\xad\x03\n\x0eCameraObstacle\x127\n\x08obstacle\x18\x01 \x01(\x0b2%.apollo.perception.PerceptionObstacle\x12A\n\x04type\x18\x15 \x01(\x0e23.apollo.perception.camera.CameraObstacle.CameraType\x12\x12\n\ntype_probs\x18\x16 \x03(\x02\x12*\n\nupper_left\x18\x17 \x01(\x0b2\x16.apollo.common.Point2D\x12+\n\x0blower_right\x18\x18 \x01(\x0b2\x16.apollo.common.Point2D\x12*\n\nkey_points\x18\x19 \x03(\x0b2\x16.apollo.common.Point2D\x12\x15\n\rdebug_message\x18\x1a \x03(\t"o\n\nCameraType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07BICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05"\xe2\x02\n\x0bCameraDebug\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x14\n\x0csource_topic\x18\x02 \x01(\t\x12I\n\nerror_code\x18\x03 \x01(\x0e2).apollo.perception.camera.CameraErrorCode:\nERROR_NONE\x12E\n\x11camera_calibrator\x18\x04 \x01(\x0b2*.apollo.perception.camera.CameraCalibrator\x12A\n\x0fcamera_laneline\x18\x05 \x03(\x0b2(.apollo.perception.camera.CameraLaneLine\x12A\n\x0fcamera_obstacle\x18\x06 \x03(\x0b2(.apollo.perception.camera.CameraObstacle*4\n\x0fCameraErrorCode\x12\x0e\n\nERROR_NONE\x10\x00\x12\x11\n\rERROR_UNKNOWN\x10\x01*V\n\x0cLaneLineType\x12\x10\n\x0cWHITE_DASHED\x10\x00\x12\x0f\n\x0bWHITE_SOLID\x10\x01\x12\x11\n\rYELLOW_DASHED\x10\x02\x12\x10\n\x0cYELLOW_SOLID\x10\x03*\x88\x02\n\x14LaneLinePositionType\x12\x19\n\x0cBOLLARD_LEFT\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x18\n\x0bFOURTH_LEFT\x10\xfc\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x17\n\nTHIRD_LEFT\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\rADJACENT_LEFT\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x15\n\x08EGO_LEFT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\r\n\tEGO_RIGHT\x10\x01\x12\x12\n\x0eADJACENT_RIGHT\x10\x02\x12\x0f\n\x0bTHIRD_RIGHT\x10\x03\x12\x10\n\x0cFOURTH_RIGHT\x10\x04\x12\x11\n\rBOLLARD_RIGHT\x10\x05\x12\t\n\x05OTHER\x10\x06\x12\x0b\n\x07UNKNOWN\x10\x07*(\n\x0fLaneLineUseType\x12\x08\n\x04REAL\x10\x00\x12\x0b\n\x07VIRTUAL\x10\x01')
_CAMERAERRORCODE = DESCRIPTOR.enum_types_by_name['CameraErrorCode']
CameraErrorCode = enum_type_wrapper.EnumTypeWrapper(_CAMERAERRORCODE)
_LANELINETYPE = DESCRIPTOR.enum_types_by_name['LaneLineType']
LaneLineType = enum_type_wrapper.EnumTypeWrapper(_LANELINETYPE)
_LANELINEPOSITIONTYPE = DESCRIPTOR.enum_types_by_name['LaneLinePositionType']
LaneLinePositionType = enum_type_wrapper.EnumTypeWrapper(_LANELINEPOSITIONTYPE)
_LANELINEUSETYPE = DESCRIPTOR.enum_types_by_name['LaneLineUseType']
LaneLineUseType = enum_type_wrapper.EnumTypeWrapper(_LANELINEUSETYPE)
ERROR_NONE = 0
ERROR_UNKNOWN = 1
WHITE_DASHED = 0
WHITE_SOLID = 1
YELLOW_DASHED = 2
YELLOW_SOLID = 3
BOLLARD_LEFT = -5
FOURTH_LEFT = -4
THIRD_LEFT = -3
ADJACENT_LEFT = -2
EGO_LEFT = -1
EGO_RIGHT = 1
ADJACENT_RIGHT = 2
THIRD_RIGHT = 3
FOURTH_RIGHT = 4
BOLLARD_RIGHT = 5
OTHER = 6
UNKNOWN = 7
REAL = 0
VIRTUAL = 1
_LANELINECUBICCURVE = DESCRIPTOR.message_types_by_name['LaneLineCubicCurve']
_ENDPOINTS = DESCRIPTOR.message_types_by_name['EndPoints']
_CAMERALANELINE = DESCRIPTOR.message_types_by_name['CameraLaneLine']
_CAMERACALIBRATOR = DESCRIPTOR.message_types_by_name['CameraCalibrator']
_CAMERAOBSTACLE = DESCRIPTOR.message_types_by_name['CameraObstacle']
_CAMERADEBUG = DESCRIPTOR.message_types_by_name['CameraDebug']
_CAMERAOBSTACLE_CAMERATYPE = _CAMERAOBSTACLE.enum_types_by_name['CameraType']
LaneLineCubicCurve = _reflection.GeneratedProtocolMessageType('LaneLineCubicCurve', (_message.Message,), {'DESCRIPTOR': _LANELINECUBICCURVE, '__module__': 'modules.perception.proto.perception_camera_pb2'})
_sym_db.RegisterMessage(LaneLineCubicCurve)
EndPoints = _reflection.GeneratedProtocolMessageType('EndPoints', (_message.Message,), {'DESCRIPTOR': _ENDPOINTS, '__module__': 'modules.perception.proto.perception_camera_pb2'})
_sym_db.RegisterMessage(EndPoints)
CameraLaneLine = _reflection.GeneratedProtocolMessageType('CameraLaneLine', (_message.Message,), {'DESCRIPTOR': _CAMERALANELINE, '__module__': 'modules.perception.proto.perception_camera_pb2'})
_sym_db.RegisterMessage(CameraLaneLine)
CameraCalibrator = _reflection.GeneratedProtocolMessageType('CameraCalibrator', (_message.Message,), {'DESCRIPTOR': _CAMERACALIBRATOR, '__module__': 'modules.perception.proto.perception_camera_pb2'})
_sym_db.RegisterMessage(CameraCalibrator)
CameraObstacle = _reflection.GeneratedProtocolMessageType('CameraObstacle', (_message.Message,), {'DESCRIPTOR': _CAMERAOBSTACLE, '__module__': 'modules.perception.proto.perception_camera_pb2'})
_sym_db.RegisterMessage(CameraObstacle)
CameraDebug = _reflection.GeneratedProtocolMessageType('CameraDebug', (_message.Message,), {'DESCRIPTOR': _CAMERADEBUG, '__module__': 'modules.perception.proto.perception_camera_pb2'})
_sym_db.RegisterMessage(CameraDebug)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CAMERAERRORCODE._serialized_start = 1818
    _CAMERAERRORCODE._serialized_end = 1870
    _LANELINETYPE._serialized_start = 1872
    _LANELINETYPE._serialized_end = 1958
    _LANELINEPOSITIONTYPE._serialized_start = 1961
    _LANELINEPOSITIONTYPE._serialized_end = 2225
    _LANELINEUSETYPE._serialized_start = 2227
    _LANELINEUSETYPE._serialized_end = 2267
    _LANELINECUBICCURVE._serialized_start = 202
    _LANELINECUBICCURVE._serialized_end = 312
    _ENDPOINTS._serialized_start = 314
    _ENDPOINTS._serialized_end = 401
    _CAMERALANELINE._serialized_start = 404
    _CAMERALANELINE._serialized_end = 963
    _CAMERACALIBRATOR._serialized_start = 965
    _CAMERACALIBRATOR._serialized_end = 1027
    _CAMERAOBSTACLE._serialized_start = 1030
    _CAMERAOBSTACLE._serialized_end = 1459
    _CAMERAOBSTACLE_CAMERATYPE._serialized_start = 1348
    _CAMERAOBSTACLE_CAMERATYPE._serialized_end = 1459
    _CAMERADEBUG._serialized_start = 1462
    _CAMERADEBUG._serialized_end = 1816