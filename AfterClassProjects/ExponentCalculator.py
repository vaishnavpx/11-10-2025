num=int(input("Enter a number: "))
exponent=int(input("Enter the exponent number: "))
ans=1

for i in range(exponent):
    ans=ans*num
print(ans)