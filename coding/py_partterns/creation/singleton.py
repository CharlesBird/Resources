"""单例模式"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


if __name__ == '__main__':
    class TestSingleton(Singleton):

        def __init__(self, a):
            self.a = a

        def __str__(self):
            return self.a

    ts1 = TestSingleton('asd')
    print(id(ts1), ts1)
    ts2 = TestSingleton('dfg')
    print(id(ts2), ts2)
    print(id(ts1), ts1)