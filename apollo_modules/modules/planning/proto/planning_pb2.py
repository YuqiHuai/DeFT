"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from ....modules.common.proto import drive_state_pb2 as modules_dot_common_dot_proto_dot_drive__state__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.planning.proto import decision_pb2 as modules_dot_planning_dot_proto_dot_decision__pb2
from ....modules.planning.proto import planning_internal_pb2 as modules_dot_planning_dot_proto_dot_planning__internal__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/planning/proto/planning.proto\x12\x0fapollo.planning\x1a"modules/canbus/proto/chassis.proto\x1a&modules/common/proto/drive_state.proto\x1a#modules/common/proto/geometry.proto\x1a!modules/common/proto/header.proto\x1a$modules/common/proto/pnc_point.proto\x1a\x1emodules/map/proto/map_id.proto\x1a%modules/planning/proto/decision.proto\x1a.modules/planning/proto/planning_internal.proto")\n\x05EStop\x12\x10\n\x08is_estop\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\t"*\n\tTaskStats\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07time_ms\x18\x02 \x01(\x01"q\n\x0cLatencyStats\x12\x15\n\rtotal_time_ms\x18\x01 \x01(\x01\x12.\n\ntask_stats\x18\x02 \x03(\x0b2\x1a.apollo.planning.TaskStats\x12\x1a\n\x12init_frame_time_ms\x18\x03 \x01(\x01"\x9f\x02\n\x07RSSInfo\x12\x13\n\x0bis_rss_safe\x18\x01 \x01(\x08\x12\x14\n\x0ccur_dist_lon\x18\x02 \x01(\x01\x12\x19\n\x11rss_safe_dist_lon\x18\x03 \x01(\x01\x12\x1d\n\x15acc_lon_range_minimum\x18\x04 \x01(\x01\x12\x1d\n\x15acc_lon_range_maximum\x18\x05 \x01(\x01\x12"\n\x1aacc_lat_left_range_minimum\x18\x06 \x01(\x01\x12"\n\x1aacc_lat_left_range_maximum\x18\x07 \x01(\x01\x12#\n\x1bacc_lat_right_range_minimum\x18\x08 \x01(\x01\x12#\n\x1bacc_lat_right_range_maximum\x18\t \x01(\x01"\xdd\x01\n\x04DeFT\x12\x17\n\x0fstart_timestamp\x18\x01 \x02(\x01\x12\x16\n\x0erouting_header\x18\x02 \x02(\x05\x12\x16\n\x0echassis_header\x18\x03 \x02(\x05\x12\x1b\n\x13localization_header\x18\x04 \x02(\x05\x12\x19\n\x11prediction_header\x18\x05 \x02(\x05\x12 \n\x14traffic_light_header\x18\x06 \x01(\x05:\x02-1\x12\x1a\n\x0estories_header\x18\x07 \x01(\x05:\x02-1\x12\x16\n\npad_header\x18\x08 \x01(\x05:\x02-1"\xc8\t\n\rADCTrajectory\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x19\n\x11total_path_length\x18\x02 \x01(\x01\x12\x17\n\x0ftotal_path_time\x18\x03 \x01(\x01\x12%\n\x05estop\x18\x06 \x01(\x0b2\x16.apollo.planning.EStop\x12.\n\x05debug\x18\x08 \x01(\x0b2\x1f.apollo.planning_internal.Debug\x12\x18\n\tis_replan\x18\t \x01(\x08:\x05false\x121\n\x04gear\x18\n \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x128\n\x10trajectory_point\x18\x0c \x03(\x0b2\x1e.apollo.common.TrajectoryPoint\x12,\n\npath_point\x18\r \x03(\x0b2\x18.apollo.common.PathPoint\x121\n\x08decision\x18\x0e \x01(\x0b2\x1f.apollo.planning.DecisionResult\x124\n\rlatency_stats\x18\x0f \x01(\x0b2\x1d.apollo.planning.LatencyStats\x12-\n\x0erouting_header\x18\x10 \x01(\x0b2\x15.apollo.common.Header\x12L\n\x13right_of_way_status\x18\x11 \x01(\x0e2/.apollo.planning.ADCTrajectory.RightOfWayStatus\x12!\n\x07lane_id\x18\x12 \x03(\x0b2\x10.apollo.hdmap.Id\x122\n\rengage_advice\x18\x13 \x01(\x0b2\x1b.apollo.common.EngageAdvice\x12F\n\x0fcritical_region\x18\x14 \x01(\x0b2-.apollo.planning.ADCTrajectory.CriticalRegion\x12O\n\x0ftrajectory_type\x18\x15 \x01(\x0e2-.apollo.planning.ADCTrajectory.TrajectoryType:\x07UNKNOWN\x12\x15\n\rreplan_reason\x18\x16 \x01(\t\x12(\n\x0etarget_lane_id\x18\x17 \x03(\x0b2\x10.apollo.hdmap.Id\x12\x17\n\x0fcar_in_dead_end\x18\x18 \x01(\x08\x12#\n\x04deft\x18\x19 \x01(\x0b2\x15.apollo.planning.DeFT\x12*\n\x08rss_info\x18d \x01(\x0b2\x18.apollo.planning.RSSInfo\x1a8\n\x0eCriticalRegion\x12&\n\x06region\x18\x01 \x03(\x0b2\x16.apollo.common.Polygon"2\n\x10RightOfWayStatus\x12\x0f\n\x0bUNPROTECTED\x10\x00\x12\r\n\tPROTECTED\x10\x01"a\n\x0eTrajectoryType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x11\n\rPATH_FALLBACK\x10\x02\x12\x12\n\x0eSPEED_FALLBACK\x10\x03\x12\x0f\n\x0bPATH_REUSED\x10\x04*_\n\x07JucType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02\x12\r\n\tFORK_ROAD\x10\x03\x12\r\n\tMAIN_SIDE\x10\x04\x12\x0c\n\x08DEAD_END\x10\x05')
_JUCTYPE = DESCRIPTOR.enum_types_by_name['JucType']
JucType = enum_type_wrapper.EnumTypeWrapper(_JUCTYPE)
UNKNOWN = 0
IN_ROAD = 1
CROSS_ROAD = 2
FORK_ROAD = 3
MAIN_SIDE = 4
DEAD_END = 5
_ESTOP = DESCRIPTOR.message_types_by_name['EStop']
_TASKSTATS = DESCRIPTOR.message_types_by_name['TaskStats']
_LATENCYSTATS = DESCRIPTOR.message_types_by_name['LatencyStats']
_RSSINFO = DESCRIPTOR.message_types_by_name['RSSInfo']
_DEFT = DESCRIPTOR.message_types_by_name['DeFT']
_ADCTRAJECTORY = DESCRIPTOR.message_types_by_name['ADCTrajectory']
_ADCTRAJECTORY_CRITICALREGION = _ADCTRAJECTORY.nested_types_by_name['CriticalRegion']
_ADCTRAJECTORY_RIGHTOFWAYSTATUS = _ADCTRAJECTORY.enum_types_by_name['RightOfWayStatus']
_ADCTRAJECTORY_TRAJECTORYTYPE = _ADCTRAJECTORY.enum_types_by_name['TrajectoryType']
EStop = _reflection.GeneratedProtocolMessageType('EStop', (_message.Message,), {'DESCRIPTOR': _ESTOP, '__module__': 'modules.planning.proto.planning_pb2'})
_sym_db.RegisterMessage(EStop)
TaskStats = _reflection.GeneratedProtocolMessageType('TaskStats', (_message.Message,), {'DESCRIPTOR': _TASKSTATS, '__module__': 'modules.planning.proto.planning_pb2'})
_sym_db.RegisterMessage(TaskStats)
LatencyStats = _reflection.GeneratedProtocolMessageType('LatencyStats', (_message.Message,), {'DESCRIPTOR': _LATENCYSTATS, '__module__': 'modules.planning.proto.planning_pb2'})
_sym_db.RegisterMessage(LatencyStats)
RSSInfo = _reflection.GeneratedProtocolMessageType('RSSInfo', (_message.Message,), {'DESCRIPTOR': _RSSINFO, '__module__': 'modules.planning.proto.planning_pb2'})
_sym_db.RegisterMessage(RSSInfo)
DeFT = _reflection.GeneratedProtocolMessageType('DeFT', (_message.Message,), {'DESCRIPTOR': _DEFT, '__module__': 'modules.planning.proto.planning_pb2'})
_sym_db.RegisterMessage(DeFT)
ADCTrajectory = _reflection.GeneratedProtocolMessageType('ADCTrajectory', (_message.Message,), {'CriticalRegion': _reflection.GeneratedProtocolMessageType('CriticalRegion', (_message.Message,), {'DESCRIPTOR': _ADCTRAJECTORY_CRITICALREGION, '__module__': 'modules.planning.proto.planning_pb2'}), 'DESCRIPTOR': _ADCTRAJECTORY, '__module__': 'modules.planning.proto.planning_pb2'})
_sym_db.RegisterMessage(ADCTrajectory)
_sym_db.RegisterMessage(ADCTrajectory.CriticalRegion)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _JUCTYPE._serialized_start = 2306
    _JUCTYPE._serialized_end = 2401
    _ESTOP._serialized_start = 363
    _ESTOP._serialized_end = 404
    _TASKSTATS._serialized_start = 406
    _TASKSTATS._serialized_end = 448
    _LATENCYSTATS._serialized_start = 450
    _LATENCYSTATS._serialized_end = 563
    _RSSINFO._serialized_start = 566
    _RSSINFO._serialized_end = 853
    _DEFT._serialized_start = 856
    _DEFT._serialized_end = 1077
    _ADCTRAJECTORY._serialized_start = 1080
    _ADCTRAJECTORY._serialized_end = 2304
    _ADCTRAJECTORY_CRITICALREGION._serialized_start = 2097
    _ADCTRAJECTORY_CRITICALREGION._serialized_end = 2153
    _ADCTRAJECTORY_RIGHTOFWAYSTATUS._serialized_start = 2155
    _ADCTRAJECTORY_RIGHTOFWAYSTATUS._serialized_end = 2205
    _ADCTRAJECTORY_TRAJECTORYTYPE._serialized_start = 2207
    _ADCTRAJECTORY_TRAJECTORYTYPE._serialized_end = 2304