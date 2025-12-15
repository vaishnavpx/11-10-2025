number=int(input("Enter a number"))
binary=" "
while number>0:
    if number%2==1:
        binary="1"+binary
    else:
        binary="0"+binary
    number=int(number/2)


print(binary)
