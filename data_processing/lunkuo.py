import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont


font = cv2.FONT_HERSHEY_SIMPLEX
'''
字体：

　　cv2.FONT_HERSHEY_SIMPLEX  正常尺寸的sans-serif字体

　　cv2.FONT_HERSHEY_SPLAIN   小尺寸的sans-serif字体

　　cv2.FONT_HERSHEY_COMPLEX  正常尺寸的serif字体

　　cv2.FONT_HERSHEY_SCREIPT_SIMPLEX  手写字体风格
'''

# def putText_Chinese(img, text, pt, textColor=(0, 255, 0), textSize=20):
#     left, top = pt[0], pt[1]
#     if (isinstance(img, np.ndarray)):
#         # 判断是否OpenCV图片类型
#         img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         draw = ImageDraw.Draw(img)
#         fontText = ImageFont.truetype("simhei.ttf", textSize, encoding="utf-8")
#         draw.text((left, top), text, textColor, font=fontText)
#         return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


img = cv2.imread(r'E:\yolov4-keras-master\img\1.jpg')

cv2.imshow('src', img)

temp = img.copy()

#cv2.cvtColor(p1,p2) 是颜色空间转换函数，p1是需要转换的图片，p2是转换成何种格式。这里是转化成了灰度图
gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)



'''
Python: cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
在其中：
src：表示的是图片源
thresh：表示的是阈值（起始值）
maxval：表示的是最大值
type：表示的是这里划分的时候使用的是什么类型的算法**，常用值为0（cv2.THRESH_BINARY）
'''

ret, thresh = cv2.threshold(gray, 200, 250, cv2.THRESH_BINARY)
cv2.imshow("thres", thresh)


contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


#%#
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    '''
    img是一个二值图，也就是它的参数；
    返回四个值，分别是x，y，w，h；    
    x，y是矩阵左上点的坐标，w，h是矩阵的宽和高    
    然后利用cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)画出矩行
    '''
    #if (w > 300 and h > 300):
        # left_most = tuple(cnt[cnt[:, :, 0].argmin()][0])
        # right_most = tuple(cnt[cnt[:, :, 0].argmax()][0])
        # top_most = tuple(cnt[cnt[:, :, 1].argmin()][0])
        # bottom_most = tuple(cnt[cnt[:, :, 1].argmax()][0])
    '''
        第一个参数：要在哪副图上画
        第二个参数：findContours函数返回的轮廓参数
        第三个参数：画第几个轮廓，-1表示画出所有轮廓
        第四个参数：轮廓颜色的RGB值
        第五个参数：轮廓的宽度
    '''
    cv2.drawContours(img, cnt,-1, (255, 0, 0), 3)

        # cv2.circle(img, left_most, 5, (0, 255, 0), -1, cv2.LINE_AA)
        # cv2.circle(img, right_most, 5, (0, 255, 0), -1, cv2.LINE_AA)
        # cv2.circle(img, top_most, 5, (0, 255, 0), -1, cv2.LINE_AA)
        # cv2.circle(img, bottom_most, 5, (0, 255, 0), -1, cv2.LINE_AA)

        # img = putText_Chinese(img, "西", left_most, (0, 255, 255), 30)
        # img = putText_Chinese(img, "东", right_most, (0, 255, 255), 30)
        # img = putText_Chinese(img, "北", top_most, (0, 255, 255), 30)
        # img = putText_Chinese(img, "南", bottom_most, (0, 255, 255), 30)
        # img = putText_Chinese(img, "中 国", (int(x + w / 2), int(y + h / 2)), (255, 255, 0), 70)

cv2.imshow('contours', img)

#cv2.imwrite('result.bmp', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
