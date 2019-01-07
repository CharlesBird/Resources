import dis
import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


# print(dis.dis(foo))


foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


def gen_func():
    yield 1
    name = 'Charles'
    yield 2
    age = 50
    return 'Shanghai'


gen = gen_func()
print(dis.dis(gen))

print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)


from collections import UserList
