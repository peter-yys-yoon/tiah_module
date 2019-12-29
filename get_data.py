import json
import numpy as np

from tiah.tools import int2round


def get_bbox_list(txtpath):
    txtfile = open(txtpath, 'r')
    txt = txtfile.readlines()

    N = int(txt[-1].split(' ')[0])
    car_list_list = [[] for x in range(N + 1)]
    hm_list_list = [[] for x in range(N + 1)]

    for tx in txt:
        txx = tx.split('\n')[0]
        idx, clss, x, y, w, h, c = txx.split(' ')
        idx, x, y, w, h, c = int(idx), max(int(x), 0), max(
            int(y), 0), int(w), int(h), float(c)

        if clss == 'person':
            hm_list_list[idx].append([x, y, x + w, y + h, c])
        else:
            car_list_list[idx].append([x, y, x + w, y + h, c])

    return car_list_list, hm_list_list


def get_bbox_dict(txtpath):
    det_dict = {}

    txtfile = open(txtpath, 'r')
    txt = txtfile.readlines()

    for tx in txt:
        txx = tx.split('\n')[0]
        txx = txx.split(',')
        # idx, x1, y1, x2, y2, conf, cls_conf, cls_pred = txx

        idx, x1, y1, x2, y2 = int2round(txx[0:5])
        conf, cls_conf = float(txx[5]), float(txx[6])
        cls_pred = txx[7]

        # self.final_result.append(f'{im_name} {x1} {y1} {x2} {y2} {conf} {cls_conf} {cls_pred}')
        # 262 490.5502014160156 399.2558288574219 920.959716796875 1059.2034912109375 0.8572085499763489 0.7573287487030029 person

        if idx in det_dict.keys():
            dets = det_dict[idx]
            dets.append([idx, x1,y1,x2,y2,conf,cls_conf, cls_pred])
            det_dict[idx] =dets
        else:
            det_dict[idx] = [[idx, x1,y1,x2,y2,conf,cls_conf, cls_pred]]

    return det_dict

