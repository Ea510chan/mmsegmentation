_base_ = [
    '../../../configs/_base_/models/upernet_r50.py',
    './_base_/datasets/aqc_seg.py', 
    '../../../configs/_base_/default_runtime.py',
    '../../../configs/_base_/schedules/schedule_20k.py'
]
custom_imports = dict(
    imports=['projects.aqc_seg_dataset.mmseg.datasets.aqc_seg'])
crop_size = (1024, 1024)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=2),
    auxiliary_head=dict(num_classes=2))

vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='TensorboardVisBackend'),
]