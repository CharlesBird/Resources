"""备忘录"""


from copy import copy, deepcopy


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return restore


class Transaction(object):

    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional(object):

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e
        return transaction


class Numobj(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '<%s, %s>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '111'
        self.increment()


if __name__ == '__main__':
    num_obj = Numobj(-1)
    print((num_obj))

    a_trasaction = Transaction(True, num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        a_trasaction.commit()
        print('--commited')

        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x'
        print(num_obj)
    except Exception as e:
        a_trasaction.rollback()
        print('--rollback')
    print(num_obj)

    print('--now do stuff..')
    try:
        num_obj.do_stuff()
    except Exception as e:
        print('--doing stuff failed')
        import sys
        import traceback
        traceback.print_exc(file=sys.stdout)
    print(num_obj)