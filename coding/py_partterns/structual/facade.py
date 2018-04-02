"""外观模式"""

import time
SLEEP = 0.5


class TC1(object):

    def run(self):
        print("测试类1")
        time.sleep(SLEEP)
        print("启动")
        time.sleep(SLEEP)
        print("运行")
        time.sleep(SLEEP)
        print("停止")
        time.sleep(SLEEP)
        print("结束\n")


class TC2(object):

    def run(self):
        print("测试类2")
        time.sleep(SLEEP)
        print("启动")
        time.sleep(SLEEP)
        print("运行")
        time.sleep(SLEEP)
        print("停止")
        time.sleep(SLEEP)
        print("结束\n")


class TC3(object):

    def run(self):
        print("测试类3")
        time.sleep(SLEEP)
        print("启动")
        time.sleep(SLEEP)
        print("运行")
        time.sleep(SLEEP)
        print("停止")
        time.sleep(SLEEP)
        print("结束\n")


class TestRunner(object):

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def run_all(self):
        [i.run() for i in self.tests]


if __name__ == '__main__':
    tr = TestRunner()
    tr.run_all()