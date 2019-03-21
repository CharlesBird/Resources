from sanic import Sanic
from sanic.response import json, text
app = Sanic()

async def handler1(request):
    return text('ok')

async def handler2(request, name):
    return text('Folder - {}'.format(name))

async def personal_handler2(request, name):
    return text('Person - {}'.format(name))

app.add_route(handler1, '/test1')
app.add_route(handler2, '/folder2/<name>')
app.add_route(personal_handler2, '/personal2/<name:[A-z]>', methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)