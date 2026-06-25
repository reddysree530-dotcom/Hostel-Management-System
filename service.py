import tkinter as tk
import subprocess

# Open Mess Page
def open_mess():
    subprocess.Popen(["python", "menu.py"])

# Open Hostel Room & Fee Page
def open_hostel_room_fee():
    subprocess.Popen(["python", "hostelroom_fee.py"])

# Main Window
root = tk.Tk()
root.title("Services Page")
root.geometry("500x400")
root.configure(bg="lightblue")

# Heading
title = tk.Label(
    root,
    text="Services Page",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
title.pack(pady=30)

# Mess Button
mess_btn = tk.Button(
    root,
    text="Mess",
    font=("Arial", 14, "bold"),
    
    fg="black",
    width=20,
    command=open_mess
)
mess_btn.pack(pady=15)

# Hostel Room & Fee Button
hostel_btn = tk.Button(
    root,
    text="Hostel Room & Fee",
    font=("Arial", 14, "bold"),
    
    fg="black",
    width=20,
    command=open_hostel_room_fee
)
hostel_btn.pack(pady=15)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    width=20,
    command=root.destroy
)
exit_btn.pack(pady=15)

root.mainloop()