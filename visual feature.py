# -*- coding:utf-8 -*-
from keras.models import Model,load_model
import cv2
import numpy as np
from matplotlib import pyplot as plt

model=load_model("E:\\dataset\\alexnet.h5")

img=cv2.imread(r'E:\dataset\hebing\test\boring\3458.png')
img=cv2.resize(img,(227,227))
img=np.expand_dims(img,axis=0)

layer_model = Model(inputs=model.input,outputs=model.layers[7].output)
layer_output = layer_model.predict(img)
print(layer_output.shape)
shape=layer_output.shape[1]
plt.figure(1)
for i in range(96):
    image=layer_output[:,:,:,i]
    image.shape=[shape,shape]
    plt.subplot(12,8,i+1)
    plt.imshow(image)
    plt.axis('off')
# plt.figure(2)
# for i in range(64):
#     image2=layer_output[:,:,:,i+64]
#     image2.shape=[shape,shape]
#     plt.subplot(8,8,i+1)
#     plt.imshow(image2)
#     plt.axis('off')
# plt.figure(3)
# for i in range(64):
#     image3=layer_output[:,:,:,i+128]
#     image3.shape=[shape,shape]
#     plt.subplot(8,8,i+1)
#     plt.imshow(image3)
#     plt.axis('off')
# plt.figure(4)
# for i in range(64):
#     image4=layer_output[:,:,:,i+64+128]
#     image4.shape=[shape,shape]
#     plt.subplot(8,8,i+1)
#     plt.imshow(image4)
#     plt.axis('off')
plt.show()