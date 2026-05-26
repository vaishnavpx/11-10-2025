from tkinter import *
import datetime

root=Tk()
root.title=("Age Calculator App")
root.geometry("400x400")

year_lbl=Label(root,text="Enter your birth year",fg="white",bg="#072f5f",height=1,width=100)
year_lbl.pack()

year=Entry(root,width=30)
year.pack(pady=10)

month_lbl=Label(root,text="Enter your birth month",bg="#3895d3",width=400)
month_lbl.pack(pady=10)

month=Entry(root,width=30)
month.pack(pady=10)

day_lbl=Label(root,text="Enter your birth day",fg="white",bg="#072f5f",height=1,width=100)
day_lbl.pack()

day=Entry(root,width=30)
day.pack(pady=10)

text_box=Text(root,height=1.5,width=45)
text_box.pack(pady=10)


def display():
    year=int(year.get())
    month=int(month.get())
    day=int(day.get())
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()

    age = today.year - birth_date.year

    birthday_not_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    final_age = age - birthday_not_passed
    text_box.delete("1.0",END)
    message=f"Your age is:\n{final_age}"
    text_box.insert(END,message)


btn=Button(root,text="Begin",command=display,bg="#1261a0",fg="white")
btn.pack()

root.mainloop()