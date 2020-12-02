import cv2
import numpy as np
from tiah.vars import *

def draw_header(img, img_id, color, msg='', height= 0.05, scale=2, thick=2):
    txt_size, baseLine1 = cv2.getTextSize(msg, cv2.FONT_HERSHEY_DUPLEX, scale, thick)
    p1_ = (10, 10 + txt_size[1] + 10)

    imgW, imgH = img.shape[1], img.shape[0]
    HEADER_height = int(10 + txt_size[1]+15)
    # HEADER_height = int(img.shape[1] * height)


    mask = np.zeros((HEADER_height, imgW, 3), dtype=np.uint8)

    mask[:, :, :] = color
    if len(msg):
        # vis_msg = f'Frame: {str(img_id).rjust(4)} {msg}'
        vis_msg = msg
    else:
        vis_msg = f'Frame: {str(img_id).rjust(4)}'

    header = cv2.addWeighted(
        img[0:HEADER_height, 0:imgW, :], 0.4, mask, 0.6, 0)


    img[0:HEADER_height, 0:imgW, :] = header[:, :, :]
    cv2.putText(img, vis_msg, p1_, cv2.FONT_HERSHEY_DUPLEX, scale, COLOR_WHITE, thick)  # point is left-bottom



def text_filled(frame, p1, label, color):
    txt_size, baseLine1 = cv2.getTextSize(label, cv2.FONT_HERSHEY_DUPLEX, FONT_SCALE, FONT_THINKESS)
    p1_ = (p1[0] - 10, p1[1] + 10)
    p2 = (p1[0] + txt_size[0] + 10, p1[1] - txt_size[1] - 10)
    cv2.rectangle(frame, p1_, p2, color, -1)
    cv2.putText(frame, label, p1, cv2.FONT_HERSHEY_DUPLEX, FONT_SCALE, WHITE, FONT_THINKESS)  # point is left-bottom


def overlayfunc(img, bbox, ratio=0.9, alpha=0.7):
    original = img.copy()
    x1, y1, x2, y2 = bbox
    cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
    w = x2 - x1
    h = y2 - y1
    center = (cx, cy)
    rad = max(w, h) * ratio

    # cx,cy == center
    # rad == max(w,h)

    for i in range(7):
        mask = np.zeros(original.shape, dtype=np.uint8)
        cv2.circle(mask, center, int(rad) - i * 15, (255, 255, 255), -1)
        mask = np.sum(mask, axis=2).astype(np.bool)
        mask = np.logical_not(mask)
        imgk = original.copy()
        imgk[mask] = [255, 255, 255]
        cv2.addWeighted(imgk, alpha, img, 1 - alpha, 0, img)
        
def text_filled(frame, p1, label, color):
    txt_size, baseLine1 = cv2.getTextSize(label, cv2.FONT_HERSHEY_DUPLEX, FONT_SCALE, FONT_THINKESS)
    p1_ = (p1[0] - 10, p1[1] + 10)
    p2 = (p1[0] + txt_size[0] + 10, p1[1] - txt_size[1] - 10)
    cv2.rectangle(frame, p1_, p2, color, -1)
    cv2.putText(frame, label, p1, cv2.FONT_HERSHEY_DUPLEX, FONT_SCALE, WHITE, FONT_THINKESS)  # point is left-bottom
