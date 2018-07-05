from queue import Queue
import threading

q = Queue()
thread_id = 1


class Consume(threading.Thread):

    def __init__(self, name=None):
        global thread_id
        threading.Thread.__init__(self, name=name)
        self.name = name
        self.q = q
        self.Thread_id = thread_id
        thread_id = thread_id + 1

    def run(self):
        while True:
            try:
                task = self.q.get(block=True, timeout=1)
            except Exception:
                print('Thread',  self.Thread_id, 'end')
                break
            print("Starting ", self.Thread_id, self.name)

            print(task)
            self.q.task_done()
            print("Ending ", self.Thread_id)


class Productor(threading.Thread):

    def __init__(self, name, m, n):
        threading.Thread.__init__(self, name=name)
        self.name = name
        self.m = m
        self.n = n
        self.q = q

    def run(self):
        for i in range(self.m, self.n):
            self.q.put(i)
            print("Starting ", self.n, self.name)


p1 = Productor('Productor1', 0, 10)
p1.start()
p2 = Productor('Productor2', 10, 20)
p2.start()
p3 = Productor('Productor3', 20, 30)
p3.start()
p1.join()
p2.join()
p3.join()


worker1 = Consume('Consume1')
worker1.start()
worker2 = Consume('Consume2')
worker2.start()
worker3 = Consume('Consume3')
worker3.start()
q.join()
print("Exiting Main Thread")
