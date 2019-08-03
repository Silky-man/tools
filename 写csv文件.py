#!/usr/bin/python
# coding:utf8

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


f = r"E:\paper\dataset\jaffe\jaffecrop_raw"
fs = os.listdir(f)
np.random.shuffle(fs)
k=213
size=224
data = np.zeros([k, size*size], dtype=np.uint8)
label = np.zeros([k], dtype=int)
i = 0
for f1 in fs:
    tmp_path = os.path.join(f, f1)
    if not os.path.isdir(tmp_path):
        # print(tmp_path[len(f):])
        img = cv2.imread(tmp_path,0)
        img = cv2.resize(img, (size,size))
            # 获得表情label
        img_label = f1[3:5]
        print(img_label)
        if img_label == 'AN':
            label[i] = 0
        elif img_label == 'DI':
            label[i] = 1
        elif img_label == 'FE':
            label[i] = 2
        elif img_label == 'HA':
            label[i] = 3
        elif img_label == 'NE':
            label[i] = 4
        elif img_label == 'SA':
            label[i] = 5
        elif img_label == 'SU':
            label[i] = 6
        # elif img_label == '7':
        #     label[i] = 7
        else:
            print("get label error.......\n")
        data[i][0:size*size] = np.ndarray.flatten(img)
        i = i + 1
    # if i==213:
    #     break
print(i)

with open(r"E:\paper\dataset\jaffe\jaffe.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['emotion', 'pixels'])
    for i in range(len(label)):
        data_list = list(data[i])
        b = " ".join(str(x) for x in data_list)
        l = np.hstack([label[i], b])
        writer.writerow(l)
