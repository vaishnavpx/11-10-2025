num=int(input("Enter a number: "))

for num in range(1,num+1):
    if num%20==0:
        print("WEEE!")

    elif num%15==0:
        pass

    elif num%5==0:
        print("FIZZ")

    elif num%3==0:
        print("BUZZ")

    else:
        print(num)