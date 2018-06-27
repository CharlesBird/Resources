from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from pipelines import MongoPipeline

# 获取浏览器句柄
# 写入数据库
# 主函数


def get_chrome_driver(url):
    """
    获取浏览器句柄
    :param url:
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  # For Linux/Unix
    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url=url)
    return driver


def write_to_db(item):
    pipe = MongoPipeline('locolhost', 27017, 'exchange_rate', 'usd_cny_minute', 'zhc', 'zhc123456')
    pipe.process_item(item)
    return


def get_item(driver):
    element_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'leftColumn')))
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    last_value = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[1]").text
    diff = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[2]").text
    change_rate = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[4]").text
    timeStamp = element_div.find_element_by_xpath(
        "//*[@class='bottom lighterGrayFont arial_11']/span[2]").get_attribute(
        'data-value')
    change_time = ''
    if timeStamp is not None:
        timeArray = time.localtime(int(timeStamp))
        change_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return {'last_value': last_value, 'diff': diff, 'change_rate': change_rate, 'change_time': change_time, 'now_time': now}


def main():
    base_url = 'https://cn.investing.com/currencies/usd-cny-historical-data'
    driver = get_chrome_driver(base_url)
    # n = 0
    try:
        while True:
            item = get_item(driver)
            write_to_db(item)
            # if n >= 10:
            #     break
            # n += 1
            time.sleep(50)
    except Exception as e:
        raise e
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
