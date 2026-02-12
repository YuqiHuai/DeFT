"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/perception/onboard/proto/radar_component_config.proto\x12\x19apollo.perception.onboard"\x82\x02\n\x14RadarComponentConfig\x12\x12\n\nradar_name\x18\x01 \x01(\t\x12\x19\n\x11tf_child_frame_id\x18\x02 \x01(\t\x12\x1e\n\x16radar_forward_distance\x18\x03 \x01(\x01\x12!\n\x19radar_preprocessor_method\x18\x04 \x01(\t\x12\x1f\n\x17radar_perception_method\x18\x05 \x01(\t\x12\x1b\n\x13radar_pipeline_name\x18\x06 \x01(\t\x12\x1d\n\x15odometry_channel_name\x18\x07 \x01(\t\x12\x1b\n\x13output_channel_name\x18\x08 \x01(\t')
_RADARCOMPONENTCONFIG = DESCRIPTOR.message_types_by_name['RadarComponentConfig']
RadarComponentConfig = _reflection.GeneratedProtocolMessageType('RadarComponentConfig', (_message.Message,), {'DESCRIPTOR': _RADARCOMPONENTCONFIG, '__module__': 'modules.perception.onboard.proto.radar_component_config_pb2'})
_sym_db.RegisterMessage(RadarComponentConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _RADARCOMPONENTCONFIG._serialized_start = 93
    _RADARCOMPONENTCONFIG._serialized_end = 351