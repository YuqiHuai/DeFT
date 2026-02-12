"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/dreamview/proto/chart.proto\x12\x10apollo.dreamview\x1a#modules/common/proto/geometry.proto"\xaa\x02\n\x07Options\x12\x1c\n\x0elegend_display\x18\x01 \x01(\x08:\x04true\x12)\n\x01x\x18\x02 \x01(\x0b2\x1e.apollo.dreamview.Options.Axis\x12)\n\x01y\x18\x03 \x01(\x0b2\x1e.apollo.dreamview.Options.Axis\x12\x14\n\x0caspect_ratio\x18\x04 \x01(\x01\x12"\n\x13sync_xy_window_size\x18\x05 \x01(\x08:\x05false\x1aq\n\x04Axis\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\x14\n\x0clabel_string\x18\x03 \x01(\t\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x01\x12\x11\n\tstep_size\x18\x05 \x01(\x01\x12\x11\n\tmid_value\x18\x06 \x01(\x01"\xd0\x01\n\x04Line\x12\r\n\x05label\x18\x01 \x01(\t\x12#\n\x14hide_label_in_legend\x18\x02 \x01(\x08:\x05false\x12%\n\x05point\x18\x03 \x03(\x0b2\x16.apollo.common.Point2D\x12:\n\nproperties\x18\x04 \x03(\x0b2&.apollo.dreamview.Line.PropertiesEntry\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd6\x01\n\x07Polygon\x12\r\n\x05label\x18\x01 \x01(\t\x12#\n\x14hide_label_in_legend\x18\x02 \x01(\x08:\x05false\x12%\n\x05point\x18\x03 \x03(\x0b2\x16.apollo.common.Point2D\x12=\n\nproperties\x18\x04 \x03(\x0b2).apollo.dreamview.Polygon.PropertiesEntry\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"o\n\x03Car\x12\r\n\x05label\x18\x01 \x01(\t\x12#\n\x14hide_label_in_legend\x18\x02 \x01(\x08:\x05false\x12\t\n\x01x\x18\x03 \x01(\x01\x12\t\n\x01y\x18\x04 \x01(\x01\x12\x0f\n\x07heading\x18\x05 \x01(\x01\x12\r\n\x05color\x18\x06 \x01(\t"\xb8\x01\n\x05Chart\x12\r\n\x05title\x18\x01 \x01(\t\x12*\n\x07options\x18\x02 \x01(\x0b2\x19.apollo.dreamview.Options\x12$\n\x04line\x18\x03 \x03(\x0b2\x16.apollo.dreamview.Line\x12*\n\x07polygon\x18\x04 \x03(\x0b2\x19.apollo.dreamview.Polygon\x12"\n\x03car\x18\x05 \x03(\x0b2\x15.apollo.dreamview.Car')
_OPTIONS = DESCRIPTOR.message_types_by_name['Options']
_OPTIONS_AXIS = _OPTIONS.nested_types_by_name['Axis']
_LINE = DESCRIPTOR.message_types_by_name['Line']
_LINE_PROPERTIESENTRY = _LINE.nested_types_by_name['PropertiesEntry']
_POLYGON = DESCRIPTOR.message_types_by_name['Polygon']
_POLYGON_PROPERTIESENTRY = _POLYGON.nested_types_by_name['PropertiesEntry']
_CAR = DESCRIPTOR.message_types_by_name['Car']
_CHART = DESCRIPTOR.message_types_by_name['Chart']
Options = _reflection.GeneratedProtocolMessageType('Options', (_message.Message,), {'Axis': _reflection.GeneratedProtocolMessageType('Axis', (_message.Message,), {'DESCRIPTOR': _OPTIONS_AXIS, '__module__': 'modules.dreamview.proto.chart_pb2'}), 'DESCRIPTOR': _OPTIONS, '__module__': 'modules.dreamview.proto.chart_pb2'})
_sym_db.RegisterMessage(Options)
_sym_db.RegisterMessage(Options.Axis)
Line = _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), {'PropertiesEntry': _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {'DESCRIPTOR': _LINE_PROPERTIESENTRY, '__module__': 'modules.dreamview.proto.chart_pb2'}), 'DESCRIPTOR': _LINE, '__module__': 'modules.dreamview.proto.chart_pb2'})
_sym_db.RegisterMessage(Line)
_sym_db.RegisterMessage(Line.PropertiesEntry)
Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {'PropertiesEntry': _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {'DESCRIPTOR': _POLYGON_PROPERTIESENTRY, '__module__': 'modules.dreamview.proto.chart_pb2'}), 'DESCRIPTOR': _POLYGON, '__module__': 'modules.dreamview.proto.chart_pb2'})
_sym_db.RegisterMessage(Polygon)
_sym_db.RegisterMessage(Polygon.PropertiesEntry)
Car = _reflection.GeneratedProtocolMessageType('Car', (_message.Message,), {'DESCRIPTOR': _CAR, '__module__': 'modules.dreamview.proto.chart_pb2'})
_sym_db.RegisterMessage(Car)
Chart = _reflection.GeneratedProtocolMessageType('Chart', (_message.Message,), {'DESCRIPTOR': _CHART, '__module__': 'modules.dreamview.proto.chart_pb2'})
_sym_db.RegisterMessage(Chart)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LINE_PROPERTIESENTRY._options = None
    _LINE_PROPERTIESENTRY._serialized_options = b'8\x01'
    _POLYGON_PROPERTIESENTRY._options = None
    _POLYGON_PROPERTIESENTRY._serialized_options = b'8\x01'
    _OPTIONS._serialized_start = 95
    _OPTIONS._serialized_end = 393
    _OPTIONS_AXIS._serialized_start = 280
    _OPTIONS_AXIS._serialized_end = 393
    _LINE._serialized_start = 396
    _LINE._serialized_end = 604
    _LINE_PROPERTIESENTRY._serialized_start = 555
    _LINE_PROPERTIESENTRY._serialized_end = 604
    _POLYGON._serialized_start = 607
    _POLYGON._serialized_end = 821
    _POLYGON_PROPERTIESENTRY._serialized_start = 555
    _POLYGON_PROPERTIESENTRY._serialized_end = 604
    _CAR._serialized_start = 823
    _CAR._serialized_end = 934
    _CHART._serialized_start = 937
    _CHART._serialized_end = 1121