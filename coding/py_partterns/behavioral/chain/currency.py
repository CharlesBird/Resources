import abc


class Handler(abc.ABC):

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        rs = self._handle(request)
        if not rs:
            self._successor.handle(request)

    @abc.abstractmethod
    def _handle(self, request):
        pass


class CNYHandler(Handler):

    def _handle(self, request):
        if request == 'CNY':
            print("人名币处理完成")
            return True


class USDHandler(Handler):

    def _handle(self, request):
        if request == 'USD':
            print("美元处理完成")
            return True

class EURHandler(Handler):

    def _handle(self, request):
        if request == 'EUR':
            print("欧元处理完成")
            return True


class UndefindHandler(Handler):

    def _handle(self, request):
        print("系统中无此%s币制处理能力，请添加" % request)
        return True


class Client(object):

    def __init__(self):
        self.handler = CNYHandler(USDHandler(EURHandler(UndefindHandler())))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


if __name__ == '__main__':
    requests = ['USD', 'CNY', 'JPY', 'EUR']
    c = Client()
    c.delegate(requests)