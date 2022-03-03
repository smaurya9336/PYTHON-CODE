from tkinter import N
import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")

t.speed(95)
n=80
h=0

for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h +=1/n
    t.color(c)

    for j in range(2):
        t.left(90)
        t.forward(i*2)

        for v in range(3):
            t.left(30)
            t.forward(i*3)
            t.right(90)

