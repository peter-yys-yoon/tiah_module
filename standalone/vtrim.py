import cv2
import argparse
import os
from tqdm import tqdm


def get_parser():
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser(description='Video trimming')
    parser.add_argument('--video', action='store', required=True)
    parser.add_argument('--range', action='store', required=True, help='start:end  ex) mm:ss,mm:ss')
    parser.add_argument('--outdir', default='', action='store')
    return parser.parse_args()


def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props


def trim(opt):
    video_path = opt.video
    assert os.path.exists(video_path)


    _path = video_path.replace('\\','/').split('/')
    # _vname = _path[-1]
    _vname = _path[-1].split('.')[0]+'.avi'

    if len(opt.outdir):
        # out_path = os.path.join(opt.outdir, '%s%s' % ('trim_', _vname))
        out_path = os.path.join(opt.outdir, '%s' % (_vname))
    else:
        out_path = out_path = os.path.join('/'.join(_path[0:-1]), '%s%s' % ('trim_', _vname))

    cap = cv2.VideoCapture()
    cap.open(video_path)
    props = get_properties(cap)
    fps = props['fps']
    s, e = range_count(opt.range, fps)

    #fourcc = cv2.VideoWriter_fourcc('H', '2', '6', '4')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter(out_path, fourcc, props['fps'], (props['width'], props['height']))

    print(out_path, props, s, '~', e, )
    name_desc = tqdm(range(e))

    count = 0
    while 1:

        name_desc.update()
        ret, frame = cap.read()
        if ret is False:
            break

        if s < count < e:
            writer.write(frame)
        count += 1

        if count > e:
            break

    cap.release()
    cap.release()


def range_count(raw, fps=30):

    if raw == '-1':
        return -1 ,99999999
    else:
        _s, _e = raw.split(',')
        s = sec2count(min2sec(_s), fps=fps)
        e = sec2count(min2sec(_e), fps=fps)
    return s, e


def min2sec(k):
    if ':' in k:
        m = k.split(':')[0]
        s = k.split(':')[1]

        return int(m) * 60 + int(s)
    else:
        return int(k)


def sec2count(k1, fps=30):
    return k1 * fps


opt = get_parser()
trim(opt)
