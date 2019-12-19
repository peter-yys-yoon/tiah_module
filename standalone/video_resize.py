import os
import argparse
import cv2
from numpy import argmax
from tqdm import tqdm

FHD = 'fhd'
HD = 'hd'
VGA = 'vga'
QVGA = 'qvga'

resolution_set = {
    FHD: (1920, 1080),
    HD: (1280, 720),
    VGA: (640, 480),
    QVGA: (320, 240)
}


def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props


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


def convert_size(org_size, opt):
    dest = opt.size
    dest = dest.upper()

    dest_size = resolution_set[dest]
    idx = int(argmax(org_size))

    ratio = dest_size[idx] / org_size[idx]

    new_size = (org_size[0] * ratio, org_size[1] * ratio)

    return int2round(new_size)


def resizing(opt):
    path = opt.video
    assert os.path.exists(path), 'Video not exist, %s' % path

    cap = cv2.VideoCapture()
    cap.open(path)

    assert cap.isOpened(), 'Video not opend'

    video_name = os.path.basename(path)
    props = get_properties(cap)
    print(video_name, props)

    org_size = (props['width'], props['height'])

    if opt.fixed:
        new_size = resolution_set[opt.size]
    else:
        new_size = convert_size(org_size, opt)

    path_outdir = opt.outdir
    print('Converting ', org_size, ' >> ', new_size)
    if len(path_outdir):
        output_path = os.path.join(path_outdir, f'{opt.size}_{video_name}')
    else:

        output_path = os.path.join(os.path.dirname(path), f'{opt.size}_{video_name}')
    print('writing at ', output_path, props['fps'], new_size)
    fourcc_avi = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    writer = cv2.VideoWriter(output_path, fourcc_avi, props['fps'], new_size)
    name_desc = tqdm(range(props['length']))

    while 1:
        ret, frame = cap.read()
        if ret is False:
            break

        resized = cv2.resize(frame, new_size)
        writer.write(resized)
        name_desc.update(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', '-v', type=str, help='full path for video', required=True, action='store')
    parser.add_argument('--size', type=str, help='desired size [fhd,hd,,vga,qvga]', required=True, action='store')
    # parser.add_argument('--fixed', dest='fixed', type=bool, default=False, action='store_true')
    parser.add_argument('--fixed', help='fixed resolution?', default=False, action='store_true')
    parser.add_argument('--save_video', dest='save_video',
                        help='whether to save rendered video', default=False, action='store_true')
    parser.add_argument('--outdir', help='output directory', type=str, action='store')

    args = parser.parse_args()

    assert args.size in resolution_set.keys(), 'Invalid size'

    resizing(args)
    # tmp(args)
