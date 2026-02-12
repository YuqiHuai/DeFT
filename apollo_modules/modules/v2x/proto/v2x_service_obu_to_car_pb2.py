"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.v2x.proto import v2x_obu_traffic_light_pb2 as modules_dot_v2x_dot_proto_dot_v2x__obu__traffic__light__pb2
from ....modules.v2x.proto import v2x_monitor_pb2 as modules_dot_v2x_dot_proto_dot_v2x__monitor__pb2
from ....modules.v2x.proto import v2x_obu_rsi_pb2 as modules_dot_v2x_dot_proto_dot_v2x__obu__rsi__pb2
from ....modules.v2x.proto import v2x_obstacles_pb2 as modules_dot_v2x_dot_proto_dot_v2x__obstacles__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/v2x/proto/v2x_service_obu_to_car.proto\x12\napollo.v2x\x1a-modules/v2x/proto/v2x_obu_traffic_light.proto\x1a#modules/v2x/proto/v2x_monitor.proto\x1a#modules/v2x/proto/v2x_obu_rsi.proto\x1a%modules/v2x/proto/v2x_obstacles.proto"I\n\x0eStatusResponse\x12\x15\n\x06status\x18\x01 \x02(\x08:\x05false\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x12\n\nerror_code\x18\x03 \x01(\x032\xbb\x02\n\x08ObuToCar\x12Q\n\x17SendPerceptionObstacles\x12\x18.apollo.v2x.V2XObstacles\x1a\x1a.apollo.v2x.StatusResponse"\x00\x12T\n\x13SendV2xTrafficLight\x12\x1f.apollo.v2x.obu.ObuTrafficLight\x1a\x1a.apollo.v2x.StatusResponse"\x00\x12B\n\nSendV2xRSI\x12\x16.apollo.v2x.obu.ObuRsi\x1a\x1a.apollo.v2x.StatusResponse"\x00\x12B\n\x0cSendObuAlarm\x12\x14.apollo.v2x.ObuAlarm\x1a\x1a.apollo.v2x.StatusResponse"\x00')
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {'DESCRIPTOR': _STATUSRESPONSE, '__module__': 'modules.v2x.proto.v2x_service_obu_to_car_pb2'})
_sym_db.RegisterMessage(StatusResponse)
_OBUTOCAR = DESCRIPTOR.services_by_name['ObuToCar']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STATUSRESPONSE._serialized_start = 222
    _STATUSRESPONSE._serialized_end = 295
    _OBUTOCAR._serialized_start = 298
    _OBUTOCAR._serialized_end = 613