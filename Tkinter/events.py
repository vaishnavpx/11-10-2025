from tkinter import *
window=Tk()
window.title("Length Converter App")
window.geometry("400x400")

lbl=Label(window,text="Enter a number to be converted from inches to centimeters",fg="white",bg="#072f5f",height=1,width=100)
lbl.pack()

cm_entry = Entry(window,width=30)
cm_entry.pack(pady=10)

text_box = Text(window,height=4,width=45)
text_box.pack(pady=10)

def display():
    text_box.delete("1.0", END)
    try:
        cm_value = float(cm_entry.get())
    except ValueError:
        text_box.insert(END, "Please enter a valid number.")
        return

    inches = cm_value * 2.54
    message = f"Your length in inches converted to centimeters is:\n{inches:.4f}"
    text_box.insert(END, message)

btn = Button(window, text="Begin", command=display, bg="#1261a0", fg="white")
btn.pack()

window.mainloop()