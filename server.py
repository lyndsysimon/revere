
import tornado.web
import tornado.websocket

subscribers = []


class EventSubscriber(tornado.websocket.WebSocketHandler):

    def open(self):
        subscribers.append(self)
        print('Socket opened.')

    def on_close(self):
        subscribers.remove(self)
        print('Socket closed.')

    def on_message(self, message):
        self.broadcast('You sent: {}'.format(message))

    def broadcast(self, message, **kwargs):
        for listener in list(subscribers):
            try:
                listener.write_message(message)
            except AttributeError:
                listener.close()

app = tornado.web.Application(
    handlers=[
        (r'/events', EventSubscriber),
    ],
    debug=True
)

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
