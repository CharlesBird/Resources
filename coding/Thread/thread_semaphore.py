# 用于控制进入数量的锁

import threading
import time


class HtmlSpider(threading.Thread):

    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text")
        self.sem.release()


class ProducerUrl(threading.Thread):

    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    producer = ProducerUrl(sem)
    producer.start()
    from queue import Queue