import cv2
import argparse
import os
from tqdm import tqdm


def get_parser():
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser(description='Spatial Temporal Graph Convolution Network')
    parser.add_argument('--video', action='store', required=True)
    parser.add_argument('--range', action='store', required=True)
    parser.add_argument('--outdir', default='', action='store')
    return parser.parse_args()


def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props


def trim(opt):
    
    
    PATH_VIDEO = '/home/peter/extra/dataset/gist/demo2019/raw_video'
    PATH_TXT = '/home/peter/extra/dataset/gist/demo2019/raw_detector'
    OUTDIR = '/home/peter/extra/dataset/gist/demo2019/trim'
    
    vide_name = opt.video
    txt_file_name = vide_name.split('.')[0]+'.txt'
    
    video_path = os.path.join(PATH_VIDEO, vide_name)
    txt_path = os.path.join(PATH_TXT, txt_file_name)
    
    assert os.path.exists(video_path)


    _vname = vide_name.split('.')[0]+'.mp4'
    _tname = vide_name.split('.')[0]+'.txt'
    
    
    video_out_path = os.path.join(OUTDIR, '%s%s' % ('trim_', _vname))
    txt_out_path  = os.path.join(OUTDIR, '%s%s' % ('trim_', _tname))
    

    cap = cv2.VideoCapture()
    cap.open(video_path)
    props = get_properties(cap)
    fps = props['fps']
    s, e = range_count(opt.range, fps)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # fourcc = cv2.VideoWriter_fourcc('H', '2', '6', '4')
    # fourcc = VideoWriter_fourcc(*'MP4V')

    writer = cv2.VideoWriter(video_out_path, fourcc, props['fps'], (props['width'], props['height']))

    print(video_out_path, props, s, '~', e, )
    name_desc = tqdm(range(e))

    out_txt_file = open(txt_out_path,'w')
    video_detect_list = get_bbox_list(txt_path)
    count = 0
    while 1:

        name_desc.update()
        ret, frame = cap.read()
        if ret is False:
            break

        if s < count < e:
            writer.write(frame)
            
            frame_detect_list = video_detect_list[count]
            
            for tx in frame_detect_list:
                txx = tx.split('\n')[0]
                idx, cls, x, y, w, h, c = txx.split(' ')
                
                newline = f'{count-s-1} {cls} {x} {y} {w} {h} {c}\n'
                out_txt_file.write(newline)
                
        count += 1

        if count > e:
            break

    cap.release()
    cap.release()


def get_bbox_list(txtpath):
    txtfile = open(txtpath, 'r')
    txt = txtfile.readlines()

    N = int(txt[-1].split(' ')[0])
    detector_list = [[] for x in range(N + 1)]
    

    for tx in txt:
        txx = tx.split('\n')[0]
        idx, cls, x, y, w, h, c = txx.split(' ')
        detector_list[int(idx)].append(tx)
        
    return detector_list


def range_count(raw, fps=30):
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
