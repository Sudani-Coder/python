import turtle

home = turtle.Turtle()

home.color("dodgerblue")

home.width(5)

angles = [
    -90, 0, 0, -90,
    135, 0, 0, 0,
    90, 0, 0, 0,
    135, -90, 0, 0,
    90, 0, 0, 0
]

for angle in angles:
    home.right(angle)
    home.forward(35)

input()
