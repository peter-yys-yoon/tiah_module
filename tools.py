

import cv2


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


def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props
