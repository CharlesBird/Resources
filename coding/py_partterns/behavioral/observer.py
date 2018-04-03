"""观察者模式，当对象发生变化时，依赖它的对象得到通知并更新"""


class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer(object):
    def update(self, subject):
        print('HexViewer: Subject %s has data 0x%x' % (subject.name, subject.data))


class DecimalViewer(object):

    def update(self, subject):
        print('DecimalViewer: Subject %s has data %d' % (subject.name, subject.data))


def main():
    d1 = Data('data 1')
    d2 =Data('data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    d1.attach(view1)
    d1.attach(view2)
    d2.attach(view2)
    d2.attach(view1)

    print("setting Data 1 = 10")
    d1.data = 10
    print("Setting Data 2 = 15")
    d2.data = 15
    print("Setting Data 1 = 3")
    d1.data = 3
    print("Setting Data 2 = 5")
    d2.data = 5
    print("Detach HexViewer from data1 and data2.")
    d1.detach(view2)
    d2.detach(view2)
    print("Setting Data 1 = 10")
    d1.data = 10
    print("Setting Data 2 = 15")
    d2.data = 15


if __name__ == '__main__':
    main()