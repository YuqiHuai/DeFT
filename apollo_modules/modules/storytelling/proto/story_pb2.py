"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/storytelling/proto/story.proto\x12\x13apollo.storytelling\x1a!modules/common/proto/header.proto"5\n\x10CloseToCrosswalk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08distance\x18\x02 \x01(\x01:\x03nan"5\n\x10CloseToClearArea\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08distance\x18\x02 \x01(\x01:\x03nan"\xa5\x01\n\x0fCloseToJunction\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e21.apollo.storytelling.CloseToJunction.JunctionType\x12\x15\n\x08distance\x18\x03 \x01(\x01:\x03nan".\n\x0cJunctionType\x12\x10\n\x0cPNC_JUNCTION\x10\x01\x12\x0c\n\x08JUNCTION\x10\x02"2\n\rCloseToSignal\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08distance\x18\x02 \x01(\x01:\x03nan"4\n\x0fCloseToStopSign\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08distance\x18\x02 \x01(\x01:\x03nan"5\n\x10CloseToYieldSign\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08distance\x18\x02 \x01(\x01:\x03nan"\xbb\x03\n\x07Stories\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12B\n\x13close_to_clear_area\x18\x02 \x01(\x0b2%.apollo.storytelling.CloseToClearArea\x12A\n\x12close_to_crosswalk\x18\x03 \x01(\x0b2%.apollo.storytelling.CloseToCrosswalk\x12?\n\x11close_to_junction\x18\x04 \x01(\x0b2$.apollo.storytelling.CloseToJunction\x12;\n\x0fclose_to_signal\x18\x05 \x01(\x0b2".apollo.storytelling.CloseToSignal\x12@\n\x12close_to_stop_sign\x18\x06 \x01(\x0b2$.apollo.storytelling.CloseToStopSign\x12B\n\x13close_to_yield_sign\x18\x07 \x01(\x0b2%.apollo.storytelling.CloseToYieldSign')
_CLOSETOCROSSWALK = DESCRIPTOR.message_types_by_name['CloseToCrosswalk']
_CLOSETOCLEARAREA = DESCRIPTOR.message_types_by_name['CloseToClearArea']
_CLOSETOJUNCTION = DESCRIPTOR.message_types_by_name['CloseToJunction']
_CLOSETOSIGNAL = DESCRIPTOR.message_types_by_name['CloseToSignal']
_CLOSETOSTOPSIGN = DESCRIPTOR.message_types_by_name['CloseToStopSign']
_CLOSETOYIELDSIGN = DESCRIPTOR.message_types_by_name['CloseToYieldSign']
_STORIES = DESCRIPTOR.message_types_by_name['Stories']
_CLOSETOJUNCTION_JUNCTIONTYPE = _CLOSETOJUNCTION.enum_types_by_name['JunctionType']
CloseToCrosswalk = _reflection.GeneratedProtocolMessageType('CloseToCrosswalk', (_message.Message,), {'DESCRIPTOR': _CLOSETOCROSSWALK, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(CloseToCrosswalk)
CloseToClearArea = _reflection.GeneratedProtocolMessageType('CloseToClearArea', (_message.Message,), {'DESCRIPTOR': _CLOSETOCLEARAREA, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(CloseToClearArea)
CloseToJunction = _reflection.GeneratedProtocolMessageType('CloseToJunction', (_message.Message,), {'DESCRIPTOR': _CLOSETOJUNCTION, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(CloseToJunction)
CloseToSignal = _reflection.GeneratedProtocolMessageType('CloseToSignal', (_message.Message,), {'DESCRIPTOR': _CLOSETOSIGNAL, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(CloseToSignal)
CloseToStopSign = _reflection.GeneratedProtocolMessageType('CloseToStopSign', (_message.Message,), {'DESCRIPTOR': _CLOSETOSTOPSIGN, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(CloseToStopSign)
CloseToYieldSign = _reflection.GeneratedProtocolMessageType('CloseToYieldSign', (_message.Message,), {'DESCRIPTOR': _CLOSETOYIELDSIGN, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(CloseToYieldSign)
Stories = _reflection.GeneratedProtocolMessageType('Stories', (_message.Message,), {'DESCRIPTOR': _STORIES, '__module__': 'modules.storytelling.proto.story_pb2'})
_sym_db.RegisterMessage(Stories)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CLOSETOCROSSWALK._serialized_start = 98
    _CLOSETOCROSSWALK._serialized_end = 151
    _CLOSETOCLEARAREA._serialized_start = 153
    _CLOSETOCLEARAREA._serialized_end = 206
    _CLOSETOJUNCTION._serialized_start = 209
    _CLOSETOJUNCTION._serialized_end = 374
    _CLOSETOJUNCTION_JUNCTIONTYPE._serialized_start = 328
    _CLOSETOJUNCTION_JUNCTIONTYPE._serialized_end = 374
    _CLOSETOSIGNAL._serialized_start = 376
    _CLOSETOSIGNAL._serialized_end = 426
    _CLOSETOSTOPSIGN._serialized_start = 428
    _CLOSETOSTOPSIGN._serialized_end = 480
    _CLOSETOYIELDSIGN._serialized_start = 482
    _CLOSETOYIELDSIGN._serialized_end = 535
    _STORIES._serialized_start = 538
    _STORIES._serialized_end = 981