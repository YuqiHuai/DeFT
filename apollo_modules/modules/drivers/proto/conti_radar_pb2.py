"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.drivers.radar.conti_radar.proto import conti_radar_conf_pb2 as modules_dot_drivers_dot_radar_dot_conti__radar_dot_proto_dot_conti__radar__conf__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/drivers/proto/conti_radar.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto\x1a>modules/drivers/radar/conti_radar/proto/conti_radar_conf.proto"m\n\x15ClusterListStatus_600\x12\x0f\n\x04near\x18\x01 \x01(\x05:\x010\x12\x0e\n\x03far\x18\x02 \x01(\x05:\x010\x12\x18\n\x0cmeas_counter\x18\x03 \x01(\x05:\x02-1\x12\x19\n\x11interface_version\x18\x04 \x01(\x05"c\n\x14ObjectListStatus_60A\x12\x16\n\x0bnof_objects\x18\x01 \x01(\x05:\x010\x12\x18\n\x0cmeas_counter\x18\x02 \x01(\x05:\x02-1\x12\x19\n\x11interface_version\x18\x03 \x01(\x05"\xe6\x01\n\x0eRadarState_201\x12\x14\n\x0cmax_distance\x18\x01 \x01(\r\x12\x13\n\x0bradar_power\x18\x02 \x01(\r\x12;\n\x0boutput_type\x18\x03 \x01(\x0e2&.apollo.drivers.conti_radar.OutputType\x12?\n\rrcs_threshold\x18\x04 \x01(\x0e2(.apollo.drivers.conti_radar.RcsThreshold\x12\x14\n\x0csend_quality\x18\x05 \x01(\x08\x12\x15\n\rsend_ext_info\x18\x06 \x01(\x08"\xc1\x04\n\rContiRadarObs\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x16\n\x0eclusterortrack\x18\x02 \x01(\x08\x12\x13\n\x0bobstacle_id\x18\x03 \x01(\x05\x12\x16\n\x0elongitude_dist\x18\x04 \x01(\x01\x12\x14\n\x0clateral_dist\x18\x05 \x01(\x01\x12\x15\n\rlongitude_vel\x18\x06 \x01(\x01\x12\x13\n\x0blateral_vel\x18\x07 \x01(\x01\x12\x0b\n\x03rcs\x18\x08 \x01(\x01\x12\x0f\n\x07dynprop\x18\t \x01(\x05\x12\x1a\n\x12longitude_dist_rms\x18\n \x01(\x01\x12\x18\n\x10lateral_dist_rms\x18\x0b \x01(\x01\x12\x19\n\x11longitude_vel_rms\x18\x0c \x01(\x01\x12\x17\n\x0flateral_vel_rms\x18\r \x01(\x01\x12\x11\n\tprobexist\x18\x0e \x01(\x01\x12\x12\n\nmeas_state\x18\x0f \x01(\x05\x12\x17\n\x0flongitude_accel\x18\x10 \x01(\x01\x12\x15\n\rlateral_accel\x18\x11 \x01(\x01\x12\x17\n\x0foritation_angle\x18\x12 \x01(\x01\x12\x1b\n\x13longitude_accel_rms\x18\x13 \x01(\x01\x12\x19\n\x11lateral_accel_rms\x18\x14 \x01(\x01\x12\x1b\n\x13oritation_angle_rms\x18\x15 \x01(\x01\x12\x0e\n\x06length\x18\x16 \x01(\x01\x12\r\n\x05width\x18\x17 \x01(\x01\x12\x16\n\x0eobstacle_class\x18\x18 \x01(\x05"\x9f\x02\n\nContiRadar\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12/\n\x08contiobs\x18\x02 \x03(\x0b2\x1d.apollo.drivers.ContiRadarObs\x123\n\x0bradar_state\x18\x03 \x01(\x0b2\x1e.apollo.drivers.RadarState_201\x12B\n\x13cluster_list_status\x18\x04 \x01(\x0b2%.apollo.drivers.ClusterListStatus_600\x12@\n\x12object_list_status\x18\x05 \x01(\x0b2$.apollo.drivers.ObjectListStatus_60A')
_CLUSTERLISTSTATUS_600 = DESCRIPTOR.message_types_by_name['ClusterListStatus_600']
_OBJECTLISTSTATUS_60A = DESCRIPTOR.message_types_by_name['ObjectListStatus_60A']
_RADARSTATE_201 = DESCRIPTOR.message_types_by_name['RadarState_201']
_CONTIRADAROBS = DESCRIPTOR.message_types_by_name['ContiRadarObs']
_CONTIRADAR = DESCRIPTOR.message_types_by_name['ContiRadar']
ClusterListStatus_600 = _reflection.GeneratedProtocolMessageType('ClusterListStatus_600', (_message.Message,), {'DESCRIPTOR': _CLUSTERLISTSTATUS_600, '__module__': 'modules.drivers.proto.conti_radar_pb2'})
_sym_db.RegisterMessage(ClusterListStatus_600)
ObjectListStatus_60A = _reflection.GeneratedProtocolMessageType('ObjectListStatus_60A', (_message.Message,), {'DESCRIPTOR': _OBJECTLISTSTATUS_60A, '__module__': 'modules.drivers.proto.conti_radar_pb2'})
_sym_db.RegisterMessage(ObjectListStatus_60A)
RadarState_201 = _reflection.GeneratedProtocolMessageType('RadarState_201', (_message.Message,), {'DESCRIPTOR': _RADARSTATE_201, '__module__': 'modules.drivers.proto.conti_radar_pb2'})
_sym_db.RegisterMessage(RadarState_201)
ContiRadarObs = _reflection.GeneratedProtocolMessageType('ContiRadarObs', (_message.Message,), {'DESCRIPTOR': _CONTIRADAROBS, '__module__': 'modules.drivers.proto.conti_radar_pb2'})
_sym_db.RegisterMessage(ContiRadarObs)
ContiRadar = _reflection.GeneratedProtocolMessageType('ContiRadar', (_message.Message,), {'DESCRIPTOR': _CONTIRADAR, '__module__': 'modules.drivers.proto.conti_radar_pb2'})
_sym_db.RegisterMessage(ContiRadar)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CLUSTERLISTSTATUS_600._serialized_start = 158
    _CLUSTERLISTSTATUS_600._serialized_end = 267
    _OBJECTLISTSTATUS_60A._serialized_start = 269
    _OBJECTLISTSTATUS_60A._serialized_end = 368
    _RADARSTATE_201._serialized_start = 371
    _RADARSTATE_201._serialized_end = 601
    _CONTIRADAROBS._serialized_start = 604
    _CONTIRADAROBS._serialized_end = 1181
    _CONTIRADAR._serialized_start = 1184
    _CONTIRADAR._serialized_end = 1471