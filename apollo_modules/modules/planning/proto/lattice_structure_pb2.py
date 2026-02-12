"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/planning/proto/lattice_structure.proto\x12\x0fapollo.planning"g\n\tStopPoint\x12\t\n\x01s\x18\x01 \x01(\x01\x123\n\x04type\x18\x02 \x01(\x0e2\x1f.apollo.planning.StopPoint.Type:\x04HARD"\x1a\n\x04Type\x12\x08\n\x04HARD\x10\x00\x12\x08\n\x04SOFT\x10\x01"V\n\x0ePlanningTarget\x12.\n\nstop_point\x18\x01 \x01(\x0b2\x1a.apollo.planning.StopPoint\x12\x14\n\x0ccruise_speed\x18\x02 \x01(\x01')
_STOPPOINT = DESCRIPTOR.message_types_by_name['StopPoint']
_PLANNINGTARGET = DESCRIPTOR.message_types_by_name['PlanningTarget']
_STOPPOINT_TYPE = _STOPPOINT.enum_types_by_name['Type']
StopPoint = _reflection.GeneratedProtocolMessageType('StopPoint', (_message.Message,), {'DESCRIPTOR': _STOPPOINT, '__module__': 'modules.planning.proto.lattice_structure_pb2'})
_sym_db.RegisterMessage(StopPoint)
PlanningTarget = _reflection.GeneratedProtocolMessageType('PlanningTarget', (_message.Message,), {'DESCRIPTOR': _PLANNINGTARGET, '__module__': 'modules.planning.proto.lattice_structure_pb2'})
_sym_db.RegisterMessage(PlanningTarget)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STOPPOINT._serialized_start = 67
    _STOPPOINT._serialized_end = 170
    _STOPPOINT_TYPE._serialized_start = 144
    _STOPPOINT_TYPE._serialized_end = 170
    _PLANNINGTARGET._serialized_start = 172
    _PLANNINGTARGET._serialized_end = 258