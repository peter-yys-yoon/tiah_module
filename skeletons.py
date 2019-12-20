import cv2
import argparse
from tiah.vars import *
from tiah_module.tools import *
from tqdm import tqdm

def getopt():
    parser = argparse.ArgumentParser(description='PyTorch AlphaPose Training')

    parser.add_argument('--vis', default=False, action='store_true', help='visualize image')

    parser.add_argument('--profile', default=False,
                        action='store_true', help='visualize image')

    parser.add_argument('--save_video', dest='save_video',
                        help='whether to save rendered video', default=False, action='store_true')
    parser.add_argument('--video', dest='video', help='video-name',
                        default="/home/peter/dataset/gist/org/mid2019/roaming_kdh_trial_1/trim_student1.avi")

    opt = parser.parse_args()
    return opt


def video_reading():


    args = getopt()
    WAIT = 25
    path =''

    cap = cv2.VideoCapture()
    cap.open(path)
    pps = get_properties(cap) # fps, fourcc, w, h , length


    if args.save_video:
        savepath = ''
        framesize = ()
        writer = cv2.VideoWriter(savepath, FOURCC, 20, framesize)


    name_desc = tqdm(range(pps[LENGTH]))
    while 1:
        ret, frame = cap.read()
        if ret is False:
            break

        img = frame

        if args.save_video:
            writer.write(img)
        if args.vis:
            cv2.imshow('11', img)
            if cv2.waitKey(WAIT) == ord('q'):
                break

        name_desc.update(1)

    if args.save_video:
        writer.release()