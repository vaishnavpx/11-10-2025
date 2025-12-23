n=int(input("Enter the number of colums and rows in your half piramid of stars: "))

for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("* ",end=" ")
    print()