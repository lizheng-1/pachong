#批量爬取百度图片

#导入需要的模块
import requests # requests是python实现的最简单易用的HTTP库
import re  #regular expression，正则表达式，是用来简洁表达一组字符串特征的表达式。最主要应用在字符串匹配中。
import os  #os库提供通用的，基本的操作系统交互功能（windows，mac os，linux）

#一般网站都有反爬虫机制，所以我们要对我们的爬虫进行伪装
#先去该网址找到他的请求头
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}

#自动创建保存图片的文件夹
word = input ('请输入想下载的图片的名称：')
if not os.path.exists(word):
    #如果不存在就自己生成一个
    os.mkdir(word)

#我们需要爬取图片的页数
num=int(input('请输入要爬取的图片页数（一页30张）：'))

urls=['https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=\
&ic=&hd=&latest=&copyright=&word=' + word +'&pn={}'.format(j) for j in range(30,num*30+1,30)
     ]
i= 1
#获取单张图片的url，并保存图片
def get_img(url):
    #获取到这个网页，并对其解码
    response=requests.get(url,headers)
    content=response.content.decode('utf-8')
    #正则表达式来查找这个content网址的thumbURL里面的内容，也就是图片的网址
    #re.S如果不设置的话就会进行单行匹配，也就是可能无法找到所有内容
    img_urls=re.findall('"thumbURL":"(.*?)"',content,re.S)
    #保存获取到的图片
    #设置成全局变量
    global i
    for img_url in img_urls:
        #对每一张图片进行处理
        response=requests.get(img_url,headers)
        content=response.content
        #以wb（二进制）的形式保存图片,并进行命名
        with open(word+'/'+ '{}.jpg'.format(i),'wb') as f:
            f.write(content)
            print("正在爬取第%d张图片"%i)
        #图片按照先后顺序进行从1到n的命名，所以i++
        i+=1
if __name__ =='__main__':
    for url in urls:
        get_img(url)
