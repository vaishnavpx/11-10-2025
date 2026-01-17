
try:
    number=int(input("Enter a number: "))
    print(f"The number entered is {number}")

except ValueError as ex:
    print("Exception:", ex)


try:
    number=int(input("Enter a number: "))
    print(f"The number entered is {number}")

except:
    print("Enter a number only please")