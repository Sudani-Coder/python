import turtle

def spiral(sides = 100, turn = 20, color = "cyan", width = 3):
    john = turtle.Turtle()
    john.color(color)
    john.width(width)
    for side in range(sides):
        john.forward(side)
        john.right(turn)

spiral(150, 45, "dodgerblue"); input()
