import tornado.websocket
import logging
_logger = logging.getLogger(__name__)


class BrentWSHandler(tornado.websocket.WebSocketHandler):
    live_web_sockets = set()

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        _logger.info(u"BrentWebSocket 连接打开.")
        self.set_nodelay(True)
        self.live_web_sockets.add(self)
        self.write_message(u"已经成功连接WS服务.")

    def on_message(self, message):
        self.write_message(u"你传输的数据: " + message)

    def on_close(self):
        _logger.info("BrentWebSocket 连接关闭.")

    @classmethod
    def send_message(cls, message):
        removable = set()
        for ws in cls.live_web_sockets:
            if not ws.ws_connection or not ws.ws_connection.stream.socket:
                removable.add(ws)
            else:
                ws.write_message(message)
        for ws in removable:
            cls.live_web_sockets.remove(ws)