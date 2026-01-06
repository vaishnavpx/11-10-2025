print("From what numbers should I find even numbers from?")
lower=int(input("From: "))
higher=int(input("To: "))
Range=higher-lower+1

for i in range(lower,higher+1):
    if i%2 == 0:
        for j in range(Range):
            print(i)