def gen_func():
    # 1、产出值
    # 2、可以接受值（调用方法传递进来的值）
    html = yield "http://baidu.com"
    print(html)
    yield 2
    yield 3
    return "asdf"

# throw，close


if __name__ == '__main__':
    gen = gen_func()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种：1、gen.send(None),2、next(gen)
    url = gen.send(None)  # 预激生成器
    print(url)
    # print(next(gen))
    v2 = gen.send("zxcv")  # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield
    print(v2)
    print(next(gen))
    print(next(gen))