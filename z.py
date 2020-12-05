import requests
import re
import xlwt

xls = xlwt.Workbook()
sheet = xls.add_sheet("一流大学建设高校")
sheet.write(0,0,"学校")
sheet.write(0,1,"一流专业")


line = 1
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

myurl ="https://daxue.eol.cn/syl.shtml"

response = requests.get(url=myurl)
response.encoding = "utf-8"

School = re.findall(r'<th colspan="5">“双一流”建设学科名单</th>(.*?)<div class="top">高考工具箱</div>',
                          response.text, re.S)[0]

Schools= re.findall(r'<a target="_blank" href="http://gkcx.eol.cn/schoolhtm/schoolTemple/.*?">(.*?)</a></td>.*? align="left".*?>(.*?)</',School,re.S)



for school,TopClasses1 in Schools:
  TopClasses1 = re.split('、', TopClasses1)
  for topclass in TopClasses1:
    sheet.write(line, 0, school)
    sheet.write(line, 1, topclass)
    line += 1
xls.save('一流大学建设高校18.xls')