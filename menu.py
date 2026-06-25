import tkinter as tk
import subprocess


def open_rating():
    app.destroy()  
    subprocess.Popen(["python", "rating.py"])

app = tk.Tk()
app.title("Hostel Food Menu")
app.geometry("500x450")

title = tk.Label(
    app,
    text="Hostel Food Menu & Timings",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

tiffin = tk.Label(
    app,
    text="Tiffin\nTime: 7:30 AM - 9:00 AM\nMenu: Idly, Dosa, Upma, Pulihora, Lemon Rice",
    font=("Arial", 12),
    justify="left"
)
tiffin.pack(pady=10)

lunch = tk.Label(
    app,
    text="Lunch\nTime: 12:30 PM - 2:00 PM\nMenu: Rice, Dal, Curry, Fry, Rasam, Curd",
    font=("Arial", 12),
    justify="left"
)
lunch.pack(pady=10)

dinner = tk.Label(
    app,
    text="Dinner\nTime: 7:30 PM - 9:00 PM\nMenu: Chapathi, Rice, Veg Rice, Biryani, Rasam",
    font=("Arial", 12),
    justify="left"
)
dinner.pack(pady=10)


button_frame = tk.Frame(app)
button_frame.pack(pady=20)


next_button = tk.Button(
    button_frame,
    text="Next",
    command=open_rating,
    width=15,
    bg="lightgreen"
)
next_button.grid(row=0, column=0, padx=10)


exit_button = tk.Button(
    button_frame,
    text="Close",
    command=app.destroy,
    width=15,
    bg="lightcoral"
)
exit_button.grid(row=0, column=1, padx=10)

app.mainloop()


