"""
1、__new__一个对象实例化的时候所调用的第一个方法
2、它的第一个参数是这个类，其他参数是用来直接传递给__init__方法
3、__new__决定是否使用该__init__方法，因为__new__可以调用其他类的构造方法或者直接返回别的实例对象作为本例的实例，如果__new__没有返回实例对象，则__init__不会被调用
4、__new__主要用于继承一个不可变类型比如tuple或者string
"""
# 通过new函数创建元类的

class Author(type):

    def __new__(cls, name, bases, attrs):
        attrs['__author__'] = 'Charles'
        return type.__new__(cls, name, bases, attrs)


class Blog(metaclass=Author):
    pass


print(Blog.__author__)
b = Blog()
print(b.__author__)


# 通过元类创建单例模式

class Singleton(type):

    def __new__(cls, name, bases, attrs):
        attrs['instance'] = None
        return super(Singleton, cls).__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class Foo(metaclass=Singleton):
    pass


f1 = Foo()
f2 = Foo()
print(id(f1), id(f2))



# 通过元类修改类属性名称，比如:my_属性

class Extend(type):

    def __new__(cls, name, bases, attrs):
        available_attrs = [(name, value) for name, value in attrs.items() if not name.startswith('__')]
        new_attrs = dict(('my_' + name, value)for name, value in available_attrs)
        return type.__new__(cls, name, bases, new_attrs)


class Bar(metaclass=Extend):
    name = 'Charles'
    age = '28'

b = Bar()
print(b.my_name, b.my_age)
