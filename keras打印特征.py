# -*- coding:utf-8 -*-
from keras.models import Model,load_model
import cv2
import numpy as np
from matplotlib import pyplot as plt

model=load_model("E:\\dataset\\alexnet.h5")

img=cv2.imread(r'E:\dataset\hebing\test\boring\3458.png')
img=cv2.resize(img,(227,227))
img=np.expand_dims(img,axis=0)

def print_feature(i):
    layer_model = Model(inputs=model.input,outputs=model.layers[i].output)
    layer_output = layer_model.predict(img)
    print(layer_output.shape)
    shape=layer_output.shape[1]
    plt.figure(i)
    for i in range(49):
        image=layer_output[:,:,:,i]
        image.shape=[shape,shape]
        plt.subplot(7,7,i+1)
        plt.imshow(image)
        plt.axis('off')
print_feature(3)
print_feature(6)
print_feature(10)
print_feature(14)
print_feature(18)
plt.show()