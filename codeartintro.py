import turtle
t=turtle.Turtle()
#this is how i position the turtle
t.penup()
t.goto(-100, -100)
t.pendown()
#this is how i made the triangle
colors=["Coral", "MediumSpringGreen", "Aqua"]
for i in range(100):
    t.color( colors[i % 3])
    t.forward(8)
    t.left( 120 )


#bellow this is how you make the spiral
t.forward(100)
t.left(60)
t.forward(100)
t.left(70),
t.forward(100)
t.left(80)
t.forward(100)
t.left(90)
t.forward(100)
t.left(100)
t.forward(100)
t.left(1100)

turtle.exitonclick()