from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def shape(n1):
    angle = 360 / n1
    for i in range(n1):

        timmy.forward(100)
        timmy.rt(angle)

for n in range(3, 11):
    shape(n)

Screen().exitonclick()
