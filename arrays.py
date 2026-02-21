import array as arr

array_num=arr.array("i",[1,3,5,3,7,9,3])
print("Original array: "+str(array_num))

print("Number of occurences of the number 3 in the said array: "+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))

a=arr.array("i",[1,2,3])

print("\nThe new created array is: ",end="")
for i in range(0,3):
    print(a[i],end="")
print()

b=arr.array("d",[2.5,3.2,3.3])

print("\nThe new created array is: ",end="")
for i in range(0,3):
    print(b[i],end="")

a.insert(1,4)

print("\nArray after insertion: ",end="")
for i in (a):
    print(i,end="")
print()

b.append(4.4)

print("\nArray after insertion: ",end="")
for i in (b):
    print(i,end="")
print()

print("Access element is: ",a[0])
print("Access element is: ",b[2])