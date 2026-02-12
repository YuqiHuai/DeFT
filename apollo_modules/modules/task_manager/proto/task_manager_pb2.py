"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from ....modules.routing.proto import routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2
from ....modules.map.proto import map_parking_space_pb2 as modules_dot_map_dot_proto_dot_map__parking__space__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/task_manager/proto/task_manager.proto\x12\x13apollo.task_manager\x1a!modules/common/proto/header.proto\x1a#modules/routing/proto/routing.proto\x1a)modules/map/proto/map_parking_space.proto"^\n\x10CycleRoutingTask\x12\x11\n\tcycle_num\x18\x01 \x01(\x05\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"a\n\x12ParkingRoutingTask\x12\x12\n\nlane_width\x18\x01 \x01(\x01\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"\x8d\x01\n\x12DeadEndRoutingTask\x12:\n\x12routing_request_in\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest\x12;\n\x13routing_request_out\x18\x03 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"\xda\x02\n\x04Task\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x11\n\ttask_name\x18\x02 \x01(\t\x120\n\ttask_type\x18\x03 \x01(\x0e2\x1d.apollo.task_manager.TaskType\x12C\n\x12cycle_routing_task\x18\x04 \x01(\x0b2%.apollo.task_manager.CycleRoutingTaskH\x00\x12G\n\x14parking_routing_task\x18\x05 \x01(\x0b2\'.apollo.task_manager.ParkingRoutingTaskH\x00\x12H\n\x15dead_end_routing_task\x18\x06 \x01(\x0b2\'.apollo.task_manager.DeadEndRoutingTaskH\x00B\x0e\n\x0crouting_task*H\n\x08TaskType\x12\x11\n\rCYCLE_ROUTING\x10\x00\x12\x13\n\x0fPARKING_ROUTING\x10\x01\x12\x14\n\x10DEAD_END_ROUTING\x10\x03*d\n\x0cJunctionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02\x12\r\n\tFORK_ROAD\x10\x03\x12\r\n\tMAIN_SIDE\x10\x04\x12\x0c\n\x08DEAD_END\x10\x05')
_TASKTYPE = DESCRIPTOR.enum_types_by_name['TaskType']
TaskType = enum_type_wrapper.EnumTypeWrapper(_TASKTYPE)
_JUNCTIONTYPE = DESCRIPTOR.enum_types_by_name['JunctionType']
JunctionType = enum_type_wrapper.EnumTypeWrapper(_JUNCTIONTYPE)
CYCLE_ROUTING = 0
PARKING_ROUTING = 1
DEAD_END_ROUTING = 3
UNKNOWN = 0
IN_ROAD = 1
CROSS_ROAD = 2
FORK_ROAD = 3
MAIN_SIDE = 4
DEAD_END = 5
_CYCLEROUTINGTASK = DESCRIPTOR.message_types_by_name['CycleRoutingTask']
_PARKINGROUTINGTASK = DESCRIPTOR.message_types_by_name['ParkingRoutingTask']
_DEADENDROUTINGTASK = DESCRIPTOR.message_types_by_name['DeadEndRoutingTask']
_TASK = DESCRIPTOR.message_types_by_name['Task']
CycleRoutingTask = _reflection.GeneratedProtocolMessageType('CycleRoutingTask', (_message.Message,), {'DESCRIPTOR': _CYCLEROUTINGTASK, '__module__': 'modules.task_manager.proto.task_manager_pb2'})
_sym_db.RegisterMessage(CycleRoutingTask)
ParkingRoutingTask = _reflection.GeneratedProtocolMessageType('ParkingRoutingTask', (_message.Message,), {'DESCRIPTOR': _PARKINGROUTINGTASK, '__module__': 'modules.task_manager.proto.task_manager_pb2'})
_sym_db.RegisterMessage(ParkingRoutingTask)
DeadEndRoutingTask = _reflection.GeneratedProtocolMessageType('DeadEndRoutingTask', (_message.Message,), {'DESCRIPTOR': _DEADENDROUTINGTASK, '__module__': 'modules.task_manager.proto.task_manager_pb2'})
_sym_db.RegisterMessage(DeadEndRoutingTask)
Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {'DESCRIPTOR': _TASK, '__module__': 'modules.task_manager.proto.task_manager_pb2'})
_sym_db.RegisterMessage(Task)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TASKTYPE._serialized_start = 873
    _TASKTYPE._serialized_end = 945
    _JUNCTIONTYPE._serialized_start = 947
    _JUNCTIONTYPE._serialized_end = 1047
    _CYCLEROUTINGTASK._serialized_start = 185
    _CYCLEROUTINGTASK._serialized_end = 279
    _PARKINGROUTINGTASK._serialized_start = 281
    _PARKINGROUTINGTASK._serialized_end = 378
    _DEADENDROUTINGTASK._serialized_start = 381
    _DEADENDROUTINGTASK._serialized_end = 522
    _TASK._serialized_start = 525
    _TASK._serialized_end = 871