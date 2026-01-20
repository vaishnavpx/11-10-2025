try:
    age=int(input("Enter your age: "))

except:
    print("This is an invalid age")

if age%2==0:
    print("Your age is an even number")
else:
    print("Your age is an odd number")