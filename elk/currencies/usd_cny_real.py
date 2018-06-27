from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')  # For Linux/Unix
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://cn.investing.com/currencies/usd-cny-historical-data')

n = 0
while True:
    n += 1
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    last_value = driver.find_element_by_xpath("//*[@class='top bold inlineblock']/span[1]").text
    diff = driver.find_element_by_xpath("//*[@class='top bold inlineblock']/span[2]").text
    change_rate = driver.find_element_by_xpath("//*[@class='top bold inlineblock']/span[4]").text
    timeStamp = driver.find_element_by_xpath("//*[@class='bottom lighterGrayFont arial_11']/span[2]").get_attribute(
        'data-value')
    change_time = ''
    if timeStamp is not None:
        timeArray = time.localtime(int(timeStamp))
        change_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(last_value, diff, change_rate, change_time, now)
    if n >= 200:
        break
    time.sleep(0.5)

driver.quit()

