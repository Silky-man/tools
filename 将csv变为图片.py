# -*- coding: utf-8 -*-
#第一步提取训练集，验证集，测试集csv文件
# import csv
# import os
#
# database_path = r'E:\paper\dataset\fer2013'
# datasets_path = r'E:\paper\dataset\restore_fer2013'
# csv_file = os.path.join(database_path, 'fer2013.csv')
# train_csv = os.path.join(datasets_path, 'train.csv')
# val_csv = os.path.join(datasets_path, 'val.csv')
# test_csv = os.path.join(datasets_path, 'test.csv')
#
#
# with open(csv_file) as f:
#     csvr = csv.reader(f)
#     header = next(csvr)
#     rows = [row for row in csvr]
#
#     trn = [row[:-1] for row in rows if row[-1] == 'Training']
#     csv.writer(open(train_csv, 'w+'), lineterminator='\n').writerows([header[:-1]] + trn)
#     print(len(trn))
#
#     val = [row[:-1] for row in rows if row[-1] == 'PublicTest']
#     csv.writer(open(val_csv, 'w+'), lineterminator='\n').writerows([header[:-1]] + val)
#     print(len(val))
#
#     tst = [row[:-1] for row in rows if row[-1] == 'PrivateTest']
#     csv.writer(open(test_csv, 'w+'), lineterminator='\n').writerows([header[:-1]] + tst)
#     print(len(tst))

#第二步将csv变为照片
import csv
import os
from PIL import Image
import numpy as np


datasets_path = r'E:\paper\dataset\restore_fer2013'

img_set = os.path.join(datasets_path, 'img')


for save_path in img_set:
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    num = 1
    with open(r"E:\paper\dataset\restore_fer2013\test.csv") as f:
        csvr = csv.reader(f)
        header = next(csvr)
        for i, (label, pixel) in enumerate(csvr):
            pixel = np.asarray([float(p) for p in pixel.split()]).reshape(48, 48)
            im = Image.fromarray(pixel).convert('L')
            image_name = os.path.join(r"E:\paper\dataset\restore_fer2013\wo", '{:05d}.jpg'.format(i))
            print(image_name)
            im.save(image_name)