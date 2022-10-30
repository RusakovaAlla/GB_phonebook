import os
import sqlite3

"""
создаем базу данных"""


def check_DB(data_base='phonebook.db'):
    if os.path.exists(data_base):
        pass
    else:
        queries = [
            """CREATE TABLE IF NOT EXISTS users( 
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name TEXT,
           last_name TEXT,
           gender TEXT,
           birthday TEXT,
           comment TEXT)
        """,
            """CREATE TABLE IF NOT EXISTS phonenumbers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_phn TEXT,
            phn TEXT,
            userid INTEGER,
            FOREIGN KEY (userid) REFERENCES users(id)) """
        ]
        [push_changes(data_base, i) for i in queries]


def push_changes(data_base, query):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
