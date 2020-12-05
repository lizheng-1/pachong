import re
import urllib.request

# 地址直接从浏览器拷过来
url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1600949887684_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E5%95%86%E9%93%BA%E7%89%8C"
# 这个步骤可以分为三步(最终获取的是该链接的所有源代码)
# 解析 urllib.request.urlopen(url)
# 获取 read()
# 转换编码 decode()
html = urllib.request.urlopen(url).read().decode("utf8")

# print(html)
# 通过正则表达式，来获取图片链接（步骤二.(4)）
html = re.findall('"thumbURL":"(.*?)"', html, re.S)
# print(html)

index = 0
# 保存图片的目录，注意目录不能是不存在的，否则会报错
localPath = r"F:\lzpython\爬虫\3"
# 设定只下载1000张，也可设得非常大，获取所有图片
while index < 1:
    for imgUrl in html:
        print('正在下载，第%d张：%s' % (index,imgUrl))
        # 将图片写入到本地
        urllib.request.urlretrieve(imgUrl, localPath + "/第%d.jpg" % index)
        index += 1
    # 这步得目的就是变更网页地址(通过 pn 关键字)，获取新的图片（步骤二.(2),(3)）
    url = re.sub("&pn=\d+", "&pn=%d" % index, url)
    print(url)
    html = urllib.request.urlopen(url).read().decode("utf8")
    html = re.findall('"thumbURL":"(.*?)"', html, re.S)
    print("+++++++len:", len(html))
