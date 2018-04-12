from test1 import Test1


class Test2(object):

    def __init__(self, c):
        self._c = c

    def uid(self):
        return self._c.s


class Test3(object):
    def __init__(self, c):
        self._c = c

    def uid(self):
        return self._c.s


if __name__ == '__main__':
    t1 = Test2(Test1('名称1', 1))
    t2 = Test2(Test1('名称2', 2))
    t3 = Test3(Test1('名称3', 3))


    print(t1._c.name, id(t1._c), t1.uid())
    print(t2._c.name, id(t2._c), t2.uid())
    print(t3._c.name, id(t3._c), t3.uid())