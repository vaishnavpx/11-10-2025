from tkinter import *
from datetime import date

root=Tk()
root.title=("Getting Started With Widgets")
root.geometry("400x300")

lbl=Label(root,text="Enter two numbers to be multiplied!",fg="white",bg="#072f5f",height=1,width=100)
lbl.pack()

num_lbl=Label(root,text="Enter two numbers",bg="#3895d3",width=400)
num_lbl.pack(pady=10)


num_entry=Entry(root,width=30)
num_entry.pack(pady=10)

num_entry2=Entry(root,width=30)
num_entry2.pack(pady=10)

text_box=Text(root,height=1.5,width=45)
text_box.pack(pady=10)


def display():
    name=num_entry.get()
    if name.strip():
        text_box.delete("1.0",END)
        num1=int(num_entry.get())
        num2=int(num_entry2.get())
        product=num1*num2
        message=f"Your product is:\n{product}"
        text_box.insert(END,message)
    else:
        text_box.delete("1.0",END)
        text_box.insert(END,"Please insert your two numbers.")




btn=Button(root,text="Begin",command=display,bg="#1261a0",fg="white")
btn.pack()

root.mainloop()