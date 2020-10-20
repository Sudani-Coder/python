import turtle

sara = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
sara.width(5)

# Move back without drawing anything
sara.penup()
sara.back(140)
sara.pendown()

# Draw three lines of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    sara.color(prettycolor)
    sara.forward(50)
    sara.penup()
    sara.forward(50)
    sara.pendown()

input()
