from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path =  r'E:\百度云\啊发发\geckodriver.exe')
#把上述地址改成你电脑中geckodriver.exe程序的地址 #在虚拟浏览器中打开 Airbnb 页面
driver.get("https://zh.airbnb.com/s/Shenzhen--China/homes") #找到页面中所有的出租房
rent_list = driver.find_elements_by_css_selector('div._v721rv') #对于每一个出租房
for eachhouse in rent_list: #找到评论数量
    try:
        comment = eachhouse.find_element_by_css_selector ('span._69pvqtq')
        comment = comment.text
    except:
        comment = 0 #找到价格
    price = eachhouse.find_element_by_css_selector('div._v721rv')
    price = price.text.replace("每晚", "").replace("价格", ""). replace("\n", "") #找到名称
    print (comment, price)