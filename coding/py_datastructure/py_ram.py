# Python 内存分配小知识
"""
Python 中的sys模块极为基础而重要，它主要提供了一些给解释器使用的变量，以及一些与解释器强交互的函数。

getsizeof()方法：
  该方法用于获取一个对象的字节大小
  它只计算直接占用的内存，而不计算对象内存所应用的内存
"""
import sys

a = [1, 2]
b = [a, a]

# a, b 都是两个元素，直接占用的大小相等
print(sys.getsizeof(a))  # 80
print(sys.getsizeof(b))  # 80
"""
说明： 一个静态创建的列表，如果只包含两个元素，那它自身占用的内存就是80字节，不管其他元素指向的对象是什么。
"""

# 1、空对象不是‘空’的
# 空对象是不是不占用内存呢？如果占内存，那占多少呢？为什么是这样分配？
print(sys.getsizeof(""))  # 49
print(sys.getsizeof([]))  # 64
print(sys.getsizeof(()))  # 48
print(sys.getsizeof(set()))  # 224
print(sys.getsizeof(dict()))  # 240
print(sys.getsizeof(1))  # 28
print(sys.getsizeof(True))  # 28
"""
排序： 基础数字<空元组<空字符串<空列表<空集合<空字典。
因为这些空对象都是容器，我们可以抽象地理解：它们的一部分内存用于创建容器的骨架、记录容器的信息（如引用次数，使用量信息等）、还有一部分内存则是预分配的。
"""

# 2、内存扩充不是均匀的
# 空对象并不为空，一部分原因是 Python 解释器为它们预分配了一些初始空间。在不超出初始内存的情况下，每次新增元素，就使用已有内存，因而避免了再去申请新的内存。
# 如果初始内存被分配完之后，新的内存是怎么分配的？
letters = "abcdefghijklmnopqrstuvwxyz"
a = []
for i in letters:
    a.append(i)
    print(f'{len(a)}, sys.getsizeof(a) = {sys.getsizeof(a)}')

b = set()
for j in letters:
    b.add(j)
    print(f'{len(b)}, sys.getsizeof(b) = {sys.getsizeof(b)}')

c = dict()
for k in letters:
    c[k] = k
    print(f'{len(c)}, sys.getsizeof(c) = {sys.getsizeof(c)}')
"""
结论：
  超额分配机制：申请新内存时并不是按需分配的，而是多分配一些，因此再添加少量元素时，不需要马上申请新内存
  非均匀分配机制：三类对象申请新内存的，频率是不同的，而同一类对象每次超额分配的内存并不是均匀的，而是逐渐扩大的
"""

# 3、列表不等于列表
# 静态创建的对象是否也有这样的分配机制呢？它跟动态扩容比，是否有区别？
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5}
dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(sys.getsizeof(set_1))  # 224
print(sys.getsizeof(set_2))  # 736
print(sys.getsizeof(dict_1))  # 240
print(sys.getsizeof(dict_2))  # 368
"""
可以看出：在元素个数相等时，静态创建的集合/字段所占的内存和动态扩容时完全一样
"""
list_1 = [1, 2]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3, 4, 5]
list_4 = [1, 2, 3, 4, 5, 6]
print(sys.getsizeof(list_1))  # 80
print(sys.getsizeof(list_2))  # 88
print(sys.getsizeof(list_3))  # 104
print(sys.getsizeof(list_4))  # 112
"""
对比区别：在元素个数相等时，静态创建的列表所占用的内存有可能小于动态扩容时的内存。
也就是说，这两种列表看似相同，实际却不同！列表不等于列表！
"""

# 4、削减元素并不会释放内存
# 扩充可变对象时，可能会申请新的内存。反过来缩减可变对象，减掉一些元素后，新申请的内存是否会自动回收掉？
a = [1, 2, 3, 4]
print(sys.getsizeof(a))  # 80
a.append(5)
print(sys.getsizeof(a))  # 128
a.pop()
print(sys.getsizeof(a))  # 128
"""
如上所示，列表在一扩一缩后，虽然回到了原样，但是所占用的内存空间 可没有自动释放。其它可变对象同理。
"""

# 5、空字典不等于空字典
# 使用 pop 方法，之后缩减可变对象中的元素，但不会释放已申请的内存空间。
# clear()，清空可变对象的所有元素
a = [1, 2, 3]
b = {1, 2, 3}
c = {'a': 1, 'b': 2, 'c': 3}
print(sys.getsizeof(a))  # 88
print(sys.getsizeof(b))  # 224
print(sys.getsizeof(c))  # 240
a.clear()
b.clear()
c.clear()
print(sys.getsizeof(a))  # 64
print(sys.getsizeof(b))  # 224
print(sys.getsizeof(c))  # 72
"""
列表与字典 清空后内存比空的少了
"""