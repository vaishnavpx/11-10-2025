from tkinter import *
from datetime import date
import random

computer_choice=random.randint(1,3)

def rock():
    hand="rock"
    if computer_choice==1:
        m="I chose rock.\nIt is a tie."
    elif computer_choice==2:
        m="I chose paper.\nYou lose."
    elif computer_choice==3:
        m="I chose scissors.\nYou win."

    text_box.delete("1.0",END)
    message=m
    text_box.insert(END,message)

def paper():
    hand="paper"
    if computer_choice==1:
        m="I chose rock.\nYou win."
    elif computer_choice==2:
        m="I chose paper.\nIt is a tie."
    elif computer_choice==3:
        m="I chose scissors.\nYou lose."
    
    text_box.delete("1.0",END)
    message=m
    text_box.insert(END,message)

def scissors():
    hand="scissors"
    if computer_choice==1:
        m="I chose rock.\nYou lose."
    elif computer_choice==2:
        m="I chose paper.\nYou win."
    elif computer_choice==3:
        m="I chose scissors.\nIt is a tie."

    text_box.delete("1.0",END)
    message=m
    text_box.insert(END,message)

root=Tk()
root.title=("Rock Paper Scissors")
root.geometry("400x300")

lbl=Label(root,text="Press rock paper or scissors!",fg="white",bg="#072f5f",height=1,width=100)
lbl.pack()

rock_btn=Button(root,text="Rock",command=rock,bg="#1261a0",fg="white")
rock_btn.place(x=40,y=100)

paper_btn=Button(root,text="Paper",command=paper,bg="#1261a0",fg="white")
paper_btn.place(x=40,y=150)

scissors_btn=Button(root,text="Scissors",command=scissors,bg="#1261a0",fg="white")
scissors_btn.place(x=40,y=200)

text_box=Text(root,height=1.5,width=45)
text_box.pack(pady=10)



root.mainloop()