import sqlite3

conn=sqlite3.connect("hostel.db")
cursor=conn.cursor()

cursor.execute("SELECT*FROM students")
data=cursor.fetchall()

print("Students data:")
print()

conn.close()