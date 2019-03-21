from sanic import Sanic
from sanic.response import json, text, redirect
app = Sanic()

# 重定向效果
@app.route("/")
async def index(request):
    url = app.url_for('post_handler', post_id=5)
    return redirect(url)

@app.route('posts/<post_id>')
async def post_handler(request, post_id):
    return text('Post - {}'.format(post_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)