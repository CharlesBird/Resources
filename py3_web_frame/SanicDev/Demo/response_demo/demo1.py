# 响应Response 对象

from sanic import Sanic
from sanic.response import json, text, redirect, html, file, file_stream, stream, raw
app = Sanic()


# 富文本
@app.route('/text')
def handle_request(request):
    return text('Hello world!')


# HTML
@app.route('/html')
def handle_request(request):
    return html('<p>Hello world!</p>')


# JSON
@app.route('/json')
def handle_request(request):
    return json({'message': 'Hello world!'})


# 文件
@app.route('/file')
async def handle_request(request):
    return await file('/Users/zhanghuaicheng/Downloads/pycharm-community-2018.3.dmg')


# 流
@app.route("/streaming")
async def index(request):
    async def streaming_fn(response):
        response.write('foo')
        response.write('bar')
    return stream(streaming_fn, content_type='text/plain')


# 文件流，用于大文件
@app.route('/big_file.dmg')
async def handle_request(request):
    return await file_stream('/Users/zhanghuaicheng/Downloads/pycharm-community-2018.3.dmg')


# 重定向
@app.route('/redirect')
def handle_request(request):
    return redirect('/json')


# 不对body编码的响应
@app.route('/raw')
def handle_request(request):
    return raw(b'raw data')


# 修改头和状态码
@app.route('/update')
def handle_request(request):
    return json(
        {'message': 'Hello world!'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)