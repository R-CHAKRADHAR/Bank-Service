import turtle
import random

tur = turtle.Turtle()
scr = turtle.Screen()

tur.shape("turtle")
tur.color("red")
tur.speed("fastest")
for i in range(150):
    tur.forward(random.randint(1,100))
    tur.right(90)
    tur.forward(random.randint(1,100))
    tur.right(90)

scr.exitonclick()