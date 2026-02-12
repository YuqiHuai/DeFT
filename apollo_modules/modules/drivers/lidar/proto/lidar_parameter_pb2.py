"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/drivers/lidar/proto/lidar_parameter.proto\x12\x14apollo.drivers.lidar"\xeb\x01\n\x0eLidarParameter\x12>\n\x05brand\x18\x01 \x02(\x0e2/.apollo.drivers.lidar.LidarParameter.LidarBrand"4\n\nLidarBrand\x12\x0c\n\x08VELODYNE\x10\x00\x12\t\n\x05HESAI\x10\x01\x12\r\n\tROBOSENSE\x10\x02"c\n\x0eLidarChannelId\x12\x13\n\x0fCHANNEL_ID_ZERO\x10\x00\x12\x12\n\x0eCHANNEL_ID_ONE\x10\x01\x12\x12\n\x0eCHANNEL_ID_TWO\x10\x02\x12\x14\n\x10CHANNEL_ID_THREE\x10\x03')
_LIDARPARAMETER = DESCRIPTOR.message_types_by_name['LidarParameter']
_LIDARPARAMETER_LIDARBRAND = _LIDARPARAMETER.enum_types_by_name['LidarBrand']
_LIDARPARAMETER_LIDARCHANNELID = _LIDARPARAMETER.enum_types_by_name['LidarChannelId']
LidarParameter = _reflection.GeneratedProtocolMessageType('LidarParameter', (_message.Message,), {'DESCRIPTOR': _LIDARPARAMETER, '__module__': 'modules.drivers.lidar.proto.lidar_parameter_pb2'})
_sym_db.RegisterMessage(LidarParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LIDARPARAMETER._serialized_start = 76
    _LIDARPARAMETER._serialized_end = 311
    _LIDARPARAMETER_LIDARBRAND._serialized_start = 158
    _LIDARPARAMETER_LIDARBRAND._serialized_end = 210
    _LIDARPARAMETER_LIDARCHANNELID._serialized_start = 212
    _LIDARPARAMETER_LIDARCHANNELID._serialized_end = 311