import json
# f = open("E:\yolov4-keras-master\File_201.json",'r')
# ln = 0
#     for line in f.readlines():
#     ln += 1
#     dic = json.loads(line)
#     t = dic['label']
#     f = open("data.txt",'a',encoding='utf-8')
#     f.writelines(str(t));f.write("\n")
# f.write(str(ln))
# f.close()
with open("E:\yolov4-keras-master\File_201.json",'r',encoding='utf8')as fp:
    json_data = json.load(fp)
    # print('这是文件中的json数据：',json_data)
    # print('这是读取到文件数据的数据类型：', type(json_data))
    for line in fp.readlines():
        dic = json.loads(line)
        t = dic['version']
        print(line)
