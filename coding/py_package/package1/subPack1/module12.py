# 在同内部中下导入模块
from . import module11


def funB():
    print('func in module12')
    module11.funA()


if __name__ == '__main__':
    funB()