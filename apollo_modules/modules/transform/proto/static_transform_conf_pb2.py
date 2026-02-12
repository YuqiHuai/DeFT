"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/transform/proto/static_transform_conf.proto\x12\x17apollo.static_transform"\\\n\rExtrinsicFile\x12\x10\n\x08frame_id\x18\x01 \x01(\t\x12\x16\n\x0echild_frame_id\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\x12\x0e\n\x06enable\x18\x04 \x01(\x08"F\n\x04Conf\x12>\n\x0eextrinsic_file\x18\x01 \x03(\x0b2&.apollo.static_transform.ExtrinsicFile')
_EXTRINSICFILE = DESCRIPTOR.message_types_by_name['ExtrinsicFile']
_CONF = DESCRIPTOR.message_types_by_name['Conf']
ExtrinsicFile = _reflection.GeneratedProtocolMessageType('ExtrinsicFile', (_message.Message,), {'DESCRIPTOR': _EXTRINSICFILE, '__module__': 'modules.transform.proto.static_transform_conf_pb2'})
_sym_db.RegisterMessage(ExtrinsicFile)
Conf = _reflection.GeneratedProtocolMessageType('Conf', (_message.Message,), {'DESCRIPTOR': _CONF, '__module__': 'modules.transform.proto.static_transform_conf_pb2'})
_sym_db.RegisterMessage(Conf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _EXTRINSICFILE._serialized_start = 80
    _EXTRINSICFILE._serialized_end = 172
    _CONF._serialized_start = 174
    _CONF._serialized_end = 244