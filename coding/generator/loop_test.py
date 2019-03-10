import asyncio
import time

# async def get_html(url):
#     print('start...')
#     # time.sleep(2)  # 不能使用正常的time.sleep
#     await asyncio.sleep(2)
#     print('end...')
#
#
# if __name__ == '__main__':
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html('www.baidu.com') for _ in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     # loop.run_until_complete(get_html("www.baidu.com"))
#     print(time.time() - start)



async def get_html(url):
    print('start...')
    await asyncio.sleep(2)
    print('end...')
    return "12345"


if __name__ == '__main__':
    # 获取协程的值
    # 两种方式：
    # 1、asyncio.ensure_future生成future对象
    # 2、loop.create_task生成
    # 其实ensure_future方法中调用了loop.create_task方法，所以最终返回结果是一样的
    start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_html("www.baidu.com"))
    loop.run_until_complete(future)
    print(future.result())
    # task = loop.create_task(get_html("www.baidu.com"))
    # loop.run_until_complete(task)
    # print(task.result())
    print(time.time() - start)