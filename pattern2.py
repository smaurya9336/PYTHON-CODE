from turtle import *
from random import randint
bgcolor('black')
speed(5)
for i in range(10):
    for j in range(4):
        pu()
        goto(50,100)
        pd()
        colormode(255)
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        color(r,g,b)
        pensize(3)
        circle(100,steps=6)
        rt(100)
hideturtle()
done()