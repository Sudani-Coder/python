import turtle

pentagon = turtle.Turtle()

pentagon.color("dodgerblue")

length = 100

sides = 5

for side in range(sides):
    pentagon.forward(length)
    pentagon.right(360 / sides)

input()
