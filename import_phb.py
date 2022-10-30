import add_contact
import os
import creatingDB
import pandas as pd
import sqlite3


# db = 'phonebook.db'
# file_txt = 'import_test.txt' # формат ввода данных - через знак ;


def check_file(some_file):
    print("Импортируем файлы с разделителем ;")
    try:
        if os.path.isfile(some_file):
            ext = some_file[-3:]
            if ext in ['csv', 'txt']:
                return True
        else:
            raise Exception
    except Exception as exc:
        print("Что то не так с файлом")
        return False


def lets_import(some_file):
    if check_file(some_file):
        if some_file[-3:] == "txt":
            with open(some_file, "r", encoding='utf-8') as imported:
                to_import = imported.read().splitlines()
                to_import1 = []
                for i in to_import:
                    to_import1.append(i.split(";"))
        else:
            with open(some_file, "r", encoding='cp1251') as imported:
                file_read = pd.read_csv('phonebook_export.csv', encoding='cp1251')
                to_import1 = []
                for i in range(file_read.shape[0]):
                    to_import1.append(list(file_read.iloc[i, ]))
        creatingDB.check_DB()  # а есть ли вообще куда добавлять
    for enum, contact in enumerate(to_import1):
        try:
            if sort_list(contact):
                if enum != 0:
                    if contact[:-2] == to_import1[enum-1][:-2]:
                        conn = sqlite3.connect("phonebook.db")#если такой пользователь уже добавлялся, и это просто еще один номер
                        with conn:
                            cur = conn.cursor()
                            cur.execute('SELECT max(id) FROM users')
                            row_id = cur.fetchone()[0]
                        data = sort_list(contact)[1]
                        data.append(row_id)
                        add_contact.add_contact_import_phone(data, conn)
                    else:
                        add_contact.add_contact_import_user(sort_list(contact))
                else:
                    add_contact.add_contact_import_user(sort_list(contact))
            continue
        except Exception:
            print(f'{Exception.args[0]}')
            continue


def sort_list(some_list):
    if len(some_list) != 7:
        print("Файл неполный, проверьте состав данных")
        return False
    else:
        return [some_list[:-2], some_list[-2:]]


# conn = sqlite3.connect("phonebook.db")#если такой пользователь уже добавлялся, и это просто еще один номер
# # with conn:
# #     cur = conn.cursor()
# #     cur.execute("""SELECT max(id) FROM users""")
# #     row_id = cur.fetchone()[0]
# conn.close()
# # print(row_id)
