"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from ....modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#modules/map/proto/map_overlap.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"p\n\x0fLaneOverlapInfo\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05end_s\x18\x02 \x01(\x01\x12\x10\n\x08is_merge\x18\x03 \x01(\x08\x12+\n\x11region_overlap_id\x18\x04 \x01(\x0b2\x10.apollo.hdmap.Id"\x13\n\x11SignalOverlapInfo"\x15\n\x13StopSignOverlapInfo"C\n\x14CrosswalkOverlapInfo\x12+\n\x11region_overlap_id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id"\x15\n\x13JunctionOverlapInfo"\x12\n\x10YieldOverlapInfo"\x16\n\x14ClearAreaOverlapInfo"\x16\n\x14SpeedBumpOverlapInfo"\x19\n\x17ParkingSpaceOverlapInfo"\x18\n\x16PNCJunctionOverlapInfo"\x10\n\x0eRSUOverlapInfo"Y\n\x11RegionOverlapInfo\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x03(\x0b2\x15.apollo.hdmap.Polygon"\xaf\x06\n\x11ObjectOverlapInfo\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12:\n\x11lane_overlap_info\x18\x03 \x01(\x0b2\x1d.apollo.hdmap.LaneOverlapInfoH\x00\x12>\n\x13signal_overlap_info\x18\x04 \x01(\x0b2\x1f.apollo.hdmap.SignalOverlapInfoH\x00\x12C\n\x16stop_sign_overlap_info\x18\x05 \x01(\x0b2!.apollo.hdmap.StopSignOverlapInfoH\x00\x12D\n\x16crosswalk_overlap_info\x18\x06 \x01(\x0b2".apollo.hdmap.CrosswalkOverlapInfoH\x00\x12B\n\x15junction_overlap_info\x18\x07 \x01(\x0b2!.apollo.hdmap.JunctionOverlapInfoH\x00\x12A\n\x17yield_sign_overlap_info\x18\x08 \x01(\x0b2\x1e.apollo.hdmap.YieldOverlapInfoH\x00\x12E\n\x17clear_area_overlap_info\x18\t \x01(\x0b2".apollo.hdmap.ClearAreaOverlapInfoH\x00\x12E\n\x17speed_bump_overlap_info\x18\n \x01(\x0b2".apollo.hdmap.SpeedBumpOverlapInfoH\x00\x12K\n\x1aparking_space_overlap_info\x18\x0b \x01(\x0b2%.apollo.hdmap.ParkingSpaceOverlapInfoH\x00\x12I\n\x19pnc_junction_overlap_info\x18\x0c \x01(\x0b2$.apollo.hdmap.PNCJunctionOverlapInfoH\x00\x128\n\x10rsu_overlap_info\x18\r \x01(\x0b2\x1c.apollo.hdmap.RSUOverlapInfoH\x00B\x0e\n\x0coverlap_info"\x91\x01\n\x07Overlap\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12/\n\x06object\x18\x02 \x03(\x0b2\x1f.apollo.hdmap.ObjectOverlapInfo\x127\n\x0eregion_overlap\x18\x03 \x03(\x0b2\x1f.apollo.hdmap.RegionOverlapInfo')
_LANEOVERLAPINFO = DESCRIPTOR.message_types_by_name['LaneOverlapInfo']
_SIGNALOVERLAPINFO = DESCRIPTOR.message_types_by_name['SignalOverlapInfo']
_STOPSIGNOVERLAPINFO = DESCRIPTOR.message_types_by_name['StopSignOverlapInfo']
_CROSSWALKOVERLAPINFO = DESCRIPTOR.message_types_by_name['CrosswalkOverlapInfo']
_JUNCTIONOVERLAPINFO = DESCRIPTOR.message_types_by_name['JunctionOverlapInfo']
_YIELDOVERLAPINFO = DESCRIPTOR.message_types_by_name['YieldOverlapInfo']
_CLEARAREAOVERLAPINFO = DESCRIPTOR.message_types_by_name['ClearAreaOverlapInfo']
_SPEEDBUMPOVERLAPINFO = DESCRIPTOR.message_types_by_name['SpeedBumpOverlapInfo']
_PARKINGSPACEOVERLAPINFO = DESCRIPTOR.message_types_by_name['ParkingSpaceOverlapInfo']
_PNCJUNCTIONOVERLAPINFO = DESCRIPTOR.message_types_by_name['PNCJunctionOverlapInfo']
_RSUOVERLAPINFO = DESCRIPTOR.message_types_by_name['RSUOverlapInfo']
_REGIONOVERLAPINFO = DESCRIPTOR.message_types_by_name['RegionOverlapInfo']
_OBJECTOVERLAPINFO = DESCRIPTOR.message_types_by_name['ObjectOverlapInfo']
_OVERLAP = DESCRIPTOR.message_types_by_name['Overlap']
LaneOverlapInfo = _reflection.GeneratedProtocolMessageType('LaneOverlapInfo', (_message.Message,), {'DESCRIPTOR': _LANEOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(LaneOverlapInfo)
SignalOverlapInfo = _reflection.GeneratedProtocolMessageType('SignalOverlapInfo', (_message.Message,), {'DESCRIPTOR': _SIGNALOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(SignalOverlapInfo)
StopSignOverlapInfo = _reflection.GeneratedProtocolMessageType('StopSignOverlapInfo', (_message.Message,), {'DESCRIPTOR': _STOPSIGNOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(StopSignOverlapInfo)
CrosswalkOverlapInfo = _reflection.GeneratedProtocolMessageType('CrosswalkOverlapInfo', (_message.Message,), {'DESCRIPTOR': _CROSSWALKOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(CrosswalkOverlapInfo)
JunctionOverlapInfo = _reflection.GeneratedProtocolMessageType('JunctionOverlapInfo', (_message.Message,), {'DESCRIPTOR': _JUNCTIONOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(JunctionOverlapInfo)
YieldOverlapInfo = _reflection.GeneratedProtocolMessageType('YieldOverlapInfo', (_message.Message,), {'DESCRIPTOR': _YIELDOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(YieldOverlapInfo)
ClearAreaOverlapInfo = _reflection.GeneratedProtocolMessageType('ClearAreaOverlapInfo', (_message.Message,), {'DESCRIPTOR': _CLEARAREAOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(ClearAreaOverlapInfo)
SpeedBumpOverlapInfo = _reflection.GeneratedProtocolMessageType('SpeedBumpOverlapInfo', (_message.Message,), {'DESCRIPTOR': _SPEEDBUMPOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(SpeedBumpOverlapInfo)
ParkingSpaceOverlapInfo = _reflection.GeneratedProtocolMessageType('ParkingSpaceOverlapInfo', (_message.Message,), {'DESCRIPTOR': _PARKINGSPACEOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(ParkingSpaceOverlapInfo)
PNCJunctionOverlapInfo = _reflection.GeneratedProtocolMessageType('PNCJunctionOverlapInfo', (_message.Message,), {'DESCRIPTOR': _PNCJUNCTIONOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(PNCJunctionOverlapInfo)
RSUOverlapInfo = _reflection.GeneratedProtocolMessageType('RSUOverlapInfo', (_message.Message,), {'DESCRIPTOR': _RSUOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(RSUOverlapInfo)
RegionOverlapInfo = _reflection.GeneratedProtocolMessageType('RegionOverlapInfo', (_message.Message,), {'DESCRIPTOR': _REGIONOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(RegionOverlapInfo)
ObjectOverlapInfo = _reflection.GeneratedProtocolMessageType('ObjectOverlapInfo', (_message.Message,), {'DESCRIPTOR': _OBJECTOVERLAPINFO, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(ObjectOverlapInfo)
Overlap = _reflection.GeneratedProtocolMessageType('Overlap', (_message.Message,), {'DESCRIPTOR': _OVERLAP, '__module__': 'modules.map.proto.map_overlap_pb2'})
_sym_db.RegisterMessage(Overlap)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANEOVERLAPINFO._serialized_start = 123
    _LANEOVERLAPINFO._serialized_end = 235
    _SIGNALOVERLAPINFO._serialized_start = 237
    _SIGNALOVERLAPINFO._serialized_end = 256
    _STOPSIGNOVERLAPINFO._serialized_start = 258
    _STOPSIGNOVERLAPINFO._serialized_end = 279
    _CROSSWALKOVERLAPINFO._serialized_start = 281
    _CROSSWALKOVERLAPINFO._serialized_end = 348
    _JUNCTIONOVERLAPINFO._serialized_start = 350
    _JUNCTIONOVERLAPINFO._serialized_end = 371
    _YIELDOVERLAPINFO._serialized_start = 373
    _YIELDOVERLAPINFO._serialized_end = 391
    _CLEARAREAOVERLAPINFO._serialized_start = 393
    _CLEARAREAOVERLAPINFO._serialized_end = 415
    _SPEEDBUMPOVERLAPINFO._serialized_start = 417
    _SPEEDBUMPOVERLAPINFO._serialized_end = 439
    _PARKINGSPACEOVERLAPINFO._serialized_start = 441
    _PARKINGSPACEOVERLAPINFO._serialized_end = 466
    _PNCJUNCTIONOVERLAPINFO._serialized_start = 468
    _PNCJUNCTIONOVERLAPINFO._serialized_end = 492
    _RSUOVERLAPINFO._serialized_start = 494
    _RSUOVERLAPINFO._serialized_end = 510
    _REGIONOVERLAPINFO._serialized_start = 512
    _REGIONOVERLAPINFO._serialized_end = 601
    _OBJECTOVERLAPINFO._serialized_start = 604
    _OBJECTOVERLAPINFO._serialized_end = 1419
    _OVERLAP._serialized_start = 1422
    _OVERLAP._serialized_end = 1567