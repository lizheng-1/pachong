from PIL import Image, ImageDraw
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

def rand(a=0, b=1):
    return np.random.rand() * (b - a) + a

def get_random_data(annotation_line,input_shape, random=True, max_boxes=20, jitter=.5, hue=.1, sat=1.5, val=1.5,
                    proc_img=True):
    '''实时数据增强的随机预处理'''
    image,box =normal_(annotation_line, input_shape)
    line = annotation_line.split()
    image = Image.open(line[0])
    iw, ih = image.size
    h, w = input_shape
    '''
    里面有一些比较重要的参数如：
    scale = rand(.25, 2)
    jitter=.5；
    hue=.1；
    sat=1.5；
    val=1.5；

    其中：
    1、scale代表原图片的缩放比率，rand(.25, 2)表示在0.25到2之间缩放。
    2、jitter代表原图片的宽高的扭曲比率，jitter=.5表示在0.5到1.5之间扭曲。
    3、hue=.1，sat=1.5，val=1.5；分别代表hsv色域中三个通道的扭曲，分别是：色调（H），饱和度（S），明度（V）。
    '''
    # 对图像进行缩放并且进行长和宽的扭曲
    new_ar = w / h * rand(1 - jitter, 1 + jitter) / rand(1 - jitter, 1 + jitter)
    scale = rand(.25, 2)
    if new_ar < 1:
        nh = int(scale * h)
        nw = int(nh * new_ar)
    else:
        nw = int(scale * w)
        nh = int(nw / new_ar)
    image = image.resize((nw, nh), Image.BICUBIC)

    # 将图像多余的部分加上灰条
    dx = int(rand(0, w - nw))
    dy = int(rand(0, h - nh))
    new_image = Image.new('RGB', (w, h), (128, 128, 128))
    new_image.paste(image, (dx, dy))
    image = new_image

    # 翻转图像
    flip = rand() < .5
    if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)

    # 色域扭曲
    hue = rand(-hue, hue)
    sat = rand(1, sat) if rand() < .5 else 1 / rand(1, sat)
    val = rand(1, val) if rand() < .5 else 1 / rand(1, val)
    x = rgb_to_hsv(np.array(image) / 255.)
    x[..., 0] += hue
    x[..., 0][x[..., 0] > 1] -= 1
    x[..., 0][x[..., 0] < 0] += 1
    x[..., 1] *= sat
    x[..., 2] *= val
    x[x > 1] = 1
    x[x < 0] = 0
    image_data = hsv_to_rgb(x)  # numpy array, 0 to 1

    # 将box进行调整
    box_data = np.zeros((max_boxes, 5))
    if len(box) > 0:
        np.random.shuffle(box)
        box[:, [0, 2]] = box[:, [0, 2]] * nw / iw + dx
        box[:, [1, 3]] = box[:, [1, 3]] * nh / ih + dy
        if flip: box[:, [0, 2]] = w - box[:, [2, 0]]
        box[:, 0:2][box[:, 0:2] < 0] = 0
        box[:, 2][box[:, 2] > w] = w
        box[:, 3][box[:, 3] > h] = h
        box_w = box[:, 2] - box[:, 0]
        box_h = box[:, 3] - box[:, 1]
        box = box[np.logical_and(box_w > 1, box_h > 1)]  # discard invalid box
        if len(box) > max_boxes: box = box[:max_boxes]
        box_data[:len(box)] = box

    return image_data, box_data

# 随机选择一条数据，然后将找到对应的图片image地址和box的坐标
def normal_(annotation_line, input_shape):
    '''random preprocessing for real-time data augmentation'''
    line = annotation_line.split()
    image = Image.open(line[0])
    box = np.array([np.array(list(map(int, box.split(',')))) for box in line[1:]])

    return image, box


# if __name__ == "__main__":
#     with open(r"E:\gfdata\000.txt") as f:
#         lines = f.readlines()
#
#     # 随机选取条图片并提取其信息
#     a = np.random.randint(0, len(lines))
#     line = lines[a]
#
#     image_data, box_data = normal_(line, [416, 416])
#     img = image_data
#
#     for j in range(len(box_data)):
#         thickness = 2
#         #框的位置
#         left, top, right, bottom = box_data[j][0:4]
#         draw = ImageDraw.Draw(img)
#         #这里是将框画的稍微粗一点
#         for i in range(thickness):
#             draw.rectangle(([left + i, top + i, right - i, bottom - i]))
#     img.show()
#
#     image_data, box_data = get_random_data(line, [416, 416])
#     print(box_data)
#     img = Image.fromarray((image_data * 255).astype(np.uint8))
#     for j in range(len(box_data)):
#         thickness = 2
#         left, top, right, bottom = box_data[j][0:4]
#         draw = ImageDraw.Draw(img)
#         for i in range(thickness):
#             draw.rectangle([left + i, top + i,left + i, top + i, right - i, bottom - i], outline=(255, 255, 255))
#     img.show()

'''
old_txt，vision_for_anchors.py生成的txt文件
save_txt,数据增强后要保存的txt文件
img_path,数据增强后的图片文件
head，数据增强图片的开头子母
'''
def enrich(old_txt,save_txt,img_path,head):
    with open(old_txt) as f:
        lines = f.readlines()
        path=img_path
        p=0
    for line in lines:
        p+=1
        image_data, box_data = get_random_data(line, [416, 416])
        img = Image.fromarray((image_data * 255).astype(np.uint8))
        line = line.split()[0]
        #shutil.copy(line,path)
        line=path+'/'+head+str(p).rjust(3,'0')+'.jpg'
        print(line)
        #plt.savefig(line)
        img.save(line)
        #img.show()
        with open(save_txt,'a+') as en:
            en.write(line)
            en.write(' ')
            for i in box_data:
                k=0
                for j in i:
                    #print(type(j))
                    en.write(str(j))
                    k+=1
                    if k==5:
                        en.write(' ')
                    else:
                        en.write(', ')
            en.write('\n')
        en.close()
old_txt=r'E:\gfdata\dataenrich\2007_train.txt'
save_txt=r'E:\yolov4-keras-master\2007_val.txt'
img_path=r'E:\yolov4-keras-master\VOCdevkit\VOC2007\JPEGImages'
enrich(old_txt,save_txt,img_path,'a')