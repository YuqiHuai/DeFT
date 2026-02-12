"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/drivers/proto/sensor_image.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto"\xa7\x01\n\x05Image\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08frame_id\x18\x02 \x01(\t\x12\x18\n\x10measurement_time\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\r\n\x05width\x18\x05 \x01(\r\x12\x10\n\x08encoding\x18\x06 \x01(\t\x12\x0c\n\x04step\x18\x07 \x01(\r\x12\x0c\n\x04data\x18\x08 \x01(\x0c"\x96\x01\n\x0fCompressedImage\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08frame_id\x18\x02 \x01(\t\x12\x0e\n\x06format\x18\x03 \x01(\t\x12\x0c\n\x04data\x18\x04 \x01(\x0c\x12\x18\n\x10measurement_time\x18\x05 \x01(\x01\x12\x12\n\nframe_type\x18\x06 \x01(\r*\xfb\x05\n\x0bPixelFormat\x12\t\n\x04RGB8\x10\xe9\x07\x12\n\n\x05RGBA8\x10\xea\x07\x12\n\n\x05RGB16\x10\xeb\x07\x12\x0b\n\x06RGBA16\x10\xec\x07\x12\t\n\x04BGR8\x10\xed\x07\x12\n\n\x05BGRA8\x10\xee\x07\x12\n\n\x05BGR16\x10\xef\x07\x12\x0b\n\x06BGRA16\x10\xf0\x07\x12\n\n\x05MONO8\x10\xf1\x07\x12\x0b\n\x06MONO16\x10\xf2\x07\x12\x0e\n\tTYPE_8UC1\x10\xd1\x0f\x12\x0e\n\tTYPE_8UC2\x10\xd2\x0f\x12\x0e\n\tTYPE_8UC3\x10\xd3\x0f\x12\x0e\n\tTYPE_8UC4\x10\xd4\x0f\x12\x0e\n\tTYPE_8SC1\x10\xd5\x0f\x12\x0e\n\tTYPE_8SC2\x10\xd6\x0f\x12\x0e\n\tTYPE_8SC3\x10\xd7\x0f\x12\x0e\n\tTYPE_8SC4\x10\xd8\x0f\x12\x0f\n\nTYPE_16UC1\x10\xd9\x0f\x12\x0f\n\nTYPE_16UC2\x10\xda\x0f\x12\x0f\n\nTYPE_16UC3\x10\xdb\x0f\x12\x0f\n\nTYPE_16UC4\x10\xdc\x0f\x12\x0f\n\nTYPE_16SC1\x10\xdd\x0f\x12\x0f\n\nTYPE_16SC2\x10\xde\x0f\x12\x0f\n\nTYPE_16SC3\x10\xdf\x0f\x12\x0f\n\nTYPE_16SC4\x10\xe0\x0f\x12\x0f\n\nTYPE_32SC1\x10\xe1\x0f\x12\x0f\n\nTYPE_32SC2\x10\xe2\x0f\x12\x0f\n\nTYPE_32SC3\x10\xe3\x0f\x12\x0f\n\nTYPE_32SC4\x10\xe4\x0f\x12\x0f\n\nTYPE_32FC1\x10\xe5\x0f\x12\x0f\n\nTYPE_32FC2\x10\xe6\x0f\x12\x0f\n\nTYPE_32FC3\x10\xe7\x0f\x12\x0f\n\nTYPE_32FC4\x10\xe8\x0f\x12\x0f\n\nTYPE_64FC1\x10\xe9\x0f\x12\x0f\n\nTYPE_64FC2\x10\xea\x0f\x12\x0f\n\nTYPE_64FC3\x10\xeb\x0f\x12\x0f\n\nTYPE_64FC4\x10\xec\x0f\x12\x10\n\x0bBAYER_RGGB8\x10\xb9\x17\x12\x10\n\x0bBAYER_BGGR8\x10\xba\x17\x12\x10\n\x0bBAYER_GBRG8\x10\xbb\x17\x12\x10\n\x0bBAYER_GRBG8\x10\xbc\x17\x12\x11\n\x0cBAYER_RGGB16\x10\xbd\x17\x12\x11\n\x0cBAYER_BGGR16\x10\xbe\x17\x12\x11\n\x0cBAYER_GBRG16\x10\xbf\x17\x12\x11\n\x0cBAYER_GRBG16\x10\xc0\x17\x12\x0b\n\x06YUV422\x10\xa1\x1f')
_PIXELFORMAT = DESCRIPTOR.enum_types_by_name['PixelFormat']
PixelFormat = enum_type_wrapper.EnumTypeWrapper(_PIXELFORMAT)
RGB8 = 1001
RGBA8 = 1002
RGB16 = 1003
RGBA16 = 1004
BGR8 = 1005
BGRA8 = 1006
BGR16 = 1007
BGRA16 = 1008
MONO8 = 1009
MONO16 = 1010
TYPE_8UC1 = 2001
TYPE_8UC2 = 2002
TYPE_8UC3 = 2003
TYPE_8UC4 = 2004
TYPE_8SC1 = 2005
TYPE_8SC2 = 2006
TYPE_8SC3 = 2007
TYPE_8SC4 = 2008
TYPE_16UC1 = 2009
TYPE_16UC2 = 2010
TYPE_16UC3 = 2011
TYPE_16UC4 = 2012
TYPE_16SC1 = 2013
TYPE_16SC2 = 2014
TYPE_16SC3 = 2015
TYPE_16SC4 = 2016
TYPE_32SC1 = 2017
TYPE_32SC2 = 2018
TYPE_32SC3 = 2019
TYPE_32SC4 = 2020
TYPE_32FC1 = 2021
TYPE_32FC2 = 2022
TYPE_32FC3 = 2023
TYPE_32FC4 = 2024
TYPE_64FC1 = 2025
TYPE_64FC2 = 2026
TYPE_64FC3 = 2027
TYPE_64FC4 = 2028
BAYER_RGGB8 = 3001
BAYER_BGGR8 = 3002
BAYER_GBRG8 = 3003
BAYER_GRBG8 = 3004
BAYER_RGGB16 = 3005
BAYER_BGGR16 = 3006
BAYER_GBRG16 = 3007
BAYER_GRBG16 = 3008
YUV422 = 4001
_IMAGE = DESCRIPTOR.message_types_by_name['Image']
_COMPRESSEDIMAGE = DESCRIPTOR.message_types_by_name['CompressedImage']
Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {'DESCRIPTOR': _IMAGE, '__module__': 'modules.drivers.proto.sensor_image_pb2'})
_sym_db.RegisterMessage(Image)
CompressedImage = _reflection.GeneratedProtocolMessageType('CompressedImage', (_message.Message,), {'DESCRIPTOR': _COMPRESSEDIMAGE, '__module__': 'modules.drivers.proto.sensor_image_pb2'})
_sym_db.RegisterMessage(CompressedImage)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PIXELFORMAT._serialized_start = 419
    _PIXELFORMAT._serialized_end = 1182
    _IMAGE._serialized_start = 96
    _IMAGE._serialized_end = 263
    _COMPRESSEDIMAGE._serialized_start = 266
    _COMPRESSEDIMAGE._serialized_end = 416