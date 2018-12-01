from numbers import Number


class IntegerField(object):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, Number):
            raise ValueError('请输入数字类型')
        self.value = value
        return

    def __delete__(self, instance):
        pass


class NoneDataField(object):
    def __get__(self, instance, owner):
        return self.value


class User(object):
    age = IntegerField()
    # age = NoneDataField()
    # age = 1


"""
如果user是某个类的实例，user.age(等价于getattr(user, 'age'))，
首先调用__getattribute__方法。如果类中定义了__getattr__，
调用__getattribute__时抛出异常AttributeError时调用__getattr__，
而对于属性描述符__get__的调用，则发生在__getattribute__内部。
那么user.age顺序如下：
1、如果 age 出现在User或者基类__dict__中，且age是 data descriptor，则调用__get__方法，否则
2、如果 age 出现在user.__dict__中，直接返回结果user.__dict__['age']，否则
3、如果 age 出现在User或者基类__dict__中
3.1、如果 age 是non-data descriptor，则调用__get__方法，否则
3.2、返回__dict__['age']
4、如果User有__getattr__方法，调用__getattr__，否则
5、抛出异常AttributeError
"""


if __name__ == '__main__':
    user = User()
    user.age = 20
    user.__dict__['age'] = 34
    print(user.__dict__)
    print(user.age)