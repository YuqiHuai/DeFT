"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/transform/proto/transform.proto\x12\x10apollo.transform\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"e\n\tTransform\x12+\n\x0btranslation\x18\x01 \x01(\x0b2\x16.apollo.common.Point3D\x12+\n\x08rotation\x18\x02 \x01(\x0b2\x19.apollo.common.Quaternion"\x81\x01\n\x10TransformStamped\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x16\n\x0echild_frame_id\x18\x02 \x01(\t\x12.\n\ttransform\x18\x03 \x01(\x0b2\x1b.apollo.transform.Transform"r\n\x11TransformStampeds\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x126\n\ntransforms\x18\x02 \x03(\x0b2".apollo.transform.TransformStamped')
_TRANSFORM = DESCRIPTOR.message_types_by_name['Transform']
_TRANSFORMSTAMPED = DESCRIPTOR.message_types_by_name['TransformStamped']
_TRANSFORMSTAMPEDS = DESCRIPTOR.message_types_by_name['TransformStampeds']
Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {'DESCRIPTOR': _TRANSFORM, '__module__': 'modules.transform.proto.transform_pb2'})
_sym_db.RegisterMessage(Transform)
TransformStamped = _reflection.GeneratedProtocolMessageType('TransformStamped', (_message.Message,), {'DESCRIPTOR': _TRANSFORMSTAMPED, '__module__': 'modules.transform.proto.transform_pb2'})
_sym_db.RegisterMessage(TransformStamped)
TransformStampeds = _reflection.GeneratedProtocolMessageType('TransformStampeds', (_message.Message,), {'DESCRIPTOR': _TRANSFORMSTAMPEDS, '__module__': 'modules.transform.proto.transform_pb2'})
_sym_db.RegisterMessage(TransformStampeds)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TRANSFORM._serialized_start = 133
    _TRANSFORM._serialized_end = 234
    _TRANSFORMSTAMPED._serialized_start = 237
    _TRANSFORMSTAMPED._serialized_end = 366
    _TRANSFORMSTAMPEDS._serialized_start = 368
    _TRANSFORMSTAMPEDS._serialized_end = 482