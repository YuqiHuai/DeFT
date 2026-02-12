"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/planning/proto/math/qp_problem.proto\x12\x0fapollo.planning"\xbd\x02\n\x1bQuadraticProgrammingProblem\x12\x12\n\nparam_size\x18\x01 \x01(\x05\x123\n\x10quadratic_matrix\x18\x02 \x01(\x0b2\x19.apollo.planning.QPMatrix\x12\x0c\n\x04bias\x18\x03 \x03(\x01\x122\n\x0fequality_matrix\x18\x04 \x01(\x0b2\x19.apollo.planning.QPMatrix\x12\x16\n\x0eequality_value\x18\x05 \x03(\x01\x124\n\x11inequality_matrix\x18\x06 \x01(\x0b2\x19.apollo.planning.QPMatrix\x12\x18\n\x10inequality_value\x18\x07 \x03(\x01\x12\x14\n\x0cinput_marker\x18\x08 \x03(\x01\x12\x15\n\roptimal_param\x18\t \x03(\x01"?\n\x08QPMatrix\x12\x10\n\x08row_size\x18\x01 \x01(\x05\x12\x10\n\x08col_size\x18\x02 \x01(\x05\x12\x0f\n\x07element\x18\x03 \x03(\x01"_\n\x1eQuadraticProgrammingProblemSet\x12=\n\x07problem\x18\x01 \x03(\x0b2,.apollo.planning.QuadraticProgrammingProblem')
_QUADRATICPROGRAMMINGPROBLEM = DESCRIPTOR.message_types_by_name['QuadraticProgrammingProblem']
_QPMATRIX = DESCRIPTOR.message_types_by_name['QPMatrix']
_QUADRATICPROGRAMMINGPROBLEMSET = DESCRIPTOR.message_types_by_name['QuadraticProgrammingProblemSet']
QuadraticProgrammingProblem = _reflection.GeneratedProtocolMessageType('QuadraticProgrammingProblem', (_message.Message,), {'DESCRIPTOR': _QUADRATICPROGRAMMINGPROBLEM, '__module__': 'modules.planning.proto.math.qp_problem_pb2'})
_sym_db.RegisterMessage(QuadraticProgrammingProblem)
QPMatrix = _reflection.GeneratedProtocolMessageType('QPMatrix', (_message.Message,), {'DESCRIPTOR': _QPMATRIX, '__module__': 'modules.planning.proto.math.qp_problem_pb2'})
_sym_db.RegisterMessage(QPMatrix)
QuadraticProgrammingProblemSet = _reflection.GeneratedProtocolMessageType('QuadraticProgrammingProblemSet', (_message.Message,), {'DESCRIPTOR': _QUADRATICPROGRAMMINGPROBLEMSET, '__module__': 'modules.planning.proto.math.qp_problem_pb2'})
_sym_db.RegisterMessage(QuadraticProgrammingProblemSet)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _QUADRATICPROGRAMMINGPROBLEM._serialized_start = 66
    _QUADRATICPROGRAMMINGPROBLEM._serialized_end = 383
    _QPMATRIX._serialized_start = 385
    _QPMATRIX._serialized_end = 448
    _QUADRATICPROGRAMMINGPROBLEMSET._serialized_start = 450
    _QUADRATICPROGRAMMINGPROBLEMSET._serialized_end = 545