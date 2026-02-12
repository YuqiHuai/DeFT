"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/common/util/testdata/simple.proto\x12\x17apollo.common.util.test\x1a!modules/common/proto/header.proto"U\n\rSimpleMessage\x12\x0f\n\x07integer\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12%\n\x06header\x18\x03 \x01(\x0b2\x15.apollo.common.Header"P\n\x15SimpleRepeatedMessage\x127\n\x07message\x18\x01 \x03(\x0b2&.apollo.common.util.test.SimpleMessage')
_SIMPLEMESSAGE = DESCRIPTOR.message_types_by_name['SimpleMessage']
_SIMPLEREPEATEDMESSAGE = DESCRIPTOR.message_types_by_name['SimpleRepeatedMessage']
SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), {'DESCRIPTOR': _SIMPLEMESSAGE, '__module__': 'modules.common.util.testdata.simple_pb2'})
_sym_db.RegisterMessage(SimpleMessage)
SimpleRepeatedMessage = _reflection.GeneratedProtocolMessageType('SimpleRepeatedMessage', (_message.Message,), {'DESCRIPTOR': _SIMPLEREPEATEDMESSAGE, '__module__': 'modules.common.util.testdata.simple_pb2'})
_sym_db.RegisterMessage(SimpleRepeatedMessage)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SIMPLEMESSAGE._serialized_start = 105
    _SIMPLEMESSAGE._serialized_end = 190
    _SIMPLEREPEATEDMESSAGE._serialized_start = 192
    _SIMPLEREPEATEDMESSAGE._serialized_end = 272