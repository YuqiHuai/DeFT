"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!modules/perception/proto/rt.proto\x12\x1bapollo.perception.inference"\x1c\n\tBlobShape\x12\x0f\n\x03dim\x18\x01 \x03(\x03B\x02\x10\x01"\xe2\x01\n\tBlobProto\x125\n\x05shape\x18\x07 \x01(\x0b2&.apollo.perception.inference.BlobShape\x12\x10\n\x04data\x18\x05 \x03(\x02B\x02\x10\x01\x12\x10\n\x04diff\x18\x06 \x03(\x02B\x02\x10\x01\x12\x17\n\x0bdouble_data\x18\x08 \x03(\x01B\x02\x10\x01\x12\x17\n\x0bdouble_diff\x18\t \x03(\x01B\x02\x10\x01\x12\x0e\n\x03num\x18\x01 \x01(\x05:\x010\x12\x13\n\x08channels\x18\x02 \x01(\x05:\x010\x12\x11\n\x06height\x18\x03 \x01(\x05:\x010\x12\x10\n\x05width\x18\x04 \x01(\x05:\x010"\x81\x01\n\x05Datum\x12\x10\n\x08channels\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0c\n\x04data\x18\x04 \x01(\x0c\x12\r\n\x05label\x18\x05 \x01(\x05\x12\x12\n\nfloat_data\x18\x06 \x03(\x02\x12\x16\n\x07encoded\x18\x07 \x01(\x08:\x05false"A\n\x0cLabelMapItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\x05\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t"C\n\x08LabelMap\x127\n\x04item\x18\x01 \x03(\x0b2).apollo.perception.inference.LabelMapItem"o\n\x07Sampler\x12\x14\n\tmin_scale\x18\x01 \x01(\x02:\x011\x12\x14\n\tmax_scale\x18\x02 \x01(\x02:\x011\x12\x1b\n\x10min_aspect_ratio\x18\x03 \x01(\x02:\x011\x12\x1b\n\x10max_aspect_ratio\x18\x04 \x01(\x02:\x011"\xd6\x01\n\x10SampleConstraint\x12\x1b\n\x13min_jaccard_overlap\x18\x01 \x01(\x02\x12\x1b\n\x13max_jaccard_overlap\x18\x02 \x01(\x02\x12\x1b\n\x13min_sample_coverage\x18\x03 \x01(\x02\x12\x1b\n\x13max_sample_coverage\x18\x04 \x01(\x02\x12\x1b\n\x13min_object_coverage\x18\x05 \x01(\x02\x12\x1b\n\x13max_object_coverage\x18\x06 \x01(\x02\x12\x14\n\x0cbalance_type\x18\x07 \x03(\x05"\xde\x01\n\x0cBatchSampler\x12 \n\x12use_original_image\x18\x01 \x01(\x08:\x04true\x125\n\x07sampler\x18\x02 \x01(\x0b2$.apollo.perception.inference.Sampler\x12H\n\x11sample_constraint\x18\x03 \x01(\x0b2-.apollo.perception.inference.SampleConstraint\x12\x12\n\nmax_sample\x18\x04 \x01(\r\x12\x17\n\nmax_trials\x18\x05 \x01(\r:\x03100"\xa0\x01\n\x0eEmitConstraint\x12O\n\temit_type\x18\x01 \x01(\x0e24.apollo.perception.inference.EmitConstraint.EmitType:\x06CENTER\x12\x14\n\x0cemit_overlap\x18\x02 \x01(\x02"\'\n\x08EmitType\x12\n\n\x06CENTER\x10\x00\x12\x0f\n\x0bMIN_OVERLAP\x10\x01"\x87\x01\n\x0eNormalizedBBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\x0c\n\x04xmax\x18\x03 \x01(\x02\x12\x0c\n\x04ymax\x18\x04 \x01(\x02\x12\r\n\x05label\x18\x05 \x01(\x05\x12\x11\n\tdifficult\x18\x06 \x01(\x08\x12\r\n\x05score\x18\x07 \x01(\x02\x12\x0c\n\x04size\x18\x08 \x01(\x02"n\n\x06BBox3D\x12\x0c\n\x01h\x18\x01 \x01(\x02:\x010\x12\x0c\n\x01w\x18\x02 \x01(\x02:\x010\x12\x0c\n\x01l\x18\x03 \x01(\x02:\x010\x12\x0c\n\x01x\x18\x04 \x01(\x02:\x010\x12\x0c\n\x01y\x18\x05 \x01(\x02:\x010\x12\x0c\n\x01z\x18\x06 \x01(\x02:\x010\x12\x10\n\x05alpha\x18\x07 \x01(\x02:\x010"\x95\x02\n\nAnnotation\x12\x16\n\x0binstance_id\x18\x01 \x01(\x05:\x010\x129\n\x04bbox\x18\x02 \x01(\x0b2+.apollo.perception.inference.NormalizedBBox\x123\n\x06bbox3d\x18\x03 \x01(\x0b2#.apollo.perception.inference.BBox3D\x12?\n\nfront_bbox\x18\x04 \x01(\x0b2+.apollo.perception.inference.NormalizedBBox\x12>\n\trear_bbox\x18\x05 \x01(\x0b2+.apollo.perception.inference.NormalizedBBox"c\n\x0fAnnotationGroup\x12\x13\n\x0bgroup_label\x18\x01 \x01(\x05\x12;\n\nannotation\x18\x02 \x03(\x0b2\'.apollo.perception.inference.Annotation"\x8b\x02\n\x0eAnnotatedDatum\x121\n\x05datum\x18\x01 \x01(\x0b2".apollo.perception.inference.Datum\x12H\n\x04type\x18\x02 \x01(\x0e2:.apollo.perception.inference.AnnotatedDatum.AnnotationType\x12F\n\x10annotation_group\x18\x03 \x03(\x0b2,.apollo.perception.inference.AnnotationGroup"4\n\x0eAnnotationType\x12\x08\n\x04BBOX\x10\x00\x12\n\n\x06BBOX3D\x10\x01\x12\x0c\n\x08BBOX3DFR\x10\x02"\xa0\x02\n\x0fFillerParameter\x12\x16\n\x04type\x18\x01 \x01(\t:\x08constant\x12\x10\n\x05value\x18\x02 \x01(\x02:\x010\x12\x0e\n\x03min\x18\x03 \x01(\x02:\x010\x12\x0e\n\x03max\x18\x04 \x01(\x02:\x011\x12\x0f\n\x04mean\x18\x05 \x01(\x02:\x010\x12\x0e\n\x03std\x18\x06 \x01(\x02:\x011\x12\x12\n\x06sparse\x18\x07 \x01(\x05:\x02-1\x12X\n\rvariance_norm\x18\x08 \x01(\x0e29.apollo.perception.inference.FillerParameter.VarianceNorm:\x06FAN_IN"4\n\x0cVarianceNorm\x12\n\n\x06FAN_IN\x10\x00\x12\x0b\n\x07FAN_OUT\x10\x01\x12\x0b\n\x07AVERAGE\x10\x02"\xe6\x02\n\x0cNetParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05input\x18\x03 \x03(\t\x12;\n\x0binput_shape\x18\x08 \x03(\x0b2&.apollo.perception.inference.BlobShape\x12\x11\n\tinput_dim\x18\x04 \x03(\x05\x12\x1d\n\x0eforce_backward\x18\x05 \x01(\x08:\x05false\x124\n\x05state\x18\x06 \x01(\x0b2%.apollo.perception.inference.NetState\x12\x19\n\ndebug_info\x18\x07 \x01(\x08:\x05false\x12:\n\x05layer\x18d \x03(\x0b2+.apollo.perception.inference.LayerParameter\x12=\n\x06layers\x18\x02 \x03(\x0b2-.apollo.perception.inference.V1LayerParameter"d\n\x08NetState\x127\n\x05phase\x18\x01 \x01(\x0e2".apollo.perception.inference.Phase:\x04TEST\x12\x10\n\x05level\x18\x02 \x01(\x05:\x010\x12\r\n\x05stage\x18\x03 \x03(\t"\x89\x01\n\x0cNetStateRule\x121\n\x05phase\x18\x01 \x01(\x0e2".apollo.perception.inference.Phase\x12\x11\n\tmin_level\x18\x02 \x01(\x05\x12\x11\n\tmax_level\x18\x03 \x01(\x05\x12\r\n\x05stage\x18\x04 \x03(\t\x12\x11\n\tnot_stage\x18\x05 \x03(\t"\xb9\x01\n\tParamSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12G\n\nshare_mode\x18\x02 \x01(\x0e23.apollo.perception.inference.ParamSpec.DimCheckMode\x12\x12\n\x07lr_mult\x18\x03 \x01(\x02:\x011\x12\x15\n\ndecay_mult\x18\x04 \x01(\x02:\x011"*\n\x0cDimCheckMode\x12\n\n\x06STRICT\x10\x00\x12\x0e\n\nPERMISSIVE\x10\x01"\xdb*\n\x0eLayerParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06bottom\x18\x03 \x03(\t\x12\x0b\n\x03top\x18\x04 \x03(\t\x121\n\x05phase\x18\n \x01(\x0e2".apollo.perception.inference.Phase\x12\x13\n\x0bloss_weight\x18\x05 \x03(\x02\x125\n\x05param\x18\x06 \x03(\x0b2&.apollo.perception.inference.ParamSpec\x125\n\x05blobs\x18\x07 \x03(\x0b2&.apollo.perception.inference.BlobProto\x12\x16\n\x0epropagate_down\x18\x0b \x03(\x08\x12:\n\x07include\x18\x08 \x03(\x0b2).apollo.perception.inference.NetStateRule\x12:\n\x07exclude\x18\t \x03(\x0b2).apollo.perception.inference.NetStateRule\x12M\n\x0ftransform_param\x18d \x01(\x0b24.apollo.perception.inference.TransformationParameter\x12>\n\nloss_param\x18e \x01(\x0b2*.apollo.perception.inference.LossParameter\x12F\n\x0eaccuracy_param\x18f \x01(\x0b2..apollo.perception.inference.AccuracyParameter\x12R\n\x14annotated_data_param\x18\xc8\x01 \x01(\x0b23.apollo.perception.inference.AnnotatedDataParameter\x12B\n\x0cargmax_param\x18g \x01(\x0b2,.apollo.perception.inference.ArgMaxParameter\x12J\n\x10batch_norm_param\x18\x8b\x01 \x01(\x0b2/.apollo.perception.inference.BatchNormParameter\x12F\n\x0ebbox_reg_param\x18\xd1\x01 \x01(\x0b2-.apollo.perception.inference.BBoxRegParameter\x12?\n\nbias_param\x18\x8d\x01 \x01(\x0b2*.apollo.perception.inference.BiasParameter\x12B\n\x0cconcat_param\x18h \x01(\x0b2,.apollo.perception.inference.ConcatParameter\x12U\n\x16contrastive_loss_param\x18i \x01(\x0b25.apollo.perception.inference.ContrastiveLossParameter\x12L\n\x11convolution_param\x18j \x01(\x0b21.apollo.perception.inference.ConvolutionParameter\x12?\n\ncrop_param\x18\x90\x01 \x01(\x0b2*.apollo.perception.inference.CropParameter\x12>\n\ndata_param\x18k \x01(\x0b2*.apollo.perception.inference.DataParameter\x12Z\n\x18detection_evaluate_param\x18\xcd\x01 \x01(\x0b27.apollo.perception.inference.DetectionEvaluateParameter\x12V\n\x16detection_output_param\x18\xcc\x01 \x01(\x0b25.apollo.perception.inference.DetectionOutputParameter\x12]\n\x1adetection_output_ssd_param\x18\xd2\x01 \x01(\x0b28.apollo.perception.inference.DetectionOutputSSDParameter\x12W\n\x18dfmb_psroi_pooling_param\x18\xd0\x01 \x01(\x0b24.apollo.perception.inference.DFMBPSROIAlignParameter\x12D\n\rdropout_param\x18l \x01(\x0b2-.apollo.perception.inference.DropoutParameter\x12I\n\x10dummy_data_param\x18m \x01(\x0b2/.apollo.perception.inference.DummyDataParameter\x12D\n\reltwise_param\x18n \x01(\x0b2-.apollo.perception.inference.EltwiseParameter\x12=\n\telu_param\x18\x8c\x01 \x01(\x0b2).apollo.perception.inference.ELUParameter\x12A\n\x0bembed_param\x18\x89\x01 \x01(\x0b2+.apollo.perception.inference.EmbedParameter\x12<\n\texp_param\x18o \x01(\x0b2).apollo.perception.inference.ExpParameter\x12E\n\rflatten_param\x18\x87\x01 \x01(\x0b2-.apollo.perception.inference.FlattenParameter\x12G\n\x0fhdf5_data_param\x18p \x01(\x0b2..apollo.perception.inference.HDF5DataParameter\x12K\n\x11hdf5_output_param\x18q \x01(\x0b20.apollo.perception.inference.HDF5OutputParameter\x12I\n\x10hinge_loss_param\x18r \x01(\x0b2/.apollo.perception.inference.HingeLossParameter\x12I\n\x10image_data_param\x18s \x01(\x0b2/.apollo.perception.inference.ImageDataParameter\x12J\n\x0fyolo_data_param\x18\xe7\x98h \x03(\x0b2/.apollo.perception.inference.ImageDataParameter\x12\x19\n\x0fdata_prob_param\x18\xe8\x98h \x03(\x02\x12O\n\x13infogain_loss_param\x18t \x01(\x0b22.apollo.perception.inference.InfogainLossParameter\x12O\n\x13inner_product_param\x18u \x01(\x0b22.apollo.perception.inference.InnerProductParameter\x12A\n\x0binput_param\x18\x8f\x01 \x01(\x0b2+.apollo.perception.inference.InputParameter\x12=\n\tlog_param\x18\x86\x01 \x01(\x0b2).apollo.perception.inference.LogParameter\x12<\n\tlrn_param\x18v \x01(\x0b2).apollo.perception.inference.LRNParameter\x12K\n\x11memory_data_param\x18w \x01(\x0b20.apollo.perception.inference.MemoryDataParameter\x12P\n\x13multibox_loss_param\x18\xc9\x01 \x01(\x0b22.apollo.perception.inference.MultiBoxLossParameter\x12C\n\x0cregion_param\x18\xac\x02 \x01(\x0b2,.apollo.perception.inference.RegionParameter\x12P\n\x13region_output_param\x18\xb6\x02 \x01(\x0b22.apollo.perception.inference.RegionOutputParameter\x12T\n\x15region_proposal_param\x18\xc0\x02 \x01(\x0b24.apollo.perception.inference.RegionProposalParameter\x12M\n\x11yolo_target_param\x18\x81\xc0\x0c \x01(\x0b20.apollo.perception.inference.YoloTargetParameter\x12O\n\x12yolo_anchors_param\x18\x82\xc0\x0c \x01(\x0b21.apollo.perception.inference.YoloAnchorsParameter\x12I\n\x0fyolo_loss_param\x18\x83\xc0\x0c \x01(\x0b2..apollo.perception.inference.YoloLossParameter\x12I\n\x0fyolo_dump_param\x18\x84\xc0\x0c \x01(\x0b2..apollo.perception.inference.YoloDumpParameter\x12E\n\rpadding_param\x18\xe9\x07 \x01(\x0b2-.apollo.perception.inference.PaddingParameter\x12A\n\x0breorg_param\x18\xad\x02 \x01(\x0b2+.apollo.perception.inference.ReorgParameter\x12<\n\tmvn_param\x18x \x01(\x0b2).apollo.perception.inference.MVNParameter\x12D\n\nnorm_param\x18\xce\x01 \x01(\x0b2/.apollo.perception.inference.NormalizeParameter\x12I\n\x0fparameter_param\x18\x91\x01 \x01(\x0b2/.apollo.perception.inference.ParameterParameter\x12E\n\rpermute_param\x18\xca\x01 \x01(\x0b2-.apollo.perception.inference.PermuteParameter\x12D\n\rpooling_param\x18y \x01(\x0b2-.apollo.perception.inference.PoolingParameter\x12@\n\x0bpower_param\x18z \x01(\x0b2+.apollo.perception.inference.PowerParameter\x12A\n\x0bprelu_param\x18\x83\x01 \x01(\x0b2+.apollo.perception.inference.PReLUParameter\x12H\n\x0fprior_box_param\x18\xcb\x01 \x01(\x0b2..apollo.perception.inference.PriorBoxParameter\x12C\n\x0cpython_param\x18\x82\x01 \x01(\x0b2,.apollo.perception.inference.PythonParameter\x12I\n\x0frecurrent_param\x18\x92\x01 \x01(\x0b2/.apollo.perception.inference.RecurrentParameter\x12I\n\x0freduction_param\x18\x88\x01 \x01(\x0b2/.apollo.perception.inference.ReductionParameter\x12>\n\nrelu_param\x18{ \x01(\x0b2*.apollo.perception.inference.ReLUParameter\x12E\n\rreshape_param\x18\x85\x01 \x01(\x0b2-.apollo.perception.inference.ReshapeParameter\x12N\n\x11roi_pooling_param\x18\xd7\xc7\xf8\x03 \x01(\x0b20.apollo.perception.inference.ROIPoolingParameter\x12A\n\x0bscale_param\x18\x8e\x01 \x01(\x0b2+.apollo.perception.inference.ScaleParameter\x12D\n\rsigmoid_param\x18| \x01(\x0b2-.apollo.perception.inference.SigmoidParameter\x12D\n\rsoftmax_param\x18} \x01(\x0b2-.apollo.perception.inference.SoftmaxParameter\x12=\n\tspp_param\x18\x84\x01 \x01(\x0b2).apollo.perception.inference.SPPParameter\x12@\n\x0bslice_param\x18~ \x01(\x0b2+.apollo.perception.inference.SliceParameter\x12>\n\ntanh_param\x18\x7f \x01(\x0b2*.apollo.perception.inference.TanHParameter\x12I\n\x0fthreshold_param\x18\x80\x01 \x01(\x0b2/.apollo.perception.inference.ThresholdParameter\x12?\n\ntile_param\x18\x8a\x01 \x01(\x0b2*.apollo.perception.inference.TileParameter\x12J\n\x10video_data_param\x18\xcf\x01 \x01(\x0b2/.apollo.perception.inference.VideoDataParameter\x12L\n\x11window_data_param\x18\x81\x01 \x01(\x0b20.apollo.perception.inference.WindowDataParameter"\xc8\x04\n\x17TransformationParameter\x12\x10\n\x05scale\x18\x01 \x01(\x02:\x011\x12\x15\n\x06mirror\x18\x02 \x01(\x08:\x05false\x12\x14\n\tcrop_size\x18\x03 \x01(\r:\x010\x12\x11\n\x06crop_h\x18\x0b \x01(\r:\x010\x12\x11\n\x06crop_w\x18\x0c \x01(\r:\x010\x12\x11\n\tmean_file\x18\x04 \x01(\t\x12\x12\n\nmean_value\x18\x05 \x03(\x02\x12\x1a\n\x0bforce_color\x18\x06 \x01(\x08:\x05false\x12\x19\n\nforce_gray\x18\x07 \x01(\x08:\x05false\x12B\n\x0cresize_param\x18\x08 \x01(\x0b2,.apollo.perception.inference.ResizeParameter\x12@\n\x0bnoise_param\x18\t \x01(\x0b2+.apollo.perception.inference.NoiseParameter\x12G\n\rdistort_param\x18\r \x01(\x0b20.apollo.perception.inference.DistortionParameter\x12E\n\x0cexpand_param\x18\x0e \x01(\x0b2/.apollo.perception.inference.ExpansionParameter\x12\x0e\n\x06jitter\x18\x0f \x01(\x02\x12D\n\x0femit_constraint\x18\n \x01(\x0b2+.apollo.perception.inference.EmitConstraint"\xd2\x04\n\x0fResizeParameter\x12\x0f\n\x04prob\x18\x01 \x01(\x02:\x011\x12S\n\x0bresize_mode\x18\x02 \x01(\x0e28.apollo.perception.inference.ResizeParameter.Resize_mode:\x04WARP\x12\x11\n\x06height\x18\x03 \x01(\r:\x010\x12\x10\n\x05width\x18\x04 \x01(\r:\x010\x12\x17\n\x0cheight_scale\x18\x08 \x01(\r:\x010\x12\x16\n\x0bwidth_scale\x18\t \x01(\r:\x010\x12Q\n\x08pad_mode\x18\x05 \x01(\x0e25.apollo.perception.inference.ResizeParameter.Pad_mode:\x08CONSTANT\x12\x11\n\tpad_value\x18\x06 \x03(\x02\x12M\n\x0binterp_mode\x18\x07 \x03(\x0e28.apollo.perception.inference.ResizeParameter.Interp_mode"G\n\x0bResize_mode\x12\x08\n\x04WARP\x10\x01\x12\x12\n\x0eFIT_SMALL_SIZE\x10\x02\x12\x1a\n\x16FIT_LARGE_SIZE_AND_PAD\x10\x03":\n\x08Pad_mode\x12\x0c\n\x08CONSTANT\x10\x01\x12\x0c\n\x08MIRRORED\x10\x02\x12\x12\n\x0eREPEAT_NEAREST\x10\x03"I\n\x0bInterp_mode\x12\n\n\x06LINEAR\x10\x01\x12\x08\n\x04AREA\x10\x02\x12\x0b\n\x07NEAREST\x10\x03\x12\t\n\x05CUBIC\x10\x04\x12\x0c\n\x08LANCZOS4\x10\x05"9\n\x13SaltPepperParameter\x12\x13\n\x08fraction\x18\x01 \x01(\x02:\x010\x12\r\n\x05value\x18\x02 \x03(\x02"\x84\x03\n\x0eNoiseParameter\x12\x0f\n\x04prob\x18\x01 \x01(\x02:\x010\x12\x16\n\x07hist_eq\x18\x02 \x01(\x08:\x05false\x12\x16\n\x07inverse\x18\x03 \x01(\x08:\x05false\x12\x19\n\ndecolorize\x18\x04 \x01(\x08:\x05false\x12\x19\n\ngauss_blur\x18\x05 \x01(\x08:\x05false\x12\x10\n\x04jpeg\x18\x06 \x01(\x02:\x02-1\x12\x18\n\tposterize\x18\x07 \x01(\x08:\x05false\x12\x14\n\x05erode\x18\x08 \x01(\x08:\x05false\x12\x19\n\nsaltpepper\x18\t \x01(\x08:\x05false\x12J\n\x10saltpepper_param\x18\n \x01(\x0b20.apollo.perception.inference.SaltPepperParameter\x12\x14\n\x05clahe\x18\x0b \x01(\x08:\x05false\x12\x1d\n\x0econvert_to_hsv\x18\x0c \x01(\x08:\x05false\x12\x1d\n\x0econvert_to_lab\x18\r \x01(\x08:\x05false"\xbd\x02\n\x13DistortionParameter\x12\x1a\n\x0fbrightness_prob\x18\x01 \x01(\x02:\x010\x12\x1b\n\x10brightness_delta\x18\x02 \x01(\x02:\x010\x12\x18\n\rcontrast_prob\x18\x03 \x01(\x02:\x010\x12\x19\n\x0econtrast_lower\x18\x04 \x01(\x02:\x010\x12\x19\n\x0econtrast_upper\x18\x05 \x01(\x02:\x010\x12\x13\n\x08hue_prob\x18\x06 \x01(\x02:\x010\x12\x14\n\thue_delta\x18\x07 \x01(\x02:\x010\x12\x1a\n\x0fsaturation_prob\x18\x08 \x01(\x02:\x010\x12\x1b\n\x10saturation_lower\x18\t \x01(\x02:\x010\x12\x1b\n\x10saturation_upper\x18\n \x01(\x02:\x010\x12\x1c\n\x11random_order_prob\x18\x0b \x01(\x02:\x010"B\n\x12ExpansionParameter\x12\x0f\n\x04prob\x18\x01 \x01(\x02:\x011\x12\x1b\n\x10max_expand_ratio\x18\x02 \x01(\x02:\x011"\xd8\x01\n\rLossParameter\x12\x14\n\x0cignore_label\x18\x01 \x01(\x05\x12Z\n\rnormalization\x18\x03 \x01(\x0e2<.apollo.perception.inference.LossParameter.NormalizationMode:\x05VALID\x12\x11\n\tnormalize\x18\x02 \x01(\x08"B\n\x11NormalizationMode\x12\x08\n\x04FULL\x10\x00\x12\t\n\x05VALID\x10\x01\x12\x0e\n\nBATCH_SIZE\x10\x02\x12\x08\n\x04NONE\x10\x03"L\n\x11AccuracyParameter\x12\x10\n\x05top_k\x18\x01 \x01(\r:\x011\x12\x0f\n\x04axis\x18\x02 \x01(\x05:\x011\x12\x14\n\x0cignore_label\x18\x03 \x01(\x05"\xdf\x01\n\x16AnnotatedDataParameter\x12@\n\rbatch_sampler\x18\x01 \x03(\x0b2).apollo.perception.inference.BatchSampler\x12\x16\n\x0elabel_map_file\x18\x02 \x01(\t\x12S\n\tanno_type\x18\x03 \x01(\x0e2:.apollo.perception.inference.AnnotatedDatum.AnnotationType:\x04BBOX\x12\x16\n\x0bnum_classes\x18\n \x01(\x05:\x013"M\n\x0fArgMaxParameter\x12\x1a\n\x0bout_max_val\x18\x01 \x01(\x08:\x05false\x12\x10\n\x05top_k\x18\x02 \x01(\r:\x011\x12\x0c\n\x04axis\x18\x03 \x01(\x05"9\n\x0fConcatParameter\x12\x0f\n\x04axis\x18\x02 \x01(\x05:\x011\x12\x15\n\nconcat_dim\x18\x01 \x01(\r:\x011"j\n\x12BatchNormParameter\x12\x18\n\x10use_global_stats\x18\x01 \x01(\x08\x12&\n\x17moving_average_fraction\x18\x02 \x01(\x02:\x050.999\x12\x12\n\x03eps\x18\x03 \x01(\x02:\x051e-05"s\n\rBiasParameter\x12\x0f\n\x04axis\x18\x01 \x01(\x05:\x011\x12\x13\n\x08num_axes\x18\x02 \x01(\x05:\x011\x12<\n\x06filler\x18\x03 \x01(\x0b2,.apollo.perception.inference.FillerParameter"L\n\x18ContrastiveLossParameter\x12\x11\n\x06margin\x18\x01 \x01(\x02:\x011\x12\x1d\n\x0elegacy_version\x18\x02 \x01(\x08:\x05false"\xbe\x04\n\x14ConvolutionParameter\x12\x12\n\nnum_output\x18\x01 \x01(\r\x12\x17\n\tbias_term\x18\x02 \x01(\x08:\x04true\x12\x0b\n\x03pad\x18\x03 \x03(\r\x12\x13\n\x0bkernel_size\x18\x04 \x03(\r\x12\x0e\n\x06stride\x18\x06 \x03(\r\x12\x10\n\x08dilation\x18\x12 \x03(\r\x12\x10\n\x05pad_h\x18\t \x01(\r:\x010\x12\x10\n\x05pad_w\x18\n \x01(\r:\x010\x12\x10\n\x08kernel_h\x18\x0b \x01(\r\x12\x10\n\x08kernel_w\x18\x0c \x01(\r\x12\x10\n\x08stride_h\x18\r \x01(\r\x12\x10\n\x08stride_w\x18\x0e \x01(\r\x12\x10\n\x05group\x18\x05 \x01(\r:\x011\x12C\n\rweight_filler\x18\x07 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12A\n\x0bbias_filler\x18\x08 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12Q\n\x06engine\x18\x0f \x01(\x0e28.apollo.perception.inference.ConvolutionParameter.Engine:\x07DEFAULT\x12\x0f\n\x04axis\x18\x10 \x01(\x05:\x011\x12\x1e\n\x0fforce_nd_im2col\x18\x11 \x01(\x08:\x05false"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"0\n\rCropParameter\x12\x0f\n\x04axis\x18\x01 \x01(\x05:\x012\x12\x0e\n\x06offset\x18\x02 \x03(\r"\xba\x02\n\rDataParameter\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x12\n\nbatch_size\x18\x04 \x01(\r\x12\x14\n\trand_skip\x18\x07 \x01(\r:\x010\x12G\n\x07backend\x18\x08 \x01(\x0e2-.apollo.perception.inference.DataParameter.DB:\x07LEVELDB\x12\x10\n\x05scale\x18\x02 \x01(\x02:\x011\x12\x11\n\tmean_file\x18\x03 \x01(\t\x12\x14\n\tcrop_size\x18\x05 \x01(\r:\x010\x12\x15\n\x06mirror\x18\x06 \x01(\x08:\x05false\x12"\n\x13force_encoded_color\x18\t \x01(\x08:\x05false\x12\x13\n\x08prefetch\x18\n \x01(\r:\x014"\x1b\n\x02DB\x12\x0b\n\x07LEVELDB\x10\x00\x12\x08\n\x04LMDB\x10\x01"\xf2\x01\n\x1aDetectionEvaluateParameter\x12\x13\n\x0bnum_classes\x18\x01 \x01(\r\x12\x1e\n\x13background_label_id\x18\x02 \x01(\r:\x010\x12\x1e\n\x11overlap_threshold\x18\x03 \x01(\x02:\x030.5\x12#\n\x15evaluate_difficult_gt\x18\x04 \x01(\x08:\x04true\x12\x16\n\x0ename_size_file\x18\x05 \x01(\t\x12B\n\x0cresize_param\x18\x06 \x01(\x0b2,.apollo.perception.inference.ResizeParameter"[\n\x1eNonMaximumSuppressionParameter\x12\x1a\n\rnms_threshold\x18\x01 \x01(\x02:\x030.3\x12\r\n\x05top_k\x18\x02 \x01(\x05\x12\x0e\n\x03eta\x18\x03 \x01(\x02:\x011"\xee\x01\n\x13SaveOutputParameter\x12\x18\n\x10output_directory\x18\x01 \x01(\t\x12\x1a\n\x12output_name_prefix\x18\x02 \x01(\t\x12\x15\n\routput_format\x18\x03 \x01(\t\x12\x16\n\x0elabel_map_file\x18\x04 \x01(\t\x12\x16\n\x0ename_size_file\x18\x05 \x01(\t\x12\x16\n\x0enum_test_image\x18\x06 \x01(\r\x12B\n\x0cresize_param\x18\x07 \x01(\x0b2,.apollo.perception.inference.ResizeParameter"\x89\x04\n\x18DetectionOutputParameter\x12\x13\n\x0bnum_classes\x18\x01 \x01(\r\x12\x1c\n\x0eshare_location\x18\x02 \x01(\x08:\x04true\x12\x1e\n\x13background_label_id\x18\x03 \x01(\x05:\x010\x12N\n\tnms_param\x18\x04 \x01(\x0b2;.apollo.perception.inference.NonMaximumSuppressionParameter\x12K\n\x11save_output_param\x18\x05 \x01(\x0b20.apollo.perception.inference.SaveOutputParameter\x12R\n\tcode_type\x18\x06 \x01(\x0e27.apollo.perception.inference.PriorBoxParameter.CodeType:\x06CORNER\x12)\n\x1avariance_encoded_in_target\x18\x08 \x01(\x08:\x05false\x12\x16\n\nkeep_top_k\x18\x07 \x01(\x05:\x02-1\x12\x1c\n\x14confidence_threshold\x18\t \x01(\x02\x12\x18\n\tvisualize\x18\n \x01(\x08:\x05false\x12\x1b\n\x13visualize_threshold\x18\x0b \x01(\x02\x12\x11\n\tsave_file\x18\x0c \x01(\t"\xa9\x02\n\x15RegionOutputParameter\x12\x13\n\x0bnum_classes\x18\x01 \x01(\r\x12N\n\tnms_param\x18\x02 \x01(\x0b2;.apollo.perception.inference.NonMaximumSuppressionParameter\x12\x16\n\nkeep_top_k\x18\x03 \x01(\x05:\x02-1\x12\x1c\n\x14confidence_threshold\x18\x04 \x01(\x02\x129\n\tanchorbox\x18\x05 \x03(\x0b2&.apollo.perception.inference.AnchorBox\x12\x10\n\x08nms_type\x18\x06 \x01(\x05\x12\x11\n\tnms_sigma\x18\x07 \x01(\x02\x12\x15\n\x06is_rpn\x18\x08 \x01(\x08:\x05false".\n\x10DropoutParameter\x12\x1a\n\rdropout_ratio\x18\x01 \x01(\x02:\x030.5"\xcc\x01\n\x12DummyDataParameter\x12A\n\x0bdata_filler\x18\x01 \x03(\x0b2,.apollo.perception.inference.FillerParameter\x125\n\x05shape\x18\x06 \x03(\x0b2&.apollo.perception.inference.BlobShape\x12\x0b\n\x03num\x18\x02 \x03(\r\x12\x10\n\x08channels\x18\x03 \x03(\r\x12\x0e\n\x06height\x18\x04 \x03(\r\x12\r\n\x05width\x18\x05 \x03(\r"\xbb\x01\n\x10EltwiseParameter\x12O\n\toperation\x18\x01 \x01(\x0e27.apollo.perception.inference.EltwiseParameter.EltwiseOp:\x03SUM\x12\r\n\x05coeff\x18\x02 \x03(\x02\x12\x1e\n\x10stable_prod_grad\x18\x03 \x01(\x08:\x04true"\'\n\tEltwiseOp\x12\x08\n\x04PROD\x10\x00\x12\x07\n\x03SUM\x10\x01\x12\x07\n\x03MAX\x10\x02" \n\x0cELUParameter\x12\x10\n\x05alpha\x18\x01 \x01(\x02:\x011"\xd8\x01\n\x0eEmbedParameter\x12\x12\n\nnum_output\x18\x01 \x01(\r\x12\x11\n\tinput_dim\x18\x02 \x01(\r\x12\x17\n\tbias_term\x18\x03 \x01(\x08:\x04true\x12C\n\rweight_filler\x18\x04 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12A\n\x0bbias_filler\x18\x05 \x01(\x0b2,.apollo.perception.inference.FillerParameter"D\n\x0cExpParameter\x12\x10\n\x04base\x18\x01 \x01(\x02:\x02-1\x12\x10\n\x05scale\x18\x02 \x01(\x02:\x011\x12\x10\n\x05shift\x18\x03 \x01(\x02:\x010"9\n\x10FlattenParameter\x12\x0f\n\x04axis\x18\x01 \x01(\x05:\x011\x12\x14\n\x08end_axis\x18\x02 \x01(\x05:\x02-1"O\n\x11HDF5DataParameter\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x12\n\nbatch_size\x18\x02 \x01(\r\x12\x16\n\x07shuffle\x18\x03 \x01(\x08:\x05false"(\n\x13HDF5OutputParameter\x12\x11\n\tfile_name\x18\x01 \x01(\t"t\n\x12HingeLossParameter\x12F\n\x04norm\x18\x01 \x01(\x0e24.apollo.perception.inference.HingeLossParameter.Norm:\x02L1"\x16\n\x04Norm\x12\x06\n\x02L1\x10\x01\x12\x06\n\x02L2\x10\x02"8\n\x0cRepeatedList\x12\x11\n\tlist_path\x18\x01 \x01(\t\x12\x15\n\nnum_repeat\x18\x02 \x01(\r:\x011"\x96\x02\n\x10DatasetParameter\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0broot_folder\x18\x02 \x01(\t\x12\x11\n\x06weight\x18\x03 \x01(\x02:\x011\x12M\n\x04type\x18\x04 \x01(\x0e29.apollo.perception.inference.DatasetParameter.DatasetType:\x04LIST\x12\x15\n\x07shuffle\x18\x05 \x01(\x08:\x04true\x12@\n\rrepeated_list\x18\x06 \x03(\x0b2).apollo.perception.inference.RepeatedList""\n\x0bDatasetType\x12\x08\n\x04LIST\x10\x01\x12\t\n\x05BLOCK\x10\x02"\xee\x02\n\x12ImageDataParameter\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x15\n\nbatch_size\x18\x04 \x01(\r:\x011\x12\x14\n\trand_skip\x18\x07 \x01(\r:\x010\x12\x16\n\x07shuffle\x18\x08 \x01(\x08:\x05false\x12\x15\n\nnew_height\x18\t \x01(\r:\x010\x12\x14\n\tnew_width\x18\n \x01(\r:\x010\x12\x16\n\x08is_color\x18\x0b \x01(\x08:\x04true\x12\x10\n\x05scale\x18\x02 \x01(\x02:\x011\x12\x11\n\tmean_file\x18\x03 \x01(\t\x12\x14\n\tcrop_size\x18\x05 \x01(\r:\x010\x12\x15\n\x06mirror\x18\x06 \x01(\x08:\x05false\x12\x15\n\x0broot_folder\x18\x0c \x01(\t:\x00\x12\x13\n\x08prefetch\x18\x14 \x01(\r:\x014\x12@\n\timage_set\x18d \x03(\x0b2-.apollo.perception.inference.DatasetParameter"\'\n\x15InfogainLossParameter\x12\x0e\n\x06source\x18\x01 \x01(\t"\xf7\x01\n\x15InnerProductParameter\x12\x12\n\nnum_output\x18\x01 \x01(\r\x12\x17\n\tbias_term\x18\x02 \x01(\x08:\x04true\x12C\n\rweight_filler\x18\x03 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12A\n\x0bbias_filler\x18\x04 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12\x0f\n\x04axis\x18\x05 \x01(\x05:\x011\x12\x18\n\ttranspose\x18\x06 \x01(\x08:\x05false"G\n\x0eInputParameter\x125\n\x05shape\x18\x01 \x03(\x0b2&.apollo.perception.inference.BlobShape"D\n\x0cLogParameter\x12\x10\n\x04base\x18\x01 \x01(\x02:\x02-1\x12\x10\n\x05scale\x18\x02 \x01(\x02:\x011\x12\x10\n\x05shift\x18\x03 \x01(\x02:\x010"\xe4\x02\n\x0cLRNParameter\x12\x15\n\nlocal_size\x18\x01 \x01(\r:\x015\x12\x10\n\x05alpha\x18\x02 \x01(\x02:\x011\x12\x12\n\x04beta\x18\x03 \x01(\x02:\x040.75\x12Z\n\x0bnorm_region\x18\x04 \x01(\x0e24.apollo.perception.inference.LRNParameter.NormRegion:\x0fACROSS_CHANNELS\x12\x0c\n\x01k\x18\x05 \x01(\x02:\x011\x12I\n\x06engine\x18\x06 \x01(\x0e20.apollo.perception.inference.LRNParameter.Engine:\x07DEFAULT"5\n\nNormRegion\x12\x13\n\x0fACROSS_CHANNELS\x10\x00\x12\x12\n\x0eWITHIN_CHANNEL\x10\x01"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"Z\n\x13MemoryDataParameter\x12\x12\n\nbatch_size\x18\x01 \x01(\r\x12\x10\n\x08channels\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\r\n\x05width\x18\x04 \x01(\r"\xec\t\n\x15MultiBoxLossParameter\x12`\n\rloc_loss_type\x18\x01 \x01(\x0e2>.apollo.perception.inference.MultiBoxLossParameter.LocLossType:\tSMOOTH_L1\x12`\n\x0econf_loss_type\x18\x02 \x01(\x0e2?.apollo.perception.inference.MultiBoxLossParameter.ConfLossType:\x07SOFTMAX\x12\x15\n\nloc_weight\x18\x03 \x01(\x02:\x011\x12\x13\n\x0bnum_classes\x18\x04 \x01(\r\x12\x1c\n\x0eshare_location\x18\x05 \x01(\x08:\x04true\x12`\n\nmatch_type\x18\x06 \x01(\x0e2<.apollo.perception.inference.MultiBoxLossParameter.MatchType:\x0ePER_PREDICTION\x12\x1e\n\x11overlap_threshold\x18\x07 \x01(\x02:\x030.5\x12$\n\x16use_prior_for_matching\x18\x08 \x01(\x08:\x04true\x12\x1e\n\x13background_label_id\x18\t \x01(\r:\x010\x12\x1e\n\x10use_difficult_gt\x18\n \x01(\x08:\x04true\x12\x15\n\rdo_neg_mining\x18\x0b \x01(\x08\x12\x18\n\rneg_pos_ratio\x18\x0c \x01(\x02:\x013\x12\x18\n\x0bneg_overlap\x18\r \x01(\x02:\x030.5\x12R\n\tcode_type\x18\x0e \x01(\x0e27.apollo.perception.inference.PriorBoxParameter.CodeType:\x06CORNER\x12(\n\x19encode_variance_in_target\x18\x10 \x01(\x08:\x05false\x12%\n\x16map_object_to_agnostic\x18\x11 \x01(\x08:\x05false\x12)\n\x1aignore_cross_boundary_bbox\x18\x12 \x01(\x08:\x05false\x12\x18\n\tbp_inside\x18\x13 \x01(\x08:\x05false\x12`\n\x0bmining_type\x18\x14 \x01(\x0e2=.apollo.perception.inference.MultiBoxLossParameter.MiningType:\x0cMAX_NEGATIVE\x12N\n\tnms_param\x18\x15 \x01(\x0b2;.apollo.perception.inference.NonMaximumSuppressionParameter\x12\x17\n\x0bsample_size\x18\x16 \x01(\x05:\x0264\x12 \n\x11use_prior_for_nms\x18\x17 \x01(\x08:\x05false"$\n\x0bLocLossType\x12\x06\n\x02L2\x10\x00\x12\r\n\tSMOOTH_L1\x10\x01")\n\x0cConfLossType\x12\x0b\n\x07SOFTMAX\x10\x00\x12\x0c\n\x08LOGISTIC\x10\x01".\n\tMatchType\x12\r\n\tBIPARTITE\x10\x00\x12\x12\n\x0ePER_PREDICTION\x10\x01":\n\nMiningType\x12\x08\n\x04NONE\x10\x00\x12\x10\n\x0cMAX_NEGATIVE\x10\x01\x12\x10\n\x0cHARD_EXAMPLE\x10\x02"d\n\x0cMVNParameter\x12 \n\x12normalize_variance\x18\x01 \x01(\x08:\x04true\x12\x1e\n\x0facross_channels\x18\x02 \x01(\x08:\x05false\x12\x12\n\x03eps\x18\x03 \x01(\x02:\x051e-09"\xa8\x01\n\x12NormalizeParameter\x12\x1c\n\x0eacross_spatial\x18\x01 \x01(\x08:\x04true\x12B\n\x0cscale_filler\x18\x02 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12\x1c\n\x0echannel_shared\x18\x03 \x01(\x08:\x04true\x12\x12\n\x03eps\x18\x04 \x01(\x02:\x051e-10"K\n\x12ParameterParameter\x125\n\x05shape\x18\x01 \x01(\x0b2&.apollo.perception.inference.BlobShape"!\n\x10PermuteParameter\x12\r\n\x05order\x18\x01 \x03(\r"\xc3\x04\n\x10PoolingParameter\x12K\n\x04pool\x18\x01 \x01(\x0e28.apollo.perception.inference.PoolingParameter.PoolMethod:\x03MAX\x12\x0e\n\x03pad\x18\x04 \x01(\r:\x010\x12\x10\n\x05pad_h\x18\t \x01(\r:\x010\x12\x10\n\x05pad_w\x18\n \x01(\r:\x010\x12\x13\n\x0bkernel_size\x18\x02 \x01(\r\x12\x10\n\x08kernel_h\x18\x05 \x01(\r\x12\x10\n\x08kernel_w\x18\x06 \x01(\r\x12\x11\n\x06stride\x18\x03 \x01(\r:\x011\x12\x10\n\x08stride_h\x18\x07 \x01(\r\x12\x10\n\x08stride_w\x18\x08 \x01(\r\x12M\n\x06engine\x18\x0b \x01(\x0e24.apollo.perception.inference.PoolingParameter.Engine:\x07DEFAULT\x12\x1d\n\x0eglobal_pooling\x18\x0c \x01(\x08:\x05false\x12Q\n\nround_mode\x18\r \x01(\x0e27.apollo.perception.inference.PoolingParameter.RoundMode:\x04CEIL".\n\nPoolMethod\x12\x07\n\x03MAX\x10\x00\x12\x07\n\x03AVE\x10\x01\x12\x0e\n\nSTOCHASTIC\x10\x02"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02" \n\tRoundMode\x12\x08\n\x04CEIL\x10\x00\x12\t\n\x05FLOOR\x10\x01"F\n\x0ePowerParameter\x12\x10\n\x05power\x18\x01 \x01(\x02:\x011\x12\x10\n\x05scale\x18\x02 \x01(\x02:\x011\x12\x10\n\x05shift\x18\x03 \x01(\x02:\x010"\xb5\x02\n\x11PriorBoxParameter\x12\x10\n\x08min_size\x18\x01 \x03(\x02\x12\x10\n\x08max_size\x18\x02 \x03(\x02\x12\x14\n\x0caspect_ratio\x18\x03 \x03(\x02\x12\x12\n\x04flip\x18\x04 \x01(\x08:\x04true\x12\x13\n\x04clip\x18\x05 \x01(\x08:\x05false\x12\x10\n\x08variance\x18\x06 \x03(\x02\x12\x10\n\x08img_size\x18\x07 \x01(\r\x12\r\n\x05img_h\x18\x08 \x01(\r\x12\r\n\x05img_w\x18\t \x01(\r\x12\x0c\n\x04step\x18\n \x01(\x02\x12\x0e\n\x06step_h\x18\x0b \x01(\x02\x12\x0e\n\x06step_w\x18\x0c \x01(\x02\x12\x13\n\x06offset\x18\r \x01(\x02:\x030.5"8\n\x08CodeType\x12\n\n\x06CORNER\x10\x01\x12\x0f\n\x0bCENTER_SIZE\x10\x02\x12\x0f\n\x0bCORNER_SIZE\x10\x03"g\n\x0fPythonParameter\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\r\n\x05layer\x18\x02 \x01(\t\x12\x13\n\tparam_str\x18\x03 \x01(\t:\x00\x12 \n\x11share_in_parallel\x18\x04 \x01(\x08:\x05false"\xec\x01\n\x12RecurrentParameter\x12\x15\n\nnum_output\x18\x01 \x01(\r:\x010\x12C\n\rweight_filler\x18\x02 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12A\n\x0bbias_filler\x18\x03 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12\x19\n\ndebug_info\x18\x04 \x01(\x08:\x05false\x12\x1c\n\rexpose_hidden\x18\x05 \x01(\x08:\x05false"\xc3\x01\n\x12ReductionParameter\x12S\n\toperation\x18\x01 \x01(\x0e2;.apollo.perception.inference.ReductionParameter.ReductionOp:\x03SUM\x12\x0f\n\x04axis\x18\x02 \x01(\x05:\x010\x12\x10\n\x05coeff\x18\x03 \x01(\x02:\x011"5\n\x0bReductionOp\x12\x07\n\x03SUM\x10\x01\x12\x08\n\x04ASUM\x10\x02\x12\t\n\x05SUMSQ\x10\x03\x12\x08\n\x04MEAN\x10\x04"\xa3\x01\n\rReLUParameter\x12\x19\n\x0enegative_slope\x18\x01 \x01(\x02:\x010\x12J\n\x06engine\x18\x02 \x01(\x0e21.apollo.perception.inference.ReLUParameter.Engine:\x07DEFAULT"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"p\n\x10ReshapeParameter\x125\n\x05shape\x18\x01 \x01(\x0b2&.apollo.perception.inference.BlobShape\x12\x0f\n\x04axis\x18\x02 \x01(\x05:\x010\x12\x14\n\x08num_axes\x18\x03 \x01(\x05:\x02-1"s\n\x13ROIPoolingParameter\x12\x13\n\x08pooled_h\x18\x01 \x01(\r:\x010\x12\x13\n\x08pooled_w\x18\x02 \x01(\r:\x010\x12\x18\n\rspatial_scale\x18\x03 \x01(\x02:\x011\x12\x18\n\tuse_floor\x18\n \x01(\x08:\x05false"\xd1\x01\n\x0eScaleParameter\x12\x0f\n\x04axis\x18\x01 \x01(\x05:\x011\x12\x13\n\x08num_axes\x18\x02 \x01(\x05:\x011\x12<\n\x06filler\x18\x03 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12\x18\n\tbias_term\x18\x04 \x01(\x08:\x05false\x12A\n\x0bbias_filler\x18\x05 \x01(\x0b2,.apollo.perception.inference.FillerParameter"\x8e\x01\n\x10SigmoidParameter\x12M\n\x06engine\x18\x01 \x01(\x0e24.apollo.perception.inference.SigmoidParameter.Engine:\x07DEFAULT"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"L\n\x0eSliceParameter\x12\x0f\n\x04axis\x18\x03 \x01(\x05:\x011\x12\x13\n\x0bslice_point\x18\x02 \x03(\r\x12\x14\n\tslice_dim\x18\x01 \x01(\r:\x011"\x9f\x01\n\x10SoftmaxParameter\x12M\n\x06engine\x18\x01 \x01(\x0e24.apollo.perception.inference.SoftmaxParameter.Engine:\x07DEFAULT\x12\x0f\n\x04axis\x18\x02 \x01(\x05:\x011"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"\x88\x01\n\rTanHParameter\x12J\n\x06engine\x18\x01 \x01(\x0e21.apollo.perception.inference.TanHParameter.Engine:\x07DEFAULT"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"/\n\rTileParameter\x12\x0f\n\x04axis\x18\x01 \x01(\x05:\x011\x12\r\n\x05tiles\x18\x02 \x01(\x05"*\n\x12ThresholdParameter\x12\x14\n\tthreshold\x18\x01 \x01(\x02:\x010"\xd1\x01\n\x12VideoDataParameter\x12U\n\nvideo_type\x18\x01 \x01(\x0e29.apollo.perception.inference.VideoDataParameter.VideoType:\x06WEBCAM\x12\x14\n\tdevice_id\x18\x02 \x01(\x05:\x010\x12\x12\n\nvideo_file\x18\x03 \x01(\t\x12\x16\n\x0bskip_frames\x18\x04 \x01(\r:\x010""\n\tVideoType\x12\n\n\x06WEBCAM\x10\x00\x12\t\n\x05VIDEO\x10\x01"\xc1\x02\n\x13WindowDataParameter\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x10\n\x05scale\x18\x02 \x01(\x02:\x011\x12\x11\n\tmean_file\x18\x03 \x01(\t\x12\x12\n\nbatch_size\x18\x04 \x01(\r\x12\x14\n\tcrop_size\x18\x05 \x01(\r:\x010\x12\x15\n\x06mirror\x18\x06 \x01(\x08:\x05false\x12\x19\n\x0cfg_threshold\x18\x07 \x01(\x02:\x030.5\x12\x19\n\x0cbg_threshold\x18\x08 \x01(\x02:\x030.5\x12\x19\n\x0bfg_fraction\x18\t \x01(\x02:\x040.25\x12\x16\n\x0bcontext_pad\x18\n \x01(\r:\x010\x12\x17\n\tcrop_mode\x18\x0b \x01(\t:\x04warp\x12\x1b\n\x0ccache_images\x18\x0c \x01(\x08:\x05false\x12\x15\n\x0broot_folder\x18\r \x01(\t:\x00"\x97\x02\n\x0cSPPParameter\x12\x16\n\x0epyramid_height\x18\x01 \x01(\r\x12G\n\x04pool\x18\x02 \x01(\x0e24.apollo.perception.inference.SPPParameter.PoolMethod:\x03MAX\x12I\n\x06engine\x18\x06 \x01(\x0e20.apollo.perception.inference.SPPParameter.Engine:\x07DEFAULT".\n\nPoolMethod\x12\x07\n\x03MAX\x10\x00\x12\x07\n\x03AVE\x10\x01\x12\x0e\n\nSTOCHASTIC\x10\x02"+\n\x06Engine\x12\x0b\n\x07DEFAULT\x10\x00\x12\t\n\x05CAFFE\x10\x01\x12\t\n\x05CUDNN\x10\x02"\xf8\x19\n\x10V1LayerParameter\x12\x0e\n\x06bottom\x18\x02 \x03(\t\x12\x0b\n\x03top\x18\x03 \x03(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12:\n\x07include\x18  \x03(\x0b2).apollo.perception.inference.NetStateRule\x12:\n\x07exclude\x18! \x03(\x0b2).apollo.perception.inference.NetStateRule\x12E\n\x04type\x18\x05 \x01(\x0e27.apollo.perception.inference.V1LayerParameter.LayerType\x125\n\x05blobs\x18\x06 \x03(\x0b2&.apollo.perception.inference.BlobProto\x12\x0e\n\x05param\x18\xe9\x07 \x03(\t\x12T\n\x0fblob_share_mode\x18\xea\x07 \x03(\x0e2:.apollo.perception.inference.V1LayerParameter.DimCheckMode\x12\x10\n\x08blobs_lr\x18\x07 \x03(\x02\x12\x14\n\x0cweight_decay\x18\x08 \x03(\x02\x12\x13\n\x0bloss_weight\x18# \x03(\x02\x12F\n\x0eaccuracy_param\x18\x1b \x01(\x0b2..apollo.perception.inference.AccuracyParameter\x12B\n\x0cargmax_param\x18\x17 \x01(\x0b2,.apollo.perception.inference.ArgMaxParameter\x12B\n\x0cconcat_param\x18\t \x01(\x0b2,.apollo.perception.inference.ConcatParameter\x12U\n\x16contrastive_loss_param\x18( \x01(\x0b25.apollo.perception.inference.ContrastiveLossParameter\x12L\n\x11convolution_param\x18\n \x01(\x0b21.apollo.perception.inference.ConvolutionParameter\x12>\n\ndata_param\x18\x0b \x01(\x0b2*.apollo.perception.inference.DataParameter\x12D\n\rdropout_param\x18\x0c \x01(\x0b2-.apollo.perception.inference.DropoutParameter\x12I\n\x10dummy_data_param\x18\x1a \x01(\x0b2/.apollo.perception.inference.DummyDataParameter\x12D\n\reltwise_param\x18\x18 \x01(\x0b2-.apollo.perception.inference.EltwiseParameter\x12<\n\texp_param\x18) \x01(\x0b2).apollo.perception.inference.ExpParameter\x12G\n\x0fhdf5_data_param\x18\r \x01(\x0b2..apollo.perception.inference.HDF5DataParameter\x12K\n\x11hdf5_output_param\x18\x0e \x01(\x0b20.apollo.perception.inference.HDF5OutputParameter\x12I\n\x10hinge_loss_param\x18\x1d \x01(\x0b2/.apollo.perception.inference.HingeLossParameter\x12I\n\x10image_data_param\x18\x0f \x01(\x0b2/.apollo.perception.inference.ImageDataParameter\x12O\n\x13infogain_loss_param\x18\x10 \x01(\x0b22.apollo.perception.inference.InfogainLossParameter\x12O\n\x13inner_product_param\x18\x11 \x01(\x0b22.apollo.perception.inference.InnerProductParameter\x12<\n\tlrn_param\x18\x12 \x01(\x0b2).apollo.perception.inference.LRNParameter\x12K\n\x11memory_data_param\x18\x16 \x01(\x0b20.apollo.perception.inference.MemoryDataParameter\x12<\n\tmvn_param\x18" \x01(\x0b2).apollo.perception.inference.MVNParameter\x12D\n\rpooling_param\x18\x13 \x01(\x0b2-.apollo.perception.inference.PoolingParameter\x12@\n\x0bpower_param\x18\x15 \x01(\x0b2+.apollo.perception.inference.PowerParameter\x12>\n\nrelu_param\x18\x1e \x01(\x0b2*.apollo.perception.inference.ReLUParameter\x12D\n\rsigmoid_param\x18& \x01(\x0b2-.apollo.perception.inference.SigmoidParameter\x12D\n\rsoftmax_param\x18\' \x01(\x0b2-.apollo.perception.inference.SoftmaxParameter\x12@\n\x0bslice_param\x18\x1f \x01(\x0b2+.apollo.perception.inference.SliceParameter\x12>\n\ntanh_param\x18% \x01(\x0b2*.apollo.perception.inference.TanHParameter\x12H\n\x0fthreshold_param\x18\x19 \x01(\x0b2/.apollo.perception.inference.ThresholdParameter\x12K\n\x11window_data_param\x18\x14 \x01(\x0b20.apollo.perception.inference.WindowDataParameter\x12M\n\x0ftransform_param\x18$ \x01(\x0b24.apollo.perception.inference.TransformationParameter\x12>\n\nloss_param\x18* \x01(\x0b2*.apollo.perception.inference.LossParameter\x12<\n\x05layer\x18\x01 \x01(\x0b2-.apollo.perception.inference.V0LayerParameter"\xd8\x04\n\tLayerType\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06ABSVAL\x10#\x12\x0c\n\x08ACCURACY\x10\x01\x12\n\n\x06ARGMAX\x10\x1e\x12\x08\n\x04BNLL\x10\x02\x12\n\n\x06CONCAT\x10\x03\x12\x14\n\x10CONTRASTIVE_LOSS\x10%\x12\x0f\n\x0bCONVOLUTION\x10\x04\x12\x08\n\x04DATA\x10\x05\x12\x11\n\rDECONVOLUTION\x10\'\x12\x0b\n\x07DROPOUT\x10\x06\x12\x0e\n\nDUMMY_DATA\x10 \x12\x12\n\x0eEUCLIDEAN_LOSS\x10\x07\x12\x0b\n\x07ELTWISE\x10\x19\x12\x07\n\x03EXP\x10&\x12\x0b\n\x07FLATTEN\x10\x08\x12\r\n\tHDF5_DATA\x10\t\x12\x0f\n\x0bHDF5_OUTPUT\x10\n\x12\x0e\n\nHINGE_LOSS\x10\x1c\x12\n\n\x06IM2COL\x10\x0b\x12\x0e\n\nIMAGE_DATA\x10\x0c\x12\x11\n\rINFOGAIN_LOSS\x10\r\x12\x11\n\rINNER_PRODUCT\x10\x0e\x12\x07\n\x03LRN\x10\x0f\x12\x0f\n\x0bMEMORY_DATA\x10\x1d\x12\x1d\n\x19MULTINOMIAL_LOGISTIC_LOSS\x10\x10\x12\x07\n\x03MVN\x10"\x12\x0b\n\x07POOLING\x10\x11\x12\t\n\x05POWER\x10\x1a\x12\x08\n\x04RELU\x10\x12\x12\x0b\n\x07SIGMOID\x10\x13\x12\x1e\n\x1aSIGMOID_CROSS_ENTROPY_LOSS\x10\x1b\x12\x0b\n\x07SILENCE\x10$\x12\x0b\n\x07SOFTMAX\x10\x14\x12\x10\n\x0cSOFTMAX_LOSS\x10\x15\x12\t\n\x05SPLIT\x10\x16\x12\t\n\x05SLICE\x10!\x12\x08\n\x04TANH\x10\x17\x12\x0f\n\x0bWINDOW_DATA\x10\x18\x12\r\n\tTHRESHOLD\x10\x1f"*\n\x0cDimCheckMode\x12\n\n\x06STRICT\x10\x00\x12\x0e\n\nPERMISSIVE\x10\x01"\xeb\x08\n\x10V0LayerParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x12\n\nnum_output\x18\x03 \x01(\r\x12\x16\n\x08biasterm\x18\x04 \x01(\x08:\x04true\x12C\n\rweight_filler\x18\x05 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12A\n\x0bbias_filler\x18\x06 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12\x0e\n\x03pad\x18\x07 \x01(\r:\x010\x12\x12\n\nkernelsize\x18\x08 \x01(\r\x12\x10\n\x05group\x18\t \x01(\r:\x011\x12\x11\n\x06stride\x18\n \x01(\r:\x011\x12K\n\x04pool\x18\x0b \x01(\x0e28.apollo.perception.inference.V0LayerParameter.PoolMethod:\x03MAX\x12\x1a\n\rdropout_ratio\x18\x0c \x01(\x02:\x030.5\x12\x15\n\nlocal_size\x18\r \x01(\r:\x015\x12\x10\n\x05alpha\x18\x0e \x01(\x02:\x011\x12\x12\n\x04beta\x18\x0f \x01(\x02:\x040.75\x12\x0c\n\x01k\x18\x16 \x01(\x02:\x011\x12\x0e\n\x06source\x18\x10 \x01(\t\x12\x10\n\x05scale\x18\x11 \x01(\x02:\x011\x12\x10\n\x08meanfile\x18\x12 \x01(\t\x12\x11\n\tbatchsize\x18\x13 \x01(\r\x12\x13\n\x08cropsize\x18\x14 \x01(\r:\x010\x12\x15\n\x06mirror\x18\x15 \x01(\x08:\x05false\x125\n\x05blobs\x182 \x03(\x0b2&.apollo.perception.inference.BlobProto\x12\x10\n\x08blobs_lr\x183 \x03(\x02\x12\x14\n\x0cweight_decay\x184 \x03(\x02\x12\x14\n\trand_skip\x185 \x01(\r:\x010\x12\x1d\n\x10det_fg_threshold\x186 \x01(\x02:\x030.5\x12\x1d\n\x10det_bg_threshold\x187 \x01(\x02:\x030.5\x12\x1d\n\x0fdet_fg_fraction\x188 \x01(\x02:\x040.25\x12\x1a\n\x0fdet_context_pad\x18: \x01(\r:\x010\x12\x1b\n\rdet_crop_mode\x18; \x01(\t:\x04warp\x12\x12\n\x07new_num\x18< \x01(\x05:\x010\x12\x17\n\x0cnew_channels\x18= \x01(\x05:\x010\x12\x15\n\nnew_height\x18> \x01(\x05:\x010\x12\x14\n\tnew_width\x18? \x01(\x05:\x010\x12\x1d\n\x0eshuffle_images\x18@ \x01(\x08:\x05false\x12\x15\n\nconcat_dim\x18A \x01(\r:\x011\x12L\n\x11hdf5_output_param\x18\xe9\x07 \x01(\x0b20.apollo.perception.inference.HDF5OutputParameter".\n\nPoolMethod\x12\x07\n\x03MAX\x10\x00\x12\x07\n\x03AVE\x10\x01\x12\x0e\n\nSTOCHASTIC\x10\x02"m\n\x0ePReLUParameter\x12<\n\x06filler\x18\x01 \x01(\x0b2,.apollo.perception.inference.FillerParameter\x12\x1d\n\x0echannel_shared\x18\x02 \x01(\x08:\x05false"j\n\x10PaddingParameter\x12\x10\n\x05pad_t\x18\x01 \x01(\r:\x010\x12\x10\n\x05pad_b\x18\x02 \x01(\r:\x010\x12\x10\n\x05pad_l\x18\x03 \x01(\r:\x010\x12\x10\n\x05pad_r\x18\x04 \x01(\r:\x010\x12\x0e\n\x03val\x18\x05 \x01(\x02:\x010"\xb8\x01\n\x11YoloLossParameter\x12\\\n\rreg_loss_type\x18\x01 \x01(\x0e2:.apollo.perception.inference.YoloLossParameter.RegLossType:\tSMOOTH_L1\x12\x17\n\x0btarget_axis\x18\x02 \x01(\x05:\x02-1",\n\x0bRegLossType\x12\x06\n\x02L2\x10\x00\x12\x06\n\x02L1\x10\x01\x12\r\n\tSMOOTH_L1\x10\x02"%\n\x11YoloDumpParameter\x12\x10\n\x08dump_dir\x18\x01 \x01(\t"P\n\x14YoloAnchorsParameter\x12\x14\n\x0canchors_file\x18\x01 \x01(\t\x12\x10\n\x05ref_w\x18\x02 \x01(\x05:\x011\x12\x10\n\x05ref_h\x18\x03 \x01(\x05:\x011"\x84\x01\n\x13DimensionStatistics\x12\x11\n\x06mean_h\x18\x01 \x01(\x02:\x010\x12\x11\n\x06mean_w\x18\x02 \x01(\x02:\x010\x12\x11\n\x06mean_l\x18\x03 \x01(\x02:\x010\x12\x10\n\x05std_h\x18\x04 \x01(\x02:\x011\x12\x10\n\x05std_w\x18\x05 \x01(\x02:\x011\x12\x10\n\x05std_l\x18\x06 \x01(\x02:\x011"\xe0\x02\n\x13YoloTargetParameter\x12\x19\n\x0eneg_rois_ratio\x18\x01 \x01(\x02:\x011\x12\x1a\n\rign_threshold\x18\x02 \x01(\x02:\x030.6\x12\x1a\n\rneg_threshold\x18\x03 \x01(\x02:\x030.1\x12\x18\n\nmin_height\x18\x04 \x01(\x02:\x040.05\x12\x18\n\nbias_match\x18\x05 \x01(\x08:\x04true\x12\x15\n\x07rescore\x18\x06 \x01(\x08:\x04true\x12\x12\n\x07ori_cyc\x18\x07 \x01(\x05:\x011\x12\x16\n\nobj_weight\x18\x08 \x01(\x02:\x0210\x12\x17\n\x0cnoobj_weight\x18\t \x01(\x02:\x011\x12\x16\n\x0bnum_classes\x18\n \x01(\x05:\x010\x12N\n\x14dimension_statistics\x18\x0b \x03(\x0b20.apollo.perception.inference.DimensionStatistics"\x8f\x04\n\x17RegionProposalParameter\x129\n\tanchorbox\x18\x01 \x03(\x0b2&.apollo.perception.inference.AnchorBox\x12\x12\n\nthresholds\x18\x02 \x03(\x02\x12\x1c\n\x11orientation_scale\x18\x0e \x01(\x02:\x010\x12\x14\n\x0cobject_scale\x18\x03 \x01(\r\x12\x16\n\x0enoobject_scale\x18\x04 \x01(\r\x12\x13\n\x0bclass_scale\x18\x05 \x01(\r\x12\x13\n\x0bcoord_scale\x18\x06 \x01(\r\x12\x0e\n\x06jitter\x18\x07 \x01(\x02\x12\x0c\n\x04bias\x18\x08 \x01(\x02\x12\x0f\n\x07rescore\x18\t \x01(\x08\x12\x13\n\x0bnum_classes\x18\n \x01(\r\x12\x12\n\nbias_match\x18\x0b \x01(\x08\x12\x11\n\tthreshold\x18\x0c \x01(\x02\x12\x18\n\x0btricky_iter\x18\r \x01(\r:\x03400\x12N\n\tnms_param\x18\x0f \x01(\x0b2;.apollo.perception.inference.NonMaximumSuppressionParameter\x12\x16\n\nkeep_top_k\x18\x10 \x01(\x05:\x02-1\x12\x15\n\rpos_threshold\x18\x11 \x01(\x02\x12\x15\n\rneg_threshold\x18\x12 \x01(\x02\x12\x14\n\tneg_ratio\x18\x13 \x01(\x05:\x013"\x93\x05\n\x0fRegionParameter\x129\n\tanchorbox\x18\x01 \x03(\x0b2&.apollo.perception.inference.AnchorBox\x12\x12\n\nthresholds\x18\x02 \x03(\x02\x12\x1c\n\x11orientation_scale\x18\x0e \x01(\x02:\x010\x12\x1a\n\x0fdimension_scale\x18\x0f \x01(\x02:\x010\x12\x16\n\x0bfront_scale\x18\x13 \x01(\x02:\x010\x12\x15\n\nrear_scale\x18\x14 \x01(\x02:\x010\x12\x14\n\x0cobject_scale\x18\x03 \x01(\r\x12\x16\n\x0enoobject_scale\x18\x04 \x01(\r\x12\x13\n\x0bclass_scale\x18\x05 \x01(\x02\x12\x13\n\x0bcoord_scale\x18\x06 \x01(\r\x12\x0e\n\x06jitter\x18\x07 \x01(\x02\x12\x0c\n\x04bias\x18\x08 \x01(\x02\x12\x0f\n\x07rescore\x18\t \x01(\x08\x12\x13\n\x0bnum_classes\x18\n \x01(\r\x12\x12\n\nbias_match\x18\x0b \x01(\x08\x12\x11\n\tthreshold\x18\x0c \x01(\x02\x12\x18\n\x0btricky_iter\x18\r \x01(\r:\x03400\x12\x1a\n\x0buse_l1_loss\x18\x10 \x01(\x08:\x05false\x12 \n\x11use_twice_softmax\x18\x11 \x01(\x08:\x05false\x12#\n\x14is_anchor_normalized\x18\x12 \x01(\x08:\x05false\x12\x12\n\nori_enable\x18\x15 \x03(\x08\x12\x1e\n\nanchorfile\x18\x16 \x01(\t:\nanchor.txt\x12\x1e\n\x0fuse_side_box_v2\x18\x17 \x01(\x08:\x05false\x12\x1e\n\x0fuse_side_box_v3\x18\x18 \x01(\x08:\x05false\x12\x14\n\tori_cycle\x18\x19 \x01(\x05:\x011"!\n\tAnchorBox\x12\t\n\x01w\x18\x01 \x01(\x02\x12\t\n\x01h\x18\x02 \x01(\x02" \n\x0eReorgParameter\x12\x0e\n\x06stride\x18\x01 \x01(\r"7\n\x10BBoxRegParameter\x12\x11\n\tbbox_mean\x18\x01 \x03(\x02\x12\x10\n\x08bbox_std\x18\x02 \x03(\x02"\xa1\x02\n\x17DFMBPSROIAlignParameter\x12\x12\n\nheat_map_a\x18\x01 \x01(\x02\x12\x12\n\noutput_dim\x18\x02 \x01(\x05\x12\x14\n\x0cgroup_height\x18\x03 \x01(\x05\x12\x13\n\x0bgroup_width\x18\x04 \x01(\x05\x12\x15\n\rpooled_height\x18\x05 \x01(\x05\x12\x14\n\x0cpooled_width\x18\x06 \x01(\x05\x12\x11\n\tpad_ratio\x18\x07 \x01(\x02\x12\x17\n\x0fsample_per_part\x18\x08 \x01(\x05\x12\x14\n\ttrans_std\x18\t \x01(\x02:\x010\x12\x16\n\x0bpart_height\x18\n \x01(\x05:\x010\x12\x15\n\npart_width\x18\x0b \x01(\x05:\x010\x12\x15\n\nheat_map_b\x18\x0c \x01(\x02:\x010"\xcd\x04\n\x1bDetectionOutputSSDParameter\x12\x12\n\nheat_map_a\x18\x01 \x01(\x02\x12\x15\n\nmin_size_h\x18\x02 \x01(\x02:\x012\x12\x15\n\nmin_size_w\x18\x03 \x01(\x02:\x012\x12o\n\rmin_size_mode\x18\x04 \x01(\x0e2F.apollo.perception.inference.DetectionOutputSSDParameter.MIN_SIZE_MODE:\x10HEIGHT_AND_WIDTH\x12\x1f\n\x14threshold_objectness\x18\x05 \x01(\x02:\x010\x12I\n\x10gen_anchor_param\x18\x06 \x01(\x0b2/.apollo.perception.inference.GenAnchorParameter\x12%\n\x16refine_out_of_map_bbox\x18\x07 \x01(\x08:\x05false\x12?\n\tnms_param\x18\x08 \x01(\x0b2,.apollo.perception.inference.NMSSSDParameter\x12\x14\n\tnum_class\x18\t \x01(\r:\x011\x12(\n\x19rpn_proposal_output_score\x18\n \x01(\x08:\x05false\x12\x18\n\x10regress_agnostic\x18\x0b \x01(\x08\x12\x11\n\tthreshold\x18\x0c \x03(\x02":\n\rMIN_SIZE_MODE\x12\x14\n\x10HEIGHT_AND_WIDTH\x10\x00\x12\x13\n\x0fHEIGHT_OR_WIDTH\x10\x01"\xc6\x02\n\x0fNMSSSDParameter\x12\x16\n\x08need_nms\x18\x01 \x01(\x08:\x04true\x12\x15\n\roverlap_ratio\x18\x02 \x03(\x02\x12\r\n\x05top_n\x18\x03 \x03(\r\x12\x18\n\tadd_score\x18\x04 \x01(\x08:\x05false\x12\x17\n\x0fmax_candidate_n\x18\x05 \x03(\x05\x12\x14\n\x0cuse_soft_nms\x18\x06 \x03(\x08\x12 \n\x11nms_among_classes\x18\x07 \x01(\x08:\x05false\x12\x0e\n\x06voting\x18\x08 \x03(\x08\x12\x10\n\x08vote_iou\x18\t \x03(\x02\x12!\n\x16force_identity_iou_thr\x18\n \x01(\x02:\x011\x12!\n\x16force_imparity_iou_thr\x18\x0b \x01(\x02:\x010\x12"\n\x16nms_gpu_max_n_per_time\x18\x0c \x01(\x05:\x02-1"A\n\x12GenAnchorParameter\x12\x14\n\x0canchor_width\x18\x01 \x03(\x02\x12\x15\n\ranchor_height\x18\x02 \x03(\x02*\x1c\n\x05Phase\x12\t\n\x05TRAIN\x10\x00\x12\x08\n\x04TEST\x10\x01')
_PHASE = DESCRIPTOR.enum_types_by_name['Phase']
Phase = enum_type_wrapper.EnumTypeWrapper(_PHASE)
TRAIN = 0
TEST = 1
_BLOBSHAPE = DESCRIPTOR.message_types_by_name['BlobShape']
_BLOBPROTO = DESCRIPTOR.message_types_by_name['BlobProto']
_DATUM = DESCRIPTOR.message_types_by_name['Datum']
_LABELMAPITEM = DESCRIPTOR.message_types_by_name['LabelMapItem']
_LABELMAP = DESCRIPTOR.message_types_by_name['LabelMap']
_SAMPLER = DESCRIPTOR.message_types_by_name['Sampler']
_SAMPLECONSTRAINT = DESCRIPTOR.message_types_by_name['SampleConstraint']
_BATCHSAMPLER = DESCRIPTOR.message_types_by_name['BatchSampler']
_EMITCONSTRAINT = DESCRIPTOR.message_types_by_name['EmitConstraint']
_NORMALIZEDBBOX = DESCRIPTOR.message_types_by_name['NormalizedBBox']
_BBOX3D = DESCRIPTOR.message_types_by_name['BBox3D']
_ANNOTATION = DESCRIPTOR.message_types_by_name['Annotation']
_ANNOTATIONGROUP = DESCRIPTOR.message_types_by_name['AnnotationGroup']
_ANNOTATEDDATUM = DESCRIPTOR.message_types_by_name['AnnotatedDatum']
_FILLERPARAMETER = DESCRIPTOR.message_types_by_name['FillerParameter']
_NETPARAMETER = DESCRIPTOR.message_types_by_name['NetParameter']
_NETSTATE = DESCRIPTOR.message_types_by_name['NetState']
_NETSTATERULE = DESCRIPTOR.message_types_by_name['NetStateRule']
_PARAMSPEC = DESCRIPTOR.message_types_by_name['ParamSpec']
_LAYERPARAMETER = DESCRIPTOR.message_types_by_name['LayerParameter']
_TRANSFORMATIONPARAMETER = DESCRIPTOR.message_types_by_name['TransformationParameter']
_RESIZEPARAMETER = DESCRIPTOR.message_types_by_name['ResizeParameter']
_SALTPEPPERPARAMETER = DESCRIPTOR.message_types_by_name['SaltPepperParameter']
_NOISEPARAMETER = DESCRIPTOR.message_types_by_name['NoiseParameter']
_DISTORTIONPARAMETER = DESCRIPTOR.message_types_by_name['DistortionParameter']
_EXPANSIONPARAMETER = DESCRIPTOR.message_types_by_name['ExpansionParameter']
_LOSSPARAMETER = DESCRIPTOR.message_types_by_name['LossParameter']
_ACCURACYPARAMETER = DESCRIPTOR.message_types_by_name['AccuracyParameter']
_ANNOTATEDDATAPARAMETER = DESCRIPTOR.message_types_by_name['AnnotatedDataParameter']
_ARGMAXPARAMETER = DESCRIPTOR.message_types_by_name['ArgMaxParameter']
_CONCATPARAMETER = DESCRIPTOR.message_types_by_name['ConcatParameter']
_BATCHNORMPARAMETER = DESCRIPTOR.message_types_by_name['BatchNormParameter']
_BIASPARAMETER = DESCRIPTOR.message_types_by_name['BiasParameter']
_CONTRASTIVELOSSPARAMETER = DESCRIPTOR.message_types_by_name['ContrastiveLossParameter']
_CONVOLUTIONPARAMETER = DESCRIPTOR.message_types_by_name['ConvolutionParameter']
_CROPPARAMETER = DESCRIPTOR.message_types_by_name['CropParameter']
_DATAPARAMETER = DESCRIPTOR.message_types_by_name['DataParameter']
_DETECTIONEVALUATEPARAMETER = DESCRIPTOR.message_types_by_name['DetectionEvaluateParameter']
_NONMAXIMUMSUPPRESSIONPARAMETER = DESCRIPTOR.message_types_by_name['NonMaximumSuppressionParameter']
_SAVEOUTPUTPARAMETER = DESCRIPTOR.message_types_by_name['SaveOutputParameter']
_DETECTIONOUTPUTPARAMETER = DESCRIPTOR.message_types_by_name['DetectionOutputParameter']
_REGIONOUTPUTPARAMETER = DESCRIPTOR.message_types_by_name['RegionOutputParameter']
_DROPOUTPARAMETER = DESCRIPTOR.message_types_by_name['DropoutParameter']
_DUMMYDATAPARAMETER = DESCRIPTOR.message_types_by_name['DummyDataParameter']
_ELTWISEPARAMETER = DESCRIPTOR.message_types_by_name['EltwiseParameter']
_ELUPARAMETER = DESCRIPTOR.message_types_by_name['ELUParameter']
_EMBEDPARAMETER = DESCRIPTOR.message_types_by_name['EmbedParameter']
_EXPPARAMETER = DESCRIPTOR.message_types_by_name['ExpParameter']
_FLATTENPARAMETER = DESCRIPTOR.message_types_by_name['FlattenParameter']
_HDF5DATAPARAMETER = DESCRIPTOR.message_types_by_name['HDF5DataParameter']
_HDF5OUTPUTPARAMETER = DESCRIPTOR.message_types_by_name['HDF5OutputParameter']
_HINGELOSSPARAMETER = DESCRIPTOR.message_types_by_name['HingeLossParameter']
_REPEATEDLIST = DESCRIPTOR.message_types_by_name['RepeatedList']
_DATASETPARAMETER = DESCRIPTOR.message_types_by_name['DatasetParameter']
_IMAGEDATAPARAMETER = DESCRIPTOR.message_types_by_name['ImageDataParameter']
_INFOGAINLOSSPARAMETER = DESCRIPTOR.message_types_by_name['InfogainLossParameter']
_INNERPRODUCTPARAMETER = DESCRIPTOR.message_types_by_name['InnerProductParameter']
_INPUTPARAMETER = DESCRIPTOR.message_types_by_name['InputParameter']
_LOGPARAMETER = DESCRIPTOR.message_types_by_name['LogParameter']
_LRNPARAMETER = DESCRIPTOR.message_types_by_name['LRNParameter']
_MEMORYDATAPARAMETER = DESCRIPTOR.message_types_by_name['MemoryDataParameter']
_MULTIBOXLOSSPARAMETER = DESCRIPTOR.message_types_by_name['MultiBoxLossParameter']
_MVNPARAMETER = DESCRIPTOR.message_types_by_name['MVNParameter']
_NORMALIZEPARAMETER = DESCRIPTOR.message_types_by_name['NormalizeParameter']
_PARAMETERPARAMETER = DESCRIPTOR.message_types_by_name['ParameterParameter']
_PERMUTEPARAMETER = DESCRIPTOR.message_types_by_name['PermuteParameter']
_POOLINGPARAMETER = DESCRIPTOR.message_types_by_name['PoolingParameter']
_POWERPARAMETER = DESCRIPTOR.message_types_by_name['PowerParameter']
_PRIORBOXPARAMETER = DESCRIPTOR.message_types_by_name['PriorBoxParameter']
_PYTHONPARAMETER = DESCRIPTOR.message_types_by_name['PythonParameter']
_RECURRENTPARAMETER = DESCRIPTOR.message_types_by_name['RecurrentParameter']
_REDUCTIONPARAMETER = DESCRIPTOR.message_types_by_name['ReductionParameter']
_RELUPARAMETER = DESCRIPTOR.message_types_by_name['ReLUParameter']
_RESHAPEPARAMETER = DESCRIPTOR.message_types_by_name['ReshapeParameter']
_ROIPOOLINGPARAMETER = DESCRIPTOR.message_types_by_name['ROIPoolingParameter']
_SCALEPARAMETER = DESCRIPTOR.message_types_by_name['ScaleParameter']
_SIGMOIDPARAMETER = DESCRIPTOR.message_types_by_name['SigmoidParameter']
_SLICEPARAMETER = DESCRIPTOR.message_types_by_name['SliceParameter']
_SOFTMAXPARAMETER = DESCRIPTOR.message_types_by_name['SoftmaxParameter']
_TANHPARAMETER = DESCRIPTOR.message_types_by_name['TanHParameter']
_TILEPARAMETER = DESCRIPTOR.message_types_by_name['TileParameter']
_THRESHOLDPARAMETER = DESCRIPTOR.message_types_by_name['ThresholdParameter']
_VIDEODATAPARAMETER = DESCRIPTOR.message_types_by_name['VideoDataParameter']
_WINDOWDATAPARAMETER = DESCRIPTOR.message_types_by_name['WindowDataParameter']
_SPPPARAMETER = DESCRIPTOR.message_types_by_name['SPPParameter']
_V1LAYERPARAMETER = DESCRIPTOR.message_types_by_name['V1LayerParameter']
_V0LAYERPARAMETER = DESCRIPTOR.message_types_by_name['V0LayerParameter']
_PRELUPARAMETER = DESCRIPTOR.message_types_by_name['PReLUParameter']
_PADDINGPARAMETER = DESCRIPTOR.message_types_by_name['PaddingParameter']
_YOLOLOSSPARAMETER = DESCRIPTOR.message_types_by_name['YoloLossParameter']
_YOLODUMPPARAMETER = DESCRIPTOR.message_types_by_name['YoloDumpParameter']
_YOLOANCHORSPARAMETER = DESCRIPTOR.message_types_by_name['YoloAnchorsParameter']
_DIMENSIONSTATISTICS = DESCRIPTOR.message_types_by_name['DimensionStatistics']
_YOLOTARGETPARAMETER = DESCRIPTOR.message_types_by_name['YoloTargetParameter']
_REGIONPROPOSALPARAMETER = DESCRIPTOR.message_types_by_name['RegionProposalParameter']
_REGIONPARAMETER = DESCRIPTOR.message_types_by_name['RegionParameter']
_ANCHORBOX = DESCRIPTOR.message_types_by_name['AnchorBox']
_REORGPARAMETER = DESCRIPTOR.message_types_by_name['ReorgParameter']
_BBOXREGPARAMETER = DESCRIPTOR.message_types_by_name['BBoxRegParameter']
_DFMBPSROIALIGNPARAMETER = DESCRIPTOR.message_types_by_name['DFMBPSROIAlignParameter']
_DETECTIONOUTPUTSSDPARAMETER = DESCRIPTOR.message_types_by_name['DetectionOutputSSDParameter']
_NMSSSDPARAMETER = DESCRIPTOR.message_types_by_name['NMSSSDParameter']
_GENANCHORPARAMETER = DESCRIPTOR.message_types_by_name['GenAnchorParameter']
_EMITCONSTRAINT_EMITTYPE = _EMITCONSTRAINT.enum_types_by_name['EmitType']
_ANNOTATEDDATUM_ANNOTATIONTYPE = _ANNOTATEDDATUM.enum_types_by_name['AnnotationType']
_FILLERPARAMETER_VARIANCENORM = _FILLERPARAMETER.enum_types_by_name['VarianceNorm']
_PARAMSPEC_DIMCHECKMODE = _PARAMSPEC.enum_types_by_name['DimCheckMode']
_RESIZEPARAMETER_RESIZE_MODE = _RESIZEPARAMETER.enum_types_by_name['Resize_mode']
_RESIZEPARAMETER_PAD_MODE = _RESIZEPARAMETER.enum_types_by_name['Pad_mode']
_RESIZEPARAMETER_INTERP_MODE = _RESIZEPARAMETER.enum_types_by_name['Interp_mode']
_LOSSPARAMETER_NORMALIZATIONMODE = _LOSSPARAMETER.enum_types_by_name['NormalizationMode']
_CONVOLUTIONPARAMETER_ENGINE = _CONVOLUTIONPARAMETER.enum_types_by_name['Engine']
_DATAPARAMETER_DB = _DATAPARAMETER.enum_types_by_name['DB']
_ELTWISEPARAMETER_ELTWISEOP = _ELTWISEPARAMETER.enum_types_by_name['EltwiseOp']
_HINGELOSSPARAMETER_NORM = _HINGELOSSPARAMETER.enum_types_by_name['Norm']
_DATASETPARAMETER_DATASETTYPE = _DATASETPARAMETER.enum_types_by_name['DatasetType']
_LRNPARAMETER_NORMREGION = _LRNPARAMETER.enum_types_by_name['NormRegion']
_LRNPARAMETER_ENGINE = _LRNPARAMETER.enum_types_by_name['Engine']
_MULTIBOXLOSSPARAMETER_LOCLOSSTYPE = _MULTIBOXLOSSPARAMETER.enum_types_by_name['LocLossType']
_MULTIBOXLOSSPARAMETER_CONFLOSSTYPE = _MULTIBOXLOSSPARAMETER.enum_types_by_name['ConfLossType']
_MULTIBOXLOSSPARAMETER_MATCHTYPE = _MULTIBOXLOSSPARAMETER.enum_types_by_name['MatchType']
_MULTIBOXLOSSPARAMETER_MININGTYPE = _MULTIBOXLOSSPARAMETER.enum_types_by_name['MiningType']
_POOLINGPARAMETER_POOLMETHOD = _POOLINGPARAMETER.enum_types_by_name['PoolMethod']
_POOLINGPARAMETER_ENGINE = _POOLINGPARAMETER.enum_types_by_name['Engine']
_POOLINGPARAMETER_ROUNDMODE = _POOLINGPARAMETER.enum_types_by_name['RoundMode']
_PRIORBOXPARAMETER_CODETYPE = _PRIORBOXPARAMETER.enum_types_by_name['CodeType']
_REDUCTIONPARAMETER_REDUCTIONOP = _REDUCTIONPARAMETER.enum_types_by_name['ReductionOp']
_RELUPARAMETER_ENGINE = _RELUPARAMETER.enum_types_by_name['Engine']
_SIGMOIDPARAMETER_ENGINE = _SIGMOIDPARAMETER.enum_types_by_name['Engine']
_SOFTMAXPARAMETER_ENGINE = _SOFTMAXPARAMETER.enum_types_by_name['Engine']
_TANHPARAMETER_ENGINE = _TANHPARAMETER.enum_types_by_name['Engine']
_VIDEODATAPARAMETER_VIDEOTYPE = _VIDEODATAPARAMETER.enum_types_by_name['VideoType']
_SPPPARAMETER_POOLMETHOD = _SPPPARAMETER.enum_types_by_name['PoolMethod']
_SPPPARAMETER_ENGINE = _SPPPARAMETER.enum_types_by_name['Engine']
_V1LAYERPARAMETER_LAYERTYPE = _V1LAYERPARAMETER.enum_types_by_name['LayerType']
_V1LAYERPARAMETER_DIMCHECKMODE = _V1LAYERPARAMETER.enum_types_by_name['DimCheckMode']
_V0LAYERPARAMETER_POOLMETHOD = _V0LAYERPARAMETER.enum_types_by_name['PoolMethod']
_YOLOLOSSPARAMETER_REGLOSSTYPE = _YOLOLOSSPARAMETER.enum_types_by_name['RegLossType']
_DETECTIONOUTPUTSSDPARAMETER_MIN_SIZE_MODE = _DETECTIONOUTPUTSSDPARAMETER.enum_types_by_name['MIN_SIZE_MODE']
BlobShape = _reflection.GeneratedProtocolMessageType('BlobShape', (_message.Message,), {'DESCRIPTOR': _BLOBSHAPE, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BlobShape)
BlobProto = _reflection.GeneratedProtocolMessageType('BlobProto', (_message.Message,), {'DESCRIPTOR': _BLOBPROTO, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BlobProto)
Datum = _reflection.GeneratedProtocolMessageType('Datum', (_message.Message,), {'DESCRIPTOR': _DATUM, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(Datum)
LabelMapItem = _reflection.GeneratedProtocolMessageType('LabelMapItem', (_message.Message,), {'DESCRIPTOR': _LABELMAPITEM, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(LabelMapItem)
LabelMap = _reflection.GeneratedProtocolMessageType('LabelMap', (_message.Message,), {'DESCRIPTOR': _LABELMAP, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(LabelMap)
Sampler = _reflection.GeneratedProtocolMessageType('Sampler', (_message.Message,), {'DESCRIPTOR': _SAMPLER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(Sampler)
SampleConstraint = _reflection.GeneratedProtocolMessageType('SampleConstraint', (_message.Message,), {'DESCRIPTOR': _SAMPLECONSTRAINT, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SampleConstraint)
BatchSampler = _reflection.GeneratedProtocolMessageType('BatchSampler', (_message.Message,), {'DESCRIPTOR': _BATCHSAMPLER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BatchSampler)
EmitConstraint = _reflection.GeneratedProtocolMessageType('EmitConstraint', (_message.Message,), {'DESCRIPTOR': _EMITCONSTRAINT, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(EmitConstraint)
NormalizedBBox = _reflection.GeneratedProtocolMessageType('NormalizedBBox', (_message.Message,), {'DESCRIPTOR': _NORMALIZEDBBOX, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NormalizedBBox)
BBox3D = _reflection.GeneratedProtocolMessageType('BBox3D', (_message.Message,), {'DESCRIPTOR': _BBOX3D, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BBox3D)
Annotation = _reflection.GeneratedProtocolMessageType('Annotation', (_message.Message,), {'DESCRIPTOR': _ANNOTATION, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(Annotation)
AnnotationGroup = _reflection.GeneratedProtocolMessageType('AnnotationGroup', (_message.Message,), {'DESCRIPTOR': _ANNOTATIONGROUP, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(AnnotationGroup)
AnnotatedDatum = _reflection.GeneratedProtocolMessageType('AnnotatedDatum', (_message.Message,), {'DESCRIPTOR': _ANNOTATEDDATUM, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(AnnotatedDatum)
FillerParameter = _reflection.GeneratedProtocolMessageType('FillerParameter', (_message.Message,), {'DESCRIPTOR': _FILLERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(FillerParameter)
NetParameter = _reflection.GeneratedProtocolMessageType('NetParameter', (_message.Message,), {'DESCRIPTOR': _NETPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NetParameter)
NetState = _reflection.GeneratedProtocolMessageType('NetState', (_message.Message,), {'DESCRIPTOR': _NETSTATE, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NetState)
NetStateRule = _reflection.GeneratedProtocolMessageType('NetStateRule', (_message.Message,), {'DESCRIPTOR': _NETSTATERULE, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NetStateRule)
ParamSpec = _reflection.GeneratedProtocolMessageType('ParamSpec', (_message.Message,), {'DESCRIPTOR': _PARAMSPEC, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ParamSpec)
LayerParameter = _reflection.GeneratedProtocolMessageType('LayerParameter', (_message.Message,), {'DESCRIPTOR': _LAYERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(LayerParameter)
TransformationParameter = _reflection.GeneratedProtocolMessageType('TransformationParameter', (_message.Message,), {'DESCRIPTOR': _TRANSFORMATIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(TransformationParameter)
ResizeParameter = _reflection.GeneratedProtocolMessageType('ResizeParameter', (_message.Message,), {'DESCRIPTOR': _RESIZEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ResizeParameter)
SaltPepperParameter = _reflection.GeneratedProtocolMessageType('SaltPepperParameter', (_message.Message,), {'DESCRIPTOR': _SALTPEPPERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SaltPepperParameter)
NoiseParameter = _reflection.GeneratedProtocolMessageType('NoiseParameter', (_message.Message,), {'DESCRIPTOR': _NOISEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NoiseParameter)
DistortionParameter = _reflection.GeneratedProtocolMessageType('DistortionParameter', (_message.Message,), {'DESCRIPTOR': _DISTORTIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DistortionParameter)
ExpansionParameter = _reflection.GeneratedProtocolMessageType('ExpansionParameter', (_message.Message,), {'DESCRIPTOR': _EXPANSIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ExpansionParameter)
LossParameter = _reflection.GeneratedProtocolMessageType('LossParameter', (_message.Message,), {'DESCRIPTOR': _LOSSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(LossParameter)
AccuracyParameter = _reflection.GeneratedProtocolMessageType('AccuracyParameter', (_message.Message,), {'DESCRIPTOR': _ACCURACYPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(AccuracyParameter)
AnnotatedDataParameter = _reflection.GeneratedProtocolMessageType('AnnotatedDataParameter', (_message.Message,), {'DESCRIPTOR': _ANNOTATEDDATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(AnnotatedDataParameter)
ArgMaxParameter = _reflection.GeneratedProtocolMessageType('ArgMaxParameter', (_message.Message,), {'DESCRIPTOR': _ARGMAXPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ArgMaxParameter)
ConcatParameter = _reflection.GeneratedProtocolMessageType('ConcatParameter', (_message.Message,), {'DESCRIPTOR': _CONCATPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ConcatParameter)
BatchNormParameter = _reflection.GeneratedProtocolMessageType('BatchNormParameter', (_message.Message,), {'DESCRIPTOR': _BATCHNORMPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BatchNormParameter)
BiasParameter = _reflection.GeneratedProtocolMessageType('BiasParameter', (_message.Message,), {'DESCRIPTOR': _BIASPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BiasParameter)
ContrastiveLossParameter = _reflection.GeneratedProtocolMessageType('ContrastiveLossParameter', (_message.Message,), {'DESCRIPTOR': _CONTRASTIVELOSSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ContrastiveLossParameter)
ConvolutionParameter = _reflection.GeneratedProtocolMessageType('ConvolutionParameter', (_message.Message,), {'DESCRIPTOR': _CONVOLUTIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ConvolutionParameter)
CropParameter = _reflection.GeneratedProtocolMessageType('CropParameter', (_message.Message,), {'DESCRIPTOR': _CROPPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(CropParameter)
DataParameter = _reflection.GeneratedProtocolMessageType('DataParameter', (_message.Message,), {'DESCRIPTOR': _DATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DataParameter)
DetectionEvaluateParameter = _reflection.GeneratedProtocolMessageType('DetectionEvaluateParameter', (_message.Message,), {'DESCRIPTOR': _DETECTIONEVALUATEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DetectionEvaluateParameter)
NonMaximumSuppressionParameter = _reflection.GeneratedProtocolMessageType('NonMaximumSuppressionParameter', (_message.Message,), {'DESCRIPTOR': _NONMAXIMUMSUPPRESSIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NonMaximumSuppressionParameter)
SaveOutputParameter = _reflection.GeneratedProtocolMessageType('SaveOutputParameter', (_message.Message,), {'DESCRIPTOR': _SAVEOUTPUTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SaveOutputParameter)
DetectionOutputParameter = _reflection.GeneratedProtocolMessageType('DetectionOutputParameter', (_message.Message,), {'DESCRIPTOR': _DETECTIONOUTPUTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DetectionOutputParameter)
RegionOutputParameter = _reflection.GeneratedProtocolMessageType('RegionOutputParameter', (_message.Message,), {'DESCRIPTOR': _REGIONOUTPUTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(RegionOutputParameter)
DropoutParameter = _reflection.GeneratedProtocolMessageType('DropoutParameter', (_message.Message,), {'DESCRIPTOR': _DROPOUTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DropoutParameter)
DummyDataParameter = _reflection.GeneratedProtocolMessageType('DummyDataParameter', (_message.Message,), {'DESCRIPTOR': _DUMMYDATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DummyDataParameter)
EltwiseParameter = _reflection.GeneratedProtocolMessageType('EltwiseParameter', (_message.Message,), {'DESCRIPTOR': _ELTWISEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(EltwiseParameter)
ELUParameter = _reflection.GeneratedProtocolMessageType('ELUParameter', (_message.Message,), {'DESCRIPTOR': _ELUPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ELUParameter)
EmbedParameter = _reflection.GeneratedProtocolMessageType('EmbedParameter', (_message.Message,), {'DESCRIPTOR': _EMBEDPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(EmbedParameter)
ExpParameter = _reflection.GeneratedProtocolMessageType('ExpParameter', (_message.Message,), {'DESCRIPTOR': _EXPPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ExpParameter)
FlattenParameter = _reflection.GeneratedProtocolMessageType('FlattenParameter', (_message.Message,), {'DESCRIPTOR': _FLATTENPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(FlattenParameter)
HDF5DataParameter = _reflection.GeneratedProtocolMessageType('HDF5DataParameter', (_message.Message,), {'DESCRIPTOR': _HDF5DATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(HDF5DataParameter)
HDF5OutputParameter = _reflection.GeneratedProtocolMessageType('HDF5OutputParameter', (_message.Message,), {'DESCRIPTOR': _HDF5OUTPUTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(HDF5OutputParameter)
HingeLossParameter = _reflection.GeneratedProtocolMessageType('HingeLossParameter', (_message.Message,), {'DESCRIPTOR': _HINGELOSSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(HingeLossParameter)
RepeatedList = _reflection.GeneratedProtocolMessageType('RepeatedList', (_message.Message,), {'DESCRIPTOR': _REPEATEDLIST, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(RepeatedList)
DatasetParameter = _reflection.GeneratedProtocolMessageType('DatasetParameter', (_message.Message,), {'DESCRIPTOR': _DATASETPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DatasetParameter)
ImageDataParameter = _reflection.GeneratedProtocolMessageType('ImageDataParameter', (_message.Message,), {'DESCRIPTOR': _IMAGEDATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ImageDataParameter)
InfogainLossParameter = _reflection.GeneratedProtocolMessageType('InfogainLossParameter', (_message.Message,), {'DESCRIPTOR': _INFOGAINLOSSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(InfogainLossParameter)
InnerProductParameter = _reflection.GeneratedProtocolMessageType('InnerProductParameter', (_message.Message,), {'DESCRIPTOR': _INNERPRODUCTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(InnerProductParameter)
InputParameter = _reflection.GeneratedProtocolMessageType('InputParameter', (_message.Message,), {'DESCRIPTOR': _INPUTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(InputParameter)
LogParameter = _reflection.GeneratedProtocolMessageType('LogParameter', (_message.Message,), {'DESCRIPTOR': _LOGPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(LogParameter)
LRNParameter = _reflection.GeneratedProtocolMessageType('LRNParameter', (_message.Message,), {'DESCRIPTOR': _LRNPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(LRNParameter)
MemoryDataParameter = _reflection.GeneratedProtocolMessageType('MemoryDataParameter', (_message.Message,), {'DESCRIPTOR': _MEMORYDATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(MemoryDataParameter)
MultiBoxLossParameter = _reflection.GeneratedProtocolMessageType('MultiBoxLossParameter', (_message.Message,), {'DESCRIPTOR': _MULTIBOXLOSSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(MultiBoxLossParameter)
MVNParameter = _reflection.GeneratedProtocolMessageType('MVNParameter', (_message.Message,), {'DESCRIPTOR': _MVNPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(MVNParameter)
NormalizeParameter = _reflection.GeneratedProtocolMessageType('NormalizeParameter', (_message.Message,), {'DESCRIPTOR': _NORMALIZEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NormalizeParameter)
ParameterParameter = _reflection.GeneratedProtocolMessageType('ParameterParameter', (_message.Message,), {'DESCRIPTOR': _PARAMETERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ParameterParameter)
PermuteParameter = _reflection.GeneratedProtocolMessageType('PermuteParameter', (_message.Message,), {'DESCRIPTOR': _PERMUTEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PermuteParameter)
PoolingParameter = _reflection.GeneratedProtocolMessageType('PoolingParameter', (_message.Message,), {'DESCRIPTOR': _POOLINGPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PoolingParameter)
PowerParameter = _reflection.GeneratedProtocolMessageType('PowerParameter', (_message.Message,), {'DESCRIPTOR': _POWERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PowerParameter)
PriorBoxParameter = _reflection.GeneratedProtocolMessageType('PriorBoxParameter', (_message.Message,), {'DESCRIPTOR': _PRIORBOXPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PriorBoxParameter)
PythonParameter = _reflection.GeneratedProtocolMessageType('PythonParameter', (_message.Message,), {'DESCRIPTOR': _PYTHONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PythonParameter)
RecurrentParameter = _reflection.GeneratedProtocolMessageType('RecurrentParameter', (_message.Message,), {'DESCRIPTOR': _RECURRENTPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(RecurrentParameter)
ReductionParameter = _reflection.GeneratedProtocolMessageType('ReductionParameter', (_message.Message,), {'DESCRIPTOR': _REDUCTIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ReductionParameter)
ReLUParameter = _reflection.GeneratedProtocolMessageType('ReLUParameter', (_message.Message,), {'DESCRIPTOR': _RELUPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ReLUParameter)
ReshapeParameter = _reflection.GeneratedProtocolMessageType('ReshapeParameter', (_message.Message,), {'DESCRIPTOR': _RESHAPEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ReshapeParameter)
ROIPoolingParameter = _reflection.GeneratedProtocolMessageType('ROIPoolingParameter', (_message.Message,), {'DESCRIPTOR': _ROIPOOLINGPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ROIPoolingParameter)
ScaleParameter = _reflection.GeneratedProtocolMessageType('ScaleParameter', (_message.Message,), {'DESCRIPTOR': _SCALEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ScaleParameter)
SigmoidParameter = _reflection.GeneratedProtocolMessageType('SigmoidParameter', (_message.Message,), {'DESCRIPTOR': _SIGMOIDPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SigmoidParameter)
SliceParameter = _reflection.GeneratedProtocolMessageType('SliceParameter', (_message.Message,), {'DESCRIPTOR': _SLICEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SliceParameter)
SoftmaxParameter = _reflection.GeneratedProtocolMessageType('SoftmaxParameter', (_message.Message,), {'DESCRIPTOR': _SOFTMAXPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SoftmaxParameter)
TanHParameter = _reflection.GeneratedProtocolMessageType('TanHParameter', (_message.Message,), {'DESCRIPTOR': _TANHPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(TanHParameter)
TileParameter = _reflection.GeneratedProtocolMessageType('TileParameter', (_message.Message,), {'DESCRIPTOR': _TILEPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(TileParameter)
ThresholdParameter = _reflection.GeneratedProtocolMessageType('ThresholdParameter', (_message.Message,), {'DESCRIPTOR': _THRESHOLDPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ThresholdParameter)
VideoDataParameter = _reflection.GeneratedProtocolMessageType('VideoDataParameter', (_message.Message,), {'DESCRIPTOR': _VIDEODATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(VideoDataParameter)
WindowDataParameter = _reflection.GeneratedProtocolMessageType('WindowDataParameter', (_message.Message,), {'DESCRIPTOR': _WINDOWDATAPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(WindowDataParameter)
SPPParameter = _reflection.GeneratedProtocolMessageType('SPPParameter', (_message.Message,), {'DESCRIPTOR': _SPPPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(SPPParameter)
V1LayerParameter = _reflection.GeneratedProtocolMessageType('V1LayerParameter', (_message.Message,), {'DESCRIPTOR': _V1LAYERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(V1LayerParameter)
V0LayerParameter = _reflection.GeneratedProtocolMessageType('V0LayerParameter', (_message.Message,), {'DESCRIPTOR': _V0LAYERPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(V0LayerParameter)
PReLUParameter = _reflection.GeneratedProtocolMessageType('PReLUParameter', (_message.Message,), {'DESCRIPTOR': _PRELUPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PReLUParameter)
PaddingParameter = _reflection.GeneratedProtocolMessageType('PaddingParameter', (_message.Message,), {'DESCRIPTOR': _PADDINGPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(PaddingParameter)
YoloLossParameter = _reflection.GeneratedProtocolMessageType('YoloLossParameter', (_message.Message,), {'DESCRIPTOR': _YOLOLOSSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(YoloLossParameter)
YoloDumpParameter = _reflection.GeneratedProtocolMessageType('YoloDumpParameter', (_message.Message,), {'DESCRIPTOR': _YOLODUMPPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(YoloDumpParameter)
YoloAnchorsParameter = _reflection.GeneratedProtocolMessageType('YoloAnchorsParameter', (_message.Message,), {'DESCRIPTOR': _YOLOANCHORSPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(YoloAnchorsParameter)
DimensionStatistics = _reflection.GeneratedProtocolMessageType('DimensionStatistics', (_message.Message,), {'DESCRIPTOR': _DIMENSIONSTATISTICS, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DimensionStatistics)
YoloTargetParameter = _reflection.GeneratedProtocolMessageType('YoloTargetParameter', (_message.Message,), {'DESCRIPTOR': _YOLOTARGETPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(YoloTargetParameter)
RegionProposalParameter = _reflection.GeneratedProtocolMessageType('RegionProposalParameter', (_message.Message,), {'DESCRIPTOR': _REGIONPROPOSALPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(RegionProposalParameter)
RegionParameter = _reflection.GeneratedProtocolMessageType('RegionParameter', (_message.Message,), {'DESCRIPTOR': _REGIONPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(RegionParameter)
AnchorBox = _reflection.GeneratedProtocolMessageType('AnchorBox', (_message.Message,), {'DESCRIPTOR': _ANCHORBOX, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(AnchorBox)
ReorgParameter = _reflection.GeneratedProtocolMessageType('ReorgParameter', (_message.Message,), {'DESCRIPTOR': _REORGPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(ReorgParameter)
BBoxRegParameter = _reflection.GeneratedProtocolMessageType('BBoxRegParameter', (_message.Message,), {'DESCRIPTOR': _BBOXREGPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(BBoxRegParameter)
DFMBPSROIAlignParameter = _reflection.GeneratedProtocolMessageType('DFMBPSROIAlignParameter', (_message.Message,), {'DESCRIPTOR': _DFMBPSROIALIGNPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DFMBPSROIAlignParameter)
DetectionOutputSSDParameter = _reflection.GeneratedProtocolMessageType('DetectionOutputSSDParameter', (_message.Message,), {'DESCRIPTOR': _DETECTIONOUTPUTSSDPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(DetectionOutputSSDParameter)
NMSSSDParameter = _reflection.GeneratedProtocolMessageType('NMSSSDParameter', (_message.Message,), {'DESCRIPTOR': _NMSSSDPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(NMSSSDParameter)
GenAnchorParameter = _reflection.GeneratedProtocolMessageType('GenAnchorParameter', (_message.Message,), {'DESCRIPTOR': _GENANCHORPARAMETER, '__module__': 'modules.perception.proto.rt_pb2'})
_sym_db.RegisterMessage(GenAnchorParameter)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BLOBSHAPE.fields_by_name['dim']._options = None
    _BLOBSHAPE.fields_by_name['dim']._serialized_options = b'\x10\x01'
    _BLOBPROTO.fields_by_name['data']._options = None
    _BLOBPROTO.fields_by_name['data']._serialized_options = b'\x10\x01'
    _BLOBPROTO.fields_by_name['diff']._options = None
    _BLOBPROTO.fields_by_name['diff']._serialized_options = b'\x10\x01'
    _BLOBPROTO.fields_by_name['double_data']._options = None
    _BLOBPROTO.fields_by_name['double_data']._serialized_options = b'\x10\x01'
    _BLOBPROTO.fields_by_name['double_diff']._options = None
    _BLOBPROTO.fields_by_name['double_diff']._serialized_options = b'\x10\x01'
    _PHASE._serialized_start = 30030
    _PHASE._serialized_end = 30058
    _BLOBSHAPE._serialized_start = 66
    _BLOBSHAPE._serialized_end = 94
    _BLOBPROTO._serialized_start = 97
    _BLOBPROTO._serialized_end = 323
    _DATUM._serialized_start = 326
    _DATUM._serialized_end = 455
    _LABELMAPITEM._serialized_start = 457
    _LABELMAPITEM._serialized_end = 522
    _LABELMAP._serialized_start = 524
    _LABELMAP._serialized_end = 591
    _SAMPLER._serialized_start = 593
    _SAMPLER._serialized_end = 704
    _SAMPLECONSTRAINT._serialized_start = 707
    _SAMPLECONSTRAINT._serialized_end = 921
    _BATCHSAMPLER._serialized_start = 924
    _BATCHSAMPLER._serialized_end = 1146
    _EMITCONSTRAINT._serialized_start = 1149
    _EMITCONSTRAINT._serialized_end = 1309
    _EMITCONSTRAINT_EMITTYPE._serialized_start = 1270
    _EMITCONSTRAINT_EMITTYPE._serialized_end = 1309
    _NORMALIZEDBBOX._serialized_start = 1312
    _NORMALIZEDBBOX._serialized_end = 1447
    _BBOX3D._serialized_start = 1449
    _BBOX3D._serialized_end = 1559
    _ANNOTATION._serialized_start = 1562
    _ANNOTATION._serialized_end = 1839
    _ANNOTATIONGROUP._serialized_start = 1841
    _ANNOTATIONGROUP._serialized_end = 1940
    _ANNOTATEDDATUM._serialized_start = 1943
    _ANNOTATEDDATUM._serialized_end = 2210
    _ANNOTATEDDATUM_ANNOTATIONTYPE._serialized_start = 2158
    _ANNOTATEDDATUM_ANNOTATIONTYPE._serialized_end = 2210
    _FILLERPARAMETER._serialized_start = 2213
    _FILLERPARAMETER._serialized_end = 2501
    _FILLERPARAMETER_VARIANCENORM._serialized_start = 2449
    _FILLERPARAMETER_VARIANCENORM._serialized_end = 2501
    _NETPARAMETER._serialized_start = 2504
    _NETPARAMETER._serialized_end = 2862
    _NETSTATE._serialized_start = 2864
    _NETSTATE._serialized_end = 2964
    _NETSTATERULE._serialized_start = 2967
    _NETSTATERULE._serialized_end = 3104
    _PARAMSPEC._serialized_start = 3107
    _PARAMSPEC._serialized_end = 3292
    _PARAMSPEC_DIMCHECKMODE._serialized_start = 3250
    _PARAMSPEC_DIMCHECKMODE._serialized_end = 3292
    _LAYERPARAMETER._serialized_start = 3295
    _LAYERPARAMETER._serialized_end = 8762
    _TRANSFORMATIONPARAMETER._serialized_start = 8765
    _TRANSFORMATIONPARAMETER._serialized_end = 9349
    _RESIZEPARAMETER._serialized_start = 9352
    _RESIZEPARAMETER._serialized_end = 9946
    _RESIZEPARAMETER_RESIZE_MODE._serialized_start = 9740
    _RESIZEPARAMETER_RESIZE_MODE._serialized_end = 9811
    _RESIZEPARAMETER_PAD_MODE._serialized_start = 9813
    _RESIZEPARAMETER_PAD_MODE._serialized_end = 9871
    _RESIZEPARAMETER_INTERP_MODE._serialized_start = 9873
    _RESIZEPARAMETER_INTERP_MODE._serialized_end = 9946
    _SALTPEPPERPARAMETER._serialized_start = 9948
    _SALTPEPPERPARAMETER._serialized_end = 10005
    _NOISEPARAMETER._serialized_start = 10008
    _NOISEPARAMETER._serialized_end = 10396
    _DISTORTIONPARAMETER._serialized_start = 10399
    _DISTORTIONPARAMETER._serialized_end = 10716
    _EXPANSIONPARAMETER._serialized_start = 10718
    _EXPANSIONPARAMETER._serialized_end = 10784
    _LOSSPARAMETER._serialized_start = 10787
    _LOSSPARAMETER._serialized_end = 11003
    _LOSSPARAMETER_NORMALIZATIONMODE._serialized_start = 10937
    _LOSSPARAMETER_NORMALIZATIONMODE._serialized_end = 11003
    _ACCURACYPARAMETER._serialized_start = 11005
    _ACCURACYPARAMETER._serialized_end = 11081
    _ANNOTATEDDATAPARAMETER._serialized_start = 11084
    _ANNOTATEDDATAPARAMETER._serialized_end = 11307
    _ARGMAXPARAMETER._serialized_start = 11309
    _ARGMAXPARAMETER._serialized_end = 11386
    _CONCATPARAMETER._serialized_start = 11388
    _CONCATPARAMETER._serialized_end = 11445
    _BATCHNORMPARAMETER._serialized_start = 11447
    _BATCHNORMPARAMETER._serialized_end = 11553
    _BIASPARAMETER._serialized_start = 11555
    _BIASPARAMETER._serialized_end = 11670
    _CONTRASTIVELOSSPARAMETER._serialized_start = 11672
    _CONTRASTIVELOSSPARAMETER._serialized_end = 11748
    _CONVOLUTIONPARAMETER._serialized_start = 11751
    _CONVOLUTIONPARAMETER._serialized_end = 12325
    _CONVOLUTIONPARAMETER_ENGINE._serialized_start = 12282
    _CONVOLUTIONPARAMETER_ENGINE._serialized_end = 12325
    _CROPPARAMETER._serialized_start = 12327
    _CROPPARAMETER._serialized_end = 12375
    _DATAPARAMETER._serialized_start = 12378
    _DATAPARAMETER._serialized_end = 12692
    _DATAPARAMETER_DB._serialized_start = 12665
    _DATAPARAMETER_DB._serialized_end = 12692
    _DETECTIONEVALUATEPARAMETER._serialized_start = 12695
    _DETECTIONEVALUATEPARAMETER._serialized_end = 12937
    _NONMAXIMUMSUPPRESSIONPARAMETER._serialized_start = 12939
    _NONMAXIMUMSUPPRESSIONPARAMETER._serialized_end = 13030
    _SAVEOUTPUTPARAMETER._serialized_start = 13033
    _SAVEOUTPUTPARAMETER._serialized_end = 13271
    _DETECTIONOUTPUTPARAMETER._serialized_start = 13274
    _DETECTIONOUTPUTPARAMETER._serialized_end = 13795
    _REGIONOUTPUTPARAMETER._serialized_start = 13798
    _REGIONOUTPUTPARAMETER._serialized_end = 14095
    _DROPOUTPARAMETER._serialized_start = 14097
    _DROPOUTPARAMETER._serialized_end = 14143
    _DUMMYDATAPARAMETER._serialized_start = 14146
    _DUMMYDATAPARAMETER._serialized_end = 14350
    _ELTWISEPARAMETER._serialized_start = 14353
    _ELTWISEPARAMETER._serialized_end = 14540
    _ELTWISEPARAMETER_ELTWISEOP._serialized_start = 14501
    _ELTWISEPARAMETER_ELTWISEOP._serialized_end = 14540
    _ELUPARAMETER._serialized_start = 14542
    _ELUPARAMETER._serialized_end = 14574
    _EMBEDPARAMETER._serialized_start = 14577
    _EMBEDPARAMETER._serialized_end = 14793
    _EXPPARAMETER._serialized_start = 14795
    _EXPPARAMETER._serialized_end = 14863
    _FLATTENPARAMETER._serialized_start = 14865
    _FLATTENPARAMETER._serialized_end = 14922
    _HDF5DATAPARAMETER._serialized_start = 14924
    _HDF5DATAPARAMETER._serialized_end = 15003
    _HDF5OUTPUTPARAMETER._serialized_start = 15005
    _HDF5OUTPUTPARAMETER._serialized_end = 15045
    _HINGELOSSPARAMETER._serialized_start = 15047
    _HINGELOSSPARAMETER._serialized_end = 15163
    _HINGELOSSPARAMETER_NORM._serialized_start = 15141
    _HINGELOSSPARAMETER_NORM._serialized_end = 15163
    _REPEATEDLIST._serialized_start = 15165
    _REPEATEDLIST._serialized_end = 15221
    _DATASETPARAMETER._serialized_start = 15224
    _DATASETPARAMETER._serialized_end = 15502
    _DATASETPARAMETER_DATASETTYPE._serialized_start = 15468
    _DATASETPARAMETER_DATASETTYPE._serialized_end = 15502
    _IMAGEDATAPARAMETER._serialized_start = 15505
    _IMAGEDATAPARAMETER._serialized_end = 15871
    _INFOGAINLOSSPARAMETER._serialized_start = 15873
    _INFOGAINLOSSPARAMETER._serialized_end = 15912
    _INNERPRODUCTPARAMETER._serialized_start = 15915
    _INNERPRODUCTPARAMETER._serialized_end = 16162
    _INPUTPARAMETER._serialized_start = 16164
    _INPUTPARAMETER._serialized_end = 16235
    _LOGPARAMETER._serialized_start = 16237
    _LOGPARAMETER._serialized_end = 16305
    _LRNPARAMETER._serialized_start = 16308
    _LRNPARAMETER._serialized_end = 16664
    _LRNPARAMETER_NORMREGION._serialized_start = 16566
    _LRNPARAMETER_NORMREGION._serialized_end = 16619
    _LRNPARAMETER_ENGINE._serialized_start = 12282
    _LRNPARAMETER_ENGINE._serialized_end = 12325
    _MEMORYDATAPARAMETER._serialized_start = 16666
    _MEMORYDATAPARAMETER._serialized_end = 16756
    _MULTIBOXLOSSPARAMETER._serialized_start = 16759
    _MULTIBOXLOSSPARAMETER._serialized_end = 18019
    _MULTIBOXLOSSPARAMETER_LOCLOSSTYPE._serialized_start = 17832
    _MULTIBOXLOSSPARAMETER_LOCLOSSTYPE._serialized_end = 17868
    _MULTIBOXLOSSPARAMETER_CONFLOSSTYPE._serialized_start = 17870
    _MULTIBOXLOSSPARAMETER_CONFLOSSTYPE._serialized_end = 17911
    _MULTIBOXLOSSPARAMETER_MATCHTYPE._serialized_start = 17913
    _MULTIBOXLOSSPARAMETER_MATCHTYPE._serialized_end = 17959
    _MULTIBOXLOSSPARAMETER_MININGTYPE._serialized_start = 17961
    _MULTIBOXLOSSPARAMETER_MININGTYPE._serialized_end = 18019
    _MVNPARAMETER._serialized_start = 18021
    _MVNPARAMETER._serialized_end = 18121
    _NORMALIZEPARAMETER._serialized_start = 18124
    _NORMALIZEPARAMETER._serialized_end = 18292
    _PARAMETERPARAMETER._serialized_start = 18294
    _PARAMETERPARAMETER._serialized_end = 18369
    _PERMUTEPARAMETER._serialized_start = 18371
    _PERMUTEPARAMETER._serialized_end = 18404
    _POOLINGPARAMETER._serialized_start = 18407
    _POOLINGPARAMETER._serialized_end = 18986
    _POOLINGPARAMETER_POOLMETHOD._serialized_start = 18861
    _POOLINGPARAMETER_POOLMETHOD._serialized_end = 18907
    _POOLINGPARAMETER_ENGINE._serialized_start = 12282
    _POOLINGPARAMETER_ENGINE._serialized_end = 12325
    _POOLINGPARAMETER_ROUNDMODE._serialized_start = 18954
    _POOLINGPARAMETER_ROUNDMODE._serialized_end = 18986
    _POWERPARAMETER._serialized_start = 18988
    _POWERPARAMETER._serialized_end = 19058
    _PRIORBOXPARAMETER._serialized_start = 19061
    _PRIORBOXPARAMETER._serialized_end = 19370
    _PRIORBOXPARAMETER_CODETYPE._serialized_start = 19314
    _PRIORBOXPARAMETER_CODETYPE._serialized_end = 19370
    _PYTHONPARAMETER._serialized_start = 19372
    _PYTHONPARAMETER._serialized_end = 19475
    _RECURRENTPARAMETER._serialized_start = 19478
    _RECURRENTPARAMETER._serialized_end = 19714
    _REDUCTIONPARAMETER._serialized_start = 19717
    _REDUCTIONPARAMETER._serialized_end = 19912
    _REDUCTIONPARAMETER_REDUCTIONOP._serialized_start = 19859
    _REDUCTIONPARAMETER_REDUCTIONOP._serialized_end = 19912
    _RELUPARAMETER._serialized_start = 19915
    _RELUPARAMETER._serialized_end = 20078
    _RELUPARAMETER_ENGINE._serialized_start = 12282
    _RELUPARAMETER_ENGINE._serialized_end = 12325
    _RESHAPEPARAMETER._serialized_start = 20080
    _RESHAPEPARAMETER._serialized_end = 20192
    _ROIPOOLINGPARAMETER._serialized_start = 20194
    _ROIPOOLINGPARAMETER._serialized_end = 20309
    _SCALEPARAMETER._serialized_start = 20312
    _SCALEPARAMETER._serialized_end = 20521
    _SIGMOIDPARAMETER._serialized_start = 20524
    _SIGMOIDPARAMETER._serialized_end = 20666
    _SIGMOIDPARAMETER_ENGINE._serialized_start = 12282
    _SIGMOIDPARAMETER_ENGINE._serialized_end = 12325
    _SLICEPARAMETER._serialized_start = 20668
    _SLICEPARAMETER._serialized_end = 20744
    _SOFTMAXPARAMETER._serialized_start = 20747
    _SOFTMAXPARAMETER._serialized_end = 20906
    _SOFTMAXPARAMETER_ENGINE._serialized_start = 12282
    _SOFTMAXPARAMETER_ENGINE._serialized_end = 12325
    _TANHPARAMETER._serialized_start = 20909
    _TANHPARAMETER._serialized_end = 21045
    _TANHPARAMETER_ENGINE._serialized_start = 12282
    _TANHPARAMETER_ENGINE._serialized_end = 12325
    _TILEPARAMETER._serialized_start = 21047
    _TILEPARAMETER._serialized_end = 21094
    _THRESHOLDPARAMETER._serialized_start = 21096
    _THRESHOLDPARAMETER._serialized_end = 21138
    _VIDEODATAPARAMETER._serialized_start = 21141
    _VIDEODATAPARAMETER._serialized_end = 21350
    _VIDEODATAPARAMETER_VIDEOTYPE._serialized_start = 21316
    _VIDEODATAPARAMETER_VIDEOTYPE._serialized_end = 21350
    _WINDOWDATAPARAMETER._serialized_start = 21353
    _WINDOWDATAPARAMETER._serialized_end = 21674
    _SPPPARAMETER._serialized_start = 21677
    _SPPPARAMETER._serialized_end = 21956
    _SPPPARAMETER_POOLMETHOD._serialized_start = 18861
    _SPPPARAMETER_POOLMETHOD._serialized_end = 18907
    _SPPPARAMETER_ENGINE._serialized_start = 12282
    _SPPPARAMETER_ENGINE._serialized_end = 12325
    _V1LAYERPARAMETER._serialized_start = 21959
    _V1LAYERPARAMETER._serialized_end = 25279
    _V1LAYERPARAMETER_LAYERTYPE._serialized_start = 24635
    _V1LAYERPARAMETER_LAYERTYPE._serialized_end = 25235
    _V1LAYERPARAMETER_DIMCHECKMODE._serialized_start = 3250
    _V1LAYERPARAMETER_DIMCHECKMODE._serialized_end = 3292
    _V0LAYERPARAMETER._serialized_start = 25282
    _V0LAYERPARAMETER._serialized_end = 26413
    _V0LAYERPARAMETER_POOLMETHOD._serialized_start = 18861
    _V0LAYERPARAMETER_POOLMETHOD._serialized_end = 18907
    _PRELUPARAMETER._serialized_start = 26415
    _PRELUPARAMETER._serialized_end = 26524
    _PADDINGPARAMETER._serialized_start = 26526
    _PADDINGPARAMETER._serialized_end = 26632
    _YOLOLOSSPARAMETER._serialized_start = 26635
    _YOLOLOSSPARAMETER._serialized_end = 26819
    _YOLOLOSSPARAMETER_REGLOSSTYPE._serialized_start = 26775
    _YOLOLOSSPARAMETER_REGLOSSTYPE._serialized_end = 26819
    _YOLODUMPPARAMETER._serialized_start = 26821
    _YOLODUMPPARAMETER._serialized_end = 26858
    _YOLOANCHORSPARAMETER._serialized_start = 26860
    _YOLOANCHORSPARAMETER._serialized_end = 26940
    _DIMENSIONSTATISTICS._serialized_start = 26943
    _DIMENSIONSTATISTICS._serialized_end = 27075
    _YOLOTARGETPARAMETER._serialized_start = 27078
    _YOLOTARGETPARAMETER._serialized_end = 27430
    _REGIONPROPOSALPARAMETER._serialized_start = 27433
    _REGIONPROPOSALPARAMETER._serialized_end = 27960
    _REGIONPARAMETER._serialized_start = 27963
    _REGIONPARAMETER._serialized_end = 28622
    _ANCHORBOX._serialized_start = 28624
    _ANCHORBOX._serialized_end = 28657
    _REORGPARAMETER._serialized_start = 28659
    _REORGPARAMETER._serialized_end = 28691
    _BBOXREGPARAMETER._serialized_start = 28693
    _BBOXREGPARAMETER._serialized_end = 28748
    _DFMBPSROIALIGNPARAMETER._serialized_start = 28751
    _DFMBPSROIALIGNPARAMETER._serialized_end = 29040
    _DETECTIONOUTPUTSSDPARAMETER._serialized_start = 29043
    _DETECTIONOUTPUTSSDPARAMETER._serialized_end = 29632
    _DETECTIONOUTPUTSSDPARAMETER_MIN_SIZE_MODE._serialized_start = 29574
    _DETECTIONOUTPUTSSDPARAMETER_MIN_SIZE_MODE._serialized_end = 29632
    _NMSSSDPARAMETER._serialized_start = 29635
    _NMSSSDPARAMETER._serialized_end = 29961
    _GENANCHORPARAMETER._serialized_start = 29963
    _GENANCHORPARAMETER._serialized_end = 30028