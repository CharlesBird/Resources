# 中间件
# 有两种中间件：请求和响应。
# 两者都使用 @app.middleware 装饰器声明，装饰器的参数是一个表示类型的字符串：'request' 或 'response'.
# 请求中间件接收仅作为 request 的参数。
# 响应中间件接收同时可以是 request 和 response

from sanic import Sanic
from sanic.response import json, text

app = Sanic(__name__)


# 最简单的中间件根本不会修改请求和响应
@app.middleware('request')
async def print_on_request(request):
    print("I print when a request is received by the server")

@app.middleware('response')
async def print_on_response(request, response):
    print("I print when a response is returned by the server")


# 中间件可以修改给定的请求或响应的参数，只要它们不返回
@app.middleware('response')
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Server"

@app.middleware('response')
async def prevent_xss(request, response):
    response.headers["x-xss-protection"] = "1; mode=block"

# 提前响应
# 如果中间件返回一个 HTTPResponse 对象，该请求会停止处理并且响应会被返回。
# 如果这发生在一个到达相应用户路由处理程序前的请求，该处理程序永远不会被调用。
# 返回响应也会阻止任何进一步的中间件运行
@app.middleware('request')
async def halt_request(request):
    return text('I halted the request')

@app.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)