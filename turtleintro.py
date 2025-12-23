import turtle   #inporting library
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle() #defined variable


#iterate loop for total number of sides
for i in range(2):
    polygon.forward(100)
    polygon.right(90)
    polygon.forward(70)
    polygon.right(90)

turtle.done()