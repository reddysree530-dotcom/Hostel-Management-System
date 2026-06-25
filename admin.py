from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("hostel_food.db")
cursor = conn.cursor()

root = Tk()
root.title("Hostel Food Rating - Admin Panel")
root.geometry("800x600")
root.configure(bg="lightyellow")


def view_all_ratings():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute(
        "SELECT student_name, food_item, rating, feedback FROM ratings"
    )

    records = cursor.fetchall()

    for record in records:
        tree.insert("", END, values=record)


def show_average_rating():
    cursor.execute("SELECT AVG(rating) FROM ratings")
    avg = cursor.fetchone()[0]

    if avg is None:
        avg_label.config(text="Average Rating: No Data Available")
    else:
        avg_label.config(text=f"Average Rating: {avg:.2f} / 5")


def view_negative_comments():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("""
        SELECT student_name, food_item, rating, feedback
        FROM ratings
        WHERE rating <= 2
    """)

    records = cursor.fetchall()

    if not records:
        messagebox.showinfo(
            "Information",
            "No negative comments found."
        )
        return

    for record in records:
        tree.insert("", END, values=record)


title_label = Label(
    root,
    text="Hostel Food Rating Admin Panel",
    font=("Arial", 18, "bold"),
    bg="lightyellow"
)
title_label.pack(pady=10)


button_frame = Frame(root, bg="lightyellow")
button_frame.pack(pady=10)

Button(
    button_frame,
    text="View All Ratings",
    command=view_all_ratings,
    bg="blue",
    fg="white",
    width=20
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Average Rating",
    command=show_average_rating,
    bg="green",
    fg="white",
    width=20
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="Negative Comments",
    command=view_negative_comments,
    bg="red",
    fg="white",
    width=20
).grid(row=0, column=2, padx=10)


avg_label = Label(
    root,
    text="Average Rating:",
    font=("Arial", 12, "bold"),
    bg="lightyellow"
)
avg_label.pack(pady=10)


columns = ("Student Name", "Food Item", "Rating", "Feedback")

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=18
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

root.mainloop()

conn.close()