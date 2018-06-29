from pipelines import MongoPipeline
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def get_driver(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  # For Linux/Unix
    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)
    driver.implicitly_wait(1)
    driver.get(url=url)
    return driver


def get_item(driver):
    element_div = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'leftColumn')), message='Not found class=leftColumn div Node')
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    name = element_div.find_element_by_xpath("//*[@class='instrumentHead']/h1").text
    last_value = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[1]").text
    diff = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[2]").text
    change_rate = element_div.find_element_by_xpath("//*[@class='top bold inlineblock']/span[4]").text
    timeStamp = element_div.find_element_by_xpath("//*[@class='bottom lighterGrayFont arial_11']/span[2]").get_attribute(
        'data-value')
    change_time = ''
    if timeStamp is not None:
        timeArray = time.localtime(int(timeStamp))
        change_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    yesterday_close = element_div.find_element_by_xpath(
        "//*[@class='bottomText float_lang_base_1']/ul/li[1]/span[2]").text
    open_value = element_div.find_element_by_xpath("//*[@class='bottomText float_lang_base_1']/ul/li[2]/span[2]").text
    today_low = element_div.find_element_by_xpath(
        "//*[@class='bottomText float_lang_base_1']/ul/li[3]/span[2]/span[1]").text
    today_high = element_div.find_element_by_xpath(
        "//*[@class='bottomText float_lang_base_1']/ul/li[3]/span[2]/span[2]").text
    return {
        'name': name,
        'last_value': last_value,
        'diff': diff,
        'change_rate': change_rate,
        'change_time': change_time,
        'now_time': now,
        'yesterday_close': yesterday_close,
        'open_value': open_value,
        'today_low': today_low,
        'today_high': today_high
    }


def get_full_item_driver(url, driver=None):
    if driver is None:
        driver = get_driver(url=url)
    item = get_item(driver)
    values = item.values()
    full = all(values)
    while not full:
        driver.quit()
        time.sleep(60)
        new_driver = get_driver(url=url)
        new_item = get_item(new_driver)
        full = all(new_item.values())
        if full:
            driver = new_driver
            break
    return driver


def write_to_db(item):
    pipe = MongoPipeline('localhost', 27017, 'brent_oil', 'brent_oil_second', 'zhc', 'zhc123456')
    pipe.process_item(item)
    return


def main():
    base_url = 'https://cn.investing.com/commodities/brent-oil'
    driver = get_full_item_driver(url=base_url)
    try:
        while True:
            item = get_item(driver)
            write_to_db(item)
            time.sleep(0.5)
    except Exception as e:
        print('Error, %s' % e)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
