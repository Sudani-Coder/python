import turtle

tom = turtle.Turtle()

tom.color("cyan")

tom.width(3)

for side in range(22):
    tom.forward(side * 10)
    tom.right(360 / 3)

input()
