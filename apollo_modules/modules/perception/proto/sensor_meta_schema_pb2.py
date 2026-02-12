"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/perception/proto/sensor_meta_schema.proto\x12\x11apollo.perception"\xad\x04\n\nSensorMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x126\n\x04type\x18\x02 \x01(\x0e2(.apollo.perception.SensorMeta.SensorType\x12D\n\x0borientation\x18\x03 \x01(\x0e2/.apollo.perception.SensorMeta.SensorOrientation"\xf7\x01\n\nSensorType\x12 \n\x13UNKNOWN_SENSOR_TYPE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0f\n\x0bVELODYNE_64\x10\x00\x12\x0f\n\x0bVELODYNE_32\x10\x01\x12\x0f\n\x0bVELODYNE_16\x10\x02\x12\r\n\tLDLIDAR_4\x10\x03\x12\r\n\tLDLIDAR_1\x10\x04\x12\x15\n\x11SHORT_RANGE_RADAR\x10\x05\x12\x14\n\x10LONG_RANGE_RADAR\x10\x06\x12\x14\n\x10MONOCULAR_CAMERA\x10\x07\x12\x11\n\rSTEREO_CAMERA\x10\x08\x12\x0e\n\nULTRASONIC\x10\t\x12\x10\n\x0cVELODYNE_128\x10\n"\x98\x01\n\x11SensorOrientation\x12\t\n\x05FRONT\x10\x00\x12\x10\n\x0cLEFT_FORWARD\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\x11\n\rLEFT_BACKWARD\x10\x03\x12\x08\n\x04REAR\x10\x04\x12\x12\n\x0eRIGHT_BACKWARD\x10\x05\x12\t\n\x05RIGHT\x10\x06\x12\x11\n\rRIGHT_FORWARD\x10\x07\x12\r\n\tPANORAMIC\x10\x08"E\n\x0fMultiSensorMeta\x122\n\x0bsensor_meta\x18\x01 \x03(\x0b2\x1d.apollo.perception.SensorMeta')
_SENSORMETA = DESCRIPTOR.message_types_by_name['SensorMeta']
_MULTISENSORMETA = DESCRIPTOR.message_types_by_name['MultiSensorMeta']
_SENSORMETA_SENSORTYPE = _SENSORMETA.enum_types_by_name['SensorType']
_SENSORMETA_SENSORORIENTATION = _SENSORMETA.enum_types_by_name['SensorOrientation']
SensorMeta = _reflection.GeneratedProtocolMessageType('SensorMeta', (_message.Message,), {'DESCRIPTOR': _SENSORMETA, '__module__': 'modules.perception.proto.sensor_meta_schema_pb2'})
_sym_db.RegisterMessage(SensorMeta)
MultiSensorMeta = _reflection.GeneratedProtocolMessageType('MultiSensorMeta', (_message.Message,), {'DESCRIPTOR': _MULTISENSORMETA, '__module__': 'modules.perception.proto.sensor_meta_schema_pb2'})
_sym_db.RegisterMessage(MultiSensorMeta)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SENSORMETA._serialized_start = 73
    _SENSORMETA._serialized_end = 630
    _SENSORMETA_SENSORTYPE._serialized_start = 228
    _SENSORMETA_SENSORTYPE._serialized_end = 475
    _SENSORMETA_SENSORORIENTATION._serialized_start = 478
    _SENSORMETA_SENSORORIENTATION._serialized_end = 630
    _MULTISENSORMETA._serialized_start = 632
    _MULTISENSORMETA._serialized_end = 701