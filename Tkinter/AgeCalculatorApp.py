import datetime
from tkinter import *

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

year_lbl = Label(
    root,
    text="Enter your birth year",
    fg="white",
    bg="#072f5f",
    height=1,
    width=100,
)
year_lbl.pack()
year_entry = Entry(root, width=30)
year_entry.pack(pady=10)

month_lbl = Label(root, text="Enter your birth month", bg="#3895d3", width=400)
month_lbl.pack(pady=10)
month_entry = Entry(
    root, width=30
)
month_entry.pack(pady=10)

day_lbl = Label(
    root,
    text="Enter your birth day",
    fg="white",
    bg="#072f5f",
    height=1,
    width=100,
)
day_lbl.pack()
day_entry = Entry(root, width=30)
day_entry.pack(pady=10)

text_box = Text(root, height=1.5, width=45)
text_box.pack(pady=10)


def display():
    y = int(year_entry.get().strip())
    m = int(month_entry.get().strip())
    d = int(day_entry.get().strip())

    birth_date = datetime.date(y, m, d)
    today = datetime.date.today()

    age = today.year - birth_date.year
    birthday_not_passed = (today.month, today.day) < (
        birth_date.month,
        birth_date.day,
    )
    final_age = age - birthday_not_passed

    text_box.delete("1.0", END)
    message = f"Your age is: {final_age}"
    text_box.insert(END, message)


btn = Button(root, text="Begin", command=display, bg="#1261a0", fg="white")
btn.pack()

root.mainloop()
