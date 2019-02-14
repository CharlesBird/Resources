# 1、主线程中可以获取某个线程的状态或者某个任务的状态，以及返回值
# 2、当一个线程完成的时候主线程能立即知道
# 3、futures可以让主线程和多进程编码接口一致
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED, Future
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# task1 = executor.submit(get_html, (2))  # 返回结果非阻塞
# task2 = executor.submit(get_html, (3))
# task3 = executor.submit(get_html, (4))
#
# print(task1.done())
# print(task2.cancel())
# print(task3.cancel())  # 执行中或者执行完成的无法取消，返回False
# time.sleep(3)
# print(task3.done())
#
# print(task1.result())  # 返回结果阻塞的

urls = [3, 2, 6, 4, 7]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} url".format(data))

# for data in executor.map(get_html, urls):
#     print("get {} url".format(data))