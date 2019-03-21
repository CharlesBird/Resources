from sanic import Sanic
from sanic.response import json, text

app = Sanic()
db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'test',
    'DB_USER': 'root'
}
app.config.update(db_settings)

@app.route('/')
async def index(request):
    return text('hello world')
    # return json({'hello': 'world'})

@app.route('tag/<tag>')
async def tag_handler(request, tag):
    return text('Tag - {}'.format(tag))

@app.route('number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('integer_arg - {}'.format(integer_arg))


@app.route('number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('number_arg - {}'.format(number_arg))

@app.route('person/<name:[]A-z]+>')
async def person_handler(request, name):
    return text('name - {}'.format(name))

@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))

@app.route('/post1', methods=['POST'])
async def post_handler(request):
    return text('POST request - {}'.format(request.json))

@app.route('/get1', methods=['GET'])
async def get_handler(request):
    return text('GET request - {}'.format(request.args))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)