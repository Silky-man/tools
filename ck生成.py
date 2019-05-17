# -*- coding:utf-8 -*-

import cv2
import os
k=0
state=True
path=r'E:\dataset\lunwenyong\kerasyong\ck\fe'
out_path=r'E:\dataset\lunwenyong\qianyi\ck'
images=os.listdir(path)
while state:
    for i in images:
        image=cv2.imread(os.path.join(path,i))
        cv2.imwrite(out_path+'\\'+'fe'+str(k)+'.png',image)
        k+=1
        print(k)
        if k==2130:
            state=False
            break

