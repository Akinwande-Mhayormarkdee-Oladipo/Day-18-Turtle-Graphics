# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("Hirst.jpg",12)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
#
# print(rgb_colors)

import turtle as turtle
import random
#
turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

color_list = [(237, 240, 243), (237, 233, 224), (226, 231, 229), (21, 27, 46), (239, 231, 236), (52, 27, 40), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



# import turtle as turtle
import random

# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('blue')


# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# for draw_segment in range(15):
#     timmy.forward(30)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#
# timmy.speed("fastest")
# turtle.colormode(255)


# def random_color():
#     return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#
#
# def draw(gap_size):
#     for i in range(int(360/gap_size)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.tilt(45)
#         timmy.setheading(timmy.heading() + gap_size)
#
# draw(20)




#
#
#
#
screen = turtle.Screen()
screen.exitonclick()


