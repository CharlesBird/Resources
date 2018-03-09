from lazy import lazy


@lazy
def f(x):
    print('1111111111')
    return x

r = f('a')  # r 是一个lazy实例
print('2222222222222')
print(r)  # f 在这使用
print(r._func(*r._args))  # 这时才会打印f中的1111111111