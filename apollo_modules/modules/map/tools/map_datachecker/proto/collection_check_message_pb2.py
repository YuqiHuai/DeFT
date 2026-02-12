"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.map.tools.map_datachecker.proto import collection_error_code_pb2 as modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFmodules/map/tools/map_datachecker/proto/collection_check_message.proto\x12\x0capollo.hdmap\x1aCmodules/map/tools/map_datachecker/proto/collection_error_code.proto"3\n\x0bVerifyRange\x12\x12\n\nstart_time\x18\x01 \x01(\x01\x12\x10\n\x08end_time\x18\x02 \x01(\x01"2\n\nLoopResult\x12\x12\n\nis_reached\x18\x01 \x02(\x08\x12\x10\n\x08loop_num\x18\x02 \x01(\x01"!\n\x0bTopicResult\x12\x12\n\ntopic_lack\x18\x01 \x03(\t"`\n\tFrameRate\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x15\n\rexpected_rate\x18\x02 \x01(\x01\x12\x14\n\x0ccurrent_rate\x18\x03 \x01(\x01\x12\x17\n\x0fbad_record_name\x18\x04 \x03(\t"a\n\x0cVerifyResult\x12)\n\x06topics\x18\x01 \x01(\x0b2\x19.apollo.hdmap.TopicResult\x12&\n\x05rates\x18\x02 \x03(\x0b2\x17.apollo.hdmap.FrameRate"\\\n\x14ChannelVerifyRequest\x12"\n\x03cmd\x18\x01 \x01(\x0e2\x15.apollo.hdmap.CmdType\x12\x12\n\ncollect_id\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t"j\n\x15ChannelVerifyResponse\x12%\n\x04code\x18\x01 \x01(\x0e2\x17.apollo.hdmap.ErrorCode\x12*\n\x06result\x18\x02 \x01(\x0b2\x1a.apollo.hdmap.VerifyResult"\x88\x01\n\x12LoopsVerifyRequest\x12"\n\x03cmd\x18\x01 \x01(\x0e2\x15.apollo.hdmap.CmdType\x12$\n\x04type\x18\x02 \x01(\x0e2\x16.apollo.hdmap.DataType\x12(\n\x05range\x18\x03 \x03(\x0b2\x19.apollo.hdmap.VerifyRange"}\n\x13LoopsVerifyResponse\x12%\n\x04code\x18\x01 \x01(\x0e2\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01\x12-\n\x0bloop_result\x18\x03 \x01(\x0b2\x18.apollo.hdmap.LoopResult"9\n\x13DynamicAlignRequest\x12"\n\x03cmd\x18\x01 \x01(\x0e2\x15.apollo.hdmap.CmdType"O\n\x14DynamicAlignResponse\x12%\n\x04code\x18\x01 \x01(\x0e2\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01"8\n\x12StaticAlignRequest\x12"\n\x03cmd\x18\x01 \x01(\x0e2\x15.apollo.hdmap.CmdType"N\n\x13StaticAlignResponse\x12%\n\x04code\x18\x01 \x01(\x0e2\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01"7\n\x11EightRouteRequest\x12"\n\x03cmd\x18\x01 \x01(\x0e2\x15.apollo.hdmap.CmdType"M\n\x12EightRouteResponse\x12%\n\x04code\x18\x01 \x01(\x0e2\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01*)\n\x07CmdType\x12\t\n\x05START\x10\x01\x12\t\n\x05CHECK\x10\x02\x12\x08\n\x04STOP\x10\x03*,\n\x08DataType\x12\x0e\n\nMAP_MAKING\x10\x01\x12\x10\n\x0cMAP_CHECKOUT\x10\x02')
_CMDTYPE = DESCRIPTOR.enum_types_by_name['CmdType']
CmdType = enum_type_wrapper.EnumTypeWrapper(_CMDTYPE)
_DATATYPE = DESCRIPTOR.enum_types_by_name['DataType']
DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
START = 1
CHECK = 2
STOP = 3
MAP_MAKING = 1
MAP_CHECKOUT = 2
_VERIFYRANGE = DESCRIPTOR.message_types_by_name['VerifyRange']
_LOOPRESULT = DESCRIPTOR.message_types_by_name['LoopResult']
_TOPICRESULT = DESCRIPTOR.message_types_by_name['TopicResult']
_FRAMERATE = DESCRIPTOR.message_types_by_name['FrameRate']
_VERIFYRESULT = DESCRIPTOR.message_types_by_name['VerifyResult']
_CHANNELVERIFYREQUEST = DESCRIPTOR.message_types_by_name['ChannelVerifyRequest']
_CHANNELVERIFYRESPONSE = DESCRIPTOR.message_types_by_name['ChannelVerifyResponse']
_LOOPSVERIFYREQUEST = DESCRIPTOR.message_types_by_name['LoopsVerifyRequest']
_LOOPSVERIFYRESPONSE = DESCRIPTOR.message_types_by_name['LoopsVerifyResponse']
_DYNAMICALIGNREQUEST = DESCRIPTOR.message_types_by_name['DynamicAlignRequest']
_DYNAMICALIGNRESPONSE = DESCRIPTOR.message_types_by_name['DynamicAlignResponse']
_STATICALIGNREQUEST = DESCRIPTOR.message_types_by_name['StaticAlignRequest']
_STATICALIGNRESPONSE = DESCRIPTOR.message_types_by_name['StaticAlignResponse']
_EIGHTROUTEREQUEST = DESCRIPTOR.message_types_by_name['EightRouteRequest']
_EIGHTROUTERESPONSE = DESCRIPTOR.message_types_by_name['EightRouteResponse']
VerifyRange = _reflection.GeneratedProtocolMessageType('VerifyRange', (_message.Message,), {'DESCRIPTOR': _VERIFYRANGE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(VerifyRange)
LoopResult = _reflection.GeneratedProtocolMessageType('LoopResult', (_message.Message,), {'DESCRIPTOR': _LOOPRESULT, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(LoopResult)
TopicResult = _reflection.GeneratedProtocolMessageType('TopicResult', (_message.Message,), {'DESCRIPTOR': _TOPICRESULT, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(TopicResult)
FrameRate = _reflection.GeneratedProtocolMessageType('FrameRate', (_message.Message,), {'DESCRIPTOR': _FRAMERATE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(FrameRate)
VerifyResult = _reflection.GeneratedProtocolMessageType('VerifyResult', (_message.Message,), {'DESCRIPTOR': _VERIFYRESULT, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(VerifyResult)
ChannelVerifyRequest = _reflection.GeneratedProtocolMessageType('ChannelVerifyRequest', (_message.Message,), {'DESCRIPTOR': _CHANNELVERIFYREQUEST, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(ChannelVerifyRequest)
ChannelVerifyResponse = _reflection.GeneratedProtocolMessageType('ChannelVerifyResponse', (_message.Message,), {'DESCRIPTOR': _CHANNELVERIFYRESPONSE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(ChannelVerifyResponse)
LoopsVerifyRequest = _reflection.GeneratedProtocolMessageType('LoopsVerifyRequest', (_message.Message,), {'DESCRIPTOR': _LOOPSVERIFYREQUEST, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(LoopsVerifyRequest)
LoopsVerifyResponse = _reflection.GeneratedProtocolMessageType('LoopsVerifyResponse', (_message.Message,), {'DESCRIPTOR': _LOOPSVERIFYRESPONSE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(LoopsVerifyResponse)
DynamicAlignRequest = _reflection.GeneratedProtocolMessageType('DynamicAlignRequest', (_message.Message,), {'DESCRIPTOR': _DYNAMICALIGNREQUEST, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(DynamicAlignRequest)
DynamicAlignResponse = _reflection.GeneratedProtocolMessageType('DynamicAlignResponse', (_message.Message,), {'DESCRIPTOR': _DYNAMICALIGNRESPONSE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(DynamicAlignResponse)
StaticAlignRequest = _reflection.GeneratedProtocolMessageType('StaticAlignRequest', (_message.Message,), {'DESCRIPTOR': _STATICALIGNREQUEST, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(StaticAlignRequest)
StaticAlignResponse = _reflection.GeneratedProtocolMessageType('StaticAlignResponse', (_message.Message,), {'DESCRIPTOR': _STATICALIGNRESPONSE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(StaticAlignResponse)
EightRouteRequest = _reflection.GeneratedProtocolMessageType('EightRouteRequest', (_message.Message,), {'DESCRIPTOR': _EIGHTROUTEREQUEST, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(EightRouteRequest)
EightRouteResponse = _reflection.GeneratedProtocolMessageType('EightRouteResponse', (_message.Message,), {'DESCRIPTOR': _EIGHTROUTERESPONSE, '__module__': 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'})
_sym_db.RegisterMessage(EightRouteResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CMDTYPE._serialized_start = 1376
    _CMDTYPE._serialized_end = 1417
    _DATATYPE._serialized_start = 1419
    _DATATYPE._serialized_end = 1463
    _VERIFYRANGE._serialized_start = 157
    _VERIFYRANGE._serialized_end = 208
    _LOOPRESULT._serialized_start = 210
    _LOOPRESULT._serialized_end = 260
    _TOPICRESULT._serialized_start = 262
    _TOPICRESULT._serialized_end = 295
    _FRAMERATE._serialized_start = 297
    _FRAMERATE._serialized_end = 393
    _VERIFYRESULT._serialized_start = 395
    _VERIFYRESULT._serialized_end = 492
    _CHANNELVERIFYREQUEST._serialized_start = 494
    _CHANNELVERIFYREQUEST._serialized_end = 586
    _CHANNELVERIFYRESPONSE._serialized_start = 588
    _CHANNELVERIFYRESPONSE._serialized_end = 694
    _LOOPSVERIFYREQUEST._serialized_start = 697
    _LOOPSVERIFYREQUEST._serialized_end = 833
    _LOOPSVERIFYRESPONSE._serialized_start = 835
    _LOOPSVERIFYRESPONSE._serialized_end = 960
    _DYNAMICALIGNREQUEST._serialized_start = 962
    _DYNAMICALIGNREQUEST._serialized_end = 1019
    _DYNAMICALIGNRESPONSE._serialized_start = 1021
    _DYNAMICALIGNRESPONSE._serialized_end = 1100
    _STATICALIGNREQUEST._serialized_start = 1102
    _STATICALIGNREQUEST._serialized_end = 1158
    _STATICALIGNRESPONSE._serialized_start = 1160
    _STATICALIGNRESPONSE._serialized_end = 1238
    _EIGHTROUTEREQUEST._serialized_start = 1240
    _EIGHTROUTEREQUEST._serialized_end = 1295
    _EIGHTROUTERESPONSE._serialized_start = 1297
    _EIGHTROUTERESPONSE._serialized_end = 1374