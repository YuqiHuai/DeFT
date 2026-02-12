"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/perception/onboard/proto/fusion_component_config.proto\x12\x19apollo.perception.onboard"\xdf\x02\n\x15FusionComponentConfig\x12.\n\x0bfusion_name\x18\x01 \x01(\t:\x19ObstacleMultiSensorFusion\x12\x15\n\rfusion_method\x18\x02 \x01(\t\x12\x1a\n\x12fusion_main_sensor\x18\x03 \x01(\t\x12\x1b\n\x13object_in_roi_check\x18\x04 \x01(\x08\x12#\n\x1bradius_for_roi_object_check\x18\x05 \x01(\x01\x12D\n\x1doutput_obstacles_channel_name\x18\x06 \x01(\t:\x1d/perception/vehicle/obstacles\x12[\n%output_viz_fused_content_channel_name\x18\x07 \x01(\t:,/perception/inner/visualization/FusedObjects')
_FUSIONCOMPONENTCONFIG = DESCRIPTOR.message_types_by_name['FusionComponentConfig']
FusionComponentConfig = _reflection.GeneratedProtocolMessageType('FusionComponentConfig', (_message.Message,), {'DESCRIPTOR': _FUSIONCOMPONENTCONFIG, '__module__': 'modules.perception.onboard.proto.fusion_component_config_pb2'})
_sym_db.RegisterMessage(FusionComponentConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FUSIONCOMPONENTCONFIG._serialized_start = 94
    _FUSIONCOMPONENTCONFIG._serialized_end = 445