"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from .....modules.contrib.lgsvl_msgs.proto import detection2d_pb2 as modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7modules/contrib/lgsvl_msgs/proto/detection2darray.proto\x12\x19apollo.contrib.lgsvl_msgs\x1a!modules/common/proto/header.proto\x1a2modules/contrib/lgsvl_msgs/proto/detection2d.proto"u\n\x10Detection2DArray\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12:\n\ndetections\x18\x02 \x03(\x0b2&.apollo.contrib.lgsvl_msgs.Detection2Db\x06proto3')
_DETECTION2DARRAY = DESCRIPTOR.message_types_by_name['Detection2DArray']
Detection2DArray = _reflection.GeneratedProtocolMessageType('Detection2DArray', (_message.Message,), {'DESCRIPTOR': _DETECTION2DARRAY, '__module__': 'modules.contrib.lgsvl_msgs.proto.detection2darray_pb2'})
_sym_db.RegisterMessage(Detection2DArray)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DETECTION2DARRAY._serialized_start = 173
    _DETECTION2DARRAY._serialized_end = 290