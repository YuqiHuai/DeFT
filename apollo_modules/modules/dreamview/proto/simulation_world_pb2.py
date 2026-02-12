"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from ....modules.common.monitor_log.proto import monitor_log_pb2 as modules_dot_common_dot_monitor__log_dot_proto_dot_monitor__log__pb2
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
from ....modules.planning.proto import planning_internal_pb2 as modules_dot_planning_dot_proto_dot_planning__internal__pb2
from ....modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2
from ....modules.routing.proto import routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/dreamview/proto/simulation_world.proto\x12\x10apollo.dreamview\x1a"modules/canbus/proto/chassis.proto\x1a2modules/common/monitor_log/proto/monitor_log.proto\x1a$modules/common/proto/pnc_point.proto\x1a2modules/perception/proto/perception_obstacle.proto\x1a.modules/planning/proto/planning_internal.proto\x1a&modules/prediction/proto/feature.proto\x1a#modules/routing/proto/routing.proto"f\n\x0cPolygonPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0c\n\x01z\x18\x03 \x01(\x01:\x010\x122\n\rgaussian_info\x18\x04 \x01(\x0b2\x1b.apollo.common.GaussianInfo"_\n\nPrediction\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12<\n\x14predicted_trajectory\x18\x02 \x03(\x0b2\x1e.apollo.dreamview.PolygonPoint"\xc4\x06\n\x08Decision\x125\n\x04type\x18\x01 \x01(\x0e2\x1f.apollo.dreamview.Decision.Type:\x06IGNORE\x125\n\rpolygon_point\x18\x02 \x03(\x0b2\x1e.apollo.dreamview.PolygonPoint\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x12\n\nposition_x\x18\x06 \x01(\x01\x12\x12\n\nposition_y\x18\x07 \x01(\x01\x12\x13\n\x06length\x18\x08 \x01(\x01:\x032.8\x12\x12\n\x05width\x18\t \x01(\x01:\x031.4\x12\x13\n\x06height\x18\n \x01(\x01:\x031.8\x12=\n\nstopReason\x18\x0b \x01(\x0e2).apollo.dreamview.Decision.StopReasonCode\x128\n\x10change_lane_type\x18\x0c \x01(\x0e2\x1e.apollo.routing.ChangeLaneType"Z\n\x04Type\x12\n\n\x06IGNORE\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\t\n\x05NUDGE\x10\x02\x12\t\n\x05YIELD\x10\x03\x12\x0c\n\x08OVERTAKE\x10\x04\x12\n\n\x06FOLLOW\x10\x05\x12\x0c\n\x08SIDEPASS\x10\x06"\xd8\x02\n\x0eStopReasonCode\x12\x1c\n\x18STOP_REASON_HEAD_VEHICLE\x10\x01\x12\x1b\n\x17STOP_REASON_DESTINATION\x10\x02\x12\x1a\n\x16STOP_REASON_PEDESTRIAN\x10\x03\x12\x18\n\x14STOP_REASON_OBSTACLE\x10\x04\x12\x16\n\x12STOP_REASON_SIGNAL\x10d\x12\x19\n\x15STOP_REASON_STOP_SIGN\x10e\x12\x1a\n\x16STOP_REASON_YIELD_SIGN\x10f\x12\x1a\n\x16STOP_REASON_CLEAR_ZONE\x10g\x12\x19\n\x15STOP_REASON_CROSSWALK\x10h\x12\x19\n\x15STOP_REASON_EMERGENCY\x10i\x12\x19\n\x15STOP_REASON_NOT_READY\x10j\x12\x19\n\x15STOP_REASON_PULL_OVER\x10k"\xcc\x0c\n\x06Object\x12\n\n\x02id\x18\x01 \x01(\t\x125\n\rpolygon_point\x18\x02 \x03(\x0b2\x1e.apollo.dreamview.PolygonPoint\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x12\n\nposition_x\x18\x06 \x01(\x01\x12\x12\n\nposition_y\x18\x07 \x01(\x01\x12\x13\n\x06length\x18\x08 \x01(\x01:\x032.8\x12\x12\n\x05width\x18\t \x01(\x01:\x031.4\x12\x13\n\x06height\x18\n \x01(\x01:\x031.8\x12\r\n\x05speed\x18\x0b \x01(\x01\x12\x1a\n\x12speed_acceleration\x18\x0c \x01(\x01\x12\x12\n\nspeed_jerk\x18\r \x01(\x01\x12\x0c\n\x04spin\x18\x0e \x01(\x01\x12\x19\n\x11spin_acceleration\x18\x0f \x01(\x01\x12\x11\n\tspin_jerk\x18\x10 \x01(\x01\x12\x15\n\rspeed_heading\x18\x11 \x01(\x01\x12\r\n\x05kappa\x18\x12 \x01(\x01\x12\x0e\n\x06dkappa\x18# \x01(\x01\x12\x12\n\nsignal_set\x18\x13 \x03(\t\x12\x16\n\x0ecurrent_signal\x18\x14 \x01(\t\x12\x15\n\rtimestamp_sec\x18\x15 \x01(\x01\x12,\n\x08decision\x18\x16 \x03(\x0b2\x1a.apollo.dreamview.Decision\x12\x1f\n\x10yielded_obstacle\x18  \x01(\x08:\x05false\x12\x1b\n\x13throttle_percentage\x18\x17 \x01(\x01\x12\x18\n\x10brake_percentage\x18\x18 \x01(\x01\x12\x1b\n\x13steering_percentage\x18\x19 \x01(\x01\x12\x16\n\x0esteering_angle\x18\x1a \x01(\x01\x12\x16\n\x0esteering_ratio\x18\x1b \x01(\x01\x12\x1a\n\x12battery_percentage\x18& \x01(\x05\x12:\n\rgear_location\x18\' \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x12>\n\x0edisengage_type\x18\x1c \x01(\x0e2&.apollo.dreamview.Object.DisengageType\x12+\n\x04type\x18\x1d \x01(\x0e2\x1d.apollo.dreamview.Object.Type\x12?\n\x08sub_type\x18" \x01(\x0e2-.apollo.perception.PerceptionObstacle.SubType\x120\n\nprediction\x18\x1e \x03(\x0b2\x1c.apollo.dreamview.Prediction\x12\x15\n\nconfidence\x18\x1f \x01(\x01:\x011\x12>\n\x11obstacle_priority\x18! \x01(\x0b2#.apollo.prediction.ObstaclePriority\x12B\n\x0finteractive_tag\x18( \x01(\x0b2).apollo.prediction.ObstacleInteractiveTag\x12J\n\x06source\x18$ \x01(\x0e2,.apollo.perception.PerceptionObstacle.Source:\x0cHOST_VEHICLE\x123\n\x08v2x_info\x18% \x01(\x0b2!.apollo.perception.V2XInformation"\xc4\x01\n\rDisengageType\x12\x12\n\x0eDISENGAGE_NONE\x10\x00\x12\x15\n\x11DISENGAGE_UNKNOWN\x10\x01\x12\x14\n\x10DISENGAGE_MANUAL\x10\x02\x12\x17\n\x13DISENGAGE_EMERGENCY\x10\x03\x12\x1d\n\x19DISENGAGE_AUTO_STEER_ONLY\x10\x04\x12\x1d\n\x19DISENGAGE_AUTO_SPEED_ONLY\x10\x05\x12\x1b\n\x17DISENGAGE_CHASSIS_ERROR\x10\x06"\x80\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07BICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\x12\x0b\n\x07VIRTUAL\x10\x06\x12\x08\n\x04CIPV\x10\x07"\x9e\x01\n\nDelaysInMs\x12\x0f\n\x07chassis\x18\x01 \x01(\x01\x12\x14\n\x0clocalization\x18\x03 \x01(\x01\x12\x1b\n\x13perception_obstacle\x18\x04 \x01(\x01\x12\x10\n\x08planning\x18\x05 \x01(\x01\x12\x12\n\nprediction\x18\x07 \x01(\x01\x12\x15\n\rtraffic_light\x18\x08 \x01(\x01\x12\x0f\n\x07control\x18\t \x01(\x01":\n\tRoutePath\x12-\n\x05point\x18\x01 \x03(\x0b2\x1e.apollo.dreamview.PolygonPoint"7\n\x07Latency\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x15\n\rtotal_time_ms\x18\x02 \x01(\x01"\xe8\x01\n\rMapElementIds\x12\x0c\n\x04lane\x18\x01 \x03(\t\x12\x11\n\tcrosswalk\x18\x02 \x03(\t\x12\x10\n\x08junction\x18\x03 \x03(\t\x12\x0e\n\x06signal\x18\x04 \x03(\t\x12\x11\n\tstop_sign\x18\x05 \x03(\t\x12\r\n\x05yield\x18\x06 \x03(\t\x12\x0f\n\x07overlap\x18\x07 \x03(\t\x12\x0c\n\x04road\x18\x08 \x03(\t\x12\x12\n\nclear_area\x18\t \x03(\t\x12\x15\n\rparking_space\x18\n \x03(\t\x12\x12\n\nspeed_bump\x18\x0b \x03(\t\x12\x14\n\x0cpnc_junction\x18\x0c \x03(\t"\xa7\x01\n\x0bControlData\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x15\n\rstation_error\x18\x02 \x01(\x01\x12\x15\n\rlateral_error\x18\x03 \x01(\x01\x12\x15\n\rheading_error\x18\x04 \x01(\x01\x12<\n\x14current_target_point\x18\x05 \x01(\x0b2\x1e.apollo.common.TrajectoryPoint"^\n\x0cNotification\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x127\n\x04item\x18\x02 \x01(\x0b2).apollo.common.monitor.MonitorMessageItem"J\n\x12SensorMeasurements\x124\n\x12sensor_measurement\x18\x01 \x03(\x0b2\x18.apollo.dreamview.Object"\xab\x0c\n\x0fSimulationWorld\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x14\n\x0csequence_num\x18\x02 \x01(\r\x12(\n\x06object\x18\x03 \x03(\x0b2\x18.apollo.dreamview.Object\x122\n\x10auto_driving_car\x18\x04 \x01(\x0b2\x18.apollo.dreamview.Object\x120\n\x0etraffic_signal\x18\x05 \x01(\x0b2\x18.apollo.dreamview.Object\x12/\n\nroute_path\x18\x06 \x03(\x0b2\x1b.apollo.dreamview.RoutePath\x12\x14\n\x0crouting_time\x18\x07 \x01(\x01\x125\n\x13planning_trajectory\x18\x08 \x03(\x0b2\x18.apollo.dreamview.Object\x12/\n\tmain_stop\x18\t \x01(\x0b2\x18.apollo.dreamview.ObjectB\x02\x18\x01\x12/\n\rmain_decision\x18\n \x01(\x0b2\x18.apollo.dreamview.Object\x12\x13\n\x0bspeed_limit\x18\x0b \x01(\x01\x12+\n\x05delay\x18\x0c \x01(\x0b2\x1c.apollo.dreamview.DelaysInMs\x12:\n\x07monitor\x18\r \x01(\x0b2%.apollo.common.monitor.MonitorMessageB\x02\x18\x01\x124\n\x0cnotification\x18\x0e \x03(\x0b2\x1e.apollo.dreamview.Notification\x12\x15\n\rengage_advice\x18\x0f \x01(\t\x12?\n\x07latency\x18\x10 \x03(\x0b2..apollo.dreamview.SimulationWorld.LatencyEntry\x128\n\x0fmap_element_ids\x18\x11 \x01(\x0b2\x1f.apollo.dreamview.MapElementIds\x12\x10\n\x08map_hash\x18\x12 \x01(\x04\x12\x12\n\nmap_radius\x18\x13 \x01(\x01\x12=\n\rplanning_data\x18\x14 \x01(\x0b2&.apollo.planning_internal.PlanningData\x12%\n\x03gps\x18\x15 \x01(\x0b2\x18.apollo.dreamview.Object\x123\n\x0blane_marker\x18\x16 \x01(\x0b2\x1e.apollo.perception.LaneMarkers\x123\n\x0ccontrol_data\x18\x17 \x01(\x0b2\x1d.apollo.dreamview.ControlData\x12,\n\x0fnavigation_path\x18\x18 \x03(\x0b2\x13.apollo.common.Path\x12\x19\n\x0bis_rss_safe\x18\x19 \x01(\x08:\x04true\x125\n\x13shadow_localization\x18\x1a \x01(\x0b2\x18.apollo.dreamview.Object\x122\n\x10perceived_signal\x18\x1b \x03(\x0b2\x18.apollo.dreamview.Object\x12?\n\x07stories\x18\x1c \x03(\x0b2..apollo.dreamview.SimulationWorld.StoriesEntry\x12V\n\x13sensor_measurements\x18\x1d \x03(\x0b29.apollo.dreamview.SimulationWorld.SensorMeasurementsEntry\x12\x1a\n\x0bis_siren_on\x18\x1e \x01(\x08:\x05false\x1aI\n\x0cLatencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b2\x19.apollo.dreamview.Latency:\x028\x01\x1a.\n\x0cStoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x028\x01\x1a_\n\x17SensorMeasurementsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x123\n\x05value\x18\x02 \x01(\x0b2$.apollo.dreamview.SensorMeasurements:\x028\x01')
_POLYGONPOINT = DESCRIPTOR.message_types_by_name['PolygonPoint']
_PREDICTION = DESCRIPTOR.message_types_by_name['Prediction']
_DECISION = DESCRIPTOR.message_types_by_name['Decision']
_OBJECT = DESCRIPTOR.message_types_by_name['Object']
_DELAYSINMS = DESCRIPTOR.message_types_by_name['DelaysInMs']
_ROUTEPATH = DESCRIPTOR.message_types_by_name['RoutePath']
_LATENCY = DESCRIPTOR.message_types_by_name['Latency']
_MAPELEMENTIDS = DESCRIPTOR.message_types_by_name['MapElementIds']
_CONTROLDATA = DESCRIPTOR.message_types_by_name['ControlData']
_NOTIFICATION = DESCRIPTOR.message_types_by_name['Notification']
_SENSORMEASUREMENTS = DESCRIPTOR.message_types_by_name['SensorMeasurements']
_SIMULATIONWORLD = DESCRIPTOR.message_types_by_name['SimulationWorld']
_SIMULATIONWORLD_LATENCYENTRY = _SIMULATIONWORLD.nested_types_by_name['LatencyEntry']
_SIMULATIONWORLD_STORIESENTRY = _SIMULATIONWORLD.nested_types_by_name['StoriesEntry']
_SIMULATIONWORLD_SENSORMEASUREMENTSENTRY = _SIMULATIONWORLD.nested_types_by_name['SensorMeasurementsEntry']
_DECISION_TYPE = _DECISION.enum_types_by_name['Type']
_DECISION_STOPREASONCODE = _DECISION.enum_types_by_name['StopReasonCode']
_OBJECT_DISENGAGETYPE = _OBJECT.enum_types_by_name['DisengageType']
_OBJECT_TYPE = _OBJECT.enum_types_by_name['Type']
PolygonPoint = _reflection.GeneratedProtocolMessageType('PolygonPoint', (_message.Message,), {'DESCRIPTOR': _POLYGONPOINT, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(PolygonPoint)
Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {'DESCRIPTOR': _PREDICTION, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(Prediction)
Decision = _reflection.GeneratedProtocolMessageType('Decision', (_message.Message,), {'DESCRIPTOR': _DECISION, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(Decision)
Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {'DESCRIPTOR': _OBJECT, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(Object)
DelaysInMs = _reflection.GeneratedProtocolMessageType('DelaysInMs', (_message.Message,), {'DESCRIPTOR': _DELAYSINMS, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(DelaysInMs)
RoutePath = _reflection.GeneratedProtocolMessageType('RoutePath', (_message.Message,), {'DESCRIPTOR': _ROUTEPATH, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(RoutePath)
Latency = _reflection.GeneratedProtocolMessageType('Latency', (_message.Message,), {'DESCRIPTOR': _LATENCY, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(Latency)
MapElementIds = _reflection.GeneratedProtocolMessageType('MapElementIds', (_message.Message,), {'DESCRIPTOR': _MAPELEMENTIDS, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(MapElementIds)
ControlData = _reflection.GeneratedProtocolMessageType('ControlData', (_message.Message,), {'DESCRIPTOR': _CONTROLDATA, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(ControlData)
Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), {'DESCRIPTOR': _NOTIFICATION, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(Notification)
SensorMeasurements = _reflection.GeneratedProtocolMessageType('SensorMeasurements', (_message.Message,), {'DESCRIPTOR': _SENSORMEASUREMENTS, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(SensorMeasurements)
SimulationWorld = _reflection.GeneratedProtocolMessageType('SimulationWorld', (_message.Message,), {'LatencyEntry': _reflection.GeneratedProtocolMessageType('LatencyEntry', (_message.Message,), {'DESCRIPTOR': _SIMULATIONWORLD_LATENCYENTRY, '__module__': 'modules.dreamview.proto.simulation_world_pb2'}), 'StoriesEntry': _reflection.GeneratedProtocolMessageType('StoriesEntry', (_message.Message,), {'DESCRIPTOR': _SIMULATIONWORLD_STORIESENTRY, '__module__': 'modules.dreamview.proto.simulation_world_pb2'}), 'SensorMeasurementsEntry': _reflection.GeneratedProtocolMessageType('SensorMeasurementsEntry', (_message.Message,), {'DESCRIPTOR': _SIMULATIONWORLD_SENSORMEASUREMENTSENTRY, '__module__': 'modules.dreamview.proto.simulation_world_pb2'}), 'DESCRIPTOR': _SIMULATIONWORLD, '__module__': 'modules.dreamview.proto.simulation_world_pb2'})
_sym_db.RegisterMessage(SimulationWorld)
_sym_db.RegisterMessage(SimulationWorld.LatencyEntry)
_sym_db.RegisterMessage(SimulationWorld.StoriesEntry)
_sym_db.RegisterMessage(SimulationWorld.SensorMeasurementsEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SIMULATIONWORLD_LATENCYENTRY._options = None
    _SIMULATIONWORLD_LATENCYENTRY._serialized_options = b'8\x01'
    _SIMULATIONWORLD_STORIESENTRY._options = None
    _SIMULATIONWORLD_STORIESENTRY._serialized_options = b'8\x01'
    _SIMULATIONWORLD_SENSORMEASUREMENTSENTRY._options = None
    _SIMULATIONWORLD_SENSORMEASUREMENTSENTRY._serialized_options = b'8\x01'
    _SIMULATIONWORLD.fields_by_name['main_stop']._options = None
    _SIMULATIONWORLD.fields_by_name['main_stop']._serialized_options = b'\x18\x01'
    _SIMULATIONWORLD.fields_by_name['monitor']._options = None
    _SIMULATIONWORLD.fields_by_name['monitor']._serialized_options = b'\x18\x01'
    _POLYGONPOINT._serialized_start = 371
    _POLYGONPOINT._serialized_end = 473
    _PREDICTION._serialized_start = 475
    _PREDICTION._serialized_end = 570
    _DECISION._serialized_start = 573
    _DECISION._serialized_end = 1409
    _DECISION_TYPE._serialized_start = 972
    _DECISION_TYPE._serialized_end = 1062
    _DECISION_STOPREASONCODE._serialized_start = 1065
    _DECISION_STOPREASONCODE._serialized_end = 1409
    _OBJECT._serialized_start = 1412
    _OBJECT._serialized_end = 3024
    _OBJECT_DISENGAGETYPE._serialized_start = 2697
    _OBJECT_DISENGAGETYPE._serialized_end = 2893
    _OBJECT_TYPE._serialized_start = 2896
    _OBJECT_TYPE._serialized_end = 3024
    _DELAYSINMS._serialized_start = 3027
    _DELAYSINMS._serialized_end = 3185
    _ROUTEPATH._serialized_start = 3187
    _ROUTEPATH._serialized_end = 3245
    _LATENCY._serialized_start = 3247
    _LATENCY._serialized_end = 3302
    _MAPELEMENTIDS._serialized_start = 3305
    _MAPELEMENTIDS._serialized_end = 3537
    _CONTROLDATA._serialized_start = 3540
    _CONTROLDATA._serialized_end = 3707
    _NOTIFICATION._serialized_start = 3709
    _NOTIFICATION._serialized_end = 3803
    _SENSORMEASUREMENTS._serialized_start = 3805
    _SENSORMEASUREMENTS._serialized_end = 3879
    _SIMULATIONWORLD._serialized_start = 3882
    _SIMULATIONWORLD._serialized_end = 5461
    _SIMULATIONWORLD_LATENCYENTRY._serialized_start = 5243
    _SIMULATIONWORLD_LATENCYENTRY._serialized_end = 5316
    _SIMULATIONWORLD_STORIESENTRY._serialized_start = 5318
    _SIMULATIONWORLD_STORIESENTRY._serialized_end = 5364
    _SIMULATIONWORLD_SENSORMEASUREMENTSENTRY._serialized_start = 5366
    _SIMULATIONWORLD_SENSORMEASUREMENTSENTRY._serialized_end = 5461