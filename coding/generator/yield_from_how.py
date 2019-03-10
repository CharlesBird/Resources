# python3引入async，await
# await 后面跟着是Awaitable类型对象，实现__await__方法
# 使用装饰器可以将生成器方法变成一个Awaitable类型
from collections import Awaitable
from types import coroutine

# async def dowloader(url):
#     return "1234"

@coroutine
def dowloader(url):
    yield 1

async def download_url(url):
    html = await dowloader(url)
    return html


if __name__ == '__main__':
    f = dowloader("www.baidu.com")
    # next(f)  # 不能使用这种
    print(f.send(None))