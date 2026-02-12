"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/planning/proto/st_drivable_boundary.proto\x12\x0fapollo.planning"s\n\x1aSTDrivableBoundaryInstance\x12\t\n\x01t\x18\x01 \x01(\x01\x12\x0f\n\x07s_lower\x18\x02 \x01(\x01\x12\x0f\n\x07s_upper\x18\x03 \x01(\x01\x12\x13\n\x0bv_obs_lower\x18\x04 \x01(\x01\x12\x13\n\x0bv_obs_upper\x18\x05 \x01(\x01"V\n\x12STDrivableBoundary\x12@\n\x0bst_boundary\x18\x01 \x03(\x0b2+.apollo.planning.STDrivableBoundaryInstance')
_STDRIVABLEBOUNDARYINSTANCE = DESCRIPTOR.message_types_by_name['STDrivableBoundaryInstance']
_STDRIVABLEBOUNDARY = DESCRIPTOR.message_types_by_name['STDrivableBoundary']
STDrivableBoundaryInstance = _reflection.GeneratedProtocolMessageType('STDrivableBoundaryInstance', (_message.Message,), {'DESCRIPTOR': _STDRIVABLEBOUNDARYINSTANCE, '__module__': 'modules.planning.proto.st_drivable_boundary_pb2'})
_sym_db.RegisterMessage(STDrivableBoundaryInstance)
STDrivableBoundary = _reflection.GeneratedProtocolMessageType('STDrivableBoundary', (_message.Message,), {'DESCRIPTOR': _STDRIVABLEBOUNDARY, '__module__': 'modules.planning.proto.st_drivable_boundary_pb2'})
_sym_db.RegisterMessage(STDrivableBoundary)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _STDRIVABLEBOUNDARYINSTANCE._serialized_start = 70
    _STDRIVABLEBOUNDARYINSTANCE._serialized_end = 185
    _STDRIVABLEBOUNDARY._serialized_start = 187
    _STDRIVABLEBOUNDARY._serialized_end = 273