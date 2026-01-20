import random
playing=True
number=str(random.randint(0,10))

print("I will generate a number between 0 and 10. Guess the number one at a time.")
print("The game ends when you guess the number correctly.")

while playing:
    guess=input("Give me your best guess!\n")
    if number==guess:
        print("You win the game!")
        print("The number was",number)
        break
    else:
        print("Your guess isn't quit right, try again\n")