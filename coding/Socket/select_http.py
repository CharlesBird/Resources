import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()
# 使用select实现http请求，单线程模式
# windows下使用的select，linux/unix下使用的poll或者epoll
# 注意windows下select参数不能为空，循环调用回调函数时判断是否已经都处理完
class Fetcher(object):

    def connector(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

    def get_url(self, url):
        self.url = urlparse(url)
        self.host = self.url.netloc
        self.path = self.url.path
        if self.path == "":
            self.path = "/"
        self.data = b""

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)  # 非阻塞设置，不用等待client握手成功

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册到selector
        # self.client.fileno() 文件描述符
        selector.register(self.client.fileno(), EVENT_WRITE, self.connector)


def loop():
    # 事件循环，不停的请求socket的状态并调用对应的函数
    # 1、select本身是不支持register模式
    # 2、socket状态变化后的回调是由程序员完成的
    while True:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    fech = Fetcher()
    fech.get_url("https://www.baidu.com")
    loop()