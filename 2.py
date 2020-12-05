from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.airbnb.cn/s/Shenzhen--China?page=1')

rent_list = driver.find_elements_by_css_selector("div._z5ixr97")
i = 1
for eachhouse in rent_list:
    # 获取名称
    name = eachhouse.find_element_by_css_selector("div._qrfr9x5")
    name = name.text
    # 获取价格
    price = eachhouse.find_element_by_css_selector("div._59f9ic")
    price = price.text[2:]
    # 获取房屋信息
    detail = eachhouse.find_element_by_css_selector("div._1etkxf1")
    detail = detail.text
    # 获取评价数
    comment = eachhouse.find_element_by_css_selector("span._69pvqtq")
    comment = comment.text
    # 最后打印信息
    print('(' + str(i) + ')' + name + price + '\n'
          + detail + '\n' + comment)
    i=i+1
