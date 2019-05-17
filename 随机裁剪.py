# coding:utf-8
import os
import cv2
import tensorflow as tf

sess = tf.InteractiveSession()
path=r'E:\dataset\yuanshi\sfew\train'
out_path=r'E:\dataset\sfew\balance\aug_yuanshi\train'
dir_list=os.listdir(path)
for list in dir_list:
    if list == 'angry':
        f = os.path.join(path,list)
        o = os.path.join(out_path,list)
    elif list == 'disgust':
        f = os.path.join(path, list)
        o = os.path.join(out_path, list)
    elif list == 'happy':
        f = os.path.join(path, list)
        o = os.path.join(out_path, list)
    elif list == 'neutral':
        f = os.path.join(path, list)
        o = os.path.join(out_path, list)
    else:
        print("get error.......\n")
        continue
# 定义图片生成器
# f = r"E:\dataset\jiaoyu\yuanshi\SFEW2.0\train\angry"
# o=r"E:\dataset\jiaoyu\aug_yuanshi\SFEW2.0\train"
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        img = cv2.imread(tmp_path)
        img = cv2.resize(img, (64, 64))
        cropped_image = tf.random_crop(img, (56, 56, 3))
        for i in range(10):
            cv2.imwrite(os.path.join(o,str(i)+f1),cropped_image.eval())
sess.close()
