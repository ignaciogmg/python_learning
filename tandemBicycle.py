import turtle
from math import log, sqrt

window = turtle.Screen()
window.bgcolor("black")

anita = turtle.Turtle()
anita.speed(0)
anita.color("yellow")
anita.pensize(5)

anita.penup()
anita.goto(-100, -200)
anita.pendown()

for n in range(1, 7400, 5):
    anita.left(sqrt(n / 2 * (n + 60)))
    anita.forward(log(n + n / 2))

window.exitonclick()
