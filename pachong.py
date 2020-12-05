import requests # requests是python实现的最简单易用的HTTP库
import re  #regular expression，正则表达式，是用来简洁表达一组字符串特征的表达式。最主要应用在字符串匹配中。
import os  #os库提供通用的，基本的操作系统交互功能（windows，mac os，linux）

word = "店铺牌"
if not os.path.exists(word):
    #如果不存在就自己生成一个
    os.mkdir(word)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}


urls='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height\=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%BA%97%E9%93%BA%E7%89%8C'


s = requests.Session()
response=s.get(url=urls,headers=headers,allow_redirects=False)
print(response)
content=response.content.decode('utf-8')
img_urls=re.findall('"thumbURL":"(.*?)"',content,re.S)
print(img_urls)
# 设置成全局变量
global i
i=1
for img_url in img_urls:
    # 对每一张图片进行处理
    s = requests.Session()
    response = s.get(url=img_url,headers=headers)
    content = response.content
    # 以wb（二进制）的形式保存图片,并进行命名
    with open(word + '/' + '{}.jpg'.format(i), 'wb') as f:
        f.write(content)
        print("正在爬取第%d张图片" % i)
    # 图片按照先后顺序进行从1到n的命名，所以i++
    i += 1



