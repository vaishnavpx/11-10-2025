sum=0
n=int(input("Enter a number: "))
i=n
while i>0:
    digit=i%10
    sum+=digit**3
    i//=10

if n==sum:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
