"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/planning/proto/planning_stats.proto\x12\x0fapollo.planning"Z\n\nStatsGroup\x12\x0b\n\x03max\x18\x01 \x01(\x01\x12\x18\n\x03min\x18\x02 \x01(\x01:\x0b10000000000\x12\x0b\n\x03sum\x18\x03 \x01(\x01\x12\x0b\n\x03avg\x18\x04 \x01(\x01\x12\x0b\n\x03num\x18\x05 \x01(\x05"\xa6\x02\n\rPlanningStats\x126\n\x11total_path_length\x18\x01 \x01(\x0b2\x1b.apollo.planning.StatsGroup\x124\n\x0ftotal_path_time\x18\x02 \x01(\x0b2\x1b.apollo.planning.StatsGroup\x12&\n\x01v\x18\x03 \x01(\x0b2\x1b.apollo.planning.StatsGroup\x12&\n\x01a\x18\x04 \x01(\x0b2\x1b.apollo.planning.StatsGroup\x12*\n\x05kappa\x18\x05 \x01(\x0b2\x1b.apollo.planning.StatsGroup\x12+\n\x06dkappa\x18\x06 \x01(\x0b2\x1b.apollo.planning.StatsGroup')
_STATSGROUP = DESCRIPTOR.message_types_by_name['StatsGroup']
_PLANNINGSTATS = DESCRIPTOR.message_types_by_name['PlanningStats']
StatsGroup = _reflection.GeneratedProtocolMessageType('StatsGroup', (_message.Message,), {'DESCRIPTOR': _STATSGROUP, '__module__': 'modules.planning.proto.planning_stats_pb2'})
_sym_db.RegisterMessage(StatsGroup)
PlanningStats = _reflection.GeneratedProtocolMessageType('PlanningStats', (_message.Message,), {'DESCRIPTOR': _PLANNINGSTATS, '__module__': 'modules.planning.proto.planning_stats_pb2'})
_sym_db.RegisterMessage(PlanningStats)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STATSGROUP._serialized_start = 64
    _STATSGROUP._serialized_end = 154
    _PLANNINGSTATS._serialized_start = 157
    _PLANNINGSTATS._serialized_end = 451