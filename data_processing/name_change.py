#查找后缀为。。。的文件，并批量修改文件名

import os
def change(path,type1):
    i=0
    for filename in os.listdir(path):   #‘logo/’是文件夹路径，你也可以替换其他
        #print(filename)
        if filename[-3:]== type1:
            file=path+filename
            os.rename(file,path+'/'+str(i).rjust(3, '0')+'.'+type1)
            print(file)
            #os.rename(file,path+'b{}.'.format(i)+type1)
            i+=1
#path='E:/Sheeps-PascalVOC-export/annotations/'
path=r'F:\chrome\zrbdata\imgs\3/'
change(path,"jpg")


