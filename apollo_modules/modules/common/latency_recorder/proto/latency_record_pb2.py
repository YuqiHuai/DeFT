"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/common/latency_recorder/proto/latency_record.proto\x12\rapollo.common\x1a!modules/common/proto/header.proto"I\n\rLatencyRecord\x12\x12\n\nbegin_time\x18\x01 \x01(\x04\x12\x10\n\x08end_time\x18\x02 \x01(\x04\x12\x12\n\nmessage_id\x18\x03 \x01(\x04"\x85\x01\n\x10LatencyRecordMap\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x125\n\x0flatency_records\x18\x03 \x03(\x0b2\x1c.apollo.common.LatencyRecord"z\n\x0bLatencyStat\x12)\n\x0cmin_duration\x18\x01 \x01(\x04:\x139223372036854775808\x12\x14\n\x0cmax_duration\x18\x02 \x01(\x04\x12\x15\n\raver_duration\x18\x03 \x01(\x04\x12\x13\n\x0bsample_size\x18\x04 \x01(\r"\xb5\x01\n\x0cLatencyTrack\x12F\n\rlatency_track\x18\x01 \x03(\x0b2/.apollo.common.LatencyTrack.LatencyTrackMessage\x1a]\n\x13LatencyTrackMessage\x12\x14\n\x0clatency_name\x18\x01 \x01(\t\x120\n\x0clatency_stat\x18\x02 \x01(\x0b2\x1a.apollo.common.LatencyStat"\x9f\x01\n\rLatencyReport\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x121\n\x0ce2es_latency\x18\x02 \x01(\x0b2\x1b.apollo.common.LatencyTrack\x124\n\x0fmodules_latency\x18\x03 \x01(\x0b2\x1b.apollo.common.LatencyTrack')
_LATENCYRECORD = DESCRIPTOR.message_types_by_name['LatencyRecord']
_LATENCYRECORDMAP = DESCRIPTOR.message_types_by_name['LatencyRecordMap']
_LATENCYSTAT = DESCRIPTOR.message_types_by_name['LatencyStat']
_LATENCYTRACK = DESCRIPTOR.message_types_by_name['LatencyTrack']
_LATENCYTRACK_LATENCYTRACKMESSAGE = _LATENCYTRACK.nested_types_by_name['LatencyTrackMessage']
_LATENCYREPORT = DESCRIPTOR.message_types_by_name['LatencyReport']
LatencyRecord = _reflection.GeneratedProtocolMessageType('LatencyRecord', (_message.Message,), {'DESCRIPTOR': _LATENCYRECORD, '__module__': 'modules.common.latency_recorder.proto.latency_record_pb2'})
_sym_db.RegisterMessage(LatencyRecord)
LatencyRecordMap = _reflection.GeneratedProtocolMessageType('LatencyRecordMap', (_message.Message,), {'DESCRIPTOR': _LATENCYRECORDMAP, '__module__': 'modules.common.latency_recorder.proto.latency_record_pb2'})
_sym_db.RegisterMessage(LatencyRecordMap)
LatencyStat = _reflection.GeneratedProtocolMessageType('LatencyStat', (_message.Message,), {'DESCRIPTOR': _LATENCYSTAT, '__module__': 'modules.common.latency_recorder.proto.latency_record_pb2'})
_sym_db.RegisterMessage(LatencyStat)
LatencyTrack = _reflection.GeneratedProtocolMessageType('LatencyTrack', (_message.Message,), {'LatencyTrackMessage': _reflection.GeneratedProtocolMessageType('LatencyTrackMessage', (_message.Message,), {'DESCRIPTOR': _LATENCYTRACK_LATENCYTRACKMESSAGE, '__module__': 'modules.common.latency_recorder.proto.latency_record_pb2'}), 'DESCRIPTOR': _LATENCYTRACK, '__module__': 'modules.common.latency_recorder.proto.latency_record_pb2'})
_sym_db.RegisterMessage(LatencyTrack)
_sym_db.RegisterMessage(LatencyTrack.LatencyTrackMessage)
LatencyReport = _reflection.GeneratedProtocolMessageType('LatencyReport', (_message.Message,), {'DESCRIPTOR': _LATENCYREPORT, '__module__': 'modules.common.latency_recorder.proto.latency_record_pb2'})
_sym_db.RegisterMessage(LatencyReport)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LATENCYRECORD._serialized_start = 112
    _LATENCYRECORD._serialized_end = 185
    _LATENCYRECORDMAP._serialized_start = 188
    _LATENCYRECORDMAP._serialized_end = 321
    _LATENCYSTAT._serialized_start = 323
    _LATENCYSTAT._serialized_end = 445
    _LATENCYTRACK._serialized_start = 448
    _LATENCYTRACK._serialized_end = 629
    _LATENCYTRACK_LATENCYTRACKMESSAGE._serialized_start = 536
    _LATENCYTRACK_LATENCYTRACKMESSAGE._serialized_end = 629
    _LATENCYREPORT._serialized_start = 632
    _LATENCYREPORT._serialized_end = 791