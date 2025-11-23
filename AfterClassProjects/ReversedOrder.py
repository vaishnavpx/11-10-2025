output=0
sum=0
num=int(input("Enter a number: "))
i=num
while i>0:
    digit=i%10
    sum+=digit**3
    i//=10
    output=output+1

print(f"Your number has {output} didgets")