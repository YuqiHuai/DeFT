"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import vehicle_signal_pb2 as modules_dot_common_dot_proto_dot_vehicle__signal__pb2
from ....modules.routing.proto import routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/planning/proto/decision.proto\x12\x0fapollo.planning\x1a#modules/common/proto/geometry.proto\x1a)modules/common/proto/vehicle_signal.proto\x1a#modules/routing/proto/routing.proto"M\n\nTargetLane\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07start_s\x18\x02 \x01(\x01\x12\r\n\x05end_s\x18\x03 \x01(\x01\x12\x13\n\x0bspeed_limit\x18\x04 \x01(\x01"\x0e\n\x0cObjectIgnore"\xb4\x01\n\nObjectStop\x124\n\x0breason_code\x18\x01 \x01(\x0e2\x1f.apollo.planning.StopReasonCode\x12\x12\n\ndistance_s\x18\x02 \x01(\x01\x12+\n\nstop_point\x18\x03 \x01(\x0b2\x17.apollo.common.PointENU\x12\x14\n\x0cstop_heading\x18\x04 \x01(\x01\x12\x19\n\x11wait_for_obstacle\x18\x05 \x03(\t"\xac\x01\n\x0bObjectNudge\x12/\n\x04type\x18\x01 \x01(\x0e2!.apollo.planning.ObjectNudge.Type\x12\x12\n\ndistance_l\x18\x02 \x01(\x01"X\n\x04Type\x12\x0e\n\nLEFT_NUDGE\x10\x01\x12\x0f\n\x0bRIGHT_NUDGE\x10\x02\x12\x16\n\x12DYNAMIC_LEFT_NUDGE\x10\x03\x12\x17\n\x13DYNAMIC_RIGHT_NUDGE\x10\x04"{\n\x0bObjectYield\x12\x12\n\ndistance_s\x18\x01 \x01(\x01\x12,\n\x0bfence_point\x18\x02 \x01(\x0b2\x17.apollo.common.PointENU\x12\x15\n\rfence_heading\x18\x03 \x01(\x01\x12\x13\n\x0btime_buffer\x18\x04 \x01(\x01"g\n\x0cObjectFollow\x12\x12\n\ndistance_s\x18\x01 \x01(\x01\x12,\n\x0bfence_point\x18\x02 \x01(\x0b2\x17.apollo.common.PointENU\x12\x15\n\rfence_heading\x18\x03 \x01(\x01"~\n\x0eObjectOvertake\x12\x12\n\ndistance_s\x18\x01 \x01(\x01\x12,\n\x0bfence_point\x18\x02 \x01(\x0b2\x17.apollo.common.PointENU\x12\x15\n\rfence_heading\x18\x03 \x01(\x01\x12\x13\n\x0btime_buffer\x18\x04 \x01(\x01"a\n\x0eObjectSidePass\x122\n\x04type\x18\x01 \x01(\x0e2$.apollo.planning.ObjectSidePass.Type"\x1b\n\x04Type\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02"\r\n\x0bObjectAvoid"\x82\x01\n\x0cObjectStatus\x126\n\x0bmotion_type\x18\x01 \x01(\x0b2!.apollo.planning.ObjectMotionType\x12:\n\rdecision_type\x18\x02 \x01(\x0b2#.apollo.planning.ObjectDecisionType"\x0e\n\x0cObjectStatic"\x0f\n\rObjectDynamic"\x84\x01\n\x10ObjectMotionType\x12/\n\x06static\x18\x01 \x01(\x0b2\x1d.apollo.planning.ObjectStaticH\x00\x121\n\x07dynamic\x18\x02 \x01(\x0b2\x1e.apollo.planning.ObjectDynamicH\x00B\x0c\n\nmotion_tag"\xa9\x03\n\x12ObjectDecisionType\x12/\n\x06ignore\x18\x01 \x01(\x0b2\x1d.apollo.planning.ObjectIgnoreH\x00\x12+\n\x04stop\x18\x02 \x01(\x0b2\x1b.apollo.planning.ObjectStopH\x00\x12/\n\x06follow\x18\x03 \x01(\x0b2\x1d.apollo.planning.ObjectFollowH\x00\x12-\n\x05yield\x18\x04 \x01(\x0b2\x1c.apollo.planning.ObjectYieldH\x00\x123\n\x08overtake\x18\x05 \x01(\x0b2\x1f.apollo.planning.ObjectOvertakeH\x00\x12-\n\x05nudge\x18\x06 \x01(\x0b2\x1c.apollo.planning.ObjectNudgeH\x00\x12-\n\x05avoid\x18\x07 \x01(\x0b2\x1c.apollo.planning.ObjectAvoidH\x00\x124\n\tside_pass\x18\x08 \x01(\x0b2\x1f.apollo.planning.ObjectSidePassH\x00B\x0c\n\nobject_tag"q\n\x0eObjectDecision\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rperception_id\x18\x02 \x01(\x05\x12<\n\x0fobject_decision\x18\x03 \x03(\x0b2#.apollo.planning.ObjectDecisionType"D\n\x0fObjectDecisions\x121\n\x08decision\x18\x01 \x03(\x0b2\x1f.apollo.planning.ObjectDecision"\xcd\x01\n\x08MainStop\x124\n\x0breason_code\x18\x01 \x01(\x0e2\x1f.apollo.planning.StopReasonCode\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12+\n\nstop_point\x18\x03 \x01(\x0b2\x17.apollo.common.PointENU\x12\x14\n\x0cstop_heading\x18\x04 \x01(\x01\x128\n\x10change_lane_type\x18\x05 \x01(\x0e2\x1e.apollo.routing.ChangeLaneType"\x18\n\x16EmergencyStopHardBrake"\x1b\n\x19EmergencyStopCruiseToStop"\x9f\x03\n\x11MainEmergencyStop\x12B\n\x0breason_code\x18\x01 \x01(\x0e2-.apollo.planning.MainEmergencyStop.ReasonCode\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12=\n\nhard_brake\x18\x03 \x01(\x0b2\'.apollo.planning.EmergencyStopHardBrakeH\x00\x12D\n\x0ecruise_to_stop\x18\x04 \x01(\x0b2*.apollo.planning.EmergencyStopCruiseToStopH\x00"\xa8\x01\n\nReasonCode\x12\x1d\n\x19ESTOP_REASON_INTERNAL_ERR\x10\x01\x12\x1a\n\x16ESTOP_REASON_COLLISION\x10\x02\x12\x1d\n\x19ESTOP_REASON_ST_FIND_PATH\x10\x03\x12!\n\x1dESTOP_REASON_ST_MAKE_DECISION\x10\x04\x12\x1d\n\x19ESTOP_REASON_SENSOR_ERROR\x10\x05B\x06\n\x04task"F\n\nMainCruise\x128\n\x10change_lane_type\x18\x01 \x01(\x0e2\x1e.apollo.routing.ChangeLaneType"\xff\x01\n\x0eMainChangeLane\x122\n\x04type\x18\x01 \x01(\x0e2$.apollo.planning.MainChangeLane.Type\x121\n\x0cdefault_lane\x18\x02 \x03(\x0b2\x1b.apollo.planning.TargetLane\x124\n\x11default_lane_stop\x18\x03 \x01(\x0b2\x19.apollo.planning.MainStop\x123\n\x10target_lane_stop\x18\x04 \x01(\x0b2\x19.apollo.planning.MainStop"\x1b\n\x04Type\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02"X\n\x13MainMissionComplete\x12+\n\nstop_point\x18\x01 \x01(\x0b2\x17.apollo.common.PointENU\x12\x14\n\x0cstop_heading\x18\x02 \x01(\x01"\x1e\n\x0cMainNotReady\x12\x0e\n\x06reason\x18\x01 \x01(\t"j\n\x0bMainParking\x12:\n\x06status\x18\x01 \x01(\x0e2*.apollo.planning.MainParking.ParkingStatus"\x1f\n\rParkingStatus\x12\x0e\n\nIN_PARKING\x10\x01"\xbe\x03\n\x0cMainDecision\x12-\n\x06cruise\x18\x01 \x01(\x0b2\x1b.apollo.planning.MainCruiseH\x00\x12)\n\x04stop\x18\x02 \x01(\x0b2\x19.apollo.planning.MainStopH\x00\x123\n\x05estop\x18\x03 \x01(\x0b2".apollo.planning.MainEmergencyStopH\x00\x12:\n\x0bchange_lane\x18\x04 \x01(\x0b2\x1f.apollo.planning.MainChangeLaneB\x02\x18\x01H\x00\x12@\n\x10mission_complete\x18\x06 \x01(\x0b2$.apollo.planning.MainMissionCompleteH\x00\x122\n\tnot_ready\x18\x07 \x01(\x0b2\x1d.apollo.planning.MainNotReadyH\x00\x12/\n\x07parking\x18\x08 \x01(\x0b2\x1c.apollo.planning.MainParkingH\x00\x124\n\x0btarget_lane\x18\x05 \x03(\x0b2\x1b.apollo.planning.TargetLaneB\x02\x18\x01B\x06\n\x04task"\xb7\x01\n\x0eDecisionResult\x124\n\rmain_decision\x18\x01 \x01(\x0b2\x1d.apollo.planning.MainDecision\x129\n\x0fobject_decision\x18\x02 \x01(\x0b2 .apollo.planning.ObjectDecisions\x124\n\x0evehicle_signal\x18\x03 \x01(\x0b2\x1c.apollo.common.VehicleSignal*\x9e\x04\n\x0eStopReasonCode\x12\x1c\n\x18STOP_REASON_HEAD_VEHICLE\x10\x01\x12\x1b\n\x17STOP_REASON_DESTINATION\x10\x02\x12\x1a\n\x16STOP_REASON_PEDESTRIAN\x10\x03\x12\x18\n\x14STOP_REASON_OBSTACLE\x10\x04\x12\x1a\n\x16STOP_REASON_PREPARKING\x10\x05\x12\x16\n\x12STOP_REASON_SIGNAL\x10d\x12\x19\n\x15STOP_REASON_STOP_SIGN\x10e\x12\x1a\n\x16STOP_REASON_YIELD_SIGN\x10f\x12\x1a\n\x16STOP_REASON_CLEAR_ZONE\x10g\x12\x19\n\x15STOP_REASON_CROSSWALK\x10h\x12\x17\n\x13STOP_REASON_CREEPER\x10i\x12\x1d\n\x19STOP_REASON_REFERENCE_END\x10j\x12\x1d\n\x19STOP_REASON_YELLOW_SIGNAL\x10k\x12\x19\n\x15STOP_REASON_PULL_OVER\x10l\x12\x1f\n\x1bSTOP_REASON_SIDEPASS_SAFETY\x10m\x12$\n\x1fSTOP_REASON_PRE_OPEN_SPACE_STOP\x10\xc8\x01\x12$\n\x1fSTOP_REASON_LANE_CHANGE_URGENCY\x10\xc9\x01\x12\x1a\n\x15STOP_REASON_EMERGENCY\x10\xca\x01')
_STOPREASONCODE = DESCRIPTOR.enum_types_by_name['StopReasonCode']
StopReasonCode = enum_type_wrapper.EnumTypeWrapper(_STOPREASONCODE)
STOP_REASON_HEAD_VEHICLE = 1
STOP_REASON_DESTINATION = 2
STOP_REASON_PEDESTRIAN = 3
STOP_REASON_OBSTACLE = 4
STOP_REASON_PREPARKING = 5
STOP_REASON_SIGNAL = 100
STOP_REASON_STOP_SIGN = 101
STOP_REASON_YIELD_SIGN = 102
STOP_REASON_CLEAR_ZONE = 103
STOP_REASON_CROSSWALK = 104
STOP_REASON_CREEPER = 105
STOP_REASON_REFERENCE_END = 106
STOP_REASON_YELLOW_SIGNAL = 107
STOP_REASON_PULL_OVER = 108
STOP_REASON_SIDEPASS_SAFETY = 109
STOP_REASON_PRE_OPEN_SPACE_STOP = 200
STOP_REASON_LANE_CHANGE_URGENCY = 201
STOP_REASON_EMERGENCY = 202
_TARGETLANE = DESCRIPTOR.message_types_by_name['TargetLane']
_OBJECTIGNORE = DESCRIPTOR.message_types_by_name['ObjectIgnore']
_OBJECTSTOP = DESCRIPTOR.message_types_by_name['ObjectStop']
_OBJECTNUDGE = DESCRIPTOR.message_types_by_name['ObjectNudge']
_OBJECTYIELD = DESCRIPTOR.message_types_by_name['ObjectYield']
_OBJECTFOLLOW = DESCRIPTOR.message_types_by_name['ObjectFollow']
_OBJECTOVERTAKE = DESCRIPTOR.message_types_by_name['ObjectOvertake']
_OBJECTSIDEPASS = DESCRIPTOR.message_types_by_name['ObjectSidePass']
_OBJECTAVOID = DESCRIPTOR.message_types_by_name['ObjectAvoid']
_OBJECTSTATUS = DESCRIPTOR.message_types_by_name['ObjectStatus']
_OBJECTSTATIC = DESCRIPTOR.message_types_by_name['ObjectStatic']
_OBJECTDYNAMIC = DESCRIPTOR.message_types_by_name['ObjectDynamic']
_OBJECTMOTIONTYPE = DESCRIPTOR.message_types_by_name['ObjectMotionType']
_OBJECTDECISIONTYPE = DESCRIPTOR.message_types_by_name['ObjectDecisionType']
_OBJECTDECISION = DESCRIPTOR.message_types_by_name['ObjectDecision']
_OBJECTDECISIONS = DESCRIPTOR.message_types_by_name['ObjectDecisions']
_MAINSTOP = DESCRIPTOR.message_types_by_name['MainStop']
_EMERGENCYSTOPHARDBRAKE = DESCRIPTOR.message_types_by_name['EmergencyStopHardBrake']
_EMERGENCYSTOPCRUISETOSTOP = DESCRIPTOR.message_types_by_name['EmergencyStopCruiseToStop']
_MAINEMERGENCYSTOP = DESCRIPTOR.message_types_by_name['MainEmergencyStop']
_MAINCRUISE = DESCRIPTOR.message_types_by_name['MainCruise']
_MAINCHANGELANE = DESCRIPTOR.message_types_by_name['MainChangeLane']
_MAINMISSIONCOMPLETE = DESCRIPTOR.message_types_by_name['MainMissionComplete']
_MAINNOTREADY = DESCRIPTOR.message_types_by_name['MainNotReady']
_MAINPARKING = DESCRIPTOR.message_types_by_name['MainParking']
_MAINDECISION = DESCRIPTOR.message_types_by_name['MainDecision']
_DECISIONRESULT = DESCRIPTOR.message_types_by_name['DecisionResult']
_OBJECTNUDGE_TYPE = _OBJECTNUDGE.enum_types_by_name['Type']
_OBJECTSIDEPASS_TYPE = _OBJECTSIDEPASS.enum_types_by_name['Type']
_MAINEMERGENCYSTOP_REASONCODE = _MAINEMERGENCYSTOP.enum_types_by_name['ReasonCode']
_MAINCHANGELANE_TYPE = _MAINCHANGELANE.enum_types_by_name['Type']
_MAINPARKING_PARKINGSTATUS = _MAINPARKING.enum_types_by_name['ParkingStatus']
TargetLane = _reflection.GeneratedProtocolMessageType('TargetLane', (_message.Message,), {'DESCRIPTOR': _TARGETLANE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(TargetLane)
ObjectIgnore = _reflection.GeneratedProtocolMessageType('ObjectIgnore', (_message.Message,), {'DESCRIPTOR': _OBJECTIGNORE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectIgnore)
ObjectStop = _reflection.GeneratedProtocolMessageType('ObjectStop', (_message.Message,), {'DESCRIPTOR': _OBJECTSTOP, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectStop)
ObjectNudge = _reflection.GeneratedProtocolMessageType('ObjectNudge', (_message.Message,), {'DESCRIPTOR': _OBJECTNUDGE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectNudge)
ObjectYield = _reflection.GeneratedProtocolMessageType('ObjectYield', (_message.Message,), {'DESCRIPTOR': _OBJECTYIELD, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectYield)
ObjectFollow = _reflection.GeneratedProtocolMessageType('ObjectFollow', (_message.Message,), {'DESCRIPTOR': _OBJECTFOLLOW, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectFollow)
ObjectOvertake = _reflection.GeneratedProtocolMessageType('ObjectOvertake', (_message.Message,), {'DESCRIPTOR': _OBJECTOVERTAKE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectOvertake)
ObjectSidePass = _reflection.GeneratedProtocolMessageType('ObjectSidePass', (_message.Message,), {'DESCRIPTOR': _OBJECTSIDEPASS, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectSidePass)
ObjectAvoid = _reflection.GeneratedProtocolMessageType('ObjectAvoid', (_message.Message,), {'DESCRIPTOR': _OBJECTAVOID, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectAvoid)
ObjectStatus = _reflection.GeneratedProtocolMessageType('ObjectStatus', (_message.Message,), {'DESCRIPTOR': _OBJECTSTATUS, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectStatus)
ObjectStatic = _reflection.GeneratedProtocolMessageType('ObjectStatic', (_message.Message,), {'DESCRIPTOR': _OBJECTSTATIC, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectStatic)
ObjectDynamic = _reflection.GeneratedProtocolMessageType('ObjectDynamic', (_message.Message,), {'DESCRIPTOR': _OBJECTDYNAMIC, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectDynamic)
ObjectMotionType = _reflection.GeneratedProtocolMessageType('ObjectMotionType', (_message.Message,), {'DESCRIPTOR': _OBJECTMOTIONTYPE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectMotionType)
ObjectDecisionType = _reflection.GeneratedProtocolMessageType('ObjectDecisionType', (_message.Message,), {'DESCRIPTOR': _OBJECTDECISIONTYPE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectDecisionType)
ObjectDecision = _reflection.GeneratedProtocolMessageType('ObjectDecision', (_message.Message,), {'DESCRIPTOR': _OBJECTDECISION, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectDecision)
ObjectDecisions = _reflection.GeneratedProtocolMessageType('ObjectDecisions', (_message.Message,), {'DESCRIPTOR': _OBJECTDECISIONS, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(ObjectDecisions)
MainStop = _reflection.GeneratedProtocolMessageType('MainStop', (_message.Message,), {'DESCRIPTOR': _MAINSTOP, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainStop)
EmergencyStopHardBrake = _reflection.GeneratedProtocolMessageType('EmergencyStopHardBrake', (_message.Message,), {'DESCRIPTOR': _EMERGENCYSTOPHARDBRAKE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(EmergencyStopHardBrake)
EmergencyStopCruiseToStop = _reflection.GeneratedProtocolMessageType('EmergencyStopCruiseToStop', (_message.Message,), {'DESCRIPTOR': _EMERGENCYSTOPCRUISETOSTOP, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(EmergencyStopCruiseToStop)
MainEmergencyStop = _reflection.GeneratedProtocolMessageType('MainEmergencyStop', (_message.Message,), {'DESCRIPTOR': _MAINEMERGENCYSTOP, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainEmergencyStop)
MainCruise = _reflection.GeneratedProtocolMessageType('MainCruise', (_message.Message,), {'DESCRIPTOR': _MAINCRUISE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainCruise)
MainChangeLane = _reflection.GeneratedProtocolMessageType('MainChangeLane', (_message.Message,), {'DESCRIPTOR': _MAINCHANGELANE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainChangeLane)
MainMissionComplete = _reflection.GeneratedProtocolMessageType('MainMissionComplete', (_message.Message,), {'DESCRIPTOR': _MAINMISSIONCOMPLETE, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainMissionComplete)
MainNotReady = _reflection.GeneratedProtocolMessageType('MainNotReady', (_message.Message,), {'DESCRIPTOR': _MAINNOTREADY, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainNotReady)
MainParking = _reflection.GeneratedProtocolMessageType('MainParking', (_message.Message,), {'DESCRIPTOR': _MAINPARKING, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainParking)
MainDecision = _reflection.GeneratedProtocolMessageType('MainDecision', (_message.Message,), {'DESCRIPTOR': _MAINDECISION, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(MainDecision)
DecisionResult = _reflection.GeneratedProtocolMessageType('DecisionResult', (_message.Message,), {'DESCRIPTOR': _DECISIONRESULT, '__module__': 'modules.planning.proto.decision_pb2'})
_sym_db.RegisterMessage(DecisionResult)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MAINDECISION.fields_by_name['change_lane']._options = None
    _MAINDECISION.fields_by_name['change_lane']._serialized_options = b'\x18\x01'
    _MAINDECISION.fields_by_name['target_lane']._options = None
    _MAINDECISION.fields_by_name['target_lane']._serialized_options = b'\x18\x01'
    _STOPREASONCODE._serialized_start = 3891
    _STOPREASONCODE._serialized_end = 4433
    _TARGETLANE._serialized_start = 175
    _TARGETLANE._serialized_end = 252
    _OBJECTIGNORE._serialized_start = 254
    _OBJECTIGNORE._serialized_end = 268
    _OBJECTSTOP._serialized_start = 271
    _OBJECTSTOP._serialized_end = 451
    _OBJECTNUDGE._serialized_start = 454
    _OBJECTNUDGE._serialized_end = 626
    _OBJECTNUDGE_TYPE._serialized_start = 538
    _OBJECTNUDGE_TYPE._serialized_end = 626
    _OBJECTYIELD._serialized_start = 628
    _OBJECTYIELD._serialized_end = 751
    _OBJECTFOLLOW._serialized_start = 753
    _OBJECTFOLLOW._serialized_end = 856
    _OBJECTOVERTAKE._serialized_start = 858
    _OBJECTOVERTAKE._serialized_end = 984
    _OBJECTSIDEPASS._serialized_start = 986
    _OBJECTSIDEPASS._serialized_end = 1083
    _OBJECTSIDEPASS_TYPE._serialized_start = 1056
    _OBJECTSIDEPASS_TYPE._serialized_end = 1083
    _OBJECTAVOID._serialized_start = 1085
    _OBJECTAVOID._serialized_end = 1098
    _OBJECTSTATUS._serialized_start = 1101
    _OBJECTSTATUS._serialized_end = 1231
    _OBJECTSTATIC._serialized_start = 1233
    _OBJECTSTATIC._serialized_end = 1247
    _OBJECTDYNAMIC._serialized_start = 1249
    _OBJECTDYNAMIC._serialized_end = 1264
    _OBJECTMOTIONTYPE._serialized_start = 1267
    _OBJECTMOTIONTYPE._serialized_end = 1399
    _OBJECTDECISIONTYPE._serialized_start = 1402
    _OBJECTDECISIONTYPE._serialized_end = 1827
    _OBJECTDECISION._serialized_start = 1829
    _OBJECTDECISION._serialized_end = 1942
    _OBJECTDECISIONS._serialized_start = 1944
    _OBJECTDECISIONS._serialized_end = 2012
    _MAINSTOP._serialized_start = 2015
    _MAINSTOP._serialized_end = 2220
    _EMERGENCYSTOPHARDBRAKE._serialized_start = 2222
    _EMERGENCYSTOPHARDBRAKE._serialized_end = 2246
    _EMERGENCYSTOPCRUISETOSTOP._serialized_start = 2248
    _EMERGENCYSTOPCRUISETOSTOP._serialized_end = 2275
    _MAINEMERGENCYSTOP._serialized_start = 2278
    _MAINEMERGENCYSTOP._serialized_end = 2693
    _MAINEMERGENCYSTOP_REASONCODE._serialized_start = 2517
    _MAINEMERGENCYSTOP_REASONCODE._serialized_end = 2685
    _MAINCRUISE._serialized_start = 2695
    _MAINCRUISE._serialized_end = 2765
    _MAINCHANGELANE._serialized_start = 2768
    _MAINCHANGELANE._serialized_end = 3023
    _MAINCHANGELANE_TYPE._serialized_start = 1056
    _MAINCHANGELANE_TYPE._serialized_end = 1083
    _MAINMISSIONCOMPLETE._serialized_start = 3025
    _MAINMISSIONCOMPLETE._serialized_end = 3113
    _MAINNOTREADY._serialized_start = 3115
    _MAINNOTREADY._serialized_end = 3145
    _MAINPARKING._serialized_start = 3147
    _MAINPARKING._serialized_end = 3253
    _MAINPARKING_PARKINGSTATUS._serialized_start = 3222
    _MAINPARKING_PARKINGSTATUS._serialized_end = 3253
    _MAINDECISION._serialized_start = 3256
    _MAINDECISION._serialized_end = 3702
    _DECISIONRESULT._serialized_start = 3705
    _DECISIONRESULT._serialized_end = 3888