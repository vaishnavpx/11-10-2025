try:
    num1,num2=eval(input("Enter two numbers, seperated by a comma: "))
    result=num1/num2
    print("The result is", result)

except ZeroDivisionError:
    print("Division by zero is an error!!!")

except SyntaxError:
    print("Comma missing. Enter numbers seperated by comma like this: 1,2")

except:
    print("Wrong input")

else:
    print("no exceptions")

finally:
    print("This will print no matter what")