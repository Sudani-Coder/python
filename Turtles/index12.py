import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def triangle_boogie(color = "red", width = 3):
    t = turtle.Turtle()
    t.color(color)
    t.speed(0)
    t.width(width)
    for shape in range(3):
        for side in range(3):
            t.forward(150)
            t.right(135)

# Call the function multiple times.
triangle_boogie("dodgerblue", 5)

input()
