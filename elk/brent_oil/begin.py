import asyncio
import tornado.web
import tornado.ioloop
from brent_from_sina.data_from_sina import main
from brent_from_sina.wsserver import BrentWSHandler


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/brent_oil', BrentWSHandler)
    ])
    app.listen(9000, '0.0.0.0')
    # tornado.ioloop.IOLoop.current(app)
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(loop))
    asyncio.ensure_future(main(loop))
    loop.run_forever().start()