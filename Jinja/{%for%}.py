from jinja2 import Template
import sqlite3

def select_cities():
    cities_list = []
    with sqlite3.connect("cities.db") as con:
        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM cities")
        cities = cur.fetchall()


        for city in cities:
            cities_list.append({'id' : city[0], 'city' : city[1]})

    return (cities_list)

a =  select_cities()

link ='''<select name = "cities">
{% for c in cities -%}
{% if c.id > 1 -%}
    <option value = "{{c['id']}}">{{c['city']}}</option>
{%else -%}
GG
{%endif -%}
{% endfor -%}
    
</select> '''

tm = Template(link)

msg = tm.render(cities = a)

print(msg)



