"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHmodules/perception/camera/common/proto/object_template_meta_schema.proto\x12\x18apollo.perception.camera"&\n\x03Dim\x12\t\n\x01H\x18\x01 \x01(\x02\x12\t\n\x01W\x18\x02 \x01(\x02\x12\t\n\x01L\x18\x03 \x01(\x02"Q\n\x0eObjectTemplate\x12\x13\n\x0bspeed_limit\x18\x01 \x01(\x02\x12*\n\x03dim\x18\x02 \x03(\x0b2\x1d.apollo.perception.camera.Dim"\x8e\x06\n\x12ObjectTemplateMeta\x129\n\x07unknown\x18\x01 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12A\n\x0funknown_movable\x18\x02 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12C\n\x11unknown_unmovable\x18\x03 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x125\n\x03car\x18\x04 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x125\n\x03van\x18\x05 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x127\n\x05truck\x18\x06 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x125\n\x03bus\x18\x07 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x129\n\x07cyclist\x18\x08 \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12>\n\x0cmotorcyclist\x18\t \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12<\n\ntricyclist\x18\n \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12<\n\npedestrian\x18\x0b \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12=\n\x0btrafficcone\x18\x0c \x01(\x0b2(.apollo.perception.camera.ObjectTemplate\x12!\n\x14max_dim_change_ratio\x18\x15 \x01(\x02:\x030.1')
_DIM = DESCRIPTOR.message_types_by_name['Dim']
_OBJECTTEMPLATE = DESCRIPTOR.message_types_by_name['ObjectTemplate']
_OBJECTTEMPLATEMETA = DESCRIPTOR.message_types_by_name['ObjectTemplateMeta']
Dim = _reflection.GeneratedProtocolMessageType('Dim', (_message.Message,), {'DESCRIPTOR': _DIM, '__module__': 'modules.perception.camera.common.proto.object_template_meta_schema_pb2'})
_sym_db.RegisterMessage(Dim)
ObjectTemplate = _reflection.GeneratedProtocolMessageType('ObjectTemplate', (_message.Message,), {'DESCRIPTOR': _OBJECTTEMPLATE, '__module__': 'modules.perception.camera.common.proto.object_template_meta_schema_pb2'})
_sym_db.RegisterMessage(ObjectTemplate)
ObjectTemplateMeta = _reflection.GeneratedProtocolMessageType('ObjectTemplateMeta', (_message.Message,), {'DESCRIPTOR': _OBJECTTEMPLATEMETA, '__module__': 'modules.perception.camera.common.proto.object_template_meta_schema_pb2'})
_sym_db.RegisterMessage(ObjectTemplateMeta)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DIM._serialized_start = 102
    _DIM._serialized_end = 140
    _OBJECTTEMPLATE._serialized_start = 142
    _OBJECTTEMPLATE._serialized_end = 223
    _OBJECTTEMPLATEMETA._serialized_start = 226
    _OBJECTTEMPLATEMETA._serialized_end = 1008