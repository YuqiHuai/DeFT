"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.control.proto import gain_scheduler_conf_pb2 as modules_dot_control_dot_proto_dot_gain__scheduler__conf__pb2
from ....modules.control.proto import leadlag_conf_pb2 as modules_dot_control_dot_proto_dot_leadlag__conf__pb2
from ....modules.control.proto import mrac_conf_pb2 as modules_dot_control_dot_proto_dot_mrac__conf__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/control/proto/lat_controller_conf.proto\x12\x0eapollo.control\x1a/modules/control/proto/gain_scheduler_conf.proto\x1a(modules/control/proto/leadlag_conf.proto\x1a%modules/control/proto/mrac_conf.proto"\xc4\x06\n\x11LatControllerConf\x12\n\n\x02ts\x18\x01 \x01(\x01\x12\x16\n\x0epreview_window\x18\x02 \x01(\x05\x12\n\n\x02cf\x18\x03 \x01(\x01\x12\n\n\x02cr\x18\x04 \x01(\x01\x12\x0f\n\x07mass_fl\x18\x05 \x01(\x05\x12\x0f\n\x07mass_fr\x18\x06 \x01(\x05\x12\x0f\n\x07mass_rl\x18\x07 \x01(\x05\x12\x0f\n\x07mass_rr\x18\x08 \x01(\x05\x12\x0b\n\x03eps\x18\t \x01(\x01\x12\x10\n\x08matrix_q\x18\n \x03(\x01\x12\x18\n\x10reverse_matrix_q\x18\x0b \x03(\x01\x12\x13\n\x0bcutoff_freq\x18\x0c \x01(\x05\x12\x1f\n\x17mean_filter_window_size\x18\r \x01(\x05\x12\x15\n\rmax_iteration\x18\x0e \x01(\x05\x12 \n\x18max_lateral_acceleration\x18\x0f \x01(\x01\x12=\n\x16lat_err_gain_scheduler\x18\x10 \x01(\x0b2\x1d.apollo.control.GainScheduler\x12A\n\x1aheading_err_gain_scheduler\x18\x11 \x01(\x0b2\x1d.apollo.control.GainScheduler\x129\n\x14reverse_leadlag_conf\x18\x12 \x01(\x0b2\x1b.apollo.control.LeadlagConf\x122\n#enable_reverse_leadlag_compensation\x18\x13 \x01(\x08:\x05false\x12-\n\x1eenable_look_ahead_back_control\x18\x14 \x01(\x08:\x05false\x12\x1c\n\x11lookahead_station\x18\x15 \x01(\x01:\x010\x12\x1b\n\x10lookback_station\x18\x16 \x01(\x01:\x010\x121\n\x0fsteer_mrac_conf\x18\x17 \x01(\x0b2\x18.apollo.control.MracConf\x12(\n\x19enable_steer_mrac_control\x18\x18 \x01(\x08:\x05false\x12\'\n\x1clookahead_station_high_speed\x18\x19 \x01(\x01:\x010\x12&\n\x1blookback_station_high_speed\x18\x1a \x01(\x01:\x010')
_LATCONTROLLERCONF = DESCRIPTOR.message_types_by_name['LatControllerConf']
LatControllerConf = _reflection.GeneratedProtocolMessageType('LatControllerConf', (_message.Message,), {'DESCRIPTOR': _LATCONTROLLERCONF, '__module__': 'modules.control.proto.lat_controller_conf_pb2'})
_sym_db.RegisterMessage(LatControllerConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LATCONTROLLERCONF._serialized_start = 198
    _LATCONTROLLERCONF._serialized_end = 1034