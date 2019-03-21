# 几个最有用的异常如下所示：
# NotFound: 当对请求对应的路由没有找到时被调用。
# ServerError: 当服务器发生了某些错误是被调用。这通常在用户代码里引发异常时发生。
# 参考 sanic.exceptions 模块以获取抛出异常的完整的列表。

from sanic import Sanic
from sanic.exceptions import ServerError, abort, NotFound
from sanic.response import text

app = Sanic()

# 抛出异常
@app.route('/killme')
async def i_am_ready_to_die(request):
    raise ServerError("Something bad happened...", status_code=500)


# abort 函数附上合适状态码
@app.route('/youshallnotpass')
async def no_no(request):
        abort(401)
        # this won't happen
        return text("OK")


# 处理异常
#要复写 Sanic 的默认异常的处理，就要用到 @app.exception 装饰器。
# 该装饰器需要一个异常列表作为参数来处理。
# 你可以传递 SanicException 以捕获所有异常！被装饰的异常处理程序必须带一个 Request 和 Exception 对象作为参数。
@app.exception(NotFound)
async def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)