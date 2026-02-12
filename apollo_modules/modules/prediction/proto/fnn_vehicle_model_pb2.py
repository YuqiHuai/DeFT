"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.prediction.proto import fnn_model_base_pb2 as modules_dot_prediction_dot_proto_dot_fnn__model__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/prediction/proto/fnn_vehicle_model.proto\x12\x11apollo.prediction\x1a-modules/prediction/proto/fnn_model_base.proto"\xd5\x01\n\x0fFnnVehicleModel\x12\x11\n\tdim_input\x18\x01 \x01(\x05\x12/\n\x0csamples_mean\x18\x02 \x01(\x0b2\x19.apollo.prediction.Vector\x12.\n\x0bsamples_std\x18\x03 \x01(\x0b2\x19.apollo.prediction.Vector\x12\x11\n\tnum_layer\x18\x04 \x01(\x05\x12\'\n\x05layer\x18\x05 \x03(\x0b2\x18.apollo.prediction.Layer\x12\x12\n\ndim_output\x18\x06 \x01(\x05')
_FNNVEHICLEMODEL = DESCRIPTOR.message_types_by_name['FnnVehicleModel']
FnnVehicleModel = _reflection.GeneratedProtocolMessageType('FnnVehicleModel', (_message.Message,), {'DESCRIPTOR': _FNNVEHICLEMODEL, '__module__': 'modules.prediction.proto.fnn_vehicle_model_pb2'})
_sym_db.RegisterMessage(FnnVehicleModel)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FNNVEHICLEMODEL._serialized_start = 119
    _FNNVEHICLEMODEL._serialized_end = 332