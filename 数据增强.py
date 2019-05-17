# coding:utf-8
import os
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

# path=r'E:\dataset\sfew\balance\crop\test'
# out_path=r'E:\dataset\sfew\balance\aug\test'
# dir_list=os.listdir(path)
# for list in dir_list:
    # if list == 'angry':
    #     f = os.path.join(path,list)
    #     o = os.path.join(out_path,list)
    # elif list == 'contempt':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # if list == 'disgust':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # elif list == 'fear':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # elif list == 'happy':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # elif list == 'neutral':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # elif list == 'sad':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # elif list == 'surprise':
    #     f = os.path.join(path, list)
    #     o = os.path.join(out_path, list)
    # else:
    #     print("get error.......\n")
    #     continue
# 定义图片生成器
f = r"E:\dataset\lunwenyong\kerasyong\jaffe\su"
o=r"E:\dataset\lunwenyong\qianyi\linshi"
fs = os.listdir(f)
for f1 in fs:
    tmp_path = os.path.join(f, f1)
    # data_gen = ImageDataGenerator(rotation_range=15,
    #                           horizontal_flip=True,
    #                           fill_mode='nearest')
    data_gen = ImageDataGenerator()
    img = load_img(tmp_path)
    x = img_to_array(img)  # 图片转化成array类型,因flow()接收numpy数组为参数
    x = x.reshape((1,) + x.shape)  # 要求为4维
    # 使用for循环迭代,生成图片
    i = 0
    for batch in data_gen.flow(x, batch_size=1,
                           save_to_dir=o,
                           save_prefix=f1):
        i += 1
        print(i)
        if i > 52:
          break
