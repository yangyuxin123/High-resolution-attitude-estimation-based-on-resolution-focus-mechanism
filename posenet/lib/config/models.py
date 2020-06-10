# ------------------------------------------------------------------------------
# Copyright (c) Microsoft
# Licensed under the MIT License.
# Written by Bin Xiao (Bin.Xiao@microsoft.com)
# ------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yacs.config import CfgNode as CN


# pose_multi_resoluton_net related params
POSENET = CN()
POSENET.PRETRAINED_LAYERS = ['*']
POSENET.STEM_INPLANES = 64
POSENET.FINAL_CONV_KERNEL = 1

POSENET.STAGE2 = CN()
POSENET.STAGE2.NUM_MODULES = 4
POSENET.STAGE2.NUM_BRANCHES = 4
POSENET.STAGE2.NUM_BLOCKS = [4, 4, 4, 4]
POSENET.STAGE2.NUM_CHANNELS = [32, 64, 128, 256]
POSENET.STAGE2.BLOCK = 'BASIC'
POSENET.STAGE2.FUSE_METHOD = 'SUM'


MODEL_EXTRAS = {
    'posenet': POSENET,
}
