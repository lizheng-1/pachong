import os
import random
import xml.etree.ElementTree as ET
from os import getcwd


def voc2yolo(xmlfilepath,saveBasePath ):
    trainval_percent = 1
    train_percent = 1

    temp_xml = os.listdir(xmlfilepath)
    total_xml = []
    for xml in temp_xml:
        if xml.endswith(".xml"):
            total_xml.append(xml)

    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    print("train and val size", tv)
    print("traub suze", tr)
    ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
    ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
    ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
    fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)
    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()

xmlfilepath = r'E:\yolov4-keras-master\VOCdevkit\VOC2007\Annotatios'
saveBasePath = r'E:\yolov4-keras-master\VOCdevkit\VOC2007\ImageSets\Main'
voc2yolo(xmlfilepath,saveBasePath )




#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes=["plant","board","person","sheep"]

def convert_annotation(xmlfilepath, list_txt):
    for filename in os.listdir(xmlfilepath):
        files = open(filename, encoding='UTF-8')
        tree=ET.parse(files)
        root = tree.getroot()
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) ==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            #b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
            b = (xmlbox.find('xmin').text, xmlbox.find('ymin').text, xmlbox.find('xmax').text, xmlbox.find('ymax').text)
            list_txt.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'.read().strip().split()
    list_file = open('%s_%s.txt'%(year,image_set),'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()
print(666)
for imgname in os.listdir(imgpath):
    imgname.write(imgpath + '/' + imgname)

