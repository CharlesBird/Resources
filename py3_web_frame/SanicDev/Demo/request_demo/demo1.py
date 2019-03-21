# 请求Request 对象的属性
# 详情可以见https://sanic-cn.readthedocs.io/zh/latest/sanic/request_data.html
from sanic import Sanic
from sanic.response import json, text, redirect
app = Sanic()

@app.route("/json")
def post_json(request):
    return json({ "received": True, "message": request.json })

@app.route("/query_string")
def query_string(request):
    return json({ "parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string })


@app.route("/files")
def post_json(request):
    test_file = request.files.get('test')
    print(test_file)

    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type,
    }

    return json({ "received": True, "file_names": request.files.keys(), "test_file_parameters": file_parameters })


@app.route("/form")
def post_json(request):
    print(dir(request))
    print(request.headers)
    return json({ "received": True, "form_data": request.form, "test": request.form.get('test') })


@app.route("/users", methods=["POST",])
def create_user(request):
    return text("You are trying to create a user with the following POST: %s" % request.body)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)