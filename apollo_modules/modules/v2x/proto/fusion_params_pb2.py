"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%modules/v2x/proto/fusion_params.proto\x12\x14apollo.v2x.ft.fusion"\x1d\n\x08KMParams\x12\x11\n\tmin_score\x18\x01 \x01(\x01"\x1d\n\x05Param\x12\t\n\x01k\x18\x01 \x01(\x01\x12\t\n\x01b\x18\x02 \x01(\x01"R\n\x11SingleCameraParam\x12\x11\n\tcamera_id\x18\x01 \x01(\x05\x12*\n\x05param\x18\x02 \x03(\x0b2\x1b.apollo.v2x.ft.fusion.Param"\xdc\x01\n\x0bScoreParams\x12\x12\n\nprob_scale\x18\x01 \x01(\x01\x12\x1a\n\x12max_match_distance\x18\x02 \x01(\x01\x12\x11\n\tmin_score\x18\x03 \x01(\x01\x12\'\n\x18use_mahalanobis_distance\x18\x04 \x01(\x08:\x05false\x12\x19\n\ncheck_type\x18\x05 \x01(\x08:\x05false\x12F\n\x10confidence_level\x18\x06 \x01(\x0e2%.apollo.v2x.ft.fusion.ConfidenceLevel:\x05C975P"\xba\x01\n\x0cFusionParams\x12>\n\rfusion_params\x18\x01 \x03(\x0b2\'.apollo.v2x.ft.fusion.SingleCameraParam\x121\n\tkm_params\x18\x02 \x01(\x0b2\x1e.apollo.v2x.ft.fusion.KMParams\x127\n\x0cscore_params\x18\x03 \x02(\x0b2!.apollo.v2x.ft.fusion.ScoreParams*:\n\x0fConfidenceLevel\x12\x08\n\x04C90P\x10\x00\x12\x08\n\x04C95P\x10\x01\x12\t\n\x05C975P\x10\x02\x12\x08\n\x04C99P\x10\x03')
_CONFIDENCELEVEL = DESCRIPTOR.enum_types_by_name['ConfidenceLevel']
ConfidenceLevel = enum_type_wrapper.EnumTypeWrapper(_CONFIDENCELEVEL)
C90P = 0
C95P = 1
C975P = 2
C99P = 3
_KMPARAMS = DESCRIPTOR.message_types_by_name['KMParams']
_PARAM = DESCRIPTOR.message_types_by_name['Param']
_SINGLECAMERAPARAM = DESCRIPTOR.message_types_by_name['SingleCameraParam']
_SCOREPARAMS = DESCRIPTOR.message_types_by_name['ScoreParams']
_FUSIONPARAMS = DESCRIPTOR.message_types_by_name['FusionParams']
KMParams = _reflection.GeneratedProtocolMessageType('KMParams', (_message.Message,), {'DESCRIPTOR': _KMPARAMS, '__module__': 'modules.v2x.proto.fusion_params_pb2'})
_sym_db.RegisterMessage(KMParams)
Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {'DESCRIPTOR': _PARAM, '__module__': 'modules.v2x.proto.fusion_params_pb2'})
_sym_db.RegisterMessage(Param)
SingleCameraParam = _reflection.GeneratedProtocolMessageType('SingleCameraParam', (_message.Message,), {'DESCRIPTOR': _SINGLECAMERAPARAM, '__module__': 'modules.v2x.proto.fusion_params_pb2'})
_sym_db.RegisterMessage(SingleCameraParam)
ScoreParams = _reflection.GeneratedProtocolMessageType('ScoreParams', (_message.Message,), {'DESCRIPTOR': _SCOREPARAMS, '__module__': 'modules.v2x.proto.fusion_params_pb2'})
_sym_db.RegisterMessage(ScoreParams)
FusionParams = _reflection.GeneratedProtocolMessageType('FusionParams', (_message.Message,), {'DESCRIPTOR': _FUSIONPARAMS, '__module__': 'modules.v2x.proto.fusion_params_pb2'})
_sym_db.RegisterMessage(FusionParams)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIDENCELEVEL._serialized_start = 621
    _CONFIDENCELEVEL._serialized_end = 679
    _KMPARAMS._serialized_start = 63
    _KMPARAMS._serialized_end = 92
    _PARAM._serialized_start = 94
    _PARAM._serialized_end = 123
    _SINGLECAMERAPARAM._serialized_start = 125
    _SINGLECAMERAPARAM._serialized_end = 207
    _SCOREPARAMS._serialized_start = 210
    _SCOREPARAMS._serialized_end = 430
    _FUSIONPARAMS._serialized_start = 433
    _FUSIONPARAMS._serialized_end = 619