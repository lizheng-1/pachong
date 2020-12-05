import requests
from lxml import etree

url='https://sh.58.com/ershoufang/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}
page_test=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_test)

li_list=tree.xpath('//ul[@class="house-list-wrap"]/li')
fp=open('58.txt','w',encoding='utf-8')
for li in li_list:
    title=li.xpath('./div[2]/h2/a/text()')[0]
    print(title)
    fp.write(title+'\n')