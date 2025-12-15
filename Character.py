word=input("enter a word: ")
char=input("enter a letter from the word: ")
i=0
count=0

while(i<len(word)):
    if(word[i]==char):
        count=count+1

    i=i+1

print(f"The total number of times {char} has occured in {word} is {count}.")