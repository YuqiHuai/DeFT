"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/common/proto/direction.proto\x12\rapollo.common*q\n\tDirection\x12\x08\n\x04EAST\x10\x00\x12\x08\n\x04WEST\x10\x01\x12\t\n\x05SOUTH\x10\x02\x12\t\n\x05NORTH\x10\x03\x12\r\n\tNORTHEAST\x10\x04\x12\r\n\tSOUTHEAST\x10\x05\x12\r\n\tSOUTHWEST\x10\x06\x12\r\n\tNORTHWEST\x10\x07')
_DIRECTION = DESCRIPTOR.enum_types_by_name['Direction']
Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
EAST = 0
WEST = 1
SOUTH = 2
NORTH = 3
NORTHEAST = 4
SOUTHEAST = 5
SOUTHWEST = 6
NORTHWEST = 7
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DIRECTION._serialized_start = 55
    _DIRECTION._serialized_end = 168