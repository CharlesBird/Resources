from sanic import Sanic

app = Sanic(__name__)

# 基础
app.config.DB_NAME = 'appdb'
app.config.DB_USER = 'appuser'

db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'appdb',
    'DB_USER': 'appuser'
}
app.config.update(db_settings)


# 加载配置
# 从环境变量
# 任何被 SANIC_ 前缀定义的变量将会被 sanic 配置接受。
# 例如，设置 SANIC_REQUEST_TIMEOUT 将被应用程序自动加载并提供给 REQUEST_TIMEOUT 配置变量。
# 你可以传递一个不同的前缀给 Sanic:
app = Sanic(load_env='MYAPP_')
# 以上的变量会是 MYAPP_REQUEST_TIMEOUT。如果你想要禁用从环境变量加载你可以用 False 替代它的设置:
app = Sanic(load_env=False)


# 从一个对象
import myapp.default_settings
app.config.from_object(myapp.default_settings)

# 从一个文件
app.config.from_envvar('MYAPP_SETTINGS')
#  >>$ MYAPP_SETTINGS=/path/to/config_file python3 myapp.py
# config_file
# DB_HOST = 'localhost'
# DB_NAME = 'appdb'
# DB_USER = 'appuser'
