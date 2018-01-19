# 主流的单线程实现并发的几种方式
# asyncio
import requests
import time
import asyncio

url_list = [
    'http://www.baidu.com',
    'https://www.python.org',
    'http://www.cnblogs.com/',
    'https://www.tmall.com/',
    'https://www.jd.com/'
]

@asyncio.coroutine
def fetch_async(fn, *args):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, fn, *args)
    response = yield from future
    print(response.text)

"""asyncio+requests代码例子"""
def test():
    tasks = [
        fetch_async(requests.get, 'http://www.baidu.com'),
        fetch_async(requests.get, 'https://www.python.org'),
        fetch_async(requests.get, 'http://www.cnblogs.com/'),
        fetch_async(requests.get, 'https://www.tmall.com/'),
        fetch_async(requests.get, 'https://www.jd.com/')
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()



if __name__ == '__main__':
    start = time.time()
    test()
    end = time.time()
    print(end-start)