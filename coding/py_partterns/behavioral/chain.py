"""责任链"""


import abc
import timeit


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if not res:
            self._successor.handle(request)

    @abc.abstractmethod
    def _handle(self, request):
        raise NotImplementedError("子类继承实现")


class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <= 10:
            print("request {} handled in hander 1".format(request))
            return True


class ConcreteHandler2(Handler):

    def _handle(self, request):
        if 10 < request <= 20:
            print("request {} handled in hander 2".format(request))
            return True


class ConcreteHandler3(Handler):

    def _handle(self, request):
        if 20 < request <= 30:
            print("request {} handled in hander 3".format(request))
            return True


class DefaultHandler(Handler):

    def _handle(self, request):
        print('end of chain, no handler for {}'.format(request))
        return True


class Client(object):

    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(DefaultHandler())))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


def coroutine(fn):
    """第二种方式"""
    def start(*args, **kwargs):
        cr = fn(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def coroutine1(target):
    while True:
        request = yield
        if 0 < request <= 10:
            print("request {} handled in hander 1".format(request))
        else:
            target.send(request)


@coroutine
def coroutine2(target):
    while True:
        request = yield
        if 10 < request <= 20:
            print("request {} handled in hander 2".format(request))
        else:
            target.send(request)


@coroutine
def coroutine3(target):
    while True:
        request = yield
        if 20 < request <= 30:
            print("request {} handled in hander 3".format(request))
        else:
            target.send(request)


@coroutine
def default_coroutine():
    while True:
        request = yield
        print('end of chain, no coroutine for {}'.format(request))


class ClientCoroutine(object):

    def __init__(self):
        self.target = coroutine1(coroutine2(coroutine3(default_coroutine())))

    def delegate(self, requests):
        for request in requests:
            self.target.send(request)


requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]


def test_c1():
    c1 = Client()
    c1.delegate(requests)


def test_c2():
    c2 = Client()
    c2.delegate(requests)


if __name__ == '__main__':
    t1 = timeit.Timer(test_c1)
    t2 = timeit.Timer(test_c2)
    print(t1.repeat(3, 1000), t2.repeat(3, 1000))