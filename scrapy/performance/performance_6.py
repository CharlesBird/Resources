# 主流的单线程实现并发的几种方式
# tornado

from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop
import time


"""tornado代码例子"""
def handle_response(response):
    if response.error:
        print("Error:", response.error)
    else:
        print(response.body)


def func():
    url_list = [
        'http://www.baidu.com',
        'https://www.python.org',
        'http://www.cnblogs.com/',
        'https://www.tmall.com/',
        'https://www.jd.com/'
    ]
    for url in url_list:
        print(url)
        http_client = AsyncHTTPClient()
        http_client.fetch(HTTPRequest(url), handle_response)


if __name__ == '__main__':
    ioloop.IOLoop.current().add_callback(func)
    ioloop.IOLoop.current().start()