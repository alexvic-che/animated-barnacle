import sqlite3
from jinja2 import Environment, FileSystemLoader
persons = []

with sqlite3.connect("cities.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM persons")

    for person in cur.fetchall():
        persons.append({"name": person[0], "old": person[1], "weight": person[2]})


#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons)
#
# print(msg)
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('content.html')
msg = tm.render(users=persons)

print(msg)