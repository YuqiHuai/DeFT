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
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from ....modules.common.proto import vehicle_signal_pb2 as modules_dot_common_dot_proto_dot_vehicle__signal__pb2
from ....modules.control.proto import input_debug_pb2 as modules_dot_control_dot_proto_dot_input__debug__pb2
from ....modules.control.proto import pad_msg_pb2 as modules_dot_control_dot_proto_dot_pad__msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/control/proto/control_cmd.proto\x12\x0eapollo.control\x1a"modules/canbus/proto/chassis.proto\x1a&modules/common/proto/drive_state.proto\x1a!modules/common/proto/header.proto\x1a$modules/common/proto/pnc_point.proto\x1a)modules/common/proto/vehicle_signal.proto\x1a\'modules/control/proto/input_debug.proto\x1a#modules/control/proto/pad_msg.proto"^\n\x0cLatencyStats\x12\x15\n\rtotal_time_ms\x18\x01 \x01(\x01\x12\x1a\n\x12controller_time_ms\x18\x02 \x03(\x01\x12\x1b\n\x13total_time_exceeded\x18\x03 \x01(\x08"\xb7\x06\n\x0eControlCommand\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08throttle\x18\x03 \x01(\x01\x12\r\n\x05brake\x18\x04 \x01(\x01\x12\x15\n\rsteering_rate\x18\x06 \x01(\x01\x12\x17\n\x0fsteering_target\x18\x07 \x01(\x01\x12\x15\n\rparking_brake\x18\x08 \x01(\x08\x12\r\n\x05speed\x18\t \x01(\x01\x12\x14\n\x0cacceleration\x18\n \x01(\x01\x12\x17\n\x0breset_model\x18\x10 \x01(\x08B\x02\x18\x01\x12\x15\n\rengine_on_off\x18\x11 \x01(\x08\x12\x1b\n\x13trajectory_fraction\x18\x12 \x01(\x01\x12<\n\x0cdriving_mode\x18\x13 \x01(\x0e2".apollo.canbus.Chassis.DrivingModeB\x02\x18\x01\x12:\n\rgear_location\x18\x14 \x01(\x0e2#.apollo.canbus.Chassis.GearPosition\x12$\n\x05debug\x18\x16 \x01(\x0b2\x15.apollo.control.Debug\x12,\n\x06signal\x18\x17 \x01(\x0b2\x1c.apollo.common.VehicleSignal\x123\n\rlatency_stats\x18\x18 \x01(\x0b2\x1c.apollo.control.LatencyStats\x12+\n\x07pad_msg\x18\x19 \x01(\x0b2\x1a.apollo.control.PadMessage\x122\n\rengage_advice\x18\x1a \x01(\x0b2\x1b.apollo.common.EngageAdvice\x12\x1e\n\x0fis_in_safe_mode\x18\x1b \x01(\x08:\x05false\x12\x15\n\tleft_turn\x18\r \x01(\x08B\x02\x18\x01\x12\x16\n\nright_turn\x18\x0e \x01(\x08B\x02\x18\x01\x12\x15\n\thigh_beam\x18\x0b \x01(\x08B\x02\x18\x01\x12\x14\n\x08low_beam\x18\x0c \x01(\x08B\x02\x18\x01\x12\x10\n\x04horn\x18\x0f \x01(\x08B\x02\x18\x01\x122\n\nturnsignal\x18\x15 \x01(\x0e2\x1a.apollo.control.TurnSignalB\x02\x18\x01"\xad\x08\n\x17SimpleLongitudinalDebug\x12\x19\n\x11station_reference\x18\x01 \x01(\x01\x12\x15\n\rstation_error\x18\x02 \x01(\x01\x12\x1d\n\x15station_error_limited\x18\x03 \x01(\x01\x12\x1d\n\x15preview_station_error\x18\x04 \x01(\x01\x12\x17\n\x0fspeed_reference\x18\x05 \x01(\x01\x12\x13\n\x0bspeed_error\x18\x06 \x01(\x01\x12&\n\x1espeed_controller_input_limited\x18\x07 \x01(\x01\x12\x1f\n\x17preview_speed_reference\x18\x08 \x01(\x01\x12\x1b\n\x13preview_speed_error\x18\t \x01(\x01\x12&\n\x1epreview_acceleration_reference\x18\n \x01(\x01\x12"\n\x1aacceleration_cmd_closeloop\x18\x0b \x01(\x01\x12\x18\n\x10acceleration_cmd\x18\x0c \x01(\x01\x12\x1b\n\x13acceleration_lookup\x18\r \x01(\x01\x12\x14\n\x0cspeed_lookup\x18\x0e \x01(\x01\x12\x19\n\x11calibration_value\x18\x0f \x01(\x01\x12\x14\n\x0cthrottle_cmd\x18\x10 \x01(\x01\x12\x11\n\tbrake_cmd\x18\x11 \x01(\x01\x12\x14\n\x0cis_full_stop\x18\x12 \x01(\x08\x12!\n\x19slope_offset_compensation\x18\x13 \x01(\x01\x12\x17\n\x0fcurrent_station\x18\x14 \x01(\x01\x12\x13\n\x0bpath_remain\x18\x15 \x01(\x01\x12\x1d\n\x15pid_saturation_status\x18\x16 \x01(\x05\x12!\n\x19leadlag_saturation_status\x18\x17 \x01(\x05\x12\x14\n\x0cspeed_offset\x18\x18 \x01(\x01\x12\x15\n\rcurrent_speed\x18\x19 \x01(\x01\x12\x1e\n\x16acceleration_reference\x18\x1a \x01(\x01\x12\x1c\n\x14current_acceleration\x18\x1b \x01(\x01\x12\x1a\n\x12acceleration_error\x18\x1c \x01(\x01\x12\x16\n\x0ejerk_reference\x18\x1d \x01(\x01\x12\x14\n\x0ccurrent_jerk\x18\x1e \x01(\x01\x12\x12\n\njerk_error\x18\x1f \x01(\x01\x12=\n\x15current_matched_point\x18  \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12?\n\x17current_reference_point\x18! \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12?\n\x17preview_reference_point\x18" \x01(\x0b2\x1e.apollo.common.TrajectoryPoint"\x93\x08\n\x12SimpleLateralDebug\x12\x15\n\rlateral_error\x18\x01 \x01(\x01\x12\x13\n\x0bref_heading\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\x15\n\rheading_error\x18\x04 \x01(\x01\x12\x1a\n\x12heading_error_rate\x18\x05 \x01(\x01\x12\x1a\n\x12lateral_error_rate\x18\x06 \x01(\x01\x12\x11\n\tcurvature\x18\x07 \x01(\x01\x12\x13\n\x0bsteer_angle\x18\x08 \x01(\x01\x12\x1f\n\x17steer_angle_feedforward\x18\t \x01(\x01\x12(\n steer_angle_lateral_contribution\x18\n \x01(\x01\x12-\n%steer_angle_lateral_rate_contribution\x18\x0b \x01(\x01\x12(\n steer_angle_heading_contribution\x18\x0c \x01(\x01\x12-\n%steer_angle_heading_rate_contribution\x18\r \x01(\x01\x12\x1c\n\x14steer_angle_feedback\x18\x0e \x01(\x01\x12\x19\n\x11steering_position\x18\x0f \x01(\x01\x12\x11\n\tref_speed\x18\x10 \x01(\x01\x12\x1b\n\x13steer_angle_limited\x18\x11 \x01(\x01\x12\x1c\n\x14lateral_acceleration\x18\x12 \x01(\x01\x12\x14\n\x0clateral_jerk\x18\x13 \x01(\x01\x12\x18\n\x10ref_heading_rate\x18\x14 \x01(\x01\x12\x14\n\x0cheading_rate\x18\x15 \x01(\x01\x12 \n\x18ref_heading_acceleration\x18\x16 \x01(\x01\x12\x1c\n\x14heading_acceleration\x18\x17 \x01(\x01\x12"\n\x1aheading_error_acceleration\x18\x18 \x01(\x01\x12\x18\n\x10ref_heading_jerk\x18\x19 \x01(\x01\x12\x14\n\x0cheading_jerk\x18\x1a \x01(\x01\x12\x1a\n\x12heading_error_jerk\x18\x1b \x01(\x01\x12\x1e\n\x16lateral_error_feedback\x18\x1c \x01(\x01\x12\x1e\n\x16heading_error_feedback\x18\x1d \x01(\x01\x12<\n\x14current_target_point\x18\x1e \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12$\n\x1csteer_angle_feedback_augment\x18\x1f \x01(\x01\x123\n\x10steer_mrac_debug\x18  \x01(\x0b2\x19.apollo.control.MracDebug\x12 \n\x18steer_mrac_enable_status\x18! \x01(\x08"\xf2\n\n\x0eSimpleMPCDebug\x12\x15\n\rlateral_error\x18\x01 \x01(\x01\x12\x13\n\x0bref_heading\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\x15\n\rheading_error\x18\x04 \x01(\x01\x12\x1a\n\x12heading_error_rate\x18\x05 \x01(\x01\x12\x1a\n\x12lateral_error_rate\x18\x06 \x01(\x01\x12\x11\n\tcurvature\x18\x07 \x01(\x01\x12\x13\n\x0bsteer_angle\x18\x08 \x01(\x01\x12\x1f\n\x17steer_angle_feedforward\x18\t \x01(\x01\x12(\n steer_angle_lateral_contribution\x18\n \x01(\x01\x12-\n%steer_angle_lateral_rate_contribution\x18\x0b \x01(\x01\x12(\n steer_angle_heading_contribution\x18\x0c \x01(\x01\x12-\n%steer_angle_heading_rate_contribution\x18\r \x01(\x01\x12\x1c\n\x14steer_angle_feedback\x18\x0e \x01(\x01\x12\x19\n\x11steering_position\x18\x0f \x01(\x01\x12\x11\n\tref_speed\x18\x10 \x01(\x01\x12\x1b\n\x13steer_angle_limited\x18\x11 \x01(\x01\x12\x19\n\x11station_reference\x18\x12 \x01(\x01\x12\x15\n\rstation_error\x18\x13 \x01(\x01\x12\x17\n\x0fspeed_reference\x18\x14 \x01(\x01\x12\x13\n\x0bspeed_error\x18\x15 \x01(\x01\x12\x1e\n\x16acceleration_reference\x18\x16 \x01(\x01\x12\x14\n\x0cis_full_stop\x18\x17 \x01(\x08\x12\x18\n\x10station_feedback\x18\x18 \x01(\x01\x12\x16\n\x0espeed_feedback\x18\x19 \x01(\x01\x12"\n\x1aacceleration_cmd_closeloop\x18\x1a \x01(\x01\x12\x18\n\x10acceleration_cmd\x18\x1b \x01(\x01\x12\x1b\n\x13acceleration_lookup\x18\x1c \x01(\x01\x12\x14\n\x0cspeed_lookup\x18\x1d \x01(\x01\x12\x19\n\x11calibration_value\x18\x1e \x01(\x01\x12(\n steer_unconstrained_control_diff\x18\x1f \x01(\x01\x12,\n$steer_angle_feedforward_compensation\x18  \x01(\x01\x12\x18\n\x10matrix_q_updated\x18! \x03(\x01\x12\x18\n\x10matrix_r_updated\x18" \x03(\x01\x12\x1c\n\x14lateral_acceleration\x18# \x01(\x01\x12\x14\n\x0clateral_jerk\x18$ \x01(\x01\x12\x18\n\x10ref_heading_rate\x18% \x01(\x01\x12\x14\n\x0cheading_rate\x18& \x01(\x01\x12 \n\x18ref_heading_acceleration\x18\' \x01(\x01\x12\x1c\n\x14heading_acceleration\x18( \x01(\x01\x12"\n\x1aheading_error_acceleration\x18) \x01(\x01\x12\x18\n\x10ref_heading_jerk\x18* \x01(\x01\x12\x14\n\x0cheading_jerk\x18+ \x01(\x01\x12\x1a\n\x12heading_error_jerk\x18, \x01(\x01\x12\x1d\n\x15acceleration_feedback\x18- \x01(\x01\x12\x1a\n\x12acceleration_error\x18. \x01(\x01\x12\x16\n\x0ejerk_reference\x18/ \x01(\x01\x12\x15\n\rjerk_feedback\x180 \x01(\x01\x12\x12\n\njerk_error\x181 \x01(\x01"\xed\x01\n\tMracDebug\x12\x18\n\x10mrac_model_order\x18\x01 \x01(\x05\x12\x1c\n\x14mrac_reference_state\x18\x02 \x03(\x01\x12\x18\n\x10mrac_state_error\x18\x03 \x03(\x01\x12<\n\x12mrac_adaptive_gain\x18\x04 \x01(\x0b2 .apollo.control.MracAdaptiveGain\x12(\n mrac_reference_saturation_status\x18\x05 \x01(\x05\x12&\n\x1emrac_control_saturation_status\x18\x06 \x01(\x05"m\n\x10MracAdaptiveGain\x12\x1b\n\x13state_adaptive_gain\x18\x01 \x03(\x01\x12\x1b\n\x13input_adaptive_gain\x18\x02 \x03(\x01\x12\x1f\n\x17nonlinear_adaptive_gain\x18\x03 \x03(\x01"\xf3\x01\n\x05Debug\x12A\n\x10simple_lon_debug\x18\x01 \x01(\x0b2\'.apollo.control.SimpleLongitudinalDebug\x12<\n\x10simple_lat_debug\x18\x02 \x01(\x0b2".apollo.control.SimpleLateralDebug\x12/\n\x0binput_debug\x18\x03 \x01(\x0b2\x1a.apollo.control.InputDebug\x128\n\x10simple_mpc_debug\x18\x04 \x01(\x0b2\x1e.apollo.control.SimpleMPCDebug*:\n\nTurnSignal\x12\r\n\tTURN_NONE\x10\x00\x12\r\n\tTURN_LEFT\x10\x01\x12\x0e\n\nTURN_RIGHT\x10\x02')
_TURNSIGNAL = DESCRIPTOR.enum_types_by_name['TurnSignal']
TurnSignal = enum_type_wrapper.EnumTypeWrapper(_TURNSIGNAL)
TURN_NONE = 0
TURN_LEFT = 1
TURN_RIGHT = 2
_LATENCYSTATS = DESCRIPTOR.message_types_by_name['LatencyStats']
_CONTROLCOMMAND = DESCRIPTOR.message_types_by_name['ControlCommand']
_SIMPLELONGITUDINALDEBUG = DESCRIPTOR.message_types_by_name['SimpleLongitudinalDebug']
_SIMPLELATERALDEBUG = DESCRIPTOR.message_types_by_name['SimpleLateralDebug']
_SIMPLEMPCDEBUG = DESCRIPTOR.message_types_by_name['SimpleMPCDebug']
_MRACDEBUG = DESCRIPTOR.message_types_by_name['MracDebug']
_MRACADAPTIVEGAIN = DESCRIPTOR.message_types_by_name['MracAdaptiveGain']
_DEBUG = DESCRIPTOR.message_types_by_name['Debug']
LatencyStats = _reflection.GeneratedProtocolMessageType('LatencyStats', (_message.Message,), {'DESCRIPTOR': _LATENCYSTATS, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(LatencyStats)
ControlCommand = _reflection.GeneratedProtocolMessageType('ControlCommand', (_message.Message,), {'DESCRIPTOR': _CONTROLCOMMAND, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(ControlCommand)
SimpleLongitudinalDebug = _reflection.GeneratedProtocolMessageType('SimpleLongitudinalDebug', (_message.Message,), {'DESCRIPTOR': _SIMPLELONGITUDINALDEBUG, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(SimpleLongitudinalDebug)
SimpleLateralDebug = _reflection.GeneratedProtocolMessageType('SimpleLateralDebug', (_message.Message,), {'DESCRIPTOR': _SIMPLELATERALDEBUG, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(SimpleLateralDebug)
SimpleMPCDebug = _reflection.GeneratedProtocolMessageType('SimpleMPCDebug', (_message.Message,), {'DESCRIPTOR': _SIMPLEMPCDEBUG, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(SimpleMPCDebug)
MracDebug = _reflection.GeneratedProtocolMessageType('MracDebug', (_message.Message,), {'DESCRIPTOR': _MRACDEBUG, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(MracDebug)
MracAdaptiveGain = _reflection.GeneratedProtocolMessageType('MracAdaptiveGain', (_message.Message,), {'DESCRIPTOR': _MRACADAPTIVEGAIN, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(MracAdaptiveGain)
Debug = _reflection.GeneratedProtocolMessageType('Debug', (_message.Message,), {'DESCRIPTOR': _DEBUG, '__module__': 'modules.control.proto.control_cmd_pb2'})
_sym_db.RegisterMessage(Debug)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONTROLCOMMAND.fields_by_name['reset_model']._options = None
    _CONTROLCOMMAND.fields_by_name['reset_model']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['driving_mode']._options = None
    _CONTROLCOMMAND.fields_by_name['driving_mode']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['left_turn']._options = None
    _CONTROLCOMMAND.fields_by_name['left_turn']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['right_turn']._options = None
    _CONTROLCOMMAND.fields_by_name['right_turn']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['high_beam']._options = None
    _CONTROLCOMMAND.fields_by_name['high_beam']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['low_beam']._options = None
    _CONTROLCOMMAND.fields_by_name['low_beam']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['horn']._options = None
    _CONTROLCOMMAND.fields_by_name['horn']._serialized_options = b'\x18\x01'
    _CONTROLCOMMAND.fields_by_name['turnsignal']._options = None
    _CONTROLCOMMAND.fields_by_name['turnsignal']._serialized_options = b'\x18\x01'
    _TURNSIGNAL._serialized_start = 5363
    _TURNSIGNAL._serialized_end = 5421
    _LATENCYSTATS._serialized_start = 329
    _LATENCYSTATS._serialized_end = 423
    _CONTROLCOMMAND._serialized_start = 426
    _CONTROLCOMMAND._serialized_end = 1249
    _SIMPLELONGITUDINALDEBUG._serialized_start = 1252
    _SIMPLELONGITUDINALDEBUG._serialized_end = 2321
    _SIMPLELATERALDEBUG._serialized_start = 2324
    _SIMPLELATERALDEBUG._serialized_end = 3367
    _SIMPLEMPCDEBUG._serialized_start = 3370
    _SIMPLEMPCDEBUG._serialized_end = 4764
    _MRACDEBUG._serialized_start = 4767
    _MRACDEBUG._serialized_end = 5004
    _MRACADAPTIVEGAIN._serialized_start = 5006
    _MRACADAPTIVEGAIN._serialized_end = 5115
    _DEBUG._serialized_start = 5118
    _DEBUG._serialized_end = 5361