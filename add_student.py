import sqlite3
conn=sqlite3.connect("hostel.db")
cursor=conn.cursor()

student_id=input("Enter Student ID:")
name=input("Enter Student Name:")
room_no=input("Enter Room Number:")
password=input("Enter Password:")

cursor.execute(
   "INSERT INTO students (id, name, room_no,password)VALUES(?,?,?,?)",
   (student_id,name,room_no,password)
)
conn.commit()

print("Student data inserted sucessfully!")
conn.close()