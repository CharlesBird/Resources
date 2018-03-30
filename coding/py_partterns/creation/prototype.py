"""原型模式，clone一份已存在对象"""


class Prototype(object):
    """原型复制功能"""

    value = 'default'

    def clone(self, **attr):
        obj = self.__class__()
        obj.__dict__.update(attr)
        return obj


class PrototypeDispatcher(object):
    """存储复制的对象"""

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]


def main():
    proto = Prototype()
    protodisp = PrototypeDispatcher()
    d = proto.clone()
    a = proto.clone(value='valueA', category='A')
    b = proto.clone(value='valueB', is_checked=True)
    protodisp.register_object('objecta', a)
    protodisp.register_object('objectb', b)
    protodisp.register_object('default', d)
    print([{k: obj.value} for k, obj in protodisp.get_objects().items()])


if __name__ == '__main__':
    main()