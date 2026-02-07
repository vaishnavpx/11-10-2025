rainy=0
sunny=0
weather=(0,0,0,0,0,1,1)

for i in range(0,8):
    if i==1:
        rainy+=1
    else:
        sunny+=1

if sunny>rainy:
    print("It will be more sunny than rainy")
elif rainy>sunny:
    print("It will be more rainy than sunny")