import multiprocessing
import time


def get_time(n):
    time.sleep(n)
    print("sub progress")
    return n


if __name__ == '__main__':
    # process = multiprocessing.Process(target=get_time, args=(2,))
    # process.start()
    # print(process.pid)
    # process.join()
    # print("main progress")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_time, args=(2,))
    #
    # pool.close()  # 先关闭进程池
    # pool.join()
    # print(result.get())

    # imap
    for result in pool.imap(get_time, [1, 5, 3]):
        print("time: {}".format(result))

    print("---------------------------")

    for result in pool.imap_unordered(get_time, [1, 5, 3]):
        print("time: {}".format(result))
