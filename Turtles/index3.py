import turtle

dizzy = turtle.Turtle()

dizzy.color("dodgerblue")

dizzy.width(5)

for length in range(0, 250, 5):
    dizzy.forward(length)
    dizzy.right(90)

input()
