import requests
from lxml import etree
import os
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
i = 100
def bizhi(path,num):
    for n in range(num):
        url = "http://www.netbian.com/desk/{}.htm".format(22770+n)
        page_test=requests.get(url=url,headers=headers).text
        tree=etree.HTML(page_test)
        li_list=tree.xpath('//*[@id="main"]/div[3]/div/p/a/img/@src')
        li = "".join(li_list)
        global i
        i += 1
        if li =='':
            continue
        print(li)
        s = requests.Session()
        response = s.get(url=li, headers=headers)
        content = response.content
        print(content)
        with open(path+'/' + '{}.jpg'.format(i), 'wb') as f:
            f.write(content)
            print("正在爬取第{}张图片".format(i))
path = r"C:\Users\Administrator\Pictures\Camera Roll"
if not os.path.exists(path):
    #如果不存在就自己生成一个
    os.mkdir(path)
bizhi(path,500)
