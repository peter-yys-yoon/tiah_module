import cv2
import argparse
import os
from tqdm import tqdm

def split(videopath, video_nxt, outdir):
    cap = cv2.VideoCapture()
    cap.open(videopath)
    n = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    n = str(n)
    n = len(n)

    frame_count = 1

    while 1:
        ret, img = cap.read()
        if ret is False:
            break

        imgpath = os.path.join(outdir, f'{video_nxt}_frame_{str(i).zfill(n)}.jpg')
        cv2.imwrite(imgpath, img)
        frame_count += 1

def merge(indirpath):
    video_name = os.path.basename(indirpath)

    outdir = os.path.dirname(indirpath)

    img_list = os.listdir(indirpath)
    tmp = cv2.imread(os.path.join(indirpath,img_list[0]))
    w, h = tmp.shape[1], tmp.shape[0]

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    writer = cv2.VideoWriter(os.path.join(outdir, f'merged_{video_name}.mp4'), fourcc, 25, (w,h))

    img_list.sort()
    name_desc = tqdm(range(len(img_list)))
    for img_name in img_list:
        img = cv2.imread(os.path.join(indirpath, img_name))
        writer.write(img)
        name_desc.update()

    writer.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str, default='', help='Path to options YMAL file.')
    parser.add_argument('--indir', type=str, default= '' ,help='Path to options YMAL file.')
    args = parser.parse_args()



    videopath = args.video
    indirpath = args.indir

    if len(videopath) >0:
        assert os.path.exists(videopath), 'Video not exist'

        base_dir = os.path.dirname(videopath)
        video_nxt = os.path.basename(videopath).split('.')[0]

        outdir = os.path.join(base_dir, video_nxt + '_images')
        if not os.path.exists(outdir):
            os.mkdir(outdir)

    elif len(indirpath) >0 :
        merge(indirpath)
