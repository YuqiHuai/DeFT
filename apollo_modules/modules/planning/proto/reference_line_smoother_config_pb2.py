"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.planning.proto.math import cos_theta_smoother_config_pb2 as modules_dot_planning_dot_proto_dot_math_dot_cos__theta__smoother__config__pb2
from ....modules.planning.proto.math import fem_pos_deviation_smoother_config_pb2 as modules_dot_planning_dot_proto_dot_math_dot_fem__pos__deviation__smoother__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;modules/planning/proto/reference_line_smoother_config.proto\x12\x0fapollo.planning\x1a;modules/planning/proto/math/cos_theta_smoother_config.proto\x1aCmodules/planning/proto/math/fem_pos_deviation_smoother_config.proto"\xbf\x01\n\x16QpSplineSmootherConfig\x12\x17\n\x0cspline_order\x18\x01 \x01(\r:\x015\x12\x1d\n\x11max_spline_length\x18\x02 \x01(\x01:\x0225\x12"\n\x15regularization_weight\x18\x03 \x01(\x01:\x030.1\x12#\n\x18second_derivative_weight\x18\x04 \x01(\x01:\x010\x12$\n\x17third_derivative_weight\x18\x05 \x01(\x01:\x03100"\xa3\x02\n\x14SpiralSmootherConfig\x12\x1a\n\rmax_deviation\x18\x01 \x01(\x01:\x030.1\x12\x1c\n\x10piecewise_length\x18\x02 \x01(\x01:\x0210\x12\x1b\n\rmax_iteration\x18\x03 \x01(\r:\x041000\x12\x16\n\x07opt_tol\x18\x04 \x01(\x01:\x051e-08\x12!\n\x12opt_acceptable_tol\x18\x05 \x01(\x01:\x051e-06\x12$\n\x18opt_acceptable_iteration\x18\x06 \x01(\r:\x0215\x12\x1e\n\x13weight_curve_length\x18\x07 \x01(\x01:\x011\x12\x17\n\x0cweight_kappa\x18\x08 \x01(\x01:\x011\x12\x1a\n\rweight_dkappa\x18\t \x01(\x01:\x03100"\xa3\x03\n\x1cDiscretePointsSmootherConfig\x12t\n\x10smoothing_method\x18\x03 \x01(\x0e2=.apollo.planning.DiscretePointsSmootherConfig.SmoothingMethod:\x1bFEM_POS_DEVIATION_SMOOTHING\x12F\n\x13cos_theta_smoothing\x18\x04 \x01(\x0b2\'.apollo.planning.CosThetaSmootherConfigH\x00\x12U\n\x1bfem_pos_deviation_smoothing\x18\x05 \x01(\x0b2..apollo.planning.FemPosDeviationSmootherConfigH\x00"\\\n\x0fSmoothingMethod\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x17\n\x13COS_THETA_SMOOTHING\x10\x01\x12\x1f\n\x1bFEM_POS_DEVIATION_SMOOTHING\x10\x02B\x10\n\x0eSmootherConfig"\x80\x04\n\x1bReferenceLineSmootherConfig\x12"\n\x17max_constraint_interval\x18\x01 \x01(\x01:\x015\x12&\n\x1blongitudinal_boundary_bound\x18\x02 \x01(\x01:\x011\x12\'\n\x1amax_lateral_boundary_bound\x18\x03 \x01(\x01:\x030.5\x12\'\n\x1amin_lateral_boundary_bound\x18\x04 \x01(\x01:\x030.2\x12 \n\x13num_of_total_points\x18\x05 \x01(\r:\x03500\x12\x17\n\ncurb_shift\x18\x06 \x01(\x01:\x030.2\x12\x1b\n\x0elateral_buffer\x18\x07 \x01(\x01:\x030.2\x12\x18\n\nresolution\x18\x08 \x01(\x01:\x040.02\x12<\n\tqp_spline\x18\x14 \x01(\x0b2\'.apollo.planning.QpSplineSmootherConfigH\x00\x127\n\x06spiral\x18\x15 \x01(\x0b2%.apollo.planning.SpiralSmootherConfigH\x00\x12H\n\x0fdiscrete_points\x18\x16 \x01(\x0b2-.apollo.planning.DiscretePointsSmootherConfigH\x00B\x10\n\x0eSmootherConfig')
_QPSPLINESMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['QpSplineSmootherConfig']
_SPIRALSMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['SpiralSmootherConfig']
_DISCRETEPOINTSSMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['DiscretePointsSmootherConfig']
_REFERENCELINESMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['ReferenceLineSmootherConfig']
_DISCRETEPOINTSSMOOTHERCONFIG_SMOOTHINGMETHOD = _DISCRETEPOINTSSMOOTHERCONFIG.enum_types_by_name['SmoothingMethod']
QpSplineSmootherConfig = _reflection.GeneratedProtocolMessageType('QpSplineSmootherConfig', (_message.Message,), {'DESCRIPTOR': _QPSPLINESMOOTHERCONFIG, '__module__': 'modules.planning.proto.reference_line_smoother_config_pb2'})
_sym_db.RegisterMessage(QpSplineSmootherConfig)
SpiralSmootherConfig = _reflection.GeneratedProtocolMessageType('SpiralSmootherConfig', (_message.Message,), {'DESCRIPTOR': _SPIRALSMOOTHERCONFIG, '__module__': 'modules.planning.proto.reference_line_smoother_config_pb2'})
_sym_db.RegisterMessage(SpiralSmootherConfig)
DiscretePointsSmootherConfig = _reflection.GeneratedProtocolMessageType('DiscretePointsSmootherConfig', (_message.Message,), {'DESCRIPTOR': _DISCRETEPOINTSSMOOTHERCONFIG, '__module__': 'modules.planning.proto.reference_line_smoother_config_pb2'})
_sym_db.RegisterMessage(DiscretePointsSmootherConfig)
ReferenceLineSmootherConfig = _reflection.GeneratedProtocolMessageType('ReferenceLineSmootherConfig', (_message.Message,), {'DESCRIPTOR': _REFERENCELINESMOOTHERCONFIG, '__module__': 'modules.planning.proto.reference_line_smoother_config_pb2'})
_sym_db.RegisterMessage(ReferenceLineSmootherConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _QPSPLINESMOOTHERCONFIG._serialized_start = 211
    _QPSPLINESMOOTHERCONFIG._serialized_end = 402
    _SPIRALSMOOTHERCONFIG._serialized_start = 405
    _SPIRALSMOOTHERCONFIG._serialized_end = 696
    _DISCRETEPOINTSSMOOTHERCONFIG._serialized_start = 699
    _DISCRETEPOINTSSMOOTHERCONFIG._serialized_end = 1118
    _DISCRETEPOINTSSMOOTHERCONFIG_SMOOTHINGMETHOD._serialized_start = 1008
    _DISCRETEPOINTSSMOOTHERCONFIG_SMOOTHINGMETHOD._serialized_end = 1100
    _REFERENCELINESMOOTHERCONFIG._serialized_start = 1121
    _REFERENCELINESMOOTHERCONFIG._serialized_end = 1633