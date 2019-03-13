# 协程结合多线程的使用
import asyncio
from concurrent.futures import ThreadPoolExecutor
import socket
from urllib.parse import urlparse


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)  # 非阻塞设置，不用等待client握手成功
    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass



    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)


if __name__ == '__main__':
    import time
    start = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for url in ['http://baidu.com', 'https://www.python.org', 'https://www.zhihu.com', 'https://www.dida365.com',
                'http://note.youdao.com', 'https://www.jetbrains.com', 'https://www.oracle.com/index.html', 'http://google.com']:
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)