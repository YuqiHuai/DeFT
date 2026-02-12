"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/control/proto/calibration_table.proto\x12\x1fapollo.control.calibrationtable"g\n\x17ControlCalibrationTable\x12L\n\x0bcalibration\x18\x01 \x03(\x0b27.apollo.control.calibrationtable.ControlCalibrationInfo"N\n\x16ControlCalibrationInfo\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x14\n\x0cacceleration\x18\x02 \x01(\x01\x12\x0f\n\x07command\x18\x03 \x01(\x01')
_CONTROLCALIBRATIONTABLE = DESCRIPTOR.message_types_by_name['ControlCalibrationTable']
_CONTROLCALIBRATIONINFO = DESCRIPTOR.message_types_by_name['ControlCalibrationInfo']
ControlCalibrationTable = _reflection.GeneratedProtocolMessageType('ControlCalibrationTable', (_message.Message,), {'DESCRIPTOR': _CONTROLCALIBRATIONTABLE, '__module__': 'modules.control.proto.calibration_table_pb2'})
_sym_db.RegisterMessage(ControlCalibrationTable)
ControlCalibrationInfo = _reflection.GeneratedProtocolMessageType('ControlCalibrationInfo', (_message.Message,), {'DESCRIPTOR': _CONTROLCALIBRATIONINFO, '__module__': 'modules.control.proto.calibration_table_pb2'})
_sym_db.RegisterMessage(ControlCalibrationInfo)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONTROLCALIBRATIONTABLE._serialized_start = 82
    _CONTROLCALIBRATIONTABLE._serialized_end = 185
    _CONTROLCALIBRATIONINFO._serialized_start = 187
    _CONTROLCALIBRATIONINFO._serialized_end = 265