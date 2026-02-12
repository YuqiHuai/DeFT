"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/drivers/proto/ultrasonic_radar.proto\x12\x0eapollo.drivers\x1a!modules/common/proto/header.proto"C\n\nUltrasonic\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x0e\n\x06ranges\x18\x02 \x03(\x02')
_ULTRASONIC = DESCRIPTOR.message_types_by_name['Ultrasonic']
Ultrasonic = _reflection.GeneratedProtocolMessageType('Ultrasonic', (_message.Message,), {'DESCRIPTOR': _ULTRASONIC, '__module__': 'modules.drivers.proto.ultrasonic_radar_pb2'})
_sym_db.RegisterMessage(Ultrasonic)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ULTRASONIC._serialized_start = 99
    _ULTRASONIC._serialized_end = 166