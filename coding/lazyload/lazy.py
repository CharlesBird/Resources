# -*- encoding: utf-8 -*-
"""构造延迟加载对象"""
class _LazyWrapper:
    """延迟封装类"""
    def __init__(self, f, args, kwargs):
        self._override = True
        self._isset = False
        self._value = None
        self._func = f
        self._args = args
        self._kwargs = kwargs
        self._override = False

    def _checkset(self):
        if not self._isset:
            self._override = True
            self._value = self._func(*self._args, **self._kwargs)
            self._isset = True
            self._checkset = lambda: True
            self._override = False

    def __getattr__(self, item):
        if self.__dict__['_override']:
            return self.__dict__[item]
        self._checkset()
        return self._value.__getattribute__(item)

    def __setattr__(self, key, value):
        if key == '_override' or self._override:
            self.__dict__[key] = value
            return
        self._checkset()
        setattr(self._value, key, value)
        return


def lazy(f):
    """装饰器函数，返回延迟加载类对象"""
    def newf(*args, **kwargs):
        return _LazyWrapper(f, args, kwargs)
    return newf


class LazyProxy(object):
    def __init__(self, cls, *args, **kwargs):
        self.__dict__['_cls'] = cls
        self.__dict__['_args'] = args
        self.__dict__['_kwargs'] = kwargs
        self.__dict__['_obj'] = None

    def __getattr__(self, item):
        if self.__dict__['_obj'] is None:
            self._init_obj()
        return getattr(self.__dict__['_obj'], item)

    def __setattr__(self, key, value):
        if self.__dict__['_obj'] is None:
            self._init_obj()
        setattr(self.__dict__['_obj'], key, value)

    def _init_obj(self):
        self.__dict__['_obj'] = object.__new__(self.__dict__['_cls'])
        self.__dict__['_obj'].__init__(*self.__dict__['_args'], **self.__dict__['_kwargs'])


class LazyInit(object):
    def __new__(cls, *args, **kwargs):
        return LazyProxy(cls, *args, **kwargs)
