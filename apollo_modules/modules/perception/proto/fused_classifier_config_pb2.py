"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/perception/proto/fused_classifier_config.proto\x12\x17apollo.perception.lidar"\xec\x01\n\x15FusedClassifierConfig\x12\x1b\n\x0ftemporal_window\x18\x01 \x01(\x01:\x0220\x12$\n\x16enable_temporal_fusion\x18\x02 \x01(\x08:\x04true\x125\n\x16one_shot_fusion_method\x18\x03 \x01(\t:\x15CCRFOneShotTypeFusion\x126\n\x16sequence_fusion_method\x18\x04 \x01(\t:\x16CCRFSequenceTypeFusion\x12!\n\x13use_tracked_objects\x18\x05 \x01(\x08:\x04true')
_FUSEDCLASSIFIERCONFIG = DESCRIPTOR.message_types_by_name['FusedClassifierConfig']
FusedClassifierConfig = _reflection.GeneratedProtocolMessageType('FusedClassifierConfig', (_message.Message,), {'DESCRIPTOR': _FUSEDCLASSIFIERCONFIG, '__module__': 'modules.perception.proto.fused_classifier_config_pb2'})
_sym_db.RegisterMessage(FusedClassifierConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FUSEDCLASSIFIERCONFIG._serialized_start = 84
    _FUSEDCLASSIFIERCONFIG._serialized_end = 320