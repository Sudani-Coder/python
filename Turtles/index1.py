import turtle

george = turtle.Turtle()

george.width(5)

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

for side in rainbow:
    george.color(side)
    george.forward(120)
    george.right(60)

michael = turtle.Turtle()

michael.width(5)

michael.color("red")

michael.penup()

michael.left(120)
michael.forward(300)
michael.right(120)

michael.pendown()

for side in range(0, 9):
    michael.forward(100)
    michael.right(45)

input()
