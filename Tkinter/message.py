from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x500")
def msg():
    messagebox.showwarning("Alert!","Stop, this may be a virus")
def msg1():
    messagebox.showerror("Error!","Error found please check code")
def msg2():
    messagebox.showinfo("Info!","Display information")
def msg3():
    messagebox.askquestion("Ask!","Are you ready?")
def msg4():
    messagebox.askokcancel("Ask!","This program was created")
def msg5():
    messagebox.askyesno("Ask!","Are you a human?")
def msg6():
    messagebox.askretrycancel("Oops!","Oops! the program did not execute")


button=Button(root,text="Scan for virus",command=msg)
button.place(x=40,y=50)
button=Button(root,text="Error message",command=msg1)
button.place(x=40,y=100)
button=Button(root,text="Show info",command=msg2)
button.place(x=40,y=150)
button=Button(root,text="Ask question",command=msg3)
button.place(x=40,y=200)
button=Button(root,text="Ok or cancel",command=msg4)
button.place(x=40,y=250)
button=Button(root,text="Human or not",command=msg5)
button.place(x=40,y=300)
button=Button(root,text="Oops!",command=msg6)
button.place(x=40,y=350)

root.mainloop()