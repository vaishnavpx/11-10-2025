L=[4,5,1,2,9,7,10,8]
print("Original list: ",L)

count=0
for i in L:
    count+=i

avg=count/len(L)
print("sum equals: ", count)
print("average equals: ", avg)
L.sort()

print("smallest element is: ",L[0])
print("largest element is: ",L[-1])