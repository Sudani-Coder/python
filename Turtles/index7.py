import turtle

square = turtle.Turtle()

square.width(5)

square.penup()
square.backward(140)
square.pendown()

for prettycolor in ["red", "orange", "yellow"]:
    square.color(prettycolor)

    for side in range(0, 4):
        square.forward(50)
        square.right(90)
    
    square.penup()
    square.forward(100)
    square.pendown()

input()
