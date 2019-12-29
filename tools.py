

import cv2
import os

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

def batch_indices(total, batch):
    indices = []

    isize = divmod(total, batch)[0]
    for i in range(isize):
        indices.append(np.arange(i * batch, (i + 1) * batch))
    indices.append(np.arange(isize * batch, total))
    return indices


def read_video(path, isprint= False):
    """
    :param path: path to video file
    :param fname: video file name
    :return: image list
    """
    assert os.path.exists(path), 'Failed to open ' + path
    cap = cv2.VideoCapture()
    cap.open(path)

    assert cap.isOpened(), 'Failed to open ' + path

    return cap, get_properties(cap)


def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props

def get_framesize(cap):
    return (    
            int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            )
    