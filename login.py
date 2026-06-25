import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess


def login():
    student_id = id_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("hostel.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=? AND password=?",
        (student_id, password)
    )

    student = cursor.fetchone()
    conn.close()

    if student:
        messagebox.showinfo(
            "Login Success",
            "Welcome " + student[1]
        )
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid ID or Password"
        )


def open_service():
    subprocess.Popen(["python", "service.py"])
    app.destroy()


app = tk.Tk()
app.title("Student Login")
app.geometry("350x300")
app.configure(bg="lightblue")


tk.Label(
    app,
    text=" Login Page",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=10)


tk.Label(
    app,
    text="Student ID",
    bg="lightblue"
).pack()

id_entry = tk.Entry(app, width=30)
id_entry.pack()


tk.Label(
    app,
    text="Password",
    bg="lightblue"
).pack()

password_entry = tk.Entry(
    app,
    width=30,
    show="*"
)
password_entry.pack()


tk.Button(
    app,
    text="Login",
    command=login,
    width=15,
    bg="blue",
    fg="white"
).pack(pady=10)


tk.Button(
    app,
    text="Next",
    command=open_service,
    width=15,
    bg="green",
    fg="white"
).pack(pady=5)

app.mainloop()


