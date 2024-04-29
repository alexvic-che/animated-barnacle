class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):

    def get(self,request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        if not "url" in request:
            raise TypeError('request не содержит обязательного ключа url')
        value = request["url"]
        return f"url:{value}"

    def render_request(self, request, method):
        if not method in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        f = getattr(self, method.lower(),False)
        if f:
            return f(request)




dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
print(html)