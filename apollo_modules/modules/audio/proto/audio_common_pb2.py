"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/audio/proto/audio_common.proto\x12\x0capollo.audio*K\n\x0cMovingResult\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bAPPROACHING\x10\x01\x12\r\n\tDEPARTING\x10\x02\x12\x0e\n\nSTATIONARY\x10\x03*G\n\tAudioType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\n\n\x06POLICE\x10\x01\x12\r\n\tAMBULANCE\x10\x02\x12\r\n\tFIRETRUCK\x10\x03*Q\n\x0eAudioDirection\x12\x15\n\x11UNKNOWN_DIRECTION\x10\x00\x12\t\n\x05FRONT\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\x08\n\x04BACK\x10\x03\x12\t\n\x05RIGHT\x10\x04')
_MOVINGRESULT = DESCRIPTOR.enum_types_by_name['MovingResult']
MovingResult = enum_type_wrapper.EnumTypeWrapper(_MOVINGRESULT)
_AUDIOTYPE = DESCRIPTOR.enum_types_by_name['AudioType']
AudioType = enum_type_wrapper.EnumTypeWrapper(_AUDIOTYPE)
_AUDIODIRECTION = DESCRIPTOR.enum_types_by_name['AudioDirection']
AudioDirection = enum_type_wrapper.EnumTypeWrapper(_AUDIODIRECTION)
UNKNOWN = 0
APPROACHING = 1
DEPARTING = 2
STATIONARY = 3
UNKNOWN_TYPE = 0
POLICE = 1
AMBULANCE = 2
FIRETRUCK = 3
UNKNOWN_DIRECTION = 0
FRONT = 1
LEFT = 2
BACK = 3
RIGHT = 4
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MOVINGRESULT._serialized_start = 56
    _MOVINGRESULT._serialized_end = 131
    _AUDIOTYPE._serialized_start = 133
    _AUDIOTYPE._serialized_end = 204
    _AUDIODIRECTION._serialized_start = 206
    _AUDIODIRECTION._serialized_end = 287