import calendar

yy=int(input("Enter a year: "))
mm=int(input("Enter a month: "))

if mm==1:
    print("January")
elif mm==2:
    print("Febuary")
elif mm==3:
    print("March")
elif mm==4:
    print("April")
elif mm==5:
    print("May")
elif mm==6:
    print("June")
elif mm==7:
    print("July")
elif mm==8:
    print("August")
elif mm==9:
    print("September")
elif mm==10:
    print("October")
elif mm==11:
    print("November")
elif mm==12:
    print("December")
else:
    print("ERROR: PLEASE ENTER A NUMBER BETWEEN 1 AND 12")


print(calendar.month(yy,mm))
