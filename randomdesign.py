from turtle import *
import turtle
import random

a=turtle.Turtle()
s=turtle.Screen()

a.speed(10)
s.bgcolor("black")
b=random.randint(0,250)
print(b)
col=('white','red','cyan','pink','yellow')

for i in range(300):
    a.pencolor(col[i%5])
    a.forward(i*3)
    a.right(b)
   
