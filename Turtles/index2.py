import turtle

amy = turtle.Turtle()

amy.color("dodgerblue")

for side in [1, 2, 3]:
    amy.forward(100)
    amy.right(120)
    amy.forward(100)
    amy.left(120)
    amy.forward(100)
    amy.right(120)

input()
