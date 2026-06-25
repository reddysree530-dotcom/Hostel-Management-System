
from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess


conn = sqlite3.connect("hostel_food.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    food_item TEXT,
    rating INTEGER,
    feedback TEXT
)
""")

conn.commit()


def submit_rating():
    name = entry_name.get()
    food = entry_food.get()
    rating = rating_var.get()
    feedback = text_feedback.get("1.0", END).strip()

    if name == "" or food == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    cursor.execute(
        "INSERT INTO ratings (student_name, food_item, rating, feedback) VALUES (?, ?, ?, ?)",
        (name, food, rating, feedback)
    )

    conn.commit()

    messagebox.showinfo("Success", "Rating Submitted Successfully!")

    entry_name.delete(0, END)
    entry_food.delete(0, END)
    text_feedback.delete("1.0", END)
    rating_var.set(5)


def open_admin():
    subprocess.Popen(["python", "admin.py"])


root = Tk()
root.title("Hostel Food Rating System")
root.geometry("500x550")
root.configure(bg="lightyellow")


Label(
    root,
    text="Hostel Food Rating System",
    font=("Arial", 18, "bold"),
    bg="lightyellow"
).pack(pady=10)


Label(root, text="Student Name:", bg="lightyellow").pack()
entry_name = Entry(root, width=40)
entry_name.pack(pady=5)


Label(root, text="Food Item:", bg="lightyellow").pack()
entry_food = Entry(root, width=40)
entry_food.pack(pady=5)


Label(root, text="Rating (1-5):", bg="lightyellow").pack()

rating_var = IntVar()
rating_var.set(5)

for i in range(1, 6):
    Radiobutton(
        root,
        text=str(i),
        variable=rating_var,
        value=i,
        bg="lightyellow"
    ).pack()


Label(root, text="Feedback Comments:", bg="lightyellow").pack()

text_feedback = Text(root, width=40, height=5)
text_feedback.pack(pady=5)


Button(
    root,
    text="Submit Rating",
    command=submit_rating,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=10)


Button(
    root,
    text="Admin Page",
    command=open_admin,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=10)


Button(
    root,
    text="Exit",
    command=root.destroy,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=10)

root.mainloop()

conn.close()

