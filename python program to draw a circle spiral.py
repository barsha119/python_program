from turtle import Turtle, Screen
import random

timmy = Turtle()

colors = ["gold", "navy", "saddle brown", "maroon", "dark slate blue", "hot pink", "orange", "green"]
direction = [0, 90, 180, 270]

timmy.speed("fastest")

for i in range(72):
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 5)



# screen = Screen()
Screen().exitonclick()
