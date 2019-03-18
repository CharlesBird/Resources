# asynio没有提供http协议的接口
# aiohttp
import socket
from urllib.parse import urlparse
import asyncio


async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    reader, writer = await asyncio.open_connection(host, port=80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    async for line in reader:
        data = line.decode("utf8")
        all_lines.append(data)
    html_data = '\n'.join(all_lines)
    # print(html_data)
    return html_data

async def get_html():
    tasks = []
    for url in ['http://baidu.com', 'https://www.python.org', 'https://www.zhihu.com', 'https://www.dida365.com',
                'http://note.youdao.com', 'https://www.jetbrains.com', 'https://www.oracle.com/index.html']:
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        html = await task
        print(html)


if __name__ == '__main__':
    import time
    start = time.time()
    loop = asyncio.get_event_loop()
    # tasks = []
    # for url in ['http://baidu.com', 'https://www.python.org', 'https://www.zhihu.com', 'https://www.dida365.com',
    #             'http://note.youdao.com', 'https://www.jetbrains.com', 'https://www.oracle.com/index.html']:
    #     tasks.append(asyncio.ensure_future(get_url(url)))
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print(task.result())  # 等待所有访问完成后才打印出来
    # 访问一个成功就打印一个的方式
    loop.run_until_complete(get_html())
    print(time.time() - start)