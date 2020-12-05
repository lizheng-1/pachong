#视频分帧

import cv2
import os
import shutil
def fenzhen(video_path,photo_path,frame):
    i=0
    j=1
    camera = cv2.VideoCapture(video_path)
    while True:
        i += 1
        res, image = camera.read()
        if i % frame == 0:
            j+=1
            cv2.imwrite(photo_path+'\{}.jpg'.format(j), image)
            print('{}.jpg'.format(j))
        if not res:
            print("图片提取结束,共提取了{}张图片".format(j))
            break
    camera.release()

#video_path=r'E:/gfdata/Video/'
#photo_path='E:/gfdata/Video/'
frame=25
for i in range(1,22):
    photo_path = "E:/gfdata/Video/{}".format(i)
    video_path = r'E:/gfdata/Video/{}.mp4'.format(i)
    if not os.path.exists(photo_path):
        # 如果不存在就自己生成一个
        os.mkdir(photo_path)
    fenzhen(video_path,photo_path,frame)
    shutil.move(video_path,photo_path)

