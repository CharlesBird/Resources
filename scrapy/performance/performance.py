import requests
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

url_list = [
    'http://www.baidu.com',
    'https://www.python.org',
    'http://www.cnblogs.com/',
    'https://www.tmall.com/',
    'https://www.jd.com/'
]

def cal_time(fn):
    def _cal_time(*args, **kwargs):
        total = 0.0
        for i in range(10):
            start = time.time()
            fn(*args, **kwargs)
            end = time.time()
            total += (end-start)
        print(total/10)
    return _cal_time


"""单线程"""
@cal_time
def test1():
    for url in url_list:
        result = requests.get(url)
        return result.text


def fetch_request(url):
    result = requests.get(url)
    return result.text

"""线程池"""
@cal_time
def test2():
    pool = ThreadPoolExecutor(5)
    for url in url_list:
        pool.submit(fetch_request, url)
    pool.shutdown()


"""进程池"""
@cal_time
def test3():
    pool = ProcessPoolExecutor(5)
    for url in url_list:
        pool.submit(fetch_request, url)
    pool.shutdown()


def fetch_async(url):
    response = requests.get(url)
    return response

def callback(future):
    print(future.result().text)


"""多线程+回调函数"""
@cal_time
def test4():
    pool = ThreadPoolExecutor(5)
    for url in url_list:
        p = pool.submit(fetch_async, url)
        p.add_done_callback(callable)
    pool.shutdown()


"""多进程+回调函数"""
@cal_time
def test5():
    pool = ProcessPoolExecutor(5)
    for url in url_list:
        p = pool.submit(fetch_async, url)
        p.add_done_callback(callable)
    pool.shutdown()


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()