from sanic import Sanic
from sanic.response import json, text, redirect
app = Sanic()

@app.route("/json")
def post_json(request):
    return json({ "received": True, "message": request.json })

@app.route("/query_string")
def query_string(request):
    return json({ "parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)