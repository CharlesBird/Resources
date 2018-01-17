from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
"""
selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）
executable_path 驱动路径
geckodriver.exe 需要下载安装浏览器启动驱动
"""

browser = webdriver.Firefox(executable_path="D:/Users/Charles/geckodriver.exe")
# browser.get("https://www.baidu.com/")
# print(browser.page_source)

browser.get("https://www.taobao.com/")

"""单个元素查找"""
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)

# input_first = browser.find_element(By.ID,"q")
# print(input_first)

"""多个元素查找"""
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)

# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis)

# """元素交互方法"""
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# """
# 将动作附加到动作链中串行执行
# 执行所有ActionChains类中存储的行为，可以理解为对整个操作的提交动作
# 鼠标双击操作
# """
# double_click = browser.find_element_by_xpath('//*[@id="J_SearchTab"]/ul/li[1]')
# print(double_click.location)
# ActionChains(browser).double_click(double_click).perform()
# time.sleep(2)

# """鼠标悬停"""
# attrible = browser.find_element_by_link_text("我的淘宝")
# ActionChains(browser).move_to_element(attrible).perform()
# time.sleep(5)
# browser.refresh()

# """Keys()类提供了键盘上按键的方法，send_keys()方法可以用来模拟键盘输入，还可以用来输入键盘上的按键、组合键。"""
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("pythonm")
# time.sleep(2)
# input_str.send_keys(Keys.BACK_SPACE)
# time.sleep(2)
# input_str.send_keys(Keys.SPACE)
# time.sleep(2)
# input_str.send_keys("selenium")
# time.sleep(2)
# input_str.send_keys(Keys.CONTROL, 'a')
# time.sleep(2)
# input_str.send_keys(Keys.CONTROL, 'x')
# time.sleep(2)
# input_str.send_keys(Keys.CONTROL, 'v')
# time.sleep(2)
# input_str.send_keys(Keys.ENTER)
# time.sleep(2)

# """执行JavaScript"""
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(5)
# browser.execute_script('alert("To Bottom")')

# """获取元素属性"""
# input_str = browser.find_element_by_id('q')
# print(input_str)
# print(input_str.get_attribute('class'))

# """获取文本值，ID，位置，标签名，高宽"""
# input_str = browser.find_element_by_id('q')
# print(input_str)
# print(input_str.text)
# print(input_str.id)
# print(input_str.location)
# print(input_str.tag_name)
# print(input_str.size)

# """浏览器前进后退"""
# browser.back()
# time.sleep(1)
# browser.forward()

# """cookie操作"""
# print(browser.get_cookies())
# browser.add_cookie({'name': '1016784928@qq.com', 'domain': 'www.taobao.com', 'value': 'charles'})
# print(browser.get_cookies())

browser.close()
