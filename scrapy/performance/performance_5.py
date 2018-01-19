# 主流的单线程实现并发的几种方式
# Twisted

# getPage相当于requets模块，defer特殊的返回值，rector是做事件循环
from twisted.web.client import getPage, defer
from twisted.internet import reactor
import time


"""twisted代码例子, 单线程最快"""
def all_done(arg):
    reactor.stop()

def callback(contents):
    print(contents)

deferred_list = []

url_list = [
    'http://www.baidu.com',
    'https://www.python.org',
    'http://www.cnblogs.com/',
    'https://www.tmall.com/',
    'https://www.jd.com/'
]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(callback)
    deferred_list.append(deferred)
#这里就是进就行一种检测，判断所有的请求是否执行完毕
dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

if __name__ == '__main__':
    start = time.time()
    reactor.run()
    end = time.time()
    print(end-start)
