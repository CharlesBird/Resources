# from queue import Queue
# 多进程中不能使用上面的Queue
# 使用multiprocessing中的Queue
from multiprocessing import Process, Queue, Pool, Manager, Pipe
import time


# def producer(queue):
#     queue.put('123')
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == '__main__':
#     queue = Queue(10)
#     pro = Process(target=producer, args=(queue,))
#     con = Process(target=consumer, args=(queue,))
#     pro.start()
#     con.start()
#     pro.join()
#     pro.join()


# 共享全局变量，多进程不能使用
# def producer(a):
#     a += 1
#     time.sleep(2)
#
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
#
# if __name__ == '__main__':
#     a = 1
#     pro = Process(target=producer, args=(a,))
#     con = Process(target=consumer, args=(a,))
#     pro.start()
#     con.start()
#     pro.join()
#     pro.join()


# multiprocessing中的Queue不能用于Pool中
# 使用Manager中的Queue
# def producer(queue):
#     queue.put('123')
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == '__main__':
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#     pool.close()
#     pool.join()


# def producer(pipe):
#     pipe.send('123')
#     time.sleep(2)
#
#
# def consumer(pipe):
#     time.sleep(2)
#     data = pipe.recv()
#     print(data)
#
#
# if __name__ == '__main__':
#     recev_pipe, send_pipe = Pipe()
#     pro = Process(target=producer, args=(send_pipe,))
#     con = Process(target=consumer, args=(recev_pipe,))
#     pro.start()
#     con.start()
#     pro.join()
#     pro.join()


# 共享内存，比如：Manager中dict
def add_data(d, k, v):
    d[k] = v

if __name__ == '__main__':
    d = Manager().dict()
    progress1 = Process(target=add_data, args=(d, 'a', '123'))
    progress2 = Process(target=add_data, args=(d, 'b', '234'))
    progress1.start()
    progress2.start()
    progress1.join()
    progress2.join()
    print(d)