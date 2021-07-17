import sqlite3

conn = sqlite3.connect('Cookies')
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM cookies")

results = cursor.fetchall()

print(results)

conn.close()

