import xml.etree.ElementTree as ET
import numpy as np
import  os
import  math
sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes=["plant","board","person","sheep"]

def convert_annotation(xml_path):#
    for xml_file in os.listdir(xml_path):
        in_file = open(xml_path+'/'+xml_file, encoding='UTF-8')
        tree=ET.parse(in_file) #分析这个xml文件
        root = tree.getroot() #获取第一标签
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (xmlbox.find('xmin').text, xmlbox.find('ymin').text, xmlbox.find('xmax').text, xmlbox.find('ymax').text)
            #print(b)
            # name_node = xmlbox.createElement("name")
            # name_text_value = xmlbox.createTextNode("kavin")
            # name_node.appendChild(name_text_value)  # 把文本节点挂到name_node节点
            # customer_node.appendChild(name_node)

            for xmin in xmlbox:
                print(xmin.text)

                s=np.array(xmin.text)
                q = math.ceil(s)
                print(q)

                # print(type(int(str(s))))
                # new_min = q
                # xmin.text=q
                #x=xmin.createTextNode('666')
                #set(x,q)



            #tree.write(xml_path + '/' + xml_file)
            #xmlbox.appendChild(data)
            #xmlbox.childNodes[0].data = 99999
            #xmlbox.data=6

        #list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

convert_annotation(r'E:\Sheeps-PascalVOC-export\123')

# wd = os.getcwd()
#
# for year, image_set in sets:
#     image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt'%(year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
#         convert_annotation(year, image_id, list_file)
#         list_file.write('\n')
#     list_file.close()
# print(666)
