n = int(input("Enter a number: "))
oddnums = [num for num in range(1, n, 2)]
print(oddnums)





fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits2 = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Capitalized fruits:", fruits2)