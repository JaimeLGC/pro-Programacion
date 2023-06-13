import sqlite3

DB_PATH = 'mail.db'

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

sql = 'Select * from login'
va = cur.execute(sql)
row = va.fetchone()
username, password, domain = row
print(row[0])
print(row[1])
print(row[2])