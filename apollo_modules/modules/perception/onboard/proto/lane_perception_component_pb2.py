"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/perception/onboard/proto/lane_perception_component.proto\x12\x19apollo.perception.onboard"\x87\x07\n\rLaneDetection\x12*\n\x0ccamera_names\x18\x01 \x01(\t:\x14front_6mm,front_12mm\x12p\n\x1ainput_camera_channel_names\x18\x02 \x01(\t:L/apollo/sensor/camera/front_6mm/image,/apollo/sensor/camera/front_12mm/image\x12\x1b\n\x10timestamp_offset\x18\x03 \x01(\x01:\x010\x12?\n\x1fcamera_lane_perception_conf_dir\x18\x04 \x01(\t:\x16conf/perception/camera\x121\n camera_lane_perception_conf_file\x18\x05 \x01(\t:\x07lane.pt\x12\x1a\n\x0eframe_capacity\x18\x06 \x01(\x05:\x0220\x12\x1c\n\x11image_channel_num\x18\x07 \x01(\x05:\x013\x12"\n\x13enable_undistortion\x18\x08 \x01(\x08:\x05false\x12#\n\x14enable_visualization\x18\t \x01(\x08:\x05false\x124\n\x19output_lanes_channel_name\x18\n \x01(\t:\x11/perception/lanes\x12\x1f\n\x14default_camera_pitch\x18\x0b \x01(\x01:\x010\x12"\n\x15default_camera_height\x18\x0c \x01(\x01:\x031.5\x127\n$lane_calibration_working_sensor_name\x18\r \x01(\t:\tfront_6mm\x12-\n\x11calibrator_method\x18\x0e \x01(\t:\x12LaneLineCalibrator\x124\n\x12calib_service_name\x18\x0f \x01(\t:\x18OnlineCalibrationService\x12\x1f\n\x11run_calib_service\x18\x10 \x01(\x08:\x04true\x12\x14\n\x07ts_diff\x18\x11 \x01(\x01:\x030.1\x121\n\x13visual_debug_folder\x18\x12 \x01(\t:\x14/apollo/debug_output\x12 \n\rvisual_camera\x18\x13 \x01(\t:\tfront_6mm\x12\x1f\n\x10write_visual_img\x18\x14 \x01(\x08:\x05false')
_LANEDETECTION = DESCRIPTOR.message_types_by_name['LaneDetection']
LaneDetection = _reflection.GeneratedProtocolMessageType('LaneDetection', (_message.Message,), {'DESCRIPTOR': _LANEDETECTION, '__module__': 'modules.perception.onboard.proto.lane_perception_component_pb2'})
_sym_db.RegisterMessage(LaneDetection)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANEDETECTION._serialized_start = 96
    _LANEDETECTION._serialized_end = 999