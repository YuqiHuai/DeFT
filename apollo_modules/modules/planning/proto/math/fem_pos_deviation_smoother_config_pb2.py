"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCmodules/planning/proto/math/fem_pos_deviation_smoother_config.proto\x12\x0fapollo.planning"\xb6\x05\n\x1dFemPosDeviationSmootherConfig\x12-\n\x18weight_fem_pos_deviation\x18\x02 \x01(\x01:\x0b10000000000\x12\x1f\n\x14weight_ref_deviation\x18\x03 \x01(\x01:\x011\x12\x1d\n\x12weight_path_length\x18\x04 \x01(\x01:\x011\x12)\n\x1aapply_curvature_constraint\x18\x05 \x01(\x08:\x05false\x122\n%weight_curvature_constraint_slack_var\x18\x06 \x01(\x01:\x03100\x12!\n\x14curvature_constraint\x18\x07 \x01(\x01:\x030.2\x12\x16\n\x07use_sqp\x18\x08 \x01(\x08:\x05false\x12\x18\n\x08sqp_ftol\x18\t \x01(\x01:\x060.0001\x12\x17\n\x08sqp_ctol\x18\n \x01(\x01:\x050.001\x12\x1c\n\x10sqp_pen_max_iter\x18\x0b \x01(\x05:\x0210\x12\x1d\n\x10sqp_sub_max_iter\x18\x0c \x01(\x05:\x03100\x12\x15\n\x08max_iter\x18d \x01(\x05:\x03500\x12\x15\n\ntime_limit\x18e \x01(\x01:\x010\x12\x16\n\x07verbose\x18f \x01(\x08:\x05false\x12 \n\x12scaled_termination\x18g \x01(\x08:\x04true\x12\x18\n\nwarm_start\x18h \x01(\x08:\x04true\x12\x17\n\x0bprint_level\x18\xc8\x01 \x01(\x05:\x010\x12#\n\x15max_num_of_iterations\x18\xc9\x01 \x01(\x05:\x03500\x12)\n\x1cacceptable_num_of_iterations\x18\xca\x01 \x01(\x05:\x0215\x12\x13\n\x03tol\x18\xcb\x01 \x01(\x01:\x051e-08\x12\x1c\n\x0eacceptable_tol\x18\xcc\x01 \x01(\x01:\x030.1')
_FEMPOSDEVIATIONSMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['FemPosDeviationSmootherConfig']
FemPosDeviationSmootherConfig = _reflection.GeneratedProtocolMessageType('FemPosDeviationSmootherConfig', (_message.Message,), {'DESCRIPTOR': _FEMPOSDEVIATIONSMOOTHERCONFIG, '__module__': 'modules.planning.proto.math.fem_pos_deviation_smoother_config_pb2'})
_sym_db.RegisterMessage(FemPosDeviationSmootherConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FEMPOSDEVIATIONSMOOTHERCONFIG._serialized_start = 89
    _FEMPOSDEVIATIONSMOOTHERCONFIG._serialized_end = 783