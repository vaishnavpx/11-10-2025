import turtle   #inporting library
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
shape=turtle.Turtle() #defined variable


for i in range(3):
    shape.forward(70)
    shape.right(120)

shape.right(90)
shape.penup()
shape.forward(40)
shape.pendown()
shape.left(90)

for i in range(3):
    shape.forward(70)
    shape.left(120)

turtle.done()