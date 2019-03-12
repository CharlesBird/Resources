# 返回一个可调用对象，该对象在其操作数上调用方法名称。 如果给出了额外的参数和/或关键字参数，它们也将被赋予该方法。
from operator import methodcaller

s = 'I am a good programmer.'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '/')
print(hiphenate(s))