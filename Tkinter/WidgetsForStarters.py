from tkinter import *
from datetime import date

root=Tk()
root.title=("Getting Started With Widgets")
root.geometry("400x300")

lbl=Label(root,text="Hey there!",fg="white",bg="#072f5f",height=1,width=100)
lbl.pack()

name_lbl=Label(root,text="Enter your name",bg="#3895d3",width=400)
name_lbl.pack(pady=10)


name_entry=Entry(root,width=30)
name_entry.pack(pady=10)

text_box=Text(root,height=5,width=45)
text_box.pack(pady=10)

def display():
    name=name_entry.get()
    if name.strip():
        text_box.delete("1.0",END)
        greet=f"Hello {name}\n"
        message=f"Welcome to the application!\nToday's date is: {date.today()}"
        text_box.insert(END,greet+message)
    else:
        text_box.delete("1.0",END)
        text_box.insert(END,"Please insert your full name.")


btn=Button(root,text="Begin",command=display,bg="#1261a0",fg="white")
btn.pack()

root.mainloop()