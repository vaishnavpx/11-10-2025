def cube(num):
    cubed_num=num**3
    print(f"The number cubed is {cubed_num}")

def divisible_by_three(num):
    if num%3==0:
        cube(num)
    else:
        print("number is not divisible by three.")
num=int(input("Enter a number to be cubed: "))

divisible_by_three(num)

print("___________________________________________________________________________________________________")

def cube(num):
    cubed_num=num**3
    return cubed_num
def divisible_by_three(num):
    if num%3==0:
        print("The cube of the given number",cube(num))
    else:
        print("number is not divisible by three.")
num=int(input("Enter a number to be cubed: "))

divisible_by_three(num)
