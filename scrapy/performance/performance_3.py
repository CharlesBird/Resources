# 主流的单线程实现并发的几种方式
# gevent
import requests
import time
import gevent
from gevent.pool import Pool
# from gevent import monkey
# monkey.patch_all()

url_list = [
    'http://www.baidu.com',
    'https://www.python.org',
    'http://www.cnblogs.com/',
    'https://www.tmall.com/',
    'https://www.jd.com/'
]

def fetch_async(method, url):
    response = requests.request(method=method, url=url)
    print(response.text)

"""gevent+requests代码例子"""
def test():
    gevent.joinall([
        gevent.spawn(fetch_async, method='get', url='http://www.baidu.com'),
        gevent.spawn(fetch_async, method='get', url='https://www.python.org'),
        gevent.spawn(fetch_async, method='get', url='http://www.cnblogs.com/'),
        gevent.spawn(fetch_async, method='get', url='https://www.tmall.com/'),
        gevent.spawn(fetch_async, method='get', url='https://www.jd.com/')
    ])

def test2():
    pool = Pool(None)
    gevent.joinall([
        pool.spawn(fetch_async, method='get', url='http://www.baidu.com'),
        pool.spawn(fetch_async, method='get', url='https://www.python.org'),
        pool.spawn(fetch_async, method='get', url='http://www.cnblogs.com/'),
        pool.spawn(fetch_async, method='get', url='https://www.tmall.com/'),
        pool.spawn(fetch_async, method='get', url='https://www.jd.com/')
    ])

if __name__ == '__main__':
    start = time.time()
    test2()
    end = time.time()
    print(end-start)