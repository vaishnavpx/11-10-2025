import datetime
from tkinter import *

root = Tk()
root.title("Interest Calculator App")
root.geometry("400x400")

p_lbl = Label(
    root,
    text="Enter principal amount",
    fg="white",
    bg="#072f5f",
    height=1,
    width=100,
)
p_lbl.pack()
p_entry = Entry(root, width=30)
p_entry.pack(pady=10)

y_lbl = Label(root, text="Enter years", bg="#3895d3", width=400)
y_lbl.pack(pady=10)
y_entry = Entry(
    root, width=30
)
y_entry.pack(pady=10)

r_lbl = Label(
    root,
    text="Enter interest rate as percentage",
    fg="white",
    bg="#072f5f",
    height=1,
    width=100,
)
r_lbl.pack()
r_entry = Entry(root, width=30)
r_entry.pack(pady=10)

text_box = Text(root, height=3, width=45)
text_box.pack(pady=10)


def display():
    try:
        p = float(p_entry.get().strip())
        y = float(y_entry.get().strip())
        r = float(r_entry.get().strip()) / 100.0
    except ValueError:
        text_box.delete("1.0", END)
        text_box.insert(END, "Please enter valid numbers for principal, years, and rate.")
        return

    simple_i = p * y * r
    amount = p * (1 + r) ** y
    compound_i = amount - p

    text_box.delete("1.0", END)
    text_box.insert(END, f"Simple Interest: {simple_i:.2f}\nCompound Interest: {compound_i:.2f}\nTotal Amount: {amount:.2f}")


btn = Button(root, text="Begin", command=display, bg="#1261a0", fg="white")
btn.pack()

root.mainloop()
