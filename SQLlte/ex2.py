import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57142),
    ('Skoda', 457789),
    ('Volvo', 29031),
    ('Bentley', 36892)
]


with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust ( name TEXT, 
                                        tr_in INTEGER,
                                        buy INTEGER)
        
        """)

    cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    last_row_id = cur.lastrowid
    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price':0})

# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#
#     cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
#             car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER
#             );
#             BEGIN;
#             INSERT INTO cars VALUES(NULL,'Audi', 52642 );
#             INSERT INTO cars VALUES(NULL,'Audi', 52642 );
#             INSERT INTO cars VALUES(NULL,'Audi', 52642 );
#             INSERT INTO cars VALUES(NULL,'Audi', 52642 );
#             INSERT INTO cars VALUES(NULL,'Audi', 52642 );
#             UPDATE cars SET price = 0 WHERE model LIKE "A%"
#
#
#             """)
#     con.commit()
#
# except sq.Error as e:
#     if con: con.rollback()
#     print("Ошибка выполнения запроса")
#
# finally:
#     if con: con.close()

