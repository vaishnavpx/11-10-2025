from tkinter import *
root=Tk()
root.title("Login App")
root.geometry("400x400")

frame=Frame(master=root,height=200,width=360,bg="#d0efff")
lbl1=Label(frame,text="Full Name",bg="#3895d3",fg="white",width=12)
lbl2=Label(frame,text="Email",bg="#3895d3",fg="white",width=12)
lbl3=Label(frame,text="Password",bg="#3895d3",fg="white",width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

def display():
    name=name_entry.get()
    greet="Hey "+name
    message="\nCongratulations on your new account"
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(bg="#BEBEBE",fg="black")
btn=Button(text="Create Account",command=display,bg="red")
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)