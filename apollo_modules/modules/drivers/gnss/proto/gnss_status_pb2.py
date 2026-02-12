"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/drivers/gnss/proto/gnss_status.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto"\xd2\x02\n\x0cStreamStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12M\n\x0fins_stream_type\x18\x02 \x01(\x0e2&.apollo.drivers.gnss.StreamStatus.Type:\x0cDISCONNECTED\x12P\n\x12rtk_stream_in_type\x18\x03 \x01(\x0e2&.apollo.drivers.gnss.StreamStatus.Type:\x0cDISCONNECTED\x12Q\n\x13rtk_stream_out_type\x18\x04 \x01(\x0e2&.apollo.drivers.gnss.StreamStatus.Type:\x0cDISCONNECTED"\'\n\x04Type\x12\x10\n\x0cDISCONNECTED\x10\x00\x12\r\n\tCONNECTED\x10\x01"\x9d\x01\n\tInsStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12:\n\x04type\x18\x02 \x01(\x0e2#.apollo.drivers.gnss.InsStatus.Type:\x07INVALID"-\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nCONVERGING\x10\x01\x12\x08\n\x04GOOD\x10\x02"\xa1\x01\n\nGnssStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12!\n\x12solution_completed\x18\x02 \x01(\x08:\x05false\x12\x1a\n\x0fsolution_status\x18\x03 \x01(\r:\x010\x12\x18\n\rposition_type\x18\x04 \x01(\r:\x010\x12\x13\n\x08num_sats\x18\x05 \x01(\x05:\x010')
_STREAMSTATUS = DESCRIPTOR.message_types_by_name['StreamStatus']
_INSSTATUS = DESCRIPTOR.message_types_by_name['InsStatus']
_GNSSSTATUS = DESCRIPTOR.message_types_by_name['GnssStatus']
_STREAMSTATUS_TYPE = _STREAMSTATUS.enum_types_by_name['Type']
_INSSTATUS_TYPE = _INSSTATUS.enum_types_by_name['Type']
StreamStatus = _reflection.GeneratedProtocolMessageType('StreamStatus', (_message.Message,), {'DESCRIPTOR': _STREAMSTATUS, '__module__': 'modules.drivers.gnss.proto.gnss_status_pb2'})
_sym_db.RegisterMessage(StreamStatus)
InsStatus = _reflection.GeneratedProtocolMessageType('InsStatus', (_message.Message,), {'DESCRIPTOR': _INSSTATUS, '__module__': 'modules.drivers.gnss.proto.gnss_status_pb2'})
_sym_db.RegisterMessage(InsStatus)
GnssStatus = _reflection.GeneratedProtocolMessageType('GnssStatus', (_message.Message,), {'DESCRIPTOR': _GNSSSTATUS, '__module__': 'modules.drivers.gnss.proto.gnss_status_pb2'})
_sym_db.RegisterMessage(GnssStatus)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STREAMSTATUS._serialized_start = 105
    _STREAMSTATUS._serialized_end = 443
    _STREAMSTATUS_TYPE._serialized_start = 404
    _STREAMSTATUS_TYPE._serialized_end = 443
    _INSSTATUS._serialized_start = 446
    _INSSTATUS._serialized_end = 603
    _INSSTATUS_TYPE._serialized_start = 558
    _INSSTATUS_TYPE._serialized_end = 603
    _GNSSSTATUS._serialized_start = 606
    _GNSSSTATUS._serialized_end = 767