# python3.3新增加

from itertools import chain

list1 = [1,2,3]
dict1 = {
    'name': 'zhangsan',
    'age': 34,
    'addr': 'shanghai'
}

# yield from 后面跟着是可迭代对象
def my_chain(*args, **kwargs):
    for l in args:
        yield from l

for i in my_chain(list1, dict1):
    print(i)


def g1(gen):
    yield from gen


def main():
    # 1、main调用g1（委托生成器）gen是子生成器
    # 2、yield from会在调用方与子生成器之间创建一个双向通道
    g = g1()
    g.send(None)