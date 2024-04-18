import sqlite3
from jinja2 import Template
# Фильтры и макросы
cars_list = []

with sqlite3.connect("cities.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    for s in cur.fetchall():
        cars_list.append({"model" : s[0], "price": s[1]})

# Фильтры
tpl = "Суммарная цена автомобилей {{cars | sum(attribute = 'price')}}"
tm = Template(tpl)
msg = tm.render(cars = cars_list)
print(msg)
tpl = "Макс цена  {{ (cars | max(attribute = 'price')).model}}"
tm = Template(tpl)
msg = tm.render(cars = cars_list)
print(msg)
tpl = "Макс цена  {{ cars | random }}"
tm = Template(tpl)
msg = tm.render(cars = cars_list)
print(msg)
tpl = "Макс цена  {{ cars | replace('o', 'O')}}"
tm = Template(tpl)
msg = tm.render(cars = cars_list)
print(msg)

tpl = '''
{%for car in cars -%}
{% filter lower %} {{car.model}} {%endfilter%}
{%endfor -%}
'''
tm = Template(tpl)
msg = tm.render(cars = cars_list)
print(msg)

#Макроопределение

html = '''
{%- macro input(name, value='', type='text', size =20) -%}
    <input type="{{type}}" name= "{{name}}" value="{{value |e}}" size="{{size}}">
{%- endmacro -%}

<p>{{input('username')}}
<p>{{input('email')}}
<p>{{input('password')}}
'''

tm = Template(html)
msg = tm.render()
print(msg)

# вложенный макрос call там для списков ul