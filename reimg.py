# coding=utf-8
import os
import os.path
import xml.dom.minidom
from PIL import Image
import cv2
import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt

# for xmlfile in files:
#
#    img=cv.imread(path+xmlfile,0)
#    # cv.imshow('le', img)
#    ret, dst = cv.threshold(img, 55, 255, cv.THRESH_BINARY)
#    # cv.imshow('dst', dst)

if __name__ == '__main__':
   path = "/home/hezhengyang/PycharmProjects/mmdetection/mmdetection-master/11/"
   files = os.listdir(path)  # 得到文件夹下所有文件名称
   for xmlfile in files:
     print(path+xmlfile)
     image = cv2.imread(path+xmlfile, 0)
     print(image)
     # plt.imshow('image',image)
     ret,dst=cv2.threshold(image,55,255,cv2.THRESH_BINARY)
     print("ok")
     plt.subplot(121)
     plt.imshow(image)
     cv2.imwrite(path+xmlfile,image)
     cv2.imshow('dst',dst)

