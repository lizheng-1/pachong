import requests
import re
import requests
from lxml import etree
import os
import xlwt
xls = xlwt.Workbook()
sheet = xls.add_sheet("一流大学建设高校")
sheet.write(0,0,"学校")
sheet.write(0,1,"专业")
line = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
myurl ="https://daxue.eol.cn/syl.shtml"
page_test = requests.get(url=myurl, headers=headers).text.encode("utf-8")
tree = etree.HTML(page_test,)
li_list = tree.xpath('/html/body/div[3]/div[2]/div[3]/table/tbody/tr')

for li in li_list:
    schools = li.xpath('./td/a/text()')
    print(schools)

