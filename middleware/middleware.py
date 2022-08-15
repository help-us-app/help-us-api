from werkzeug.wrappers import Request, Response


class middleware:
    def __init__(self, app, key):
        self.app = app
        self.key = key

    def __call__(self, environ, start_response):
        request = Request(environ)
        key = request.headers.get('Authorization')
        res = Response(u'Authorization failed', mimetype='text/plain', status=401)

        if key is None:
            return self.app(environ, start_response)
        else:
            key = key.split(' ')[1]
            if key == self.key:
                return self.app(environ, start_response)
            else:
                return res(environ, start_response)
