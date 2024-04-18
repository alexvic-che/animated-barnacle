import sqlite3


with sqlite3.connect("cities.db") as con:
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS cities(
        city TEXT NOT NULL);
        INSERT INTO cities VALUES ('Москва');
        INSERT INTO cities VALUES ('Тверь');
        INSERT INTO cities VALUES ('Минск');
        INSERT INTO cities VALUES ('Смоленкс');
        INSERT INTO cities VALUES ('Калуга');
        """)

with sqlite3.connect("cities.db") as con:
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
        model TEXT NOT NULL,
        price INTEGER DEFAULT 0);
        INSERT INTO cars VALUES ('Audi', 23000);
        INSERT INTO cars VALUES ('Skoda', 17300);
        INSERT INTO cars VALUES ('Volva', 44300);
        INSERT INTO cars VALUES ('Folkswagen', 21300);
        """)
with sqlite3.connect("cities.db") as con:
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS persons(
        name TEXT NOT NULL,
        old INTEGER DEFAULT 0,
        weight REAL);
        INSERT INTO persons VALUES ('Aleksei', 15, 78.5);
        INSERT INTO persons VALUES ('Иван', 28, 82.5);
        INSERT INTO persons VALUES ('Nikola', 33, 94);
        """)