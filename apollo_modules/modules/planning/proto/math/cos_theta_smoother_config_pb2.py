"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;modules/planning/proto/math/cos_theta_smoother_config.proto\x12\x0fapollo.planning"\xc8\x02\n\x16CosThetaSmootherConfig\x12(\n\x19weight_cos_included_angle\x18\x01 \x01(\x01:\x0510000\x12\x1f\n\x14weight_anchor_points\x18\x02 \x01(\x01:\x011\x12\x18\n\rweight_length\x18\x03 \x01(\x01:\x011\x12\x16\n\x0bprint_level\x18\x04 \x01(\x05:\x010\x12"\n\x15max_num_of_iterations\x18\x05 \x01(\x05:\x03500\x12(\n\x1cacceptable_num_of_iterations\x18\x06 \x01(\x05:\x0215\x12\x12\n\x03tol\x18\x07 \x01(\x01:\x051e-08\x12\x1b\n\x0eacceptable_tol\x18\x08 \x01(\x01:\x030.1\x122\n#ipopt_use_automatic_differentiation\x18\t \x01(\x08:\x05false')
_COSTHETASMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['CosThetaSmootherConfig']
CosThetaSmootherConfig = _reflection.GeneratedProtocolMessageType('CosThetaSmootherConfig', (_message.Message,), {'DESCRIPTOR': _COSTHETASMOOTHERCONFIG, '__module__': 'modules.planning.proto.math.cos_theta_smoother_config_pb2'})
_sym_db.RegisterMessage(CosThetaSmootherConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _COSTHETASMOOTHERCONFIG._serialized_start = 81
    _COSTHETASMOOTHERCONFIG._serialized_end = 409