import turtle
from matplotlib import colors
turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(60)
turtle.pensize(1)
colors=("magenta","orange","yellow","dark green","red")

for i in range(200):
    turtle.forward(i*4)
    turtle.right(91)
    turtle.color(colors[i%5])

    for x in range(3):
        turtle.forward(x*4)
        turtle.right(91)

        for a in range(2):
            turtle.forward(a*4)
            turtle.right(91)

            for n in range(739):
                turtle.forward(n*4)
                turtle.right(891)