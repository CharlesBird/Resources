from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import platform
system = platform.system()
if system == 'Darwin':
    driver_path = './chromedriver_mac/chromedriver'
else:
    driver_path = './chromedriver_win/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')  # For Linux/Unix
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://cn.investing.com/currencies/usd-cny-historical-data')

n = 0
while True:
    n += 1
    element_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'leftColumn')))
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    last_value = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[1]").text
    diff = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[2]").text
    change_rate = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[4]").text
    timeStamp = element_div.find_element_by_xpath("//*[@class='bottom lighterGrayFont arial_11']/span[2]").get_attribute(
        'data-value')
    change_time = ''
    if timeStamp is not None:
        timeArray = time.localtime(int(timeStamp))
        change_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(last_value, diff, change_rate, change_time, now)
    if n >= 200:
        break
    time.sleep(50)

driver.quit()

