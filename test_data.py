import sqlite3

"""добавим записи в таблицу"""

db = 'phonebook.db'
users_phones = [
    ("Иван", "Иванов", "муж", "20/08/1980", "no comment"),
    ("Петр", "Петров", "муж", "15/01/1988", "дружище"),
    ("Марина", "Самойлова", "жен", "1/01/1985", "жена"),
    ("Сын", "", "", "08/07/1995", "")
]
users_phn = [
    ("мобильный", "+7(956)758-47-56", 1),
    ("домашний", "+7(4912)25-48-75", 1),
    ("домашний", "+7(4912)75-28-59", 2),
    ("рабочий", "+7(978)789-25-69", 3),
    ("мобильный", "+7(912)709-75-68", 4)
]
test_data = [users_phones, users_phn]

conn = sqlite3.connect(db)
with conn:
    cur = conn.cursor()
    query = """INSERT INTO users(first_name,last_name,gender,birthday,comment) VALUES (?,?,?,?,?)"""
    cur.executemany(query, users_phones)
    conn.commit()
with conn:
    cur = conn.cursor()
    query = """INSERT INTO phonenumbers(type_phn, phn, userid) VALUES (?,?,?)"""
    cur.executemany(query, users_phn)
    conn.commit()
