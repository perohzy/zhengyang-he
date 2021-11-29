import os
path = '/home/hezhengyang/PycharmProjects/deep-learning-for-image-processing-master/pytorch_object_detection/faster_rcnn/VOCdevkit/VOC2012/Annotations/'
filenames=os.listdir(path)
for filename in filenames:
  print(filename)
  with open(os.path.join(path,filename),'r') as f:
    text=f.readlines()
    # print(text)
    # print(text)
    text[2]=text[2].replace('.png','.jpg')
    print(text[2])
    text[3] = text[3].replace('.png', '.jpg')
    print(text[3])
  with open(os.path.join(path,filename),'w+') as f:
    f.writelines(text)
