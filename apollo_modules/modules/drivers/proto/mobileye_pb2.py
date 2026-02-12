"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/drivers/proto/mobileye.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto"\xa3\x01\n\x07Lka_768\x12\x11\n\tlane_type\x18\x01 \x01(\x05\x12\x0f\n\x07quality\x18\x02 \x01(\x05\x12\x14\n\x0cmodel_degree\x18\x03 \x01(\x05\x12\x10\n\x08position\x18\x04 \x01(\x01\x12\x11\n\tcurvature\x18\x05 \x01(\x01\x12\x1c\n\x14curvature_derivative\x18\x06 \x01(\x01\x12\x1b\n\x13width_right_marking\x18\x07 \x01(\x01"1\n\x07Num_76b\x12&\n\x1enum_of_next_lane_mark_reported\x18\x01 \x01(\x05"\xea\x01\n\x0fAftermarket_669\x12\x16\n\x0elane_conf_left\x18\x01 \x01(\x05\x12\x1d\n\x15ldw_availability_left\x18\x02 \x01(\x08\x12\x16\n\x0elane_type_left\x18\x03 \x01(\x05\x12\x1a\n\x12distance_to_lane_l\x18\x04 \x01(\x01\x12\x17\n\x0flane_conf_right\x18\x05 \x01(\x05\x12\x1e\n\x16ldw_availability_right\x18\x06 \x01(\x08\x12\x17\n\x0flane_type_right\x18\x07 \x01(\x05\x12\x1a\n\x12distance_to_lane_r\x18\x08 \x01(\x01"U\n\x07Lka_769\x12\x15\n\rheading_angle\x18\x01 \x01(\x01\x12\x12\n\nview_range\x18\x02 \x01(\x01\x12\x1f\n\x17view_range_availability\x18\x03 \x01(\x08"\xc3\x01\n\rReference_76a\x12\x1c\n\x14ref_point_1_position\x18\x01 \x01(\x01\x12\x1c\n\x14ref_point_1_distance\x18\x02 \x01(\x01\x12\x1c\n\x14ref_point_1_validity\x18\x03 \x01(\x08\x12\x1c\n\x14ref_point_2_position\x18\x04 \x01(\x01\x12\x1c\n\x14ref_point_2_distance\x18\x05 \x01(\x01\x12\x1c\n\x14ref_point_2_validity\x18\x06 \x01(\x08"\x9c\x02\n\x0bDetails_738\x12\x15\n\rnum_obstacles\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x05\x12\x1b\n\x13application_version\x18\x03 \x01(\x05\x12%\n\x1dactive_version_number_section\x18\x04 \x01(\x05\x12\x1e\n\x16left_close_rang_cut_in\x18\x05 \x01(\x08\x12\x1f\n\x17right_close_rang_cut_in\x18\x06 \x01(\x08\x12\n\n\x02go\x18\x07 \x01(\x05\x12\x18\n\x10protocol_version\x18\x08 \x01(\x05\x12\x11\n\tclose_car\x18\t \x01(\x08\x12\x10\n\x08failsafe\x18\n \x01(\x05\x12\x13\n\x0breserved_10\x18\x0b \x01(\x05"\xa0\x01\n\x08Next_76c\x12\x11\n\tlane_type\x18\x01 \x01(\x05\x12\x0f\n\x07quality\x18\x02 \x01(\x05\x12\x14\n\x0cmodel_degree\x18\x03 \x01(\x05\x12\x10\n\x08position\x18\x04 \x01(\x01\x12\x11\n\tcurvature\x18\x05 \x01(\x01\x12\x1c\n\x14curvature_derivative\x18\x06 \x01(\x01\x12\x17\n\x0flane_mark_width\x18\x07 \x01(\x01"\xd4\x01\n\x0bDetails_737\x12\x16\n\x0elane_curvature\x18\x01 \x01(\x01\x12\x14\n\x0clane_heading\x18\x02 \x01(\x01\x12\x1c\n\x14ca_construction_area\x18\x03 \x01(\x08\x12\x1e\n\x16right_ldw_availability\x18\x04 \x01(\x08\x12\x1d\n\x15left_ldw_availability\x18\x05 \x01(\x08\x12\x12\n\nreserved_1\x18\x06 \x01(\x08\x12\x11\n\tyaw_angle\x18\x07 \x01(\x01\x12\x13\n\x0bpitch_angle\x18\x08 \x01(\x01"U\n\x07Lka_767\x12\x15\n\rheading_angle\x18\x01 \x01(\x01\x12\x12\n\nview_range\x18\x02 \x01(\x01\x12\x1f\n\x17view_range_availability\x18\x03 \x01(\x08"\xa2\x01\n\x07Lka_766\x12\x11\n\tlane_type\x18\x01 \x01(\x05\x12\x0f\n\x07quality\x18\x02 \x01(\x05\x12\x14\n\x0cmodel_degree\x18\x03 \x01(\x05\x12\x10\n\x08position\x18\x04 \x01(\x01\x12\x11\n\tcurvature\x18\x05 \x01(\x01\x12\x1c\n\x14curvature_derivative\x18\x06 \x01(\x01\x12\x1a\n\x12width_left_marking\x18\x07 \x01(\x01"V\n\x08Next_76d\x12\x15\n\rheading_angle\x18\x01 \x01(\x01\x12\x12\n\nview_range\x18\x02 \x01(\x01\x12\x1f\n\x17view_range_availability\x18\x03 \x01(\x08"\xbe\x02\n\x0bDetails_739\x12\x13\n\x0bobstacle_id\x18\x01 \x01(\x05\x12\x16\n\x0eobstacle_pos_x\x18\x02 \x01(\x01\x12\x11\n\treseved_2\x18\x03 \x01(\x05\x12\x16\n\x0eobstacle_pos_y\x18\x04 \x01(\x01\x12\x14\n\x0cblinker_info\x18\x05 \x01(\x05\x12\x16\n\x0ecut_in_and_out\x18\x06 \x01(\x05\x12\x1a\n\x12obstacle_rel_vel_x\x18\x07 \x01(\x01\x12\x15\n\robstacle_type\x18\x08 \x01(\x05\x12\x12\n\nreserved_3\x18\t \x01(\x08\x12\x17\n\x0fobstacle_status\x18\n \x01(\x05\x12\x1d\n\x15obstacle_brake_lights\x18\x0b \x01(\x08\x12\x12\n\nreserved_4\x18\x0c \x01(\x05\x12\x16\n\x0eobstacle_valid\x18\r \x01(\x05"\x9e\x02\n\x0bDetails_73a\x12\x17\n\x0fobstacle_length\x18\x01 \x01(\x01\x12\x16\n\x0eobstacle_width\x18\x02 \x01(\x01\x12\x14\n\x0cobstacle_age\x18\x03 \x01(\x05\x12\x15\n\robstacle_lane\x18\x04 \x01(\x05\x12\x11\n\tcipv_flag\x18\x05 \x01(\x08\x12\x12\n\nreserved_5\x18\x06 \x01(\x08\x12\x13\n\x0bradar_pos_x\x18\x07 \x01(\x01\x12\x13\n\x0bradar_vel_x\x18\x08 \x01(\x01\x12\x1e\n\x16radar_match_confidence\x18\t \x01(\x05\x12\x12\n\nreserved_6\x18\n \x01(\x08\x12\x18\n\x10matched_radar_id\x18\x0b \x01(\x05\x12\x12\n\nreserved_7\x18\x0c \x01(\x08"\xbc\x01\n\x0bDetails_73b\x12\x1b\n\x13obstacle_angle_rate\x18\x01 \x01(\x01\x12\x1d\n\x15obstacle_scale_change\x18\x02 \x01(\x01\x12\x16\n\x0eobject_accel_x\x18\x03 \x01(\x01\x12\x12\n\nreserved_8\x18\x04 \x01(\x05\x12\x19\n\x11obstacle_replaced\x18\x05 \x01(\x08\x12\x12\n\nreserved_9\x18\x06 \x01(\x05\x12\x16\n\x0eobstacle_angle\x18\x07 \x01(\x01"\xc5\x05\n\x08Mobileye\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x128\n\x0faftermarket_669\x18\x02 \x01(\x0b2\x1f.apollo.drivers.Aftermarket_669\x120\n\x0bdetails_737\x18\x03 \x01(\x0b2\x1b.apollo.drivers.Details_737\x120\n\x0bdetails_738\x18\x04 \x01(\x0b2\x1b.apollo.drivers.Details_738\x120\n\x0bdetails_739\x18\x05 \x03(\x0b2\x1b.apollo.drivers.Details_739\x120\n\x0bdetails_73a\x18\x06 \x03(\x0b2\x1b.apollo.drivers.Details_73a\x120\n\x0bdetails_73b\x18\x07 \x03(\x0b2\x1b.apollo.drivers.Details_73b\x12(\n\x07lka_766\x18\x08 \x01(\x0b2\x17.apollo.drivers.Lka_766\x12(\n\x07lka_767\x18\t \x01(\x0b2\x17.apollo.drivers.Lka_767\x12(\n\x07lka_768\x18\n \x01(\x0b2\x17.apollo.drivers.Lka_768\x12(\n\x07lka_769\x18\x0b \x01(\x0b2\x17.apollo.drivers.Lka_769\x124\n\rreference_76a\x18\x0c \x01(\x0b2\x1d.apollo.drivers.Reference_76a\x12(\n\x07num_76b\x18\r \x01(\x0b2\x17.apollo.drivers.Num_76b\x12*\n\x08next_76c\x18\x0e \x03(\x0b2\x18.apollo.drivers.Next_76c\x12*\n\x08next_76d\x18\x0f \x03(\x0b2\x18.apollo.drivers.Next_76d')
_LKA_768 = DESCRIPTOR.message_types_by_name['Lka_768']
_NUM_76B = DESCRIPTOR.message_types_by_name['Num_76b']
_AFTERMARKET_669 = DESCRIPTOR.message_types_by_name['Aftermarket_669']
_LKA_769 = DESCRIPTOR.message_types_by_name['Lka_769']
_REFERENCE_76A = DESCRIPTOR.message_types_by_name['Reference_76a']
_DETAILS_738 = DESCRIPTOR.message_types_by_name['Details_738']
_NEXT_76C = DESCRIPTOR.message_types_by_name['Next_76c']
_DETAILS_737 = DESCRIPTOR.message_types_by_name['Details_737']
_LKA_767 = DESCRIPTOR.message_types_by_name['Lka_767']
_LKA_766 = DESCRIPTOR.message_types_by_name['Lka_766']
_NEXT_76D = DESCRIPTOR.message_types_by_name['Next_76d']
_DETAILS_739 = DESCRIPTOR.message_types_by_name['Details_739']
_DETAILS_73A = DESCRIPTOR.message_types_by_name['Details_73a']
_DETAILS_73B = DESCRIPTOR.message_types_by_name['Details_73b']
_MOBILEYE = DESCRIPTOR.message_types_by_name['Mobileye']
Lka_768 = _reflection.GeneratedProtocolMessageType('Lka_768', (_message.Message,), {'DESCRIPTOR': _LKA_768, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Lka_768)
Num_76b = _reflection.GeneratedProtocolMessageType('Num_76b', (_message.Message,), {'DESCRIPTOR': _NUM_76B, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Num_76b)
Aftermarket_669 = _reflection.GeneratedProtocolMessageType('Aftermarket_669', (_message.Message,), {'DESCRIPTOR': _AFTERMARKET_669, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Aftermarket_669)
Lka_769 = _reflection.GeneratedProtocolMessageType('Lka_769', (_message.Message,), {'DESCRIPTOR': _LKA_769, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Lka_769)
Reference_76a = _reflection.GeneratedProtocolMessageType('Reference_76a', (_message.Message,), {'DESCRIPTOR': _REFERENCE_76A, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Reference_76a)
Details_738 = _reflection.GeneratedProtocolMessageType('Details_738', (_message.Message,), {'DESCRIPTOR': _DETAILS_738, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Details_738)
Next_76c = _reflection.GeneratedProtocolMessageType('Next_76c', (_message.Message,), {'DESCRIPTOR': _NEXT_76C, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Next_76c)
Details_737 = _reflection.GeneratedProtocolMessageType('Details_737', (_message.Message,), {'DESCRIPTOR': _DETAILS_737, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Details_737)
Lka_767 = _reflection.GeneratedProtocolMessageType('Lka_767', (_message.Message,), {'DESCRIPTOR': _LKA_767, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Lka_767)
Lka_766 = _reflection.GeneratedProtocolMessageType('Lka_766', (_message.Message,), {'DESCRIPTOR': _LKA_766, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Lka_766)
Next_76d = _reflection.GeneratedProtocolMessageType('Next_76d', (_message.Message,), {'DESCRIPTOR': _NEXT_76D, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Next_76d)
Details_739 = _reflection.GeneratedProtocolMessageType('Details_739', (_message.Message,), {'DESCRIPTOR': _DETAILS_739, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Details_739)
Details_73a = _reflection.GeneratedProtocolMessageType('Details_73a', (_message.Message,), {'DESCRIPTOR': _DETAILS_73A, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Details_73a)
Details_73b = _reflection.GeneratedProtocolMessageType('Details_73b', (_message.Message,), {'DESCRIPTOR': _DETAILS_73B, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Details_73b)
Mobileye = _reflection.GeneratedProtocolMessageType('Mobileye', (_message.Message,), {'DESCRIPTOR': _MOBILEYE, '__module__': 'modules.drivers.proto.mobileye_pb2'})
_sym_db.RegisterMessage(Mobileye)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LKA_768._serialized_start = 92
    _LKA_768._serialized_end = 255
    _NUM_76B._serialized_start = 257
    _NUM_76B._serialized_end = 306
    _AFTERMARKET_669._serialized_start = 309
    _AFTERMARKET_669._serialized_end = 543
    _LKA_769._serialized_start = 545
    _LKA_769._serialized_end = 630
    _REFERENCE_76A._serialized_start = 633
    _REFERENCE_76A._serialized_end = 828
    _DETAILS_738._serialized_start = 831
    _DETAILS_738._serialized_end = 1115
    _NEXT_76C._serialized_start = 1118
    _NEXT_76C._serialized_end = 1278
    _DETAILS_737._serialized_start = 1281
    _DETAILS_737._serialized_end = 1493
    _LKA_767._serialized_start = 1495
    _LKA_767._serialized_end = 1580
    _LKA_766._serialized_start = 1583
    _LKA_766._serialized_end = 1745
    _NEXT_76D._serialized_start = 1747
    _NEXT_76D._serialized_end = 1833
    _DETAILS_739._serialized_start = 1836
    _DETAILS_739._serialized_end = 2154
    _DETAILS_73A._serialized_start = 2157
    _DETAILS_73A._serialized_end = 2443
    _DETAILS_73B._serialized_start = 2446
    _DETAILS_73B._serialized_end = 2634
    _MOBILEYE._serialized_start = 2637
    _MOBILEYE._serialized_end = 3346