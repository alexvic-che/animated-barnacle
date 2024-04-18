class RenderList:
    def __init__(self, type_list):
        self.type_list = "ol" if type_list=="ol" else 'ul'


    def __call__(self,lst_in, *args, **kwargs):
        lst = """"""
        for el in lst_in:
            lst +=f"<li>{el}</li>\n"
        return f'<{self.type_list}>\n{lst}</{self.type_list}>'

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)