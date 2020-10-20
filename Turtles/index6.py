import turtle

paul = turtle.Turtle()

paul.color("dodgerblue")

sides = list(range(0, 4))

for side in sides:
    paul.forward(100)
    paul.right(90)

    for side in sides:
        paul.forward(10)
        paul.right(90)

input()
