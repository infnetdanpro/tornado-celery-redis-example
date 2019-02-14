import tornado.ioloop
import tornado.web
import redis
from tasks import main

class RedisHandler(tornado.web.RequestHandler):    
    def get(self):
        main.delay(1)
        self.write('added delays')

def make_app():
    return tornado.web.Application([
        (r"/", RedisHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()