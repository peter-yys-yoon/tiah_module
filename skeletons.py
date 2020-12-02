import cv2
import argparse
from tiah.vars import *
from tiah_module.tools import *
from tqdm import tqdm
import os
import platform
import argparse


    
def runner():

    PUMA = 'puma'
    OBAMA = 'obama'

    PATH_DATASET = '/home/peter/dataset'
    if platform.node() == PUMA:  #
        PATH_DATASET = '/home/peter/dataset'
        PATH_CONDA = '/home/peter/.conda/envs'

    else:
        PATH_DATASET = '/home/peter/workspace/dataset'
        PATH_CONDA = '/home/peter/anaconda3/envs'



    "---------------------HERE-------------------------"
    DATAPATH = '/home/peter/workspace/dataset/gist/elevator'
    ENV = 'elev'
    PROJECTPATH = '/home/peter/workspace/code/elev'
    PYNAME = 'yolotest.py'
    OUTPATH = os.path.join(PROJECTPATH, 'output/yolo')
    "---------------------------------------------------"

    PATH_CONDA = '/home/peter/anaconda3/envs'
    PY = f'{PROJECTPATH}/{PYNAME}'
    EXE = f'{PATH_CONDA}/{ENV}/bin/python'
    # os.makedirs(OUTPATH, exist_ok=True)

    filelist = os.listdir(DATAPATH)
    filelist.sort()
    print("Total files: ", len(filelist))
    for idx, vname in enumerate(filelist):
        if not vname.endswith('avi'):
            continue

        "---------------------HERE-------------------------"
        print('Running on ', vname, idx, '/', len(filelist))
        A_idx = vname.index('A')
        target = vname[A_idx:A_idx + 4]
        if target not in ['A002', 'A004', 'A006']:
            continue
        "---------------------------------------------------"

        invideo = os.path.join(DATAPATH, vname)
        command = f'{EXE} {PY} --save_video --video {invideo}'
        os.system(command)



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
    video_path =''
    
    "----------------------------------"
    cap, atts = read_video(video_path)
    framesize = get_framesize(cap)
    
    if args.save_video:
        savepath = ''
        writer = cv2.VideoWriter(savepath, XVID, 20, framesize)

    name_desc = tqdm(range(atts[LENGTH]))
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