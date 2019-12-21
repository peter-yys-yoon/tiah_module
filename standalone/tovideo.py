import os
import argparse
import cv2
from tqdm import tqdm
from vars import FOURCC

def make_video(img_dir_path, outdir='', fps=30):
    flist = os.listdir(img_dir_path)
    video_name = os.path.basename(img_dir_path)

    if len(outdir):
        output_path = os.path.join(outdir, video_name)
    else:
        output_path = os.path.join(os.path.dirname(img_dir_path), video_name)

    _img_shape = cv2.imread(os.path.join(img_dir_path, flist[0])).shape[0:2]
    img_shape = _img_shape[::-1]
    print('writing at ', output_path, ' img shape ', img_shape)
    writer = cv2.VideoWriter(output_path, FOURCC, fps, img_shape)

    length = len(flist)
    name_desc = tqdm(range(length))
    for f in flist:
        name_desc.update(1)
        img = cv2.imread(os.path.join(img_dir_path, f))
        writer.write(img)
    writer.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', '-indir', type=str, dest='video', required=True, action='store')
    parser.add_argument('--outdir', dest='outdir', default='', type=str, action='store')
    parser.add_argument('--fps', dest='fps', default=30, type=int, action='store')

    args = parser.parse_args()

    make_video(args.indir, args.outdir, args.fps)
