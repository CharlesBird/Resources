"""测试代理类延迟加载方式"""
from lazy import LazyInit

class A(LazyInit):
    def __init__(self, x):
        print('init A')
        self.x = x


a = A(1)  # A实例化的时候没有打印init A
print("Start")
print(a.x)  # 当调用属性的时候打印了，说明调用属性的时候A开始实例化