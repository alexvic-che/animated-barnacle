from jinja2 import Template
import jinja2
name = "Fedor"
data = """ {% raw %}Modul jinja sddad asdfas asd {{ name }} sadasdasd{%endraw%} """
link = '''<a href = "#"> Ssilka </a>'''

tm = Template(data)
msg = tm.render(name= name)
print(msg)

tm = Template(link)
msg = tm.render(link = link)
print(msg)

tm = Template("{{link | e}}")
msg = tm.render(link = link)
print(msg)


#{% raw %}................{%endraw%} - выводит как есть (экранирование)
