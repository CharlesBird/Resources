from flask import Flask, request, make_response, redirect, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager

app = Flask(__name__)
Bootstrap(app)
manager = Manager(app)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return 'The browse is %s' % user_agent

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie.</h1>')
#     response.set_cookie('secret', '007')
#     print(response.__dict__)
#     return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/baidu/')
def baidu():
    return redirect('/web/login/')

@app.route('/web/login/')
def login():
    return '<h1>Login success!!!</h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'yiji':
        return '<h1>Bad Request</h1>', 404
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()