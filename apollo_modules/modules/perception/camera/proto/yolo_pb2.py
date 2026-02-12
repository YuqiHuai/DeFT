"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*modules/perception/camera/proto/yolo.proto\x12\x1dapollo.perception.camera.yolo"\xc7\x01\n\tYoloParam\x12>\n\x0bmodel_param\x18\x01 \x01(\x0b2).apollo.perception.camera.yolo.ModelParam\x12>\n\tnet_param\x18\x02 \x01(\x0b2+.apollo.perception.camera.yolo.NetworkParam\x12:\n\tnms_param\x18\x03 \x01(\x0b2\'.apollo.perception.camera.yolo.NMSParam"\xc9\t\n\nModelParam\x12\x1b\n\nmodel_name\x18\x01 \x01(\t:\x07yolo-2d\x12\x1c\n\nproto_file\x18\x02 \x01(\t:\x08caffe.pt\x12 \n\x0bweight_file\x18\x03 \x01(\t:\x0bcaffe.model\x12\x1b\n\tstage1_pt\x18\x15 \x01(\t:\x08caffe.pt\x12\x1e\n\tstage1_md\x18\x16 \x01(\t:\x0bcaffe.model\x12\x1b\n\tstage2_pt\x18\x17 \x01(\t:\x08caffe.pt\x12\x1e\n\tstage2_md\x18\x18 \x01(\t:\x0bcaffe.model\x12!\n\x0canchors_file\x18\x04 \x01(\t:\x0banchors.txt\x12\x1d\n\ntypes_file\x18\x05 \x01(\t:\ttypes.txt\x12 \n\x0cfeature_file\x18\x06 \x01(\t:\nfeature.pt\x12\x1e\n\x0coffset_ratio\x18\x07 \x01(\x02:\x080.288889\x12\x1f\n\rcropped_ratio\x18\r \x01(\x02:\x080.711111\x12\x1b\n\rresized_width\x18\x0e \x01(\x05:\x041440\x12\x19\n\raligned_pixel\x18\x0f \x01(\x05:\x0232\x12!\n\x14confidence_threshold\x18\x08 \x01(\x02:\x030.1\x12%\n\x18light_vis_conf_threshold\x18! \x01(\x02:\x030.5\x12%\n\x18light_swt_conf_threshold\x18" \x01(\x02:\x030.5\x12\x1f\n\x12roi_conf_threshold\x18\x19 \x01(\x02:\x030.1\x12\x1f\n\x12box_conf_threshold\x18\x1a \x01(\x02:\x030.5\x12!\n\x14stage2_nms_threshold\x18\x1b \x01(\x02:\x030.4\x12\x18\n\rmin_2d_height\x18\t \x01(\x02:\x010\x12\x18\n\rmin_3d_height\x18\x1e \x01(\x02:\x010\x12\x17\n\x0cmin_3d_width\x18\x1f \x01(\x02:\x010\x12\x18\n\rmin_3d_length\x18  \x01(\x02:\x010\x12\x1f\n\x13calibratetable_root\x18\x0b \x01(\t:\x02./\x12\x1c\n\nmodel_type\x18\x0c \x01(\t:\x08CaffeNet\x12\x14\n\tori_cycle\x18\x10 \x01(\x05:\x011\x12\x1a\n\x0bper_cls_reg\x18\x11 \x01(\x08:\x05false\x12P\n\x14dimension_statistics\x18\x12 \x03(\x0b22.apollo.perception.camera.yolo.DimensionStatistics\x12F\n\x0fbbox_statistics\x18\x13 \x03(\x0b2-.apollo.perception.camera.yolo.BBoxStatistics\x12\x1f\n\x0bexpand_file\x18\x14 \x01(\t:\nexpand.txt\x12\x19\n\nwith_box3d\x18) \x01(\x08:\x05false\x12\x19\n\nwith_frbox\x18* \x01(\x08:\x05false\x12\x1a\n\x0bwith_lights\x18+ \x01(\x08:\x05false\x12\x1a\n\x0bwith_ratios\x18, \x01(\x08:\x05false\x12\x14\n\tnum_areas\x18. \x01(\x05:\x010\x12\x1a\n\x0cborder_ratio\x18- \x01(\x02:\x040.01"\x84\n\n\x0cNetworkParam\x12\'\n\rdet1_loc_blob\x18\x01 \x01(\t:\x10detect1_loc_pred\x12\'\n\rdet1_obj_blob\x18\x02 \x01(\t:\x10detect1_obj_pred\x12\'\n\rdet1_cls_blob\x18\x03 \x01(\t:\x10detect1_cls_pred\x12\'\n\rdet1_ori_blob\x18\x04 \x01(\t:\x10detect1_ori_pred\x121\n\x12det1_ori_conf_blob\x18\x05 \x01(\t:\x15detect1_ori_conf_pred\x12\'\n\rdet1_dim_blob\x18\x06 \x01(\t:\x10detect1_dim_pred\x12\'\n\rdet2_loc_blob\x18\x07 \x01(\t:\x10detect2_loc_pred\x12\'\n\rdet2_obj_blob\x18\x08 \x01(\t:\x10detect2_obj_pred\x12\'\n\rdet2_cls_blob\x18\t \x01(\t:\x10detect2_cls_pred\x12\'\n\rdet2_ori_blob\x18\n \x01(\t:\x10detect2_ori_pred\x121\n\x12det2_ori_conf_blob\x18\x0b \x01(\t:\x15detect2_ori_conf_pred\x12\'\n\rdet2_dim_blob\x18\x0c \x01(\t:\x10detect2_dim_pred\x12\'\n\rdet3_loc_blob\x18\r \x01(\t:\x10detect3_loc_pred\x12\'\n\rdet3_obj_blob\x18\x0e \x01(\t:\x10detect3_obj_pred\x12\'\n\rdet3_cls_blob\x18\x0f \x01(\t:\x10detect3_cls_pred\x12\'\n\rdet3_ori_blob\x18\x10 \x01(\t:\x10detect3_ori_pred\x121\n\x12det3_ori_conf_blob\x18\x11 \x01(\t:\x15detect3_ori_conf_pred\x12\'\n\rdet3_dim_blob\x18\x12 \x01(\t:\x10detect3_dim_pred\x12\x1a\n\x08lof_blob\x18\x13 \x01(\t:\x08lof_pred\x12\x1a\n\x08lor_blob\x18\x14 \x01(\t:\x08lor_pred\x12\x18\n\ninput_blob\x18\x15 \x01(\t:\x04data\x12\x1c\n\trois_blob\x18\x16 \x01(\t:\trois_pred\x12\x1c\n\tfeat_blob\x18\x17 \x01(\t:\tconv_feat\x12\x1a\n\x08box_blob\x18\x18 \x01(\t:\x08box_pred\x12\x1a\n\x08iou_blob\x18\x19 \x01(\t:\x08iou_pred\x12\x1e\n\nbrvis_blob\x18\x1a \x01(\t:\nbrvis_pred\x12\x1e\n\nbrswt_blob\x18\x1b \x01(\t:\nbrswt_pred\x12\x1e\n\nltvis_blob\x18\x1c \x01(\t:\nltvis_pred\x12\x1e\n\nltswt_blob\x18\x1d \x01(\t:\nltswt_pred\x12\x1e\n\nrtvis_blob\x18\x1e \x01(\t:\nrtvis_pred\x12\x1e\n\nrtswt_blob\x18\x1f \x01(\t:\nrtswt_pred\x12"\n\x0carea_id_blob\x18  \x01(\t:\x0carea_id_pred\x12$\n\x12visible_ratio_blob\x18! \x01(\t:\x08vis_pred\x12$\n\x12cut_off_ratio_blob\x18" \x01(\t:\x08cut_pred"\x94\x01\n\x08NMSParam\x12\x17\n\x04type\x18\x01 \x01(\t:\tNormalNMS\x12\x16\n\tthreshold\x18\x02 \x01(\x02:\x030.4\x12\x12\n\x05sigma\x18\x03 \x01(\x02:\x030.4\x12"\n\x15inter_cls_conf_thresh\x18\x04 \x01(\x02:\x030.1\x12\x1f\n\x14inter_cls_nms_thresh\x18\x05 \x01(\x02:\x011"+\n\x0eBBoxStatistics\x12\x0c\n\x04mean\x18\x01 \x03(\x02\x12\x0b\n\x03std\x18\x02 \x03(\x02"\x84\x01\n\x13DimensionStatistics\x12\x11\n\x06mean_h\x18\x01 \x01(\x02:\x010\x12\x11\n\x06mean_w\x18\x02 \x01(\x02:\x010\x12\x11\n\x06mean_l\x18\x03 \x01(\x02:\x010\x12\x10\n\x05std_h\x18\x04 \x01(\x02:\x011\x12\x10\n\x05std_w\x18\x05 \x01(\x02:\x011\x12\x10\n\x05std_l\x18\x06 \x01(\x02:\x011')
_YOLOPARAM = DESCRIPTOR.message_types_by_name['YoloParam']
_MODELPARAM = DESCRIPTOR.message_types_by_name['ModelParam']
_NETWORKPARAM = DESCRIPTOR.message_types_by_name['NetworkParam']
_NMSPARAM = DESCRIPTOR.message_types_by_name['NMSParam']
_BBOXSTATISTICS = DESCRIPTOR.message_types_by_name['BBoxStatistics']
_DIMENSIONSTATISTICS = DESCRIPTOR.message_types_by_name['DimensionStatistics']
YoloParam = _reflection.GeneratedProtocolMessageType('YoloParam', (_message.Message,), {'DESCRIPTOR': _YOLOPARAM, '__module__': 'modules.perception.camera.proto.yolo_pb2'})
_sym_db.RegisterMessage(YoloParam)
ModelParam = _reflection.GeneratedProtocolMessageType('ModelParam', (_message.Message,), {'DESCRIPTOR': _MODELPARAM, '__module__': 'modules.perception.camera.proto.yolo_pb2'})
_sym_db.RegisterMessage(ModelParam)
NetworkParam = _reflection.GeneratedProtocolMessageType('NetworkParam', (_message.Message,), {'DESCRIPTOR': _NETWORKPARAM, '__module__': 'modules.perception.camera.proto.yolo_pb2'})
_sym_db.RegisterMessage(NetworkParam)
NMSParam = _reflection.GeneratedProtocolMessageType('NMSParam', (_message.Message,), {'DESCRIPTOR': _NMSPARAM, '__module__': 'modules.perception.camera.proto.yolo_pb2'})
_sym_db.RegisterMessage(NMSParam)
BBoxStatistics = _reflection.GeneratedProtocolMessageType('BBoxStatistics', (_message.Message,), {'DESCRIPTOR': _BBOXSTATISTICS, '__module__': 'modules.perception.camera.proto.yolo_pb2'})
_sym_db.RegisterMessage(BBoxStatistics)
DimensionStatistics = _reflection.GeneratedProtocolMessageType('DimensionStatistics', (_message.Message,), {'DESCRIPTOR': _DIMENSIONSTATISTICS, '__module__': 'modules.perception.camera.proto.yolo_pb2'})
_sym_db.RegisterMessage(DimensionStatistics)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _YOLOPARAM._serialized_start = 78
    _YOLOPARAM._serialized_end = 277
    _MODELPARAM._serialized_start = 280
    _MODELPARAM._serialized_end = 1505
    _NETWORKPARAM._serialized_start = 1508
    _NETWORKPARAM._serialized_end = 2792
    _NMSPARAM._serialized_start = 2795
    _NMSPARAM._serialized_end = 2943
    _BBOXSTATISTICS._serialized_start = 2945
    _BBOXSTATISTICS._serialized_end = 2988
    _DIMENSIONSTATISTICS._serialized_start = 2991
    _DIMENSIONSTATISTICS._serialized_end = 3123