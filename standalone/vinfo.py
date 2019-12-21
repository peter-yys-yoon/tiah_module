import cv2
import argparse
import os


def get_parser():
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser(description='Printing video properties')
    parser.add_argument('--video', action='store', required=True)
    return parser.parse_args()


def get_properties(cap):
    props = {'fps': int(cap.get(cv2.CAP_PROP_FPS)), 'fourcc': int(cap.get(cv2.CAP_PROP_FOURCC)),
             'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
             'length': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
    return props


def trim(opt):
    video_path = opt.video
    assert os.path.exists(video_path)
    cap = cv2.VideoCapture()
    cap.open(video_path)
    props = get_properties(cap)
    print(props)
opt = get_parser()
trim(opt)
