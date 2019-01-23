import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import time
# 1、多进程对于消耗cpu的操作，计算


def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def random_sleep(n):
    time.sleep(n)
    return n


def test_progress():
    with ProcessPoolExecutor(3) as execute:
        all_task = [execute.submit(fib, (num)) for num in range(20, 30)]
        for future in as_completed(all_task):
            data = future.result()
            print("result: {}".format(data))


def test_thread():
    with ThreadPoolExecutor(3) as execute:
        all_task = [execute.submit(fib, (num)) for num in range(20, 30)]
        for future in as_completed(all_task):
            data = future.result()
            print("result: {}".format(data))


def test_progress2():
    with ProcessPoolExecutor(3) as execute:
        all_task = [execute.submit(random_sleep, (num)) for num in [2]*30]
        for future in as_completed(all_task):
            data = future.result()
            print("result: {}".format(data))


def test_thread2():
    with ThreadPoolExecutor(3) as execute:
        all_task = [execute.submit(random_sleep, (num)) for num in [2]*30]
        for future in as_completed(all_task):
            data = future.result()
            print("result: {}".format(data))


if __name__ == '__main__':
    import timeit
    # t1 = timeit.Timer(test_progress)
    # t2 = timeit.Timer(test_thread)
    # print(t1.repeat(3, 100), t2.repeat(3, 100))
    t1 = timeit.Timer(test_progress2)
    t2 = timeit.Timer(test_thread2)
    print(t1.repeat(3, 100), t2.repeat(3, 100))