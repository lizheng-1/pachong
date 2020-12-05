import requests
import re
import xlwt

xls = xlwt.Workbook()
sheet = xls.add_sheet("一流大学建设高校")
sheet.write(0,0,"学校")
sheet.write(0,1,"专业")


line = 1
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

myurl ="https://daxue.eol.cn/syl.shtml"

response = requests.get(url=myurl)
response.encoding = "utf-8"

firstSchools = re.findall(r'<th colspan="5">“双一流”建设学科名单</th>(.*?)<div class="top">高考工具箱</div>',
                          response.text, re.S)[0]
reallFirstSchools = re.findall(r'<td width="150">([\u4e00-\u9fa5])(.*?)</td>',
                               firstSchools, re.S)
print(reallFirstSchools)
for school in reallFirstSchools:
    sheet.write(line, 0, school)
    line += 1
    print(line)
schools = re.findall(r'<th colspan="6">一流大学建设高校</th>(.*?)<div class="top">高考工具箱</div>',
                          response.text, re.S)[0]

reallSchools =re.findall(r'align="left".*?>(.*?)</' ,schools, re.S)

print(reallSchools)
line = 1
for school1 in reallSchools:
    sheet.write(line, 1, school1)
    line += 1
    print(line)
#exit()


# for i in range (len(reallFirstSchools)):

# for j in range (len(reallSchools)):
#     sheet.write(line,1,reallSchools)
#     line1 +=1
#     print(line)

xls.save('一流大学建设高校1.xls')
