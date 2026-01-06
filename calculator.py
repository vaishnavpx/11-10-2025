def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operator=input("Enter an operator: A for Addition, B for Substraction, C for Multiplication, and D for Division: ")

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))

if operator=="A":
    print("Your answer is", add(num1,num2))

elif operator=="B":
    print("Your answer is", subtract(num1,num2))

elif operator=="C":
    print("Your answer is", multiply(num1,num2))

elif operator=="D":
    print("Your answer is", divide(num1,num2))