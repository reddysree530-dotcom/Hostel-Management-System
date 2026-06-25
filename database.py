import sqlite3

conn = sqlite3.connect("hostel.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    room_no TEXT,
    password TEXT
)
""") 

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       student_name TEXT,
       food_item TEXT,
       rating INTEGER,
       comment TEXT
)
""")
conn.commit()
conn.close()
print("Database Created Successfully")
                                                       
               