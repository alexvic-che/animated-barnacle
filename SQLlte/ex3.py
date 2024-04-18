import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57142),
    ('Skoda', 457789),
    ('Volvo', 29031),
    ('Bentley', 36892)
]

with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    #cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    cur.execute("SELECT model, price FROM cars")



    for r in cur:
        print(r['model'], r['price'])