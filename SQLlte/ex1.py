import sqlite3 as sq

names = ['Misha', 'Pasha', 'Sasha', 'Masha', 'Gula', 'Marat']
olds = [18, 20, 10, 15, 45, 60]
sexs = [1, 1, 1, 2, 2, 1]
scores = [1000, 2000, 3000, 500, 400, 100]

with sq.connect("saper.db") as con:
    cur = con.cursor()
    # cur.execute("""DROP TABLE IF EXISTS users""")
    # cur.execute("""DROP TABLE IF EXISTS games""")

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        sex INTEGER DEFAULT 1,
        old INTEGER DEFAULT 1,
        score INTEGER DEFAULT 0
        )""")
    for i in range(len(names)):

        cur.execute(f"""INSERT INTO users(name, old, sex, score) VALUES ('{names[i]}', {olds[i]},
                    {sexs[i]}, {scores[i]})""")

    cur.execute("""CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER DEFAULT 0,
        time INTEGER DEFAULT 0    
        )""")











    # cur.execute("""INSERT INTO users(old) VALUES (18)""")

    # cur.execute("""SELECT name, old, score FROM users
    #             WHERE old >= 18 LIMIT 5""")
    # result = cur.fetchall()
    # print(result)
    # for result in cur:
    #     print(result)

    # Обновление и удаление из таблиц
    # UPDATE users SET score = 1000, old =45 WHERE old > 40
    # DELETE FROM users WHERE rowid IN(2,5)

    #Агрегирующая функции:
    # SELECT count(user_id) FROM games WHERE user_id = 1

    # count() - подсчет числа записей
    # sum() -
    # avr() - среднеарефметическое
    # min()
    # msx()

    # Группировка записей:
    # SELECT user_id, sum(score) as sum FROM games
    # GROUP BY user_id
    # ORDER BY sum DESC - сортировка по убыванию

    # Связывание таблиц через JOIN:
    # SELECT name, sex, games.score FROM games
    # JOIN users ON games.user_id = users.rowid
    # LEFT JOIN users ON games.user_id = users.rowid - пишет данные даже если нечего подставить

    # 




