import sqlite3
import pandas as pd


def export_format(format):
    db = 'phonebook.db'
    sql_query = """select first_name, last_name, gender, birthday, comment, phonenumbers.type_phn, phonenumbers.phn
                from users join phonenumbers on phonenumbers.userid=users.id"""
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql_query)
    if format == "txt":
        with open("phonebook_export.txt", "w") as phb:
            for string in cur:
                phb.write(f"{str(string)}\n")
                print(string)
    elif format == "csv":
        get_ready = pd.read_sql(sql_query, conn)
        get_ready.to_csv("phonebook_export.csv", index=False, encoding='cp1251')
    conn.close()

def check_format():
    print("В каком формате выгрузить данные?")
    ext = input("Доступны: csv, txt")
    while ext not in ['csv', 'txt']:
        try:
            ext = input("Выберите формат из доступных: csv, txt ")
        except Exception as exc:
            print(exc.args[0])
            continue

    return ext
