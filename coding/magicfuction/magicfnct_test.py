"""基本魔法算法，及属性操作，__delete__属性用法不理解"""
class MagicClass(object):

    def __init__(self, name, birth, namer=None, origin=None):
        self.name = name
        self.birth = birth
        self.namer = namer
        self.origin = origin

    def __del__(self):
        print(self, 'Del')

    def __call__(self, name, birth):
        print('Call')
        return name + '-' + birth

    def __len__(self):
        print('Len')
        return len(self.name)

    def __repr__(self):
        print('repr')
        return '%s.%s.%s.%s' % (self.name, self.birth, self.namer, self.origin)

    def __str__(self):
        print('Str')
        return self.name

    def __bytes__(self):
        print('bytes')
        return bytes(self.name, encoding='utf-8')

    def __hash__(self):
        print('Hash')
        return hash(self.name)

    def __bool__(self):
        print('Bool')
        if self.name:
            return True
        else:
            return False

    def __format__(self, format_spec):
        print('format', format_spec)
        return format_spec + self.name

    def __getattr__(self, item):
        print('getattr')
        return item + " from getattr"

    def __getattribute__(self, item):
        print('getattribute')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('setattr')
        # super(MagicClass, self).__setattr__(key, value)
        if key not in ('name', 'birth', 'namer', 'origin'):
            value = str(value) + ' from setattr'
            # setattr(self, key, value)
        return super(MagicClass, self).__setattr__(key, value)

    def __delattr__(self, item):
        """del mc.name触发delattr"""
        print('delattr')
        self.__dict__.pop(item)

    def __dir__(self):
        print('dir')
        return super(MagicClass, self).__dir__()

    def __get__(self, instance, owner):
        """如果class定义了它，则这个class为discriptor，通过自己访问是不会触发__get__，而触发__call__，只有descriptor作为其它类的属性才有意义"""
        print('get', self, instance, owner)
        return self

    def __set__(self, instance, value):
        print('set', self, instance, value)
        return object.__set__(instance, value)

    def __delete__(self, instance):
        print('delete', instance)
        return object.__delete__(instance)


mc = MagicClass('大变活人', '2018', 'Charles', 'Shanghai')
print(mc('隐身无敌', '2018'))
print(mc.name, mc.origin)
print('###########基本魔法方法##################')
print(len(mc), repr(mc), str(mc), bytes(mc), hash(mc), bool(mc), format(mc, '什么魔术？'), '\n')
print('###########有关属性##################')
print('-----getattr,getattribute--------------')
print(mc.x, mc.name)
print('-----setattr--------------')
mc.xatt = '123'
print(mc.xatt)
print('-----delattr--------------')
del mc.name  # 触发delattr
print(mc.name)
print('-----dir--------------')
print(dir(mc))
print('-----get--------------')
class TestGet(object):
    t_mc = MagicClass('天火', '2018')
tg = TestGet()
print(tg.t_mc)
print(tg.t_mc.name)
print('-----set--------------')
class TestSet(object):
    t_mc2 = MagicClass('陨石', '2018')
ts = TestSet()
print(ts.t_mc2)
TestSet.t_mc2 = 'Hello2'
print('result', TestSet.t_mc2, ts.t_mc2)
print('-----delete--------------')
# print(tg.t_mc.__dict__)
# del tg.t_mc.name
# print(tg.t_mc.__dict__)

