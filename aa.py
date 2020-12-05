# import requests
# import re
# import xlwt
#
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
# }
# #爬取网址
# myurl ="https://daxue.eol.cn/syl.shtml"
#
# response = requests.get(url=myurl)
# response.encoding = "utf-8"
# #r''
# firstSchools = re.findall(r'<th colspan="5">“双一流”建设学科名单</th>(.*?)<div class="top">高考工具箱</div>',
#                           response.text, re.S)[0]
# reallFirstSchools = re.findall(r'<a target="_blank" href="http://gkcx.eol.cn/schoolhtm/schoolTemple/.*?">(.*?)</a>',
#                                firstSchools, re.S)
# # print(reallFirstSchools)
#
# schools = re.findall(r'<th colspan="5">“双一流”建设学科名单</th>(.*?)<div class="top">高考工具箱</div>',
#                           response.text, re.S)[0]
#
# reallSchools =re.findall(r'align="left".*?>(.*?)</' ,schools, re.S)
#
# xls = xlwt.Workbook()
# sheet = xls.add_sheet("一流大学建设高校")
# sheet.write(0,0,"学校")
# sheet.write(0,1,"一流专业")
# line = 1
# for s in range(len(reallFirstSchools)):
#     school1 = re.split('、',reallSchools[s])
#     for i in range(len(school1)):
#          print(reallFirstSchools[s],school1[i])
#          sheet.write(line, 0, reallFirstSchools[s])
#          sheet.write(line, 1, school1[i])
#          line += 1
# xls.save('一流大学建设高校0.xls')
import pandasql


import pandas as pd
from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print( pysqldf(sql))

