"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/perception/proto/roi_boundary_filter_config.proto\x12\x17apollo.perception.lidar"\xa6\x01\n\x17ROIBoundaryFilterConfig\x12)\n\x1edistance_to_boundary_threshold\x18\x01 \x01(\x01:\x011\x12!\n\x14confidence_threshold\x18\x02 \x01(\x02:\x030.5\x12 \n\x13cross_roi_threshold\x18\x03 \x01(\x02:\x030.6\x12\x1b\n\x10inside_threshold\x18\x04 \x01(\x01:\x011')
_ROIBOUNDARYFILTERCONFIG = DESCRIPTOR.message_types_by_name['ROIBoundaryFilterConfig']
ROIBoundaryFilterConfig = _reflection.GeneratedProtocolMessageType('ROIBoundaryFilterConfig', (_message.Message,), {'DESCRIPTOR': _ROIBOUNDARYFILTERCONFIG, '__module__': 'modules.perception.proto.roi_boundary_filter_config_pb2'})
_sym_db.RegisterMessage(ROIBoundaryFilterConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ROIBOUNDARYFILTERCONFIG._serialized_start = 87
    _ROIBOUNDARYFILTERCONFIG._serialized_end = 253