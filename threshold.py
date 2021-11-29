# coding=utf-8
import os
import os.path
import xml.dom.minidom
import cv2 as cv

path = "/home/hezhengyang/PycharmProjects/mmdetection/mmdetection-master/11/"
files = os.listdir(path)  # 得到文件夹下所有文件名称

for xmlfile in files:
   img=cv.imread(xmlfile,0)
   cv.imshow('le',img)
   ret,dst=cv.threshold(img,55,255,cv.THRESH_BINARY)
   cv.imshow('dst',dst)

