import requests
from lxml import etree
import os
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
i = 0
def bizhi(path,n):
    url = "http://www.netbian.com/e/search/result/index.php?page={}&searchid=54".format(n)
    page_test=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_test)
    li_list=tree.xpath('//*[@id="main"]/div[3]/ul/li')
    #print(li_list)
    for li in li_list:
        urlss = li.xpath('./a/@href')
        urls = "http://www.netbian.com"+"".join(urlss)
        print(urls)
        page_test1 = requests.get(url=urls, headers=headers).text
        tree1 = etree.HTML(page_test1)
        img_url = tree1.xpath('//*[@id="main"]/div[3]/div/p/a/img/@src')
        img_url = "".join(img_url)
        print(img_url)
        global i
        i += 1
        if img_url =='':
            continue
        s = requests.Session()
        response = s.get(url=img_url, headers=headers)
        content = response.content
        with open(path+'/' + '{}.jpg'.format(i), 'wb') as f:
            f.write(content)
            print("正在爬取第{}张图片".format(i))
path = r"F:\lzpython\爬虫\美女"
if not os.path.exists(path):
    #如果不存在就自己生成一个
    os.mkdir(path)
for y in range(1,13):
    bizhi(path,y)
