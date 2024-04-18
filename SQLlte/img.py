import sqlite3 as sq

def readAva(n):
    try:
        with open(f"Avas/{n}.png", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False

def writeAva(name, data):
    try:
        with open(name, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False


with sq.connect("img.db") as con:
    con.row_factory =sq.Row
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        ava BLOB,
        score INTEGER
    
    )""")

    img = readAva(1)
    if img:
        binary = sq.Binary(img)
        cur.execute("INSERT INTO users VALUES ('Nikola', ?, 1000)", (binary,))
    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']

    writeAva("out.png", img)
