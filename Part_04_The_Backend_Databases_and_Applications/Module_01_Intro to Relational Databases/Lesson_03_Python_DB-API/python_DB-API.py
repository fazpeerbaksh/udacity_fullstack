import sqlite3

conn = sqlite3.connect('cookies')
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM moz_cookies")

results = cursor.fetchall()

print(results)

conn.close()

