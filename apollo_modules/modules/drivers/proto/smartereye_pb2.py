"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/drivers/proto/smartereye.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto"\x87\x01\n\x0fLdwLaneBoundary\x12\x0e\n\x06degree\x18\x01 \x01(\x05\x12\x13\n\x0bc0_position\x18\x02 \x01(\x01\x12\x18\n\x10c1_heading_angle\x18\x03 \x01(\x01\x12\x14\n\x0cc2_curvature\x18\x04 \x01(\x01\x12\x1f\n\x17c3_curvature_derivative\x18\x05 \x01(\x01"\xc7\x01\n\x07LdwLane\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0f\n\x07quality\x18\x02 \x01(\x05\x12+\n\x05style\x18\x03 \x01(\x0e2\x1c.apollo.drivers.LdwLaneStyle\x126\n\rleft_boundary\x18\x04 \x01(\x0b2\x1f.apollo.drivers.LdwLaneBoundary\x127\n\x0eright_boundary\x18\x05 \x01(\x0b2\x1f.apollo.drivers.LdwLaneBoundary"\x8e\x02\n\nLdwRoadway\x12\x0f\n\x07width_0\x18\x01 \x01(\x05\x12\x0f\n\x07width_1\x18\x02 \x01(\x05\x12\x0f\n\x07width_2\x18\x03 \x01(\x05\x12\x13\n\x0bis_tracking\x18\x04 \x01(\x08\x12*\n\tleft_lane\x18\x05 \x01(\x0b2\x17.apollo.drivers.LdwLane\x12+\n\nright_lane\x18\x06 \x01(\x0b2\x17.apollo.drivers.LdwLane\x12.\n\radj_left_lane\x18\x07 \x01(\x0b2\x17.apollo.drivers.LdwLane\x12/\n\x0eadj_right_lane\x18\x08 \x01(\x0b2\x17.apollo.drivers.LdwLane"\xcb\x01\n\x0bLdwLensInfo\x12\x15\n\rx_image_focal\x18\x01 \x01(\x02\x12\x15\n\ry_image_focal\x18\x02 \x01(\x02\x12\x1a\n\x12xratio_focal_pixel\x18\x03 \x01(\x02\x12\x1a\n\x12yratio_focal_pixel\x18\x04 \x01(\x02\x12\x16\n\x0emountingheight\x18\x05 \x01(\x02\x12\x0e\n\x06mcosrx\x18\x06 \x01(\x02\x12\x0e\n\x06msinrx\x18\x07 \x01(\x02\x12\x0e\n\x06mcosry\x18\x08 \x01(\x02\x12\x0e\n\x06msinry\x18\t \x01(\x02"\xce\x01\n\x0cLdwDataPacks\x12+\n\x07roadway\x18\x01 \x01(\x0b2\x1a.apollo.drivers.LdwRoadway\x121\n\nsoftstatus\x18\x02 \x01(\x0e2\x1d.apollo.drivers.LdwSoftStatus\x123\n\x0bsteerstatus\x18\x03 \x01(\x0e2\x1e.apollo.drivers.LdwSteerStatus\x12)\n\x04lens\x18\x04 \x01(\x0b2\x1b.apollo.drivers.LdwLensInfo"\x82\t\n\x0eOutputObstacle\x12\x14\n\x0ccurrentspeed\x18\x01 \x01(\x02\x12\x11\n\tframerate\x18\x02 \x01(\x02\x12\x0f\n\x07trackid\x18\x03 \x01(\r\x12\x15\n\rtrackframenum\x18\x04 \x01(\r\x12\x12\n\nstatelabel\x18\x05 \x01(\r\x12\x12\n\nclasslabel\x18\x06 \x01(\r\x12\x17\n\x0fcontinuouslabel\x18\x07 \x01(\r\x12\x1c\n\x14fuzzyestimationvalid\x18\x08 \x01(\r\x12D\n\x0cobstacletype\x18\t \x01(\x0e2..apollo.drivers.OutputObstacle.RecognitionType\x12\x0f\n\x07avgdisp\x18\n \x01(\x02\x12\x14\n\x0cavgdistancez\x18\x0b \x01(\x02\x12\x15\n\rneardistancez\x18\x0c \x01(\x02\x12\x14\n\x0cfardistancez\x18\r \x01(\x02\x12\x13\n\x0breal3dleftx\x18\x0e \x01(\x02\x12\x14\n\x0creal3drightx\x18\x0f \x01(\x02\x12\x15\n\rreal3dcenterx\x18\x10 \x01(\x02\x12\x11\n\treal3dupy\x18\x11 \x01(\x02\x12\x12\n\nreal3dlowy\x18\x12 \x01(\x02\x12\x13\n\x0bfirstpointx\x18\x13 \x01(\r\x12\x13\n\x0bfirstpointy\x18\x14 \x01(\r\x12\x14\n\x0csecondpointx\x18\x15 \x01(\r\x12\x14\n\x0csecondpointy\x18\x16 \x01(\r\x12\x13\n\x0bthirdpointx\x18\x17 \x01(\r\x12\x13\n\x0bthirdpointy\x18\x18 \x01(\r\x12\x14\n\x0cfourthpointx\x18\x19 \x01(\r\x12\x14\n\x0cfourthpointy\x18\x1a \x01(\r\x12\x1e\n\x16fuzzyrelativedistancez\x18\x1b \x01(\x02\x12\x1b\n\x13fuzzyrelativespeedz\x18\x1c \x01(\x02\x12\x1b\n\x13fuzzycollisiontimez\x18\x1d \x01(\x02\x12\x17\n\x0ffuzzycollisionx\x18\x1e \x01(\r\x12\x14\n\x0cfuzzy3dwidth\x18\x1f \x01(\x02\x12\x16\n\x0efuzzy3dcenterx\x18  \x01(\x02\x12\x14\n\x0cfuzzy3dleftx\x18! \x01(\x02\x12\x15\n\rfuzzy3drightx\x18" \x01(\x02\x12\x15\n\rfuzzy3dheight\x18# \x01(\x02\x12\x12\n\nfuzzy3dupy\x18$ \x01(\x02\x12\x13\n\x0bfuzzy3dlowy\x18% \x01(\x02\x12!\n\x19fuzzyrelativespeedcenterx\x18& \x01(\x02\x12\x1f\n\x17fuzzyrelativespeedleftx\x18\' \x01(\x02\x12 \n\x18fuzzyrelativespeedrightx\x18( \x01(\x02"\x9c\x01\n\x0fRecognitionType\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07VEHICLE\x10\x01\x12\x0e\n\nPEDESTRIAN\x10\x02\x12\t\n\x05CHILD\x10\x03\x12\x0b\n\x07BICYCLE\x10\x04\x12\x08\n\x04MOTO\x10\x05\x12\t\n\x05TRUCK\x10\x06\x12\x07\n\x03BUS\x10\x07\x12\n\n\x06OTHERS\x10\x08\x12\r\n\tESTIMATED\x10\t\x12\x0e\n\nCONTINUOUS\x10\n"\xff\x01\n\x13SmartereyeObstacles\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x15\n\rnum_obstacles\x18\x02 \x01(\x05\x12R\n\x10output_obstacles\x18\x03 \x03(\x0b28.apollo.drivers.SmartereyeObstacles.OutputObstaclesEntry\x1aV\n\x14OutputObstaclesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12-\n\x05value\x18\x02 \x01(\x0b2\x1e.apollo.drivers.OutputObstacle:\x028\x01"J\n\x12SmartereyeLanemark\x124\n\x0elane_road_data\x18\x04 \x01(\x0b2\x1c.apollo.drivers.LdwDataPacks*S\n\x0bLdwVersions\x12\x12\n\x0eLDW_VERSION_C1\x10\x00\x12\x12\n\x0eLDW_VERSION_C2\x10\x01\x12\x1c\n\x18LDW_VERSION_FOUR_LANE_C2\x10\x02*\xf9\x01\n\x0cLdwLaneStyle\x12\x1c\n\x18LDW_LANE_STYLE_NONE_LANE\x10\x00\x12\x1f\n\x1bLDW_LANE_STYLE_PREDICT_LANE\x10\x01\x12\x1e\n\x1aLDW_LANE_STYLE_BROKEN_LANE\x10\x02\x12\x1d\n\x19LDW_LANE_STYLE_SOLID_LANE\x10\x03\x12%\n!LDW_LANE_STYLE_DOUBLE_BROKEN_LANE\x10\x04\x12$\n LDW_LANE_STYLE_DOUBLE_SOLID_LANE\x10\x05\x12\x1e\n\x1aLDW_LANE_STYLE_TRIPLE_LANE\x10\x06*\x9a\x01\n\x0eLdwSteerStatus\x12\x14\n\x10LDW_NORMAL_STEER\x10\x00\x12\x1b\n\x17LDW_STEER_ON_LEFT__LANE\x10\x01\x12\x1b\n\x17LDW_STEER_ON_RIGHT_LANE\x10\x02\x12\x1b\n\x17LDW_STEER_WARNING_LEFT_\x10\x03\x12\x1b\n\x17LDW_STEER_WARNING_RIGHT\x10\x04*\x8b\x01\n\rLdwSoftStatus\x12\x16\n\x12LDW_SOFT_DETECTION\x10\x00\x12\x1a\n\x16LDW_SOFT_SELF_LEARNING\x10\x01\x12"\n\x1eLDW_SOFT_MANUAL_LEARNING_MODE0\x10\x02\x12"\n\x1eLDW_SOFT_MANUAL_LEARNING_MODE1\x10\x03*U\n\x0fLdwWarningGrade\x12\x13\n\x0fLDW_WARNING_LOW\x10\x00\x12\x16\n\x12LDW_WARNING_NORMAL\x10\x01\x12\x15\n\x11LDW_WARNING_HIGHT\x10\x02')
_LDWVERSIONS = DESCRIPTOR.enum_types_by_name['LdwVersions']
LdwVersions = enum_type_wrapper.EnumTypeWrapper(_LDWVERSIONS)
_LDWLANESTYLE = DESCRIPTOR.enum_types_by_name['LdwLaneStyle']
LdwLaneStyle = enum_type_wrapper.EnumTypeWrapper(_LDWLANESTYLE)
_LDWSTEERSTATUS = DESCRIPTOR.enum_types_by_name['LdwSteerStatus']
LdwSteerStatus = enum_type_wrapper.EnumTypeWrapper(_LDWSTEERSTATUS)
_LDWSOFTSTATUS = DESCRIPTOR.enum_types_by_name['LdwSoftStatus']
LdwSoftStatus = enum_type_wrapper.EnumTypeWrapper(_LDWSOFTSTATUS)
_LDWWARNINGGRADE = DESCRIPTOR.enum_types_by_name['LdwWarningGrade']
LdwWarningGrade = enum_type_wrapper.EnumTypeWrapper(_LDWWARNINGGRADE)
LDW_VERSION_C1 = 0
LDW_VERSION_C2 = 1
LDW_VERSION_FOUR_LANE_C2 = 2
LDW_LANE_STYLE_NONE_LANE = 0
LDW_LANE_STYLE_PREDICT_LANE = 1
LDW_LANE_STYLE_BROKEN_LANE = 2
LDW_LANE_STYLE_SOLID_LANE = 3
LDW_LANE_STYLE_DOUBLE_BROKEN_LANE = 4
LDW_LANE_STYLE_DOUBLE_SOLID_LANE = 5
LDW_LANE_STYLE_TRIPLE_LANE = 6
LDW_NORMAL_STEER = 0
LDW_STEER_ON_LEFT__LANE = 1
LDW_STEER_ON_RIGHT_LANE = 2
LDW_STEER_WARNING_LEFT_ = 3
LDW_STEER_WARNING_RIGHT = 4
LDW_SOFT_DETECTION = 0
LDW_SOFT_SELF_LEARNING = 1
LDW_SOFT_MANUAL_LEARNING_MODE0 = 2
LDW_SOFT_MANUAL_LEARNING_MODE1 = 3
LDW_WARNING_LOW = 0
LDW_WARNING_NORMAL = 1
LDW_WARNING_HIGHT = 2
_LDWLANEBOUNDARY = DESCRIPTOR.message_types_by_name['LdwLaneBoundary']
_LDWLANE = DESCRIPTOR.message_types_by_name['LdwLane']
_LDWROADWAY = DESCRIPTOR.message_types_by_name['LdwRoadway']
_LDWLENSINFO = DESCRIPTOR.message_types_by_name['LdwLensInfo']
_LDWDATAPACKS = DESCRIPTOR.message_types_by_name['LdwDataPacks']
_OUTPUTOBSTACLE = DESCRIPTOR.message_types_by_name['OutputObstacle']
_SMARTEREYEOBSTACLES = DESCRIPTOR.message_types_by_name['SmartereyeObstacles']
_SMARTEREYEOBSTACLES_OUTPUTOBSTACLESENTRY = _SMARTEREYEOBSTACLES.nested_types_by_name['OutputObstaclesEntry']
_SMARTEREYELANEMARK = DESCRIPTOR.message_types_by_name['SmartereyeLanemark']
_OUTPUTOBSTACLE_RECOGNITIONTYPE = _OUTPUTOBSTACLE.enum_types_by_name['RecognitionType']
LdwLaneBoundary = _reflection.GeneratedProtocolMessageType('LdwLaneBoundary', (_message.Message,), {'DESCRIPTOR': _LDWLANEBOUNDARY, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(LdwLaneBoundary)
LdwLane = _reflection.GeneratedProtocolMessageType('LdwLane', (_message.Message,), {'DESCRIPTOR': _LDWLANE, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(LdwLane)
LdwRoadway = _reflection.GeneratedProtocolMessageType('LdwRoadway', (_message.Message,), {'DESCRIPTOR': _LDWROADWAY, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(LdwRoadway)
LdwLensInfo = _reflection.GeneratedProtocolMessageType('LdwLensInfo', (_message.Message,), {'DESCRIPTOR': _LDWLENSINFO, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(LdwLensInfo)
LdwDataPacks = _reflection.GeneratedProtocolMessageType('LdwDataPacks', (_message.Message,), {'DESCRIPTOR': _LDWDATAPACKS, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(LdwDataPacks)
OutputObstacle = _reflection.GeneratedProtocolMessageType('OutputObstacle', (_message.Message,), {'DESCRIPTOR': _OUTPUTOBSTACLE, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(OutputObstacle)
SmartereyeObstacles = _reflection.GeneratedProtocolMessageType('SmartereyeObstacles', (_message.Message,), {'OutputObstaclesEntry': _reflection.GeneratedProtocolMessageType('OutputObstaclesEntry', (_message.Message,), {'DESCRIPTOR': _SMARTEREYEOBSTACLES_OUTPUTOBSTACLESENTRY, '__module__': 'modules.drivers.proto.smartereye_pb2'}), 'DESCRIPTOR': _SMARTEREYEOBSTACLES, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(SmartereyeObstacles)
_sym_db.RegisterMessage(SmartereyeObstacles.OutputObstaclesEntry)
SmartereyeLanemark = _reflection.GeneratedProtocolMessageType('SmartereyeLanemark', (_message.Message,), {'DESCRIPTOR': _SMARTEREYELANEMARK, '__module__': 'modules.drivers.proto.smartereye_pb2'})
_sym_db.RegisterMessage(SmartereyeLanemark)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SMARTEREYEOBSTACLES_OUTPUTOBSTACLESENTRY._options = None
    _SMARTEREYEOBSTACLES_OUTPUTOBSTACLESENTRY._serialized_options = b'8\x01'
    _LDWVERSIONS._serialized_start = 2612
    _LDWVERSIONS._serialized_end = 2695
    _LDWLANESTYLE._serialized_start = 2698
    _LDWLANESTYLE._serialized_end = 2947
    _LDWSTEERSTATUS._serialized_start = 2950
    _LDWSTEERSTATUS._serialized_end = 3104
    _LDWSOFTSTATUS._serialized_start = 3107
    _LDWSOFTSTATUS._serialized_end = 3246
    _LDWWARNINGGRADE._serialized_start = 3248
    _LDWWARNINGGRADE._serialized_end = 3333
    _LDWLANEBOUNDARY._serialized_start = 94
    _LDWLANEBOUNDARY._serialized_end = 229
    _LDWLANE._serialized_start = 232
    _LDWLANE._serialized_end = 431
    _LDWROADWAY._serialized_start = 434
    _LDWROADWAY._serialized_end = 704
    _LDWLENSINFO._serialized_start = 707
    _LDWLENSINFO._serialized_end = 910
    _LDWDATAPACKS._serialized_start = 913
    _LDWDATAPACKS._serialized_end = 1119
    _OUTPUTOBSTACLE._serialized_start = 1122
    _OUTPUTOBSTACLE._serialized_end = 2276
    _OUTPUTOBSTACLE_RECOGNITIONTYPE._serialized_start = 2120
    _OUTPUTOBSTACLE_RECOGNITIONTYPE._serialized_end = 2276
    _SMARTEREYEOBSTACLES._serialized_start = 2279
    _SMARTEREYEOBSTACLES._serialized_end = 2534
    _SMARTEREYEOBSTACLES_OUTPUTOBSTACLESENTRY._serialized_start = 2448
    _SMARTEREYEOBSTACLES_OUTPUTOBSTACLESENTRY._serialized_end = 2534
    _SMARTEREYELANEMARK._serialized_start = 2536
    _SMARTEREYELANEMARK._serialized_end = 2610