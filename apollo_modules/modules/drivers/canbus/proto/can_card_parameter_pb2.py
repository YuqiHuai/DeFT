"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/drivers/canbus/proto/can_card_parameter.proto\x12\x15apollo.drivers.canbus"\xa9\x05\n\x10CANCardParameter\x12C\n\x05brand\x18\x01 \x01(\x0e24.apollo.drivers.canbus.CANCardParameter.CANCardBrand\x12A\n\x04type\x18\x02 \x01(\x0e23.apollo.drivers.canbus.CANCardParameter.CANCardType\x12H\n\nchannel_id\x18\x03 \x01(\x0e24.apollo.drivers.canbus.CANCardParameter.CANChannelId\x12G\n\tinterface\x18\x04 \x01(\x0e24.apollo.drivers.canbus.CANCardParameter.CANInterface\x12\x14\n\tnum_ports\x18\x05 \x01(\r:\x014"M\n\x0cCANCardBrand\x12\x0c\n\x08FAKE_CAN\x10\x00\x12\x0b\n\x07ESD_CAN\x10\x01\x12\x12\n\x0eSOCKET_CAN_RAW\x10\x02\x12\x0e\n\nHERMES_CAN\x10\x03")\n\x0bCANCardType\x12\x0c\n\x08PCI_CARD\x10\x00\x12\x0c\n\x08USB_CARD\x10\x01"\xb5\x01\n\x0cCANChannelId\x12\x13\n\x0fCHANNEL_ID_ZERO\x10\x00\x12\x12\n\x0eCHANNEL_ID_ONE\x10\x01\x12\x12\n\x0eCHANNEL_ID_TWO\x10\x02\x12\x14\n\x10CHANNEL_ID_THREE\x10\x03\x12\x13\n\x0fCHANNEL_ID_FOUR\x10\x04\x12\x13\n\x0fCHANNEL_ID_FIVE\x10\x05\x12\x12\n\x0eCHANNEL_ID_SIX\x10\x06\x12\x14\n\x10CHANNEL_ID_SEVEN\x10\x07"2\n\x0cCANInterface\x12\n\n\x06NATIVE\x10\x00\x12\x0b\n\x07VIRTUAL\x10\x01\x12\t\n\x05SLCAN\x10\x02')
_CANCARDPARAMETER = DESCRIPTOR.message_types_by_name['CANCardParameter']
_CANCARDPARAMETER_CANCARDBRAND = _CANCARDPARAMETER.enum_types_by_name['CANCardBrand']
_CANCARDPARAMETER_CANCARDTYPE = _CANCARDPARAMETER.enum_types_by_name['CANCardType']
_CANCARDPARAMETER_CANCHANNELID = _CANCARDPARAMETER.enum_types_by_name['CANChannelId']
_CANCARDPARAMETER_CANINTERFACE = _CANCARDPARAMETER.enum_types_by_name['CANInterface']
CANCardParameter = _reflection.GeneratedProtocolMessageType('CANCardParameter', (_message.Message,), {'DESCRIPTOR': _CANCARDPARAMETER, '__module__': 'modules.drivers.canbus.proto.can_card_parameter_pb2'})
_sym_db.RegisterMessage(CANCardParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CANCARDPARAMETER._serialized_start = 81
    _CANCARDPARAMETER._serialized_end = 762
    _CANCARDPARAMETER_CANCARDBRAND._serialized_start = 406
    _CANCARDPARAMETER_CANCARDBRAND._serialized_end = 483
    _CANCARDPARAMETER_CANCARDTYPE._serialized_start = 485
    _CANCARDPARAMETER_CANCARDTYPE._serialized_end = 526
    _CANCARDPARAMETER_CANCHANNELID._serialized_start = 529
    _CANCARDPARAMETER_CANCHANNELID._serialized_end = 710
    _CANCARDPARAMETER_CANINTERFACE._serialized_start = 712
    _CANCARDPARAMETER_CANINTERFACE._serialized_end = 762