import requests
from lxml import etree
import os
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
i = 0
first = "https://www.doutula.com/article/list/?page=2"
page_test = requests.get(url=first, headers=headers).text
tree = etree.HTML(page_test)
divss = tree.xpath('//*[@id="home"]/div/div[2]')
for as1 in divss:
    url1 = as1.xpath('./a/@href')
    name = as1.xpath('./a/div[1]/text()')
    url1 = "".join(url1)

    page_test1 = requests.get(url=url1, headers=headers).text
    tree1 = etree.HTML(page_test1)
    divs1 = tree1.xpath('./html/body/div[2]/div[1]/div/div[2]/li/div[2]')
    print(divs1)
    for as2 in divs1:
        print(as2)
        # url2 = as2.xpath('./div[1]/table/tbody/tr[1]/td/a/@href')
        url2 = as2.xpath('./div[1]/table/tbody/tr[1]/td/a/img/@src')
        print(url2)
