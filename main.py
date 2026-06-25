from PIL import Image 
from PIL import ImageTk
from PIL import ImageFilter
import tkinter as tk

import subprocess

def next_page():
    app.destroy()
    subprocess.run(["python", "login.py"])


app=tk.Tk()
app.title("Hostel Food Rating System")
app.geometry("500x400")

image = Image.open("C:/Hostel Management System/hostel image/d.jpg")
image = image.resize((500,500))
image = image.filter(ImageFilter.GaussianBlur(radius=3))

bg_image = ImageTk.PhotoImage(image)

background = tk.Label(app,image=bg_image)
background.place(x=0, y=0, relwidth=1,relheight=1)


label=tk.Label(
   app,
   text=" Hostel Management System",
   font=("Arial",15,"bold"),
   
)   

label.pack(pady=40)

next_button = tk.Button(
    app,
    text="Next",
    font=("Arial", 12, "bold"),
    bg="silver",
    fg="white",
    width=10,
    command=next_page
)
next_button.pack(pady=80)  

app.mainloop()