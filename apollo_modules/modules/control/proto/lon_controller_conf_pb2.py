"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.control.proto import calibration_table_pb2 as modules_dot_control_dot_proto_dot_calibration__table__pb2
from ....modules.control.proto import leadlag_conf_pb2 as modules_dot_control_dot_proto_dot_leadlag__conf__pb2
from ....modules.control.proto import pid_conf_pb2 as modules_dot_control_dot_proto_dot_pid__conf__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/control/proto/lon_controller_conf.proto\x12\x0eapollo.control\x1a-modules/control/proto/calibration_table.proto\x1a(modules/control/proto/leadlag_conf.proto\x1a$modules/control/proto/pid_conf.proto"!\n\nFilterConf\x12\x13\n\x0bcutoff_freq\x18\x01 \x01(\x05"\xec\x06\n\x11LonControllerConf\x12\n\n\x02ts\x18\x01 \x01(\x01\x12\x1c\n\x14brake_minimum_action\x18\x02 \x01(\x01\x12\x1f\n\x17throttle_minimum_action\x18\x03 \x01(\x01\x12$\n\x1cspeed_controller_input_limit\x18\x04 \x01(\x01\x12\x1b\n\x13station_error_limit\x18\x05 \x01(\x01\x12\x16\n\x0epreview_window\x18\x06 \x01(\x01\x12\x1f\n\x17standstill_acceleration\x18\x07 \x01(\x01\x121\n\x10station_pid_conf\x18\x08 \x01(\x0b2\x17.apollo.control.PidConf\x123\n\x12low_speed_pid_conf\x18\t \x01(\x0b2\x17.apollo.control.PidConf\x124\n\x13high_speed_pid_conf\x18\n \x01(\x0b2\x17.apollo.control.PidConf\x12\x14\n\x0cswitch_speed\x18\x0b \x01(\x01\x129\n\x18reverse_station_pid_conf\x18\x0c \x01(\x0b2\x17.apollo.control.PidConf\x127\n\x16reverse_speed_pid_conf\x18\r \x01(\x0b2\x17.apollo.control.PidConf\x12;\n\x17pitch_angle_filter_conf\x18\x0e \x01(\x0b2\x1a.apollo.control.FilterConf\x12A\n\x1creverse_station_leadlag_conf\x18\x0f \x01(\x0b2\x1b.apollo.control.LeadlagConf\x12?\n\x1areverse_speed_leadlag_conf\x18\x10 \x01(\x0b2\x1b.apollo.control.LeadlagConf\x12S\n\x11calibration_table\x18\x11 \x01(\x0b28.apollo.control.calibrationtable.ControlCalibrationTable\x122\n#enable_reverse_leadlag_compensation\x18\x12 \x01(\x08:\x05false\x12\x1e\n\x13switch_speed_window\x18\x13 \x01(\x01:\x010')
_FILTERCONF = DESCRIPTOR.message_types_by_name['FilterConf']
_LONCONTROLLERCONF = DESCRIPTOR.message_types_by_name['LonControllerConf']
FilterConf = _reflection.GeneratedProtocolMessageType('FilterConf', (_message.Message,), {'DESCRIPTOR': _FILTERCONF, '__module__': 'modules.control.proto.lon_controller_conf_pb2'})
_sym_db.RegisterMessage(FilterConf)
LonControllerConf = _reflection.GeneratedProtocolMessageType('LonControllerConf', (_message.Message,), {'DESCRIPTOR': _LONCONTROLLERCONF, '__module__': 'modules.control.proto.lon_controller_conf_pb2'})
_sym_db.RegisterMessage(LonControllerConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FILTERCONF._serialized_start = 194
    _FILTERCONF._serialized_end = 227
    _LONCONTROLLERCONF._serialized_start = 230
    _LONCONTROLLERCONF._serialized_end = 1106