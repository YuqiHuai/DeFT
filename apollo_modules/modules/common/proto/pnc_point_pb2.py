"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/common/proto/pnc_point.proto\x12\rapollo.common"\x1f\n\x07SLPoint\x12\t\n\x01s\x18\x01 \x01(\x01\x12\t\n\x01l\x18\x02 \x01(\x01"A\n\x10FrenetFramePoint\x12\t\n\x01s\x18\x01 \x01(\x01\x12\t\n\x01l\x18\x02 \x01(\x01\x12\n\n\x02dl\x18\x03 \x01(\x01\x12\x0b\n\x03ddl\x18\x04 \x01(\x01"D\n\nSpeedPoint\x12\t\n\x01s\x18\x01 \x01(\x01\x12\t\n\x01t\x18\x02 \x01(\x01\x12\t\n\x01v\x18\x03 \x01(\x01\x12\t\n\x01a\x18\x04 \x01(\x01\x12\n\n\x02da\x18\x05 \x01(\x01"\xb3\x01\n\tPathPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\r\n\x05theta\x18\x04 \x01(\x01\x12\r\n\x05kappa\x18\x05 \x01(\x01\x12\t\n\x01s\x18\x06 \x01(\x01\x12\x0e\n\x06dkappa\x18\x07 \x01(\x01\x12\x0f\n\x07ddkappa\x18\x08 \x01(\x01\x12\x0f\n\x07lane_id\x18\t \x01(\t\x12\x14\n\x0cx_derivative\x18\n \x01(\x01\x12\x14\n\x0cy_derivative\x18\x0b \x01(\x01"B\n\x04Path\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\npath_point\x18\x02 \x03(\x0b2\x18.apollo.common.PathPoint"\xbb\x01\n\x0fTrajectoryPoint\x12,\n\npath_point\x18\x01 \x01(\x0b2\x18.apollo.common.PathPoint\x12\t\n\x01v\x18\x02 \x01(\x01\x12\t\n\x01a\x18\x03 \x01(\x01\x12\x15\n\rrelative_time\x18\x04 \x01(\x01\x12\n\n\x02da\x18\x05 \x01(\x01\x12\r\n\x05steer\x18\x06 \x01(\x01\x122\n\rgaussian_info\x18\x07 \x01(\x0b2\x1b.apollo.common.GaussianInfo"T\n\nTrajectory\x12\x0c\n\x04name\x18\x01 \x01(\t\x128\n\x10trajectory_point\x18\x02 \x03(\x0b2\x1e.apollo.common.TrajectoryPoint"]\n\x12VehicleMotionPoint\x128\n\x10trajectory_point\x18\x01 \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12\r\n\x05steer\x18\x02 \x01(\x01"^\n\rVehicleMotion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x14vehicle_motion_point\x18\x02 \x03(\x0b2!.apollo.common.VehicleMotionPoint"\x96\x01\n\x0cGaussianInfo\x12\x0f\n\x07sigma_x\x18\x01 \x01(\x01\x12\x0f\n\x07sigma_y\x18\x02 \x01(\x01\x12\x13\n\x0bcorrelation\x18\x03 \x01(\x01\x12\x18\n\x10area_probability\x18\x04 \x01(\x01\x12\x11\n\tellipse_a\x18\x05 \x01(\x01\x12\x11\n\tellipse_b\x18\x06 \x01(\x01\x12\x0f\n\x07theta_a\x18\x07 \x01(\x01')
_SLPOINT = DESCRIPTOR.message_types_by_name['SLPoint']
_FRENETFRAMEPOINT = DESCRIPTOR.message_types_by_name['FrenetFramePoint']
_SPEEDPOINT = DESCRIPTOR.message_types_by_name['SpeedPoint']
_PATHPOINT = DESCRIPTOR.message_types_by_name['PathPoint']
_PATH = DESCRIPTOR.message_types_by_name['Path']
_TRAJECTORYPOINT = DESCRIPTOR.message_types_by_name['TrajectoryPoint']
_TRAJECTORY = DESCRIPTOR.message_types_by_name['Trajectory']
_VEHICLEMOTIONPOINT = DESCRIPTOR.message_types_by_name['VehicleMotionPoint']
_VEHICLEMOTION = DESCRIPTOR.message_types_by_name['VehicleMotion']
_GAUSSIANINFO = DESCRIPTOR.message_types_by_name['GaussianInfo']
SLPoint = _reflection.GeneratedProtocolMessageType('SLPoint', (_message.Message,), {'DESCRIPTOR': _SLPOINT, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(SLPoint)
FrenetFramePoint = _reflection.GeneratedProtocolMessageType('FrenetFramePoint', (_message.Message,), {'DESCRIPTOR': _FRENETFRAMEPOINT, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(FrenetFramePoint)
SpeedPoint = _reflection.GeneratedProtocolMessageType('SpeedPoint', (_message.Message,), {'DESCRIPTOR': _SPEEDPOINT, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(SpeedPoint)
PathPoint = _reflection.GeneratedProtocolMessageType('PathPoint', (_message.Message,), {'DESCRIPTOR': _PATHPOINT, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(PathPoint)
Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {'DESCRIPTOR': _PATH, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(Path)
TrajectoryPoint = _reflection.GeneratedProtocolMessageType('TrajectoryPoint', (_message.Message,), {'DESCRIPTOR': _TRAJECTORYPOINT, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(TrajectoryPoint)
Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), {'DESCRIPTOR': _TRAJECTORY, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(Trajectory)
VehicleMotionPoint = _reflection.GeneratedProtocolMessageType('VehicleMotionPoint', (_message.Message,), {'DESCRIPTOR': _VEHICLEMOTIONPOINT, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(VehicleMotionPoint)
VehicleMotion = _reflection.GeneratedProtocolMessageType('VehicleMotion', (_message.Message,), {'DESCRIPTOR': _VEHICLEMOTION, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(VehicleMotion)
GaussianInfo = _reflection.GeneratedProtocolMessageType('GaussianInfo', (_message.Message,), {'DESCRIPTOR': _GAUSSIANINFO, '__module__': 'modules.common.proto.pnc_point_pb2'})
_sym_db.RegisterMessage(GaussianInfo)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SLPOINT._serialized_start = 55
    _SLPOINT._serialized_end = 86
    _FRENETFRAMEPOINT._serialized_start = 88
    _FRENETFRAMEPOINT._serialized_end = 153
    _SPEEDPOINT._serialized_start = 155
    _SPEEDPOINT._serialized_end = 223
    _PATHPOINT._serialized_start = 226
    _PATHPOINT._serialized_end = 405
    _PATH._serialized_start = 407
    _PATH._serialized_end = 473
    _TRAJECTORYPOINT._serialized_start = 476
    _TRAJECTORYPOINT._serialized_end = 663
    _TRAJECTORY._serialized_start = 665
    _TRAJECTORY._serialized_end = 749
    _VEHICLEMOTIONPOINT._serialized_start = 751
    _VEHICLEMOTIONPOINT._serialized_end = 844
    _VEHICLEMOTION._serialized_start = 846
    _VEHICLEMOTION._serialized_end = 940
    _GAUSSIANINFO._serialized_start = 943
    _GAUSSIANINFO._serialized_end = 1093