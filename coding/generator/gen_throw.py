def gen_func():
    try:
        yield 1
    except Exception:
        pass
    yield 2
    yield 3
    return "asdf"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    v2 = gen.throw(Exception, 'IO error')
    print(v2)
    print(next(gen))
    # print(next(gen))