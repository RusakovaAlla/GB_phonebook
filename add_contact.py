# ввод с хранение данных принимаем структурой в два списка
# first_name, last_name, gender, birthday, comment - список1
# type_phn, phn, userid - список2, последнее значение получаем по добавлении
import creatingDB
import sqlite3
import modul_vvod


def input_new_user():
    return modul_vvod.get_info()


def add_contact_manual_user(data_base='phonebook.db'):
    conn = sqlite3.connect(data_base)
    data = input_new_user()
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO users(first_name,last_name,gender,birthday,comment) VALUES (?,?,?,?,?)"""
        cur.execute(query, data[0])
        data[1].append(cur.lastrowid)
        conn.commit()
    add_contact_manual_phone(data, conn)


def add_contact_manual_phone(data, conn=None):
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO phonenumbers(type_phn, phn, userid) VALUES (?,?,?)"""
        cur.execute(query, data[1])
        conn.commit()


def add_contact_import_user(from_file, data_base='phonebook.db'):
    conn = sqlite3.connect(data_base)
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO users(first_name,last_name,gender,birthday,comment) VALUES (?,?,?,?,?)"""
        cur.execute(query, from_file[0])
        from_file[1].append(cur.lastrowid)
        conn.commit()
    add_contact_import_phone(from_file[1], conn)


def add_contact_import_phone(data, conn=None):
    with conn:
        cur = conn.cursor()
        query = """INSERT INTO phonenumbers(type_phn, phn, userid) VALUES (?,?,?)"""
        cur.execute(query, data)
        conn.commit()
