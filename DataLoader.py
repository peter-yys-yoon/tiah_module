import os
from tiah_module.var import *
import cv2
from cv2 import FONT_HERSHEY_COMPLEX, VideoWriter_fourcc

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
ORANGE = (255, 140, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
LIGHT_GREEN = (9, 249, 17)
BALCK = (0, 0, 0)
WHITE = (255, 255, 255)

PLOT_COLOR = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
# PLOT_COLOR = ['go', 'bo','ro']
PLOT_MARKER = ['-',  # 0
               '.',  # 1 dot
               ',',  # 2 pixel
               '--.',  # 3 d otted-line
               'o'  # 4 circle
               ]
VIDEO_EXT_LIST = ['mp4', 'avi']
COLOR_LIST = [RED, GREEN, BLUE, ORANGE, YELLOW, MAGENTA, LIGHT_GREEN, WHITE, BALCK]



FONT_FACE = FONT_HERSHEY_COMPLEX
THICKNESS = 2
FONT_SCALE = 1
FONT_THINKESS = 1

FRAME_COUNT_LOC = (30, 50)
FRAME_DIST_LOC = (990, 50)
FRAME_STATUS_LOC = (410, 50)

UPPER = 'upper'
LOWER = 'lower'
MEAN = 'mean'

fourcc_avi = VideoWriter_fourcc('D', 'I', 'V', 'X')

def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props



def is_video(_path):

    if os.path.isdir(path):
       return False

    ext = path.split('.')[1]
    if ext in VIDEO_EXT_LIST:
        return True
    else:
        return False




def read_video(path, isprint= False):
    """
    :param path: path to video file
    :param fname: video file name
    :return: image list
    """
    assert os.path.exists(path)
    cap = cv2.VideoCapture()
    cap.open(path)

    assert cap.isOpened(), 'Failed to open ' + path

    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}


    return cap, props



def frame_indexing(frame,idx):
    cv2.putText(frame, 'idx ' + str(idx), FRAME_COUNT_LOC, FONT_FACE, FONT_SCALE, WHITE, THICKNESS)  # frame


def text_filled(frame, p1, label, color):
    txt_size, baseLine1 = cv2.getTextSize(label, cv2.FONT_HERSHEY_DUPLEX, FONT_SCALE, FONT_THINKESS)
    p1_ = (p1[0] - 10, p1[1] + 10)
    p2 = (p1[0] + txt_size[0] + 10, p1[1] - txt_size[1] - 10)
    cv2.rectangle(frame, p1_, p2, color, -1)
    cv2.putText(frame, label, p1, cv2.FONT_HERSHEY_DUPLEX, FONT_SCALE, WHITE, FONT_THINKESS)  # point is left-bottom



def int2round(src):
    """
    returns rounded integer recursively
    :param src:
    :return:
    """
    if isinstance(src, float):
        return int(round(src))

    elif isinstance(src, tuple):
        res = []
        for i in range(len(src)):
            res.append(int(round(src[i])))
        return tuple(res)

    elif isinstance(src, list):
        res = []
        for i in range(len(src)):
            res.append(int2round(src[i]))
        return res
    elif isinstance(src, int):
        return src
    if isinstance(src, str):
        return int(src)



def center_to_upper(rect):
    """

    :param rect: center(x,y) and (w,h)
    :return: [x1, x2, y1 ,y2 ]
    """
    xc = rect[0]
    yc = rect[1]
    w = rect[2]
    h = rect[3]

    ux = xc - (w / 2)
    uy = yc - (h / 2)
    return (ux, ux + w, uy, uy + h)


def overlapping_area_size(a, b):
    """

    :param a: (x1, x2, y1, y2)
    :param b: (x1, x2, y1, y2)
    :return:
    """
    dx = min(a[1], b[1]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[2], b[2])
    if (dx >= 0) and (dy >= 0):
        return dx * dy
    else:
        return -1



def batch_indices(total, batch):
    indices = []

    isize = divmod(total, batch)[0]
    for i in range(isize):
        indices.append(np.arange(i * batch, (i + 1) * batch))
    indices.append(np.arange(isize * batch, total))
    return indices
