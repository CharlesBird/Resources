"""享元模式， 避免相同对象的创建，减少内存占用"""


import weakref


class Card(object):

    _CardPool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value+suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value+suit] = obj
            obj.value = value
            obj.suit = suit
        return obj

    def __str__(self):
        return "Card: %s, %s" % (self.value, self.suit)


if __name__ == '__main__':
    c1 = Card('10', 'f')
    c2 = Card('10', 'f')
    print(c1, c2)
    print(id(c1), id(c2))
    print(c1 == c2, c1 is c2)

    c1.temp = None
    c3 = Card('10', 'f')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None
    c3 = Card('10', 'f')
    print(hasattr(c3, 'temp'))