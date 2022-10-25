#ввод с хранение данных принимаем структурой в два списка
#first_name, last_name, gender, birthday, comment - список1
# type_phn, phn, userid - список2, последнее значение получаем по добавлении
import sqlite3

def input_new_user():
    structure = ['имя', 'фамилия', 'пол', 'дата_рождения', 'комментарий']
    to_insert_new = [[], []]
    to_insert_new[0].append(input('Введите имя: '))
    to_insert_new[0].append(input('Введите фамилию: '))
    to_insert_new[1].append(input('Введите номер телефона'))
    to_insert_new[1].insert(0, input('Тип номера: '))
    to_insert_new[0].append(input('Укажите пол: '))
    to_insert_new[0].append(input('Укажите дату рождения: '))
    to_insert_new[0].append(input('Комментарий: '))

    return to_insert_new

new_user = input_new_user()
print(new_user)

db = 'phonebook.db'
conn = sqlite3.connect(db)
with conn:
    cur = conn.cursor()
    query = """INSERT INTO users(first_name,last_name,gender,birthday,comment) VALUES (?,?,?,?,?)"""
    cur.execute(query, new_user[0])
    new_user[1].append(cur.lastrowid)
    conn.commit()
print(new_user)
with conn:
    cur = conn.cursor()
    query = """INSERT INTO phonenumbers(type_phn, phn, userid) VALUES (?,?,?)"""
    cur.execute(query, new_user[1])
    conn.commit()
