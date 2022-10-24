import sqlite3

conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
cur.execute("""select * from users 
join phonenumbers on users.id = phonenumbers.userid
""")
for string in cur:
    print(string)

