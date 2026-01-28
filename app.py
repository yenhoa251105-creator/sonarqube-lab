import os
import sqlite3

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")

user = input("Enter username: ")

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user,))

print(cursor.fetchall())
