"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/perception/camera/app/proto/perception.proto\x12\x1capollo.perception.camera.app"B\n\x0bPluginParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08root_dir\x18\x02 \x01(\t\x12\x13\n\x0bconfig_file\x18\x03 \x01(\t"e\n\rDetectorParam\x12?\n\x0cplugin_param\x18\x01 \x01(\x0b2).apollo.perception.camera.app.PluginParam\x12\x13\n\x0bcamera_name\x18\x02 \x01(\t"O\n\x0cTrackerParam\x12?\n\x0cplugin_param\x18\x01 \x01(\x0b2).apollo.perception.camera.app.PluginParam"S\n\x10TransformerParam\x12?\n\x0cplugin_param\x18\x01 \x01(\x0b2).apollo.perception.camera.app.PluginParam"U\n\x12PostprocessorParam\x12?\n\x0cplugin_param\x18\x01 \x01(\x0b2).apollo.perception.camera.app.PluginParam"O\n\x0cFeatureParam\x12?\n\x0cplugin_param\x18\x01 \x01(\x0b2).apollo.perception.camera.app.PluginParam"\xd0\x01\n\nDebugParam\x12\x19\n\x11detection_out_dir\x18\x01 \x01(\t\x12!\n\x19tracked_detection_out_dir\x18\x02 \x01(\t\x12\x16\n\x0etrack_out_file\x18\x03 \x01(\t\x12\x1a\n\x12detect_feature_dir\x18\x04 \x01(\t\x12\x14\n\x0clane_out_dir\x18\x05 \x01(\t\x12\x1d\n\x15camera2world_out_file\x18\x06 \x01(\t\x12\x1b\n\x13calibration_out_dir\x18\x07 \x01(\t"\x83\x02\n\x13LanePerceptionParam\x12H\n\x13lane_detector_param\x18\x01 \x01(\x0b2+.apollo.perception.camera.app.DetectorParam\x12K\n\x18lane_postprocessor_param\x18\x02 \x01(\x0b2).apollo.perception.camera.app.PluginParam\x12E\n\x12lane_tracker_param\x18\x03 \x01(\x0b2).apollo.perception.camera.app.PluginParam\x12\x0e\n\x06gpu_id\x18\x04 \x01(\x05"u\n\x17CalibrationServiceParam\x12\x19\n\x11calibrator_method\x18\x02 \x01(\t\x12?\n\x0cplugin_param\x18\x03 \x01(\x0b2).apollo.perception.camera.app.PluginParam"V\n\x13ObjectTemplateParam\x12?\n\x0cplugin_param\x18\x01 \x01(\x0b2).apollo.perception.camera.app.PluginParam"\xd3\x05\n\x0fPerceptionParam\x12C\n\x0edetector_param\x18\x01 \x03(\x0b2+.apollo.perception.camera.app.DetectorParam\x12A\n\rtracker_param\x18\x02 \x01(\x0b2*.apollo.perception.camera.app.TrackerParam\x12I\n\x11transformer_param\x18\x03 \x01(\x0b2..apollo.perception.camera.app.TransformerParam\x12M\n\x13postprocessor_param\x18\x04 \x01(\x0b20.apollo.perception.camera.app.PostprocessorParam\x12\x0e\n\x06gpu_id\x18\x05 \x01(\x05\x12\x19\n\x11camera_intrinsics\x18\x06 \x01(\t\x12A\n\rfeature_param\x18\x07 \x01(\x0b2*.apollo.perception.camera.app.FeatureParam\x12E\n\nlane_param\x18\x08 \x03(\x0b21.apollo.perception.camera.app.LanePerceptionParam\x12X\n\x19calibration_service_param\x18\t \x01(\x0b25.apollo.perception.camera.app.CalibrationServiceParam\x12=\n\x0bdebug_param\x18\n \x01(\x0b2(.apollo.perception.camera.app.DebugParam\x12P\n\x15object_template_param\x18\x0b \x01(\x0b21.apollo.perception.camera.app.ObjectTemplateParam"\xab\x01\n\x11TrafficLightParam\x12C\n\x0edetector_param\x18\x01 \x03(\x0b2+.apollo.perception.camera.app.DetectorParam\x12A\n\rtracker_param\x18\x02 \x01(\x0b2*.apollo.perception.camera.app.TrackerParam\x12\x0e\n\x06gpu_id\x18\x03 \x01(\x05')
_PLUGINPARAM = DESCRIPTOR.message_types_by_name['PluginParam']
_DETECTORPARAM = DESCRIPTOR.message_types_by_name['DetectorParam']
_TRACKERPARAM = DESCRIPTOR.message_types_by_name['TrackerParam']
_TRANSFORMERPARAM = DESCRIPTOR.message_types_by_name['TransformerParam']
_POSTPROCESSORPARAM = DESCRIPTOR.message_types_by_name['PostprocessorParam']
_FEATUREPARAM = DESCRIPTOR.message_types_by_name['FeatureParam']
_DEBUGPARAM = DESCRIPTOR.message_types_by_name['DebugParam']
_LANEPERCEPTIONPARAM = DESCRIPTOR.message_types_by_name['LanePerceptionParam']
_CALIBRATIONSERVICEPARAM = DESCRIPTOR.message_types_by_name['CalibrationServiceParam']
_OBJECTTEMPLATEPARAM = DESCRIPTOR.message_types_by_name['ObjectTemplateParam']
_PERCEPTIONPARAM = DESCRIPTOR.message_types_by_name['PerceptionParam']
_TRAFFICLIGHTPARAM = DESCRIPTOR.message_types_by_name['TrafficLightParam']
PluginParam = _reflection.GeneratedProtocolMessageType('PluginParam', (_message.Message,), {'DESCRIPTOR': _PLUGINPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(PluginParam)
DetectorParam = _reflection.GeneratedProtocolMessageType('DetectorParam', (_message.Message,), {'DESCRIPTOR': _DETECTORPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(DetectorParam)
TrackerParam = _reflection.GeneratedProtocolMessageType('TrackerParam', (_message.Message,), {'DESCRIPTOR': _TRACKERPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(TrackerParam)
TransformerParam = _reflection.GeneratedProtocolMessageType('TransformerParam', (_message.Message,), {'DESCRIPTOR': _TRANSFORMERPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(TransformerParam)
PostprocessorParam = _reflection.GeneratedProtocolMessageType('PostprocessorParam', (_message.Message,), {'DESCRIPTOR': _POSTPROCESSORPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(PostprocessorParam)
FeatureParam = _reflection.GeneratedProtocolMessageType('FeatureParam', (_message.Message,), {'DESCRIPTOR': _FEATUREPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(FeatureParam)
DebugParam = _reflection.GeneratedProtocolMessageType('DebugParam', (_message.Message,), {'DESCRIPTOR': _DEBUGPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(DebugParam)
LanePerceptionParam = _reflection.GeneratedProtocolMessageType('LanePerceptionParam', (_message.Message,), {'DESCRIPTOR': _LANEPERCEPTIONPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(LanePerceptionParam)
CalibrationServiceParam = _reflection.GeneratedProtocolMessageType('CalibrationServiceParam', (_message.Message,), {'DESCRIPTOR': _CALIBRATIONSERVICEPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(CalibrationServiceParam)
ObjectTemplateParam = _reflection.GeneratedProtocolMessageType('ObjectTemplateParam', (_message.Message,), {'DESCRIPTOR': _OBJECTTEMPLATEPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(ObjectTemplateParam)
PerceptionParam = _reflection.GeneratedProtocolMessageType('PerceptionParam', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(PerceptionParam)
TrafficLightParam = _reflection.GeneratedProtocolMessageType('TrafficLightParam', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTPARAM, '__module__': 'modules.perception.camera.app.proto.perception_pb2'})
_sym_db.RegisterMessage(TrafficLightParam)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PLUGINPARAM._serialized_start = 86
    _PLUGINPARAM._serialized_end = 152
    _DETECTORPARAM._serialized_start = 154
    _DETECTORPARAM._serialized_end = 255
    _TRACKERPARAM._serialized_start = 257
    _TRACKERPARAM._serialized_end = 336
    _TRANSFORMERPARAM._serialized_start = 338
    _TRANSFORMERPARAM._serialized_end = 421
    _POSTPROCESSORPARAM._serialized_start = 423
    _POSTPROCESSORPARAM._serialized_end = 508
    _FEATUREPARAM._serialized_start = 510
    _FEATUREPARAM._serialized_end = 589
    _DEBUGPARAM._serialized_start = 592
    _DEBUGPARAM._serialized_end = 800
    _LANEPERCEPTIONPARAM._serialized_start = 803
    _LANEPERCEPTIONPARAM._serialized_end = 1062
    _CALIBRATIONSERVICEPARAM._serialized_start = 1064
    _CALIBRATIONSERVICEPARAM._serialized_end = 1181
    _OBJECTTEMPLATEPARAM._serialized_start = 1183
    _OBJECTTEMPLATEPARAM._serialized_end = 1269
    _PERCEPTIONPARAM._serialized_start = 1272
    _PERCEPTIONPARAM._serialized_end = 1995
    _TRAFFICLIGHTPARAM._serialized_start = 1998
    _TRAFFICLIGHTPARAM._serialized_end = 2169