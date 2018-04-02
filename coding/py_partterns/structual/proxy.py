"""代理模式"""


import time


class SalesManager(object):

    def talk(self):
        print("Sales manager ready to talk.")


class Proxy(object):

    def __init__(self):
        self.busy = "No"
        self.sales = None

    def talk(self):
        print("Proxy checking for SalesManager availability.")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy.")


class NoTalkProxy(Proxy):

    def talk(self):
        print("Proxy checking for SalesManager availability.")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you, whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = "Yes"
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()