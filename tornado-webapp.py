import tornado.ioloop
import tornado.web
import redis
from tasks import results, prior

class RedisHandler(tornado.web.RequestHandler):    
    def get(self):
        results.delay(4, 4)
        prior.delay(10, 10)
        self.write('added delays')

def make_app():
    return tornado.web.Application([
        (r"/", RedisHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()