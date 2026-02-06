lower=int(input("Enter the lower value: "))
higher=int(input("Enter the higher value: "))
odd=[]
even=[]

for i in range(lower,higher+1):
    i2=i*i
    if i2%2==0:
        even.append(i2)
    else:
        odd.append(i2)

print("EVEN:")
print(even)
print("ODD:")
print(odd)