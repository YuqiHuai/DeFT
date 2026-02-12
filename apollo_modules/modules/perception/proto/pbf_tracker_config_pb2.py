"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/perception/proto/pbf_tracker_config.proto\x12\x18apollo.perception.fusion"\xd1\x01\n\x10PbfTrackerConfig\x12)\n\x12type_fusion_method\x18\x01 \x01(\t:\rDstTypeFusion\x120\n\x14motion_fusion_method\x18\x02 \x01(\t:\x12KalmanMotionFusion\x12+\n\x13shape_fusion_method\x18\x03 \x01(\t:\x0ePbfShapeFusion\x123\n\x17existence_fusion_method\x18\x04 \x01(\t:\x12DstExistenceFusion')
_PBFTRACKERCONFIG = DESCRIPTOR.message_types_by_name['PbfTrackerConfig']
PbfTrackerConfig = _reflection.GeneratedProtocolMessageType('PbfTrackerConfig', (_message.Message,), {'DESCRIPTOR': _PBFTRACKERCONFIG, '__module__': 'modules.perception.proto.pbf_tracker_config_pb2'})
_sym_db.RegisterMessage(PbfTrackerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PBFTRACKERCONFIG._serialized_start = 80
    _PBFTRACKERCONFIG._serialized_end = 289