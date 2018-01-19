# 主流的单线程实现并发的几种方式
# Twisted
import grequests
import time

request_list = [
    grequests.get('http://www.baidu.com'),
    grequests.get('https://www.python.org'),
    grequests.get('http://www.cnblogs.com/'),
    grequests.get('https://www.tmall.com/'),
    grequests.get('https://www.jd.com/')
]


"""grequests代码例子, 测试目前最快"""
def test():
    response_list = grequests.map(request_list)
    for response in response_list:
        print(response.text)


if __name__ == '__main__':
    start = time.time()
    test()
    end = time.time()
    print(end-start)