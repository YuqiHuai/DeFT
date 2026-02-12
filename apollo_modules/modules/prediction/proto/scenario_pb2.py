"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/prediction/proto/scenario.proto\x12\x11apollo.prediction"\xe8\x01\n\x08Scenario\x127\n\x04type\x18\x01 \x01(\x0e2 .apollo.prediction.Scenario.Type:\x07UNKNOWN\x12\x13\n\x0bjunction_id\x18\x02 \x01(\t"\x8d\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x06CRUISE\x10\xe8\x07\x12\x11\n\x0cCRUISE_URBAN\x10\xe9\x07\x12\x13\n\x0eCRUISE_HIGHWAY\x10\xea\x07\x12\r\n\x08JUNCTION\x10\xd0\x0f\x12\x1b\n\x16JUNCTION_TRAFFIC_LIGHT\x10\xd1\x0f\x12\x17\n\x12JUNCTION_STOP_SIGN\x10\xd2\x0f')
_SCENARIO = DESCRIPTOR.message_types_by_name['Scenario']
_SCENARIO_TYPE = _SCENARIO.enum_types_by_name['Type']
Scenario = _reflection.GeneratedProtocolMessageType('Scenario', (_message.Message,), {'DESCRIPTOR': _SCENARIO, '__module__': 'modules.prediction.proto.scenario_pb2'})
_sym_db.RegisterMessage(Scenario)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIO._serialized_start = 63
    _SCENARIO._serialized_end = 295
    _SCENARIO_TYPE._serialized_start = 154
    _SCENARIO_TYPE._serialized_end = 295