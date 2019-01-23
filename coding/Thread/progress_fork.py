import os
import time
pid = os.fork()
print("Charles")
if pid == 0:
    print("子进程: {}, 父进程: {}".format(os.getpid(), os.getppid()))
else:
    print("父进程: {}".format(os.getpid()))
time.sleep(2)