import requests
from lxml import etree
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
urls='https://blog.csdn.net/weixin_45755332?spm=1011.2124.3001.5113'
urls1 = "https://xiaobaibubai.blog.csdn.net/article/list/2"
url2 = "https://blog.csdn.net/qq_17623363/article/details/109190212"
i = 2
for n in range(50):
    s = requests.Session()
    response = s.get(url=url2, headers=headers)
    content = response.content

    page_test = requests.get(url=urls, headers=headers).text

    tree = etree.HTML(page_test)
    li_list = tree.xpath('//*[@id="articleMeList-blog"]/div[2]/div')
    for li in li_list:
        url = li.xpath('./h4/a/@href')
        name = li.xpath('./h4/a/text()')[1].strip()
        url = "".join(url)
        print(name,url,"\n")
        s = requests.Session()
        response = s.get(url=url,headers=headers)
        content = response.content
    time.sleep(60)
