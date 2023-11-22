from tkinter import *
import random
import math
from tkinter import messagebox

p = ""
n=0
gui = Tk() 
gui.title("Password Generator (CODSOFT TASK - 3)") 
gui.geometry("300x210")
def letter():
    global p
    p = p + chr(random.randint(65,90))
    p = p + (str(random.randint(0,9)))
    p = p + chr(random.randint(97,122))
    p = p + chr(random.randint(33,47))

def edit():
    global p
    p=""
    regen_btn["state"] = DISABLED
    gen_btn["state"] = NORMAL
    password_field.config(state=NORMAL)
    
def gen():
    global n 
    try:
        n = int(password_field.get())
        for i in range(0,math.ceil(n/4)):
            letter()
        regen_btn["state"] = NORMAL
        edit_btn["state"] = NORMAL
        gen_btn["state"] = DISABLED
        password_field.config(state=DISABLED)
        messagebox.showinfo("Generated Password",p[:n]) 
    except:
        messagebox.showerror("showerror", "Enter Numerical Value")
    

def regen():
    global p
    p = ""
    for i in range(0,math.ceil(n/4)):
        letter()
    messagebox.showinfo("Regenerated Password",p[:n]) 
password = StringVar()
pass_lbl = Label(gui, text = "Enter No. of characters you want in your password - ") 
password_field = Entry(gui, textvariable=password)
gen_btn = Button(gui, text=' Generate Password ', command=gen, height=1, width=15)
regen_btn = Button(gui, text=' Regenerate ', command=regen, height=1, width=15)
edit_btn = Button(gui, text=' Edit ', command=edit, height=1, width=38)

regen_btn["state"] = DISABLED
edit_btn["state"] = DISABLED

pass_lbl.place(x = 10,y = 10) 
password_field.place(x = 90,y = 40)
gen_btn.place(x = 170,y = 100) 
regen_btn.place(x = 10,y = 100) 
edit_btn.place(x = 10,y = 130) 

gui.mainloop()
