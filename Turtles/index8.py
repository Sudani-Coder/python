import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

stars = turtle.Turtle()

stars.width(5)

stars.speed(0)

for each_color in rainbow:
    stars.color(each_color)
    for star in range(0, 5):
        stars.forward(50)
        stars.right(144)
    
    stars.right(60)
    stars.penup()
    stars.forward(50)
    stars.pendown()

input()
