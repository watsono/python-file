# 1、导入webdriver

from selenium import webdriver
import time

# 2、调用环境变量指定的PhantomJs浏览器创建浏览器对象

# driver = webdriver.PhantomJs()

# 3、如果没有在环境变量执行的PhantomJs位置，需要手动加入

driver = webdriver.PhantomJS(
    executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")

# 4、请求页面
driver.get("https://www.baidu.com/")
print(driver.page_source)

# 5、截屏工具

driver.save_screenshot('01.png')
# with open('baidu.html','w',encoding='utf-8') as fp:
#    fp.write(driver.page_source)

# 6、模拟输入人名点击搜索
# 截屏
driver.save_screenshot('02.png')
# 输入胡歌
driver.find_element_by_id('kw').send_keys('手机')
driver.save_screenshot('03.png')

# 点击百度一下
driver.find_element_by_id('su').click()
# 留出充足时间等待响应
time.sleep(6)
driver.save_screenshot('04.png')
print(driver.title)