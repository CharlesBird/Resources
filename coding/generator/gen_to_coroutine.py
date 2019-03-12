# 生成器是可以暂停的函数
# 获取生成器状态

import inspect

def gen_func():
    yield 1
    return '123'


if __name__ == '__main__':
    g = gen_func()
    print(inspect.getgeneratorstate(g))
    next(g)
    print(inspect.getgeneratorstate(g))
    try:
        next(g)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(g))