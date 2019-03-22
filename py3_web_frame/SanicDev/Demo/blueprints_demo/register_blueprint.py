# 蓝图 (Blueprints) 是用在一个应用程序里可用作子路由的对象。
# 作为添加路由到应用程序实例的替代者，蓝图为添加路由定义了相似的方法，即用一种灵活而且可插拔的方法注册到应用程序实例。
# 蓝图对于大型应用特别有用，当你的应用逻辑能被分解成若干个组或者责任区域。

from sanic import Sanic
from my_blueprint import bp

app = Sanic(__name__)
# 注册蓝图
app.blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)