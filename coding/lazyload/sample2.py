from lazy import lazy
import time


def show(v):
    print('show() init + print')
    s = str(v)
    print('show() v: ' + s)
    print('show() done')


@lazy
def st():
    print('return 3')
    return 3


v = st()
show(v)