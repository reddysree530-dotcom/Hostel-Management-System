
import tkinter as tk
from tkinter import messagebox
import subprocess

TOTAL_FEE = 54000

def calculate_balance():
    try:
        student_name = entry_name.get()
        room_no = entry_room.get()
        paid = int(entry_paid.get())

        if student_name == "":
            messagebox.showerror("Error", "Please enter Student Name!")
            return

        if room_no == "":
            messagebox.showerror("Error", "Please enter Room Number!")
            return

        if paid < 0:
            messagebox.showerror("Error", "Enter a valid amount!")
            return

        balance = TOTAL_FEE - paid

        lbl_balance.config(
            text=f"Student: {student_name}\nRoom No: {room_no}\nRemaining Balance: ₹{balance}"
        )

        if balance <= 0:
            messagebox.showinfo(
                "Success",
                f"Hostel Fee Paid Successfully!\nStudent: {student_name}"
            )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter numbers only in Paid Amount!"
        )

def go_back():
    subprocess.Popen(["python", "service.py"])
    root.destroy()

root = tk.Tk()
root.title("Hostel Room & Fee Payment")
root.geometry("700x800")
root.configure(bg="lightblue")

tk.Label(
    root,
    text="Hostel Room & Fee Payment",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack(pady=10)

tk.Label(
    root,
    text="Student Name:",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

tk.Label(
    root,
    text="Room Number:",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_room = tk.Entry(root, width=30)
entry_room.pack(pady=5)

tk.Label(
    root,
    text="Total Hostel Fee: ₹54000",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack(pady=10)

tk.Label(
    root,
    text="Enter Paid Amount:",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_paid = tk.Entry(root, width=30)
entry_paid.pack(pady=5)

tk.Button(
    root,
    text="Pay Fee",
    bg="green",
    fg="white",
    command=calculate_balance
).pack(pady=10)

lbl_balance = tk.Label(
    root,
    text="Remaining Balance: ₹54000",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)
lbl_balance.pack(pady=10)

tk.Button(
    root,
    text="Back to Service Page",
    bg="orange",
    fg="white",
    command=go_back
).pack(pady=10)

tk.Label(
    root,
    text="Hostel Facilities",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=10)

facilities = """
✓ Wi-Fi Available
✓ 24/7 Security
✓ RO Drinking Water
✓ Laundry Service
✓ Study Room
✓ Mess Facility
✓ Medical Assistance
✓ CCTV Surveillance
✓ Power Backup
✓ Indoor Games Room
"""

tk.Label(
    root,
    text=facilities,
    justify="left",
    bg="lightblue",
    font=("Arial", 12)
).pack()

root.mainloop()


