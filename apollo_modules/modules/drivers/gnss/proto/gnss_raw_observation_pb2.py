"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/drivers/gnss/proto/gnss_raw_observation.proto\x12\x13apollo.drivers.gnss"\x92\x02\n\x0fBandObservation\x12>\n\x07band_id\x18\x01 \x01(\x0e2\x1f.apollo.drivers.gnss.GnssBandID:\x0cBAND_UNKNOWN\x12\x17\n\x0ffrequency_value\x18\x02 \x01(\x01\x12B\n\x0bpseudo_type\x18\x03 \x01(\x0e2\x1f.apollo.drivers.gnss.PseudoType:\x0cCODE_UNKNOWN\x12\x14\n\x0cpseudo_range\x18\x04 \x01(\x01\x12\x15\n\rcarrier_phase\x18\x05 \x01(\x01\x12\x17\n\x0floss_lock_index\x18\x06 \x01(\r\x12\x0f\n\x07doppler\x18\x07 \x01(\x01\x12\x0b\n\x03snr\x18\x08 \x01(\x02"\xae\x01\n\x14SatelliteObservation\x12\x0f\n\x07sat_prn\x18\x01 \x01(\r\x127\n\x07sat_sys\x18\x02 \x01(\x0e2\x1d.apollo.drivers.gnss.GnssType:\x07GPS_SYS\x12\x14\n\x0cband_obs_num\x18\x03 \x01(\r\x126\n\x08band_obs\x18\x04 \x03(\x0b2$.apollo.drivers.gnss.BandObservation"\xbb\x02\n\x10EpochObservation\x12\x13\n\x0breceiver_id\x18\x01 \x01(\r\x12C\n\x0egnss_time_type\x18\x02 \x01(\x0e2!.apollo.drivers.gnss.GnssTimeType:\x08GPS_TIME\x12\x11\n\tgnss_week\x18\x03 \x01(\r\x12\x15\n\rgnss_second_s\x18\x04 \x01(\x01\x12\x12\n\nposition_x\x18\x05 \x01(\x01\x12\x12\n\nposition_y\x18\x06 \x01(\x01\x12\x12\n\nposition_z\x18\x07 \x01(\x01\x12\x16\n\x0bhealth_flag\x18\x08 \x01(\r:\x010\x12\x13\n\x0bsat_obs_num\x18\t \x01(\r\x12:\n\x07sat_obs\x18\n \x03(\x0b2).apollo.drivers.gnss.SatelliteObservation"\xa7\x05\n\x0cKepplerOrbit\x129\n\tgnss_type\x18\x01 \x01(\x0e2\x1d.apollo.drivers.gnss.GnssType:\x07GPS_SYS\x12\x0f\n\x07sat_prn\x18\x02 \x01(\r\x12C\n\x0egnss_time_type\x18\x03 \x01(\x0e2!.apollo.drivers.gnss.GnssTimeType:\x08GPS_TIME\x12\x0c\n\x04year\x18\x04 \x01(\r\x12\r\n\x05month\x18\x05 \x01(\r\x12\x0b\n\x03day\x18\x06 \x01(\r\x12\x0c\n\x04hour\x18\x07 \x01(\r\x12\x0e\n\x06minute\x18\x08 \x01(\r\x12\x10\n\x08second_s\x18\t \x01(\x01\x12\x10\n\x08week_num\x18\n \x01(\r\x12\x10\n\x08reserved\x18\x0b \x01(\x01\x12\x0b\n\x03af0\x18\x0c \x01(\x01\x12\x0b\n\x03af1\x18\r \x01(\x01\x12\x0b\n\x03af2\x18\x0e \x01(\x01\x12\x0c\n\x04iode\x18\x0f \x01(\x01\x12\x0e\n\x06deltan\x18\x10 \x01(\x01\x12\n\n\x02m0\x18\x11 \x01(\x01\x12\t\n\x01e\x18\x12 \x01(\x01\x12\r\n\x05roota\x18\x13 \x01(\x01\x12\x0b\n\x03toe\x18\x14 \x01(\x01\x12\x0b\n\x03toc\x18\x15 \x01(\x01\x12\x0b\n\x03cic\x18\x16 \x01(\x01\x12\x0b\n\x03crc\x18\x17 \x01(\x01\x12\x0b\n\x03cis\x18\x18 \x01(\x01\x12\x0b\n\x03crs\x18\x19 \x01(\x01\x12\x0b\n\x03cuc\x18\x1a \x01(\x01\x12\x0b\n\x03cus\x18\x1b \x01(\x01\x12\x0e\n\x06omega0\x18\x1c \x01(\x01\x12\r\n\x05omega\x18\x1d \x01(\x01\x12\n\n\x02i0\x18\x1e \x01(\x01\x12\x10\n\x08omegadot\x18\x1f \x01(\x01\x12\x0c\n\x04idot\x18  \x01(\x01\x12\x18\n\x10codesonL2channel\x18! \x01(\x01\x12\x13\n\x0bL2Pdataflag\x18" \x01(\r\x12\x10\n\x08accuracy\x18# \x01(\r\x12\x0e\n\x06health\x18$ \x01(\r\x12\x0b\n\x03tgd\x18% \x01(\x01\x12\x0c\n\x04iodc\x18& \x01(\x01"\xeb\x04\n\x0cGlonassOrbit\x129\n\tgnss_type\x18\x01 \x01(\x0e2\x1d.apollo.drivers.gnss.GnssType:\x07GLO_SYS\x12\x10\n\x08slot_prn\x18\x02 \x01(\r\x12C\n\x0egnss_time_type\x18\x03 \x01(\x0e2!.apollo.drivers.gnss.GnssTimeType:\x08GLO_TIME\x12\x0b\n\x03toe\x18\x04 \x01(\x01\x12\x0c\n\x04year\x18\x05 \x01(\r\x12\r\n\x05month\x18\x06 \x01(\r\x12\x0b\n\x03day\x18\x07 \x01(\r\x12\x0c\n\x04hour\x18\x08 \x01(\r\x12\x0e\n\x06minute\x18\t \x01(\r\x12\x10\n\x08second_s\x18\n \x01(\x01\x12\x14\n\x0cfrequency_no\x18\x0b \x01(\x05\x12\x10\n\x08week_num\x18\x0c \x01(\r\x12\x15\n\rweek_second_s\x18\r \x01(\x01\x12\n\n\x02tk\x18\x0e \x01(\x01\x12\x14\n\x0cclock_offset\x18\x0f \x01(\x01\x12\x13\n\x0bclock_drift\x18\x10 \x01(\x01\x12\x0e\n\x06health\x18\x11 \x01(\r\x12\x12\n\nposition_x\x18\x12 \x01(\x01\x12\x12\n\nposition_y\x18\x13 \x01(\x01\x12\x12\n\nposition_z\x18\x14 \x01(\x01\x12\x12\n\nvelocity_x\x18\x15 \x01(\x01\x12\x12\n\nvelocity_y\x18\x16 \x01(\x01\x12\x12\n\nvelocity_z\x18\x17 \x01(\x01\x12\x14\n\x0caccelerate_x\x18\x18 \x01(\x01\x12\x14\n\x0caccelerate_y\x18\x19 \x01(\x01\x12\x14\n\x0caccelerate_z\x18\x1a \x01(\x01\x12\x11\n\tinfor_age\x18\x1b \x01(\x01\x12\x0f\n\x07sat_prn\x18\x1c \x01(\r"\xbe\x01\n\rGnssEphemeris\x129\n\tgnss_type\x18\x01 \x01(\x0e2\x1d.apollo.drivers.gnss.GnssType:\x07GLO_SYS\x128\n\rkeppler_orbit\x18\x02 \x01(\x0b2!.apollo.drivers.gnss.KepplerOrbit\x128\n\rglonass_orbit\x18\x03 \x01(\x0b2!.apollo.drivers.gnss.GlonassOrbit*\x8a\x01\n\nGnssBandID\x12\x10\n\x0cBAND_UNKNOWN\x10\x00\x12\n\n\x06GPS_L1\x10\x01\x12\n\n\x06GPS_L2\x10\x02\x12\n\n\x06GPS_L5\x10\x03\x12\n\n\x06BDS_B1\x10\x04\x12\n\n\x06BDS_B2\x10\x05\x12\n\n\x06BDS_B3\x10\x06\x12\n\n\x06GLO_G1\x10\x07\x12\n\n\x06GLO_G2\x10\x08\x12\n\n\x06GLO_G3\x10\t*X\n\x0cGnssTimeType\x12\x10\n\x0cTIME_UNKNOWN\x10\x00\x12\x0c\n\x08GPS_TIME\x10\x01\x12\x0c\n\x08BDS_TIME\x10\x02\x12\x0c\n\x08GLO_TIME\x10\x03\x12\x0c\n\x08GAL_TIME\x10\x04*O\n\x08GnssType\x12\x0f\n\x0bSYS_UNKNOWN\x10\x00\x12\x0b\n\x07GPS_SYS\x10\x01\x12\x0b\n\x07BDS_SYS\x10\x02\x12\x0b\n\x07GLO_SYS\x10\x03\x12\x0b\n\x07GAL_SYS\x10\x04*B\n\nPseudoType\x12\x10\n\x0cCODE_UNKNOWN\x10\x00\x12\x0e\n\nCORSE_CODE\x10\x01\x12\x12\n\x0ePRECISION_CODE\x10\x02')
_GNSSBANDID = DESCRIPTOR.enum_types_by_name['GnssBandID']
GnssBandID = enum_type_wrapper.EnumTypeWrapper(_GNSSBANDID)
_GNSSTIMETYPE = DESCRIPTOR.enum_types_by_name['GnssTimeType']
GnssTimeType = enum_type_wrapper.EnumTypeWrapper(_GNSSTIMETYPE)
_GNSSTYPE = DESCRIPTOR.enum_types_by_name['GnssType']
GnssType = enum_type_wrapper.EnumTypeWrapper(_GNSSTYPE)
_PSEUDOTYPE = DESCRIPTOR.enum_types_by_name['PseudoType']
PseudoType = enum_type_wrapper.EnumTypeWrapper(_PSEUDOTYPE)
BAND_UNKNOWN = 0
GPS_L1 = 1
GPS_L2 = 2
GPS_L5 = 3
BDS_B1 = 4
BDS_B2 = 5
BDS_B3 = 6
GLO_G1 = 7
GLO_G2 = 8
GLO_G3 = 9
TIME_UNKNOWN = 0
GPS_TIME = 1
BDS_TIME = 2
GLO_TIME = 3
GAL_TIME = 4
SYS_UNKNOWN = 0
GPS_SYS = 1
BDS_SYS = 2
GLO_SYS = 3
GAL_SYS = 4
CODE_UNKNOWN = 0
CORSE_CODE = 1
PRECISION_CODE = 2
_BANDOBSERVATION = DESCRIPTOR.message_types_by_name['BandObservation']
_SATELLITEOBSERVATION = DESCRIPTOR.message_types_by_name['SatelliteObservation']
_EPOCHOBSERVATION = DESCRIPTOR.message_types_by_name['EpochObservation']
_KEPPLERORBIT = DESCRIPTOR.message_types_by_name['KepplerOrbit']
_GLONASSORBIT = DESCRIPTOR.message_types_by_name['GlonassOrbit']
_GNSSEPHEMERIS = DESCRIPTOR.message_types_by_name['GnssEphemeris']
BandObservation = _reflection.GeneratedProtocolMessageType('BandObservation', (_message.Message,), {'DESCRIPTOR': _BANDOBSERVATION, '__module__': 'modules.drivers.gnss.proto.gnss_raw_observation_pb2'})
_sym_db.RegisterMessage(BandObservation)
SatelliteObservation = _reflection.GeneratedProtocolMessageType('SatelliteObservation', (_message.Message,), {'DESCRIPTOR': _SATELLITEOBSERVATION, '__module__': 'modules.drivers.gnss.proto.gnss_raw_observation_pb2'})
_sym_db.RegisterMessage(SatelliteObservation)
EpochObservation = _reflection.GeneratedProtocolMessageType('EpochObservation', (_message.Message,), {'DESCRIPTOR': _EPOCHOBSERVATION, '__module__': 'modules.drivers.gnss.proto.gnss_raw_observation_pb2'})
_sym_db.RegisterMessage(EpochObservation)
KepplerOrbit = _reflection.GeneratedProtocolMessageType('KepplerOrbit', (_message.Message,), {'DESCRIPTOR': _KEPPLERORBIT, '__module__': 'modules.drivers.gnss.proto.gnss_raw_observation_pb2'})
_sym_db.RegisterMessage(KepplerOrbit)
GlonassOrbit = _reflection.GeneratedProtocolMessageType('GlonassOrbit', (_message.Message,), {'DESCRIPTOR': _GLONASSORBIT, '__module__': 'modules.drivers.gnss.proto.gnss_raw_observation_pb2'})
_sym_db.RegisterMessage(GlonassOrbit)
GnssEphemeris = _reflection.GeneratedProtocolMessageType('GnssEphemeris', (_message.Message,), {'DESCRIPTOR': _GNSSEPHEMERIS, '__module__': 'modules.drivers.gnss.proto.gnss_raw_observation_pb2'})
_sym_db.RegisterMessage(GnssEphemeris)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GNSSBANDID._serialized_start = 2348
    _GNSSBANDID._serialized_end = 2486
    _GNSSTIMETYPE._serialized_start = 2488
    _GNSSTIMETYPE._serialized_end = 2576
    _GNSSTYPE._serialized_start = 2578
    _GNSSTYPE._serialized_end = 2657
    _PSEUDOTYPE._serialized_start = 2659
    _PSEUDOTYPE._serialized_end = 2725
    _BANDOBSERVATION._serialized_start = 79
    _BANDOBSERVATION._serialized_end = 353
    _SATELLITEOBSERVATION._serialized_start = 356
    _SATELLITEOBSERVATION._serialized_end = 530
    _EPOCHOBSERVATION._serialized_start = 533
    _EPOCHOBSERVATION._serialized_end = 848
    _KEPPLERORBIT._serialized_start = 851
    _KEPPLERORBIT._serialized_end = 1530
    _GLONASSORBIT._serialized_start = 1533
    _GLONASSORBIT._serialized_end = 2152
    _GNSSEPHEMERIS._serialized_start = 2155
    _GNSSEPHEMERIS._serialized_end = 2345