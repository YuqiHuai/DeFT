"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/dreamview/proto/data_collection_table.proto\x12\x10apollo.dreamview"\x84\x01\n\tCriterion\x12\r\n\x05field\x18\x01 \x01(\t\x12A\n\x13comparison_operator\x18\x02 \x01(\x0e2$.apollo.dreamview.ComparisonOperator\x12\r\n\x05value\x18\x03 \x01(\x02\x12\x16\n\x0evehicle_config\x18\x04 \x01(\t"E\n\x05Range\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\tcriterion\x18\x02 \x03(\x0b2\x1b.apollo.dreamview.Criterion"?\n\x07Feature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05range\x18\x02 \x03(\x0b2\x17.apollo.dreamview.Range"6\n\x08Scenario\x12*\n\x07feature\x18\x01 \x03(\x0b2\x19.apollo.dreamview.Feature"\xd8\x01\n\x13DataCollectionTable\x12E\n\x08scenario\x18\x01 \x03(\x0b23.apollo.dreamview.DataCollectionTable.ScenarioEntry\x12\x17\n\x0fframe_threshold\x18\x02 \x02(\r\x12\x14\n\x0ctotal_frames\x18\x03 \x02(\r\x1aK\n\rScenarioEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.apollo.dreamview.Scenario:\x028\x01*\x82\x01\n\x12ComparisonOperator\x12\t\n\x05EQUAL\x10\x00\x12\r\n\tNOT_EQUAL\x10\x01\x12\x10\n\x0cGREATER_THAN\x10\x02\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x03\x12\r\n\tLESS_THAN\x10\x04\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x05')
_COMPARISONOPERATOR = DESCRIPTOR.enum_types_by_name['ComparisonOperator']
ComparisonOperator = enum_type_wrapper.EnumTypeWrapper(_COMPARISONOPERATOR)
EQUAL = 0
NOT_EQUAL = 1
GREATER_THAN = 2
GREATER_THAN_OR_EQUAL = 3
LESS_THAN = 4
LESS_THAN_OR_EQUAL = 5
_CRITERION = DESCRIPTOR.message_types_by_name['Criterion']
_RANGE = DESCRIPTOR.message_types_by_name['Range']
_FEATURE = DESCRIPTOR.message_types_by_name['Feature']
_SCENARIO = DESCRIPTOR.message_types_by_name['Scenario']
_DATACOLLECTIONTABLE = DESCRIPTOR.message_types_by_name['DataCollectionTable']
_DATACOLLECTIONTABLE_SCENARIOENTRY = _DATACOLLECTIONTABLE.nested_types_by_name['ScenarioEntry']
Criterion = _reflection.GeneratedProtocolMessageType('Criterion', (_message.Message,), {'DESCRIPTOR': _CRITERION, '__module__': 'modules.dreamview.proto.data_collection_table_pb2'})
_sym_db.RegisterMessage(Criterion)
Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {'DESCRIPTOR': _RANGE, '__module__': 'modules.dreamview.proto.data_collection_table_pb2'})
_sym_db.RegisterMessage(Range)
Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {'DESCRIPTOR': _FEATURE, '__module__': 'modules.dreamview.proto.data_collection_table_pb2'})
_sym_db.RegisterMessage(Feature)
Scenario = _reflection.GeneratedProtocolMessageType('Scenario', (_message.Message,), {'DESCRIPTOR': _SCENARIO, '__module__': 'modules.dreamview.proto.data_collection_table_pb2'})
_sym_db.RegisterMessage(Scenario)
DataCollectionTable = _reflection.GeneratedProtocolMessageType('DataCollectionTable', (_message.Message,), {'ScenarioEntry': _reflection.GeneratedProtocolMessageType('ScenarioEntry', (_message.Message,), {'DESCRIPTOR': _DATACOLLECTIONTABLE_SCENARIOENTRY, '__module__': 'modules.dreamview.proto.data_collection_table_pb2'}), 'DESCRIPTOR': _DATACOLLECTIONTABLE, '__module__': 'modules.dreamview.proto.data_collection_table_pb2'})
_sym_db.RegisterMessage(DataCollectionTable)
_sym_db.RegisterMessage(DataCollectionTable.ScenarioEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DATACOLLECTIONTABLE_SCENARIOENTRY._options = None
    _DATACOLLECTIONTABLE_SCENARIOENTRY._serialized_options = b'8\x01'
    _COMPARISONOPERATOR._serialized_start = 620
    _COMPARISONOPERATOR._serialized_end = 750
    _CRITERION._serialized_start = 74
    _CRITERION._serialized_end = 206
    _RANGE._serialized_start = 208
    _RANGE._serialized_end = 277
    _FEATURE._serialized_start = 279
    _FEATURE._serialized_end = 342
    _SCENARIO._serialized_start = 344
    _SCENARIO._serialized_end = 398
    _DATACOLLECTIONTABLE._serialized_start = 401
    _DATACOLLECTIONTABLE._serialized_end = 617
    _DATACOLLECTIONTABLE_SCENARIOENTRY._serialized_start = 542
    _DATACOLLECTIONTABLE_SCENARIOENTRY._serialized_end = 617