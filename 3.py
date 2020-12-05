
import requests
import re
page_url = "https://img.plmm.com.cn/xinggan/"  # 百度获取index的URL
response =requests.get(page_url)
response.encoding ='utf-8'#转换格式
html = response.text#转化为文本格式的网址
#print(response.text)
imgs = re.findall(r'"thumbURL":"(.*?)"',html)
#print(imgs)#得到了每一个图片的网址
for index,img_url in enumerate(imgs):
    response=requests.get(img_url)
    with open('%s.%s.jpg'%(index, img_url.split('.')[-1]),'wb') as f:
        f.write(response.content)