import os
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk 

r = tk.Tk() # root window
r.title('Study Bot')
w = tk.Canvas(r, width=500, height=700) # bg window

bgx = (Image.open("bg2.jpg"))
r_img = bgx.resize((500,700), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(r_img)

label1 = Label(r, image=bg)
label1.place(x=0, y=0)

l2 = Label(r, text="Study Bot", font=("Arial Black", 22, "bold"))
l2.config(bg = "black", fg="#00cb00")
l2.place(x=180,y=8)

intro = "Hello, I am Study Bot. \nI offer following functionalities\n1. Opening Apps\n2. Open Google, Wikipedia \nand StackOverflow\n3.Play local music files\n4. Open my source code\n and more! Check me out!"
l3=Label(r, text=intro , font=("Arial", 16))
l3.config(bg = "#777777",fg="#fff7e8",height=16, width=40)
l3.place(x=5,y=70)

def run_va():
    va = "F:\\College\\Engineering\\Study\\Fourth\\EDI\\Code\\study_bot.py"
    os.system(va)

b1= Button(r, text="Run", command= run_va)
b1.config(bg="red", fg="white", font=("Arial", 16), padx=10, pady=15)
b1.place(x=180, y=530)

w.pack()
b2 = Button(r,text="Exit", command=lambda:exit(0))
b2.config(bg="yellow", fg="black", font=("Arial", 16), padx=10, pady=15)
b2.place(x=280, y=530)

r.mainloop()


