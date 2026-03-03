numbers=[1,2,3,4,5,6]
even=[x for x in numbers if x%2==0]
print("List of even numbers from original", even)

myDict={str(x):x**2 for x in [1,2,3,4,5]}
print(myDict)