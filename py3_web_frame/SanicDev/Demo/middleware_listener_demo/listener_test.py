# 监听器
# 如果你想执行 startup/teardown 代码作为你服务应用的启动或关闭，你可以使用以下监听器：
#
# before_server_start
# after_server_start
# before_server_stop
# after_server_stop

from sanic import Sanic
import asyncio

app = Sanic(__name__)

async def db_setup():
    print('DB successfully connected')


@app.listener('before_server_start')
async def setup_db(app, loop):
    app.db = await db_setup()


@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server successfully started!')

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    print('Server shutting down!')

@app.listener('after_server_stop')
async def close_db(app, loop):
    await app.db.close()


# 也有可能使用 register_listener 方法来注册监听器。
async def setup_db(app, loop):
    app.db = await db_setup()

app.register_listener(setup_db, 'before_server_start')


# 如果你想要在 loop 已经启动后安排一个后台任务来执行，Sanic 提供了 add_task 方法来简单地实现。
async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print('Server successfully started!')

app.add_task(notify_server_started_after_five_seconds())


# Sanic 会尝试自动注入 app，作为参数传递给任务：
async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print(app.name)
    print('Server successfully started!')

app.add_task(notify_server_started_after_five_seconds)

# 或者同样效果地你可以明确地传递 app
async def notify_server_started_after_five_seconds(app):
    await asyncio.sleep(5)
    print(app.name)

app.add_task(notify_server_started_after_five_seconds(app))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)