def gen_func():
    try:
        yield 1
    except GeneratorExit:
        pass
    yield 2
    yield 3
    return "asdf"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)

    # GeneratorExit是继承自BaseException，用户一般继承的是Exception