"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/drivers/gnss/proto/heading.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto"\x87\x04\n\x07Heading\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x17\n\x0fsolution_status\x18\x03 \x01(\r\x12\x15\n\rposition_type\x18\x04 \x01(\r\x12\x17\n\x0fbaseline_length\x18\x05 \x01(\x02\x12\x0f\n\x07heading\x18\x06 \x01(\x02\x12\r\n\x05pitch\x18\x07 \x01(\x02\x12\x10\n\x08reserved\x18\x08 \x01(\x02\x12\x17\n\x0fheading_std_dev\x18\t \x01(\x02\x12\x15\n\rpitch_std_dev\x18\n \x01(\x02\x12\x12\n\nstation_id\x18\x0b \x01(\x0c\x12 \n\x18satellite_tracked_number\x18\x0c \x01(\r\x12"\n\x1asatellite_soulution_number\x18\r \x01(\r\x12\x1c\n\x14satellite_number_obs\x18\x0e \x01(\r\x12\x1e\n\x16satellite_number_multi\x18\x0f \x01(\r\x12\x17\n\x0fsolution_source\x18\x10 \x01(\r\x12 \n\x18extended_solution_status\x18\x11 \x01(\r\x12\x1f\n\x17galileo_beidou_sig_mask\x18\x12 \x01(\r\x12\x1c\n\x14gps_glonass_sig_mask\x18\x13 \x01(\r')
_HEADING = DESCRIPTOR.message_types_by_name['Heading']
Heading = _reflection.GeneratedProtocolMessageType('Heading', (_message.Message,), {'DESCRIPTOR': _HEADING, '__module__': 'modules.drivers.gnss.proto.heading_pb2'})
_sym_db.RegisterMessage(Heading)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HEADING._serialized_start = 101
    _HEADING._serialized_end = 620