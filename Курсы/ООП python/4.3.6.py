class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

class Callback:
    def __init__(self, path, router_cls):
        self.path = path
        self.router_cls = router_cls

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'



route = Router.get('/')
if route:
    ret = route()
    print(ret)