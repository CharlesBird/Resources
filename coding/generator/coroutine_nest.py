# 怎么关闭loop的
import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

# async def get_html(sleep_times):
#     print("Start get html")
#     await asyncio.sleep(sleep_times)
#     print("Get html success.")
#
# if __name__ == '__main__':
#     task1 = get_html(2)
#     task2 = get_html(3)
#     task3 = get_html(4)
#     tasks = [task1, task2, task3]
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         all_tasks = asyncio.Task.all_tasks()
#         for task in all_tasks:
#             print("cancel task")
#             print(task.cancel())
#     finally:
#         loop.stop()
#         loop.run_forever()  # 注意调用这个，去掉这个会有问题
#         loop.close()


# 协程里嵌套协程，注意运行时序图
async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()