import turtle   #inporting library
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
shape=turtle.Turtle() #defined variable

distance=10

for i in range(25):
    shape.forward(distance)
    shape.right(90)
    distance=distance+10

turtle.done()