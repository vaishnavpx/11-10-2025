print("There will be a half piramid based on the number you input: ")
n=int(input("Enter the number of colums and rows in your half piramid of stars: "))

for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()