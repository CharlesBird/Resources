# 响应 cookies 可被设置成字典值并且有一下有效参数:
#
#     expires (datetime): cookies 在客户端的浏览器上的过期时间。
#     path (string): cookie 使用的子 URL。默认为 /.
#     comment (string): 注释 (元数据).
#     domain (string): cookie 有效的指定域名。一个明确的指定域名必须总是有 . 开始。
#     max-age (number): cookie 可以存活的最大秒数。
#     secure (boolean): 指定 cookie 是否只能通过 HTTPS 发送。
#     httponly (boolean): 指定 cookie 是否不能被 Javascript 读取。

from sanic import Sanic
from sanic.response import json, text

app = Sanic()

# 读 cookies
@app.route("/cookie/read")
async def read(request):
    test_cookie = request.cookies.get('test')
    return text("Test cookie set to: {}".format(test_cookie))

# 写 cookies
@app.route("/cookie/write")
async def write(request):
    response = text("There's a cookie up in this response")
    response.cookies['test'] = 'It worked!'
    response.cookies['test']['domain'] = '.gotta-go-fast.com'
    response.cookies['test']['httponly'] = True
    return response

# 删除 cookies
@app.route("/cookie/delete")
async def delete(request):
    response = text("Time to eat some cookies muahaha")

    # This cookie will be set to expire in 0 seconds
    del response.cookies['kill_me']

    # This cookie will self destruct in 5 seconds
    response.cookies['short_life'] = 'Glad to be here'
    response.cookies['short_life']['max-age'] = 5
    del response.cookies['favorite_color']

    # This cookie will remain unchanged
    response.cookies['favorite_color'] = 'blue'
    response.cookies['favorite_color'] = 'pink'
    del response.cookies['favorite_color']

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)