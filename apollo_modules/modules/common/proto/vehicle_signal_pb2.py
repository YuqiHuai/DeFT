"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/common/proto/vehicle_signal.proto\x12\rapollo.common"\xd5\x01\n\rVehicleSignal\x12<\n\x0bturn_signal\x18\x01 \x01(\x0e2\'.apollo.common.VehicleSignal.TurnSignal\x12\x11\n\thigh_beam\x18\x02 \x01(\x08\x12\x10\n\x08low_beam\x18\x03 \x01(\x08\x12\x0c\n\x04horn\x18\x04 \x01(\x08\x12\x17\n\x0femergency_light\x18\x05 \x01(\x08":\n\nTurnSignal\x12\r\n\tTURN_NONE\x10\x00\x12\r\n\tTURN_LEFT\x10\x01\x12\x0e\n\nTURN_RIGHT\x10\x02')
_VEHICLESIGNAL = DESCRIPTOR.message_types_by_name['VehicleSignal']
_VEHICLESIGNAL_TURNSIGNAL = _VEHICLESIGNAL.enum_types_by_name['TurnSignal']
VehicleSignal = _reflection.GeneratedProtocolMessageType('VehicleSignal', (_message.Message,), {'DESCRIPTOR': _VEHICLESIGNAL, '__module__': 'modules.common.proto.vehicle_signal_pb2'})
_sym_db.RegisterMessage(VehicleSignal)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VEHICLESIGNAL._serialized_start = 61
    _VEHICLESIGNAL._serialized_end = 274
    _VEHICLESIGNAL_TURNSIGNAL._serialized_start = 216
    _VEHICLESIGNAL_TURNSIGNAL._serialized_end = 274