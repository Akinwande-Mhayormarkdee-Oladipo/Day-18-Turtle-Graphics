from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')


# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# for draw_segment in range(15):
#     timmy.forward(30)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


no_of_sides = 4
side_length = 100
angle = 360 / no_of_sides

while no_of_sides < 8:

    for _ in range(no_of_sides):
        timmy.forward(side_length)
        timmy.right(angle)

    no_of_sides += 1














screen = Screen()
screen.exitonclick()