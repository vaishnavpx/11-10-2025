import random
import string

password_len=random.randint(5,15)
password=" "
for i in range(password_len):
    all_letters=string.ascii_letters
    random_letter=random.choice(all_letters)
    random_num=random.randint(0,9)
    password_didgit=random.randint(0,1)
    if password_didgit==0:
        password=password+random_letter
    elif password_didgit==1:
        password=password+str(random_num)

print("Your random password is: \n", password)