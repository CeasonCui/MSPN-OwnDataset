"""
@author: Wenbo Li
@contact: fenglinglwb@gmail.com
"""

from easydict import EasyDict as edict

class COCO:
    NAME = 'COCO'

    KEYPOINT = edict()
    KEYPOINT.NUM = 17
    KEYPOINT.FLIP_PAIRS = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [15, 16]]
    KEYPOINT.UPPER_BODY_IDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    KEYPOINT.LOWER_BODY_IDS = [11, 12, 13, 14, 15, 16]
    KEYPOINT.LOAD_MIN_NUM = 1

    INPUT_SHAPE = (256, 192) # height, width
    OUTPUT_SHAPE = (64, 48)
    WIDTH_HEIGHT_RATIO = INPUT_SHAPE[1] / INPUT_SHAPE[0]

    PIXEL_STD = 200
    COLOR_RGB = False

    TRAIN = edict()
    TRAIN.BASIC_EXTENTION = 0.05
    TRAIN.RANDOM_EXTENTION = True
    TRAIN.X_EXTENTION = 0.6 
    TRAIN.Y_EXTENTION = 0.8 
    TRAIN.SCALE_FACTOR_LOW = -0.25 
    TRAIN.SCALE_FACTOR_HIGH = 0.25 
    TRAIN.SCALE_SHRINK_RATIO = 0.8
    TRAIN.ROTATION_FACTOR = 45 
    TRAIN.PROB_ROTATION = 0.5
    TRAIN.PROB_FLIP = 0.5
    TRAIN.NUM_KEYPOINTS_HALF_BODY = 3
    TRAIN.PROB_HALF_BODY = 0.3
    TRAIN.X_EXTENTION_HALF_BODY = 0.6 
    TRAIN.Y_EXTENTION_HALF_BODY = 0.8
    TRAIN.ADD_MORE_AUG = False
    TRAIN.GAUSSIAN_KERNELS = [(15, 15), (11, 11), (9, 9), (7, 7), (5, 5)]

    TEST = edict()
    TEST.FLIP = True
    TEST.X_EXTENTION = 0.01 * 9.0
    TEST.Y_EXTENTION = 0.015 * 9.0
    TEST.SHIFT_RATIOS = [0.25]
    TEST.GAUSSIAN_KERNEL = 5


class MPII:
    NAME = 'MPII'

    KEYPOINT = edict()
    KEYPOINT.NUM = 16
    KEYPOINT.FLIP_PAIRS = [[0, 5], [1, 4], [2, 3], [10, 15], [11, 14], [12, 13]]
    KEYPOINT.UPPER_BODY_IDS = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    KEYPOINT.LOWER_BODY_IDS = [0, 1, 2, 3, 4, 5, 6] #coco把臀部在上下两个都包含，mpii把臀部只放下半部分了emmm 
    KEYPOINT.LOAD_MIN_NUM = 1

    INPUT_SHAPE = (256, 256) # height, width
    OUTPUT_SHAPE = (64, 64)
    WIDTH_HEIGHT_RATIO = INPUT_SHAPE[1] / INPUT_SHAPE[0]

    PIXEL_STD = 200
    COLOR_RGB = False

    TRAIN = edict()
    TRAIN.BASIC_EXTENTION = 0.0
    TRAIN.RANDOM_EXTENTION = False 
    TRAIN.X_EXTENTION = 0.25 
    TRAIN.Y_EXTENTION = 0.25
    TRAIN.SCALE_FACTOR_LOW = -0.25 
    TRAIN.SCALE_FACTOR_HIGH = 0.25 
    TRAIN.SCALE_SHRINK_RATIO = 1.0
    TRAIN.ROTATION_FACTOR = 60
    TRAIN.PROB_ROTATION = 0.5
    TRAIN.PROB_FLIP = 0.5
    TRAIN.NUM_KEYPOINTS_HALF_BODY = 8
    TRAIN.PROB_HALF_BODY = 0.5
    TRAIN.X_EXTENTION_HALF_BODY = 0.6 
    TRAIN.Y_EXTENTION_HALF_BODY = 0.6
    TRAIN.ADD_MORE_AUG = False
    TRAIN.GAUSSIAN_KERNELS = [(15, 15), (11, 11), (9, 9), (7, 7), (5, 5)]

    TEST = edict()
    TEST.FLIP = True
    TEST.X_EXTENTION = 0.25 
    TEST.Y_EXTENTION = 0.25 
    TEST.SHIFT_RATIOS = [0.25]
    TEST.GAUSSIAN_KERNEL = 9

class SELF:
    NAME = 'SELF'

    KEYPOINT = edict()
    KEYPOINT.NUM = 17
    KEYPOINT.FLIP_PAIRS = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
            [13, 14], [15, 16]]
    KEYPOINT.UPPER_BODY_IDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    KEYPOINT.LOWER_BODY_IDS = [11, 12, 13, 14, 15, 16]
    # KEYPOINT.NUM = 19 #应该写19还是多少？待定，先写19
    #其实是17个和coco一样
    # KEYPOINT.FLIP_PAIRS = [[2, 3], [4, 5], [7, 8], [9, 10], [11, 12], [13, 14],
    #                        [15, 16], [17, 18]] #旋转配对，应该是左右的意思
    # KEYPOINT.UPPER_BODY_IDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #腰以上
    # KEYPOINT.LOWER_BODY_IDS = [13, 14, 15, 16, 17, 18] #腰以下
    KEYPOINT.LOAD_MIN_NUM = 1

    INPUT_SHAPE = (256, 192) # height, width #coco是长方形的，mpii是正方形的，为啥
    OUTPUT_SHAPE = (64, 48) #直觉觉得我的数据得弄成长方形的
    WIDTH_HEIGHT_RATIO = INPUT_SHAPE[1] / INPUT_SHAPE[0]

    PIXEL_STD = 200
    COLOR_RGB = False

    TRAIN = edict()
    TRAIN.BASIC_EXTENTION = 0.05
    TRAIN.RANDOM_EXTENTION = True
    TRAIN.X_EXTENTION = 0.6 
    TRAIN.Y_EXTENTION = 0.8 
    TRAIN.SCALE_FACTOR_LOW = -0.25 
    TRAIN.SCALE_FACTOR_HIGH = 0.25 
    TRAIN.SCALE_SHRINK_RATIO = 0.8
    TRAIN.ROTATION_FACTOR = 45 
    TRAIN.PROB_ROTATION = 0.5
    TRAIN.PROB_FLIP = 0.5
    TRAIN.NUM_KEYPOINTS_HALF_BODY = 3
    TRAIN.PROB_HALF_BODY = 0.3
    TRAIN.X_EXTENTION_HALF_BODY = 0.6 
    TRAIN.Y_EXTENTION_HALF_BODY = 0.8
    TRAIN.ADD_MORE_AUG = False
    TRAIN.GAUSSIAN_KERNELS = [(15, 15), (11, 11), (9, 9), (7, 7), (5, 5)]

    TEST = edict()
    TEST.FLIP = True
    TEST.X_EXTENTION = 0.01 * 9.0
    TEST.Y_EXTENTION = 0.015 * 9.0
    TEST.SHIFT_RATIOS = [0.25]
    TEST.GAUSSIAN_KERNEL = 5

def load_dataset(name):
    if name == 'COCO':
        dataset = COCO()
    elif name == 'MPII':
        dataset = MPII()
    elif name == 'SELF':
        dataset = SELF()
    return dataset
