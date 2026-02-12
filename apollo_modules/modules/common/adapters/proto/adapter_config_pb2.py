"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/common/adapters/proto/adapter_config.proto\x12\x15apollo.common.adapter"\xb1\x0e\n\rAdapterConfig\x12>\n\x04type\x18\x01 \x01(\x0e20.apollo.common.adapter.AdapterConfig.MessageType\x127\n\x04mode\x18\x02 \x01(\x0e2).apollo.common.adapter.AdapterConfig.Mode\x12!\n\x15message_history_limit\x18\x03 \x01(\x05:\x0210\x12\x14\n\x05latch\x18\x04 \x01(\x08:\x05false\x12\r\n\x05topic\x18\x05 \x01(\t"\xa6\x0c\n\x0bMessageType\x12\x0f\n\x0bPOINT_CLOUD\x10\x01\x12\x15\n\x11VLP16_POINT_CLOUD\x10:\x12\x07\n\x03GPS\x10\x02\x12\x07\n\x03IMU\x10\x03\x12\x0b\n\x07CHASSIS\x10\x04\x12\x10\n\x0cLOCALIZATION\x10\x05\x12\x17\n\x13PLANNING_TRAJECTORY\x10\x06\x12\x0b\n\x07MONITOR\x10\x07\x12\x07\n\x03PAD\x10\x08\x12\x13\n\x0fCONTROL_COMMAND\x10\t\x12\x0e\n\nPREDICTION\x10\n\x12\x18\n\x14PERCEPTION_OBSTACLES\x10\x0b\x12\x1b\n\x17TRAFFIC_LIGHT_DETECTION\x10\x0c\x12\x12\n\x0eCHASSIS_DETAIL\x10\r\x12\x10\n\x08DECISION\x10\x0e\x1a\x02\x08\x01\x12\n\n\x06CANBUS\x10\x0f\x12\x13\n\x0fROUTING_REQUEST\x10\x10\x12\x14\n\x10ROUTING_RESPONSE\x10\x11\x12\x15\n\x11RELATIVE_ODOMETRY\x10\x12\x12\x0c\n\x08INS_STAT\x10\x13\x12\x13\n\x0bHMI_COMMAND\x10\x14\x1a\x02\x08\x01\x12\x0c\n\x08MOBILEYE\x10\x15\x12\r\n\tDELPHIESR\x10\x16\x12\x14\n\x10COMPRESSED_IMAGE\x10\x17\x12\x11\n\rSYSTEM_STATUS\x10\x18\x12\x0e\n\nINS_STATUS\x10\x19\x12\x0f\n\x0bGNSS_STATUS\x10\x1a\x12\x0f\n\x0bCONTI_RADAR\x10\x1b\x12\x0f\n\x0bIMAGE_SHORT\x10\x1c\x12\x0e\n\nIMAGE_LONG\x10\x1d\x12\x0f\n\x0bDRIVE_EVENT\x10\x1e\x12\x10\n\x0cGNSS_RTK_OBS\x10\x1f\x12\x10\n\x0cGNSS_RTK_EPH\x10 \x12\x12\n\x0eGNSS_BEST_POSE\x10!\x12\x19\n\x15LOCALIZATION_MSF_GNSS\x10"\x12\x1a\n\x16LOCALIZATION_MSF_LIDAR\x10#\x12\x1d\n\x19LOCALIZATION_MSF_SINS_PVA\x10$\x12\x0b\n\x07RAW_IMU\x10%\x12\x1b\n\x17LOCALIZATION_MSF_STATUS\x10&\x12\x0f\n\x0bSTATIC_INFO\x10\'\x12\x10\n\x0cRELATIVE_MAP\x10(\x12\x0e\n\nNAVIGATION\x10)\x12\x14\n\x10ULTRASONIC_RADAR\x10*\x12\x11\n\rAUDIO_CAPTURE\x10+\x12\x0f\n\x0bIMAGE_FRONT\x10-\x12\x17\n\x13PANDORA_POINT_CLOUD\x10.\x12\x1e\n\x1aPANDORA_CAMERA_FRONT_COLOR\x10/\x12\x1d\n\x19PANDORA_CAMERA_RIGHT_GRAY\x100\x12\x1c\n\x18PANDORA_CAMERA_LEFT_GRAY\x101\x12\x1d\n\x19PANDORA_CAMERA_FRONT_GRAY\x102\x12\x1c\n\x18PANDORA_CAMERA_BACK_GRAY\x103\x12\x18\n\x14PERCEPTION_LANE_MASK\x104\x12\x0c\n\x08GUARDIAN\x105\x12\x11\n\rGNSS_RAW_DATA\x106\x12\x11\n\rSTREAM_STATUS\x107\x12\x10\n\x0cGNSS_HEADING\x108\x12\r\n\tRTCM_DATA\x109\x12\x11\n\rRACOBIT_RADAR\x10;\x12\x15\n\x11POINT_CLOUD_DENSE\x10<\x12\x19\n\x15POINT_CLOUD_DENSE_RAW\x10=\x12\x17\n\x13VELODYNE_SCAN_DENSE\x10>\x12\x18\n\x14POINT_CLOUD_SPARSE_1\x10?\x12\x1c\n\x18POINT_CLOUD_SPARSE_RAW_1\x10@\x12\x1a\n\x16VELODYNE_SCAN_SPARSE_1\x10A\x12\x18\n\x14POINT_CLOUD_SPARSE_2\x10B\x12\x1c\n\x18POINT_CLOUD_SPARSE_RAW_2\x10C\x12\x1a\n\x16VELODYNE_SCAN_SPARSE_2\x10D\x12\x18\n\x14POINT_CLOUD_SPARSE_3\x10E\x12\x1c\n\x18POINT_CLOUD_SPARSE_RAW_3\x10F\x12\x1a\n\x16VELODYNE_SCAN_SPARSE_3\x10G\x12\x15\n\x11CAMERA_IMAGE_LONG\x10H\x12\x16\n\x12CAMERA_IMAGE_SHORT\x10I\x12\x10\n\x0cPLANNING_PAD\x10J\x12\x10\n\x0cSTORYTELLING\x10K"6\n\x04Mode\x12\x10\n\x0cRECEIVE_ONLY\x10\x00\x12\x10\n\x0cPUBLISH_ONLY\x10\x01\x12\n\n\x06DUPLEX\x10\x02"\\\n\x14AdapterManagerConfig\x124\n\x06config\x18\x01 \x03(\x0b2$.apollo.common.adapter.AdapterConfig\x12\x0e\n\x06is_ros\x18\x02 \x01(\x08')
_ADAPTERCONFIG = DESCRIPTOR.message_types_by_name['AdapterConfig']
_ADAPTERMANAGERCONFIG = DESCRIPTOR.message_types_by_name['AdapterManagerConfig']
_ADAPTERCONFIG_MESSAGETYPE = _ADAPTERCONFIG.enum_types_by_name['MessageType']
_ADAPTERCONFIG_MODE = _ADAPTERCONFIG.enum_types_by_name['Mode']
AdapterConfig = _reflection.GeneratedProtocolMessageType('AdapterConfig', (_message.Message,), {'DESCRIPTOR': _ADAPTERCONFIG, '__module__': 'modules.common.adapters.proto.adapter_config_pb2'})
_sym_db.RegisterMessage(AdapterConfig)
AdapterManagerConfig = _reflection.GeneratedProtocolMessageType('AdapterManagerConfig', (_message.Message,), {'DESCRIPTOR': _ADAPTERMANAGERCONFIG, '__module__': 'modules.common.adapters.proto.adapter_config_pb2'})
_sym_db.RegisterMessage(AdapterManagerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ADAPTERCONFIG_MESSAGETYPE.values_by_name['DECISION']._options = None
    _ADAPTERCONFIG_MESSAGETYPE.values_by_name['DECISION']._serialized_options = b'\x08\x01'
    _ADAPTERCONFIG_MESSAGETYPE.values_by_name['HMI_COMMAND']._options = None
    _ADAPTERCONFIG_MESSAGETYPE.values_by_name['HMI_COMMAND']._serialized_options = b'\x08\x01'
    _ADAPTERCONFIG._serialized_start = 78
    _ADAPTERCONFIG._serialized_end = 1919
    _ADAPTERCONFIG_MESSAGETYPE._serialized_start = 289
    _ADAPTERCONFIG_MESSAGETYPE._serialized_end = 1863
    _ADAPTERCONFIG_MODE._serialized_start = 1865
    _ADAPTERCONFIG_MODE._serialized_end = 1919
    _ADAPTERMANAGERCONFIG._serialized_start = 1921
    _ADAPTERMANAGERCONFIG._serialized_end = 2013