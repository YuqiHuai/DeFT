"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.v2x.proto import v2x_car_status_pb2 as modules_dot_v2x_dot_proto_dot_v2x__car__status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/v2x/proto/v2x_service_car_to_obu.proto\x12\napollo.v2x\x1a&modules/v2x/proto/v2x_car_status.proto"&\n\x0cUpdateStatus\x12\x16\n\x07updated\x18\x01 \x02(\x08:\x05false2N\n\x08CarToObu\x12B\n\rPushCarStatus\x12\x15.apollo.v2x.CarStatus\x1a\x18.apollo.v2x.UpdateStatus"\x00')
_UPDATESTATUS = DESCRIPTOR.message_types_by_name['UpdateStatus']
UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), {'DESCRIPTOR': _UPDATESTATUS, '__module__': 'modules.v2x.proto.v2x_service_car_to_obu_pb2'})
_sym_db.RegisterMessage(UpdateStatus)
_CARTOOBU = DESCRIPTOR.services_by_name['CarToObu']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _UPDATESTATUS._serialized_start = 102
    _UPDATESTATUS._serialized_end = 140
    _CARTOOBU._serialized_start = 142
    _CARTOOBU._serialized_end = 220