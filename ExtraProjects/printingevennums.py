lower=int(input("Enter the lower number: "))
higher=int(input("Enter the higher number: "))
n=0

for i in range(0,higher+1):
    if n%2==0 and n>lower-1:
        print(n)
    n=n+1