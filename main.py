# import colorgram
# rgbcolors = []
# colors = colorgram.extract("colordots.jpg",30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgbcolors.append(new_color)
#
# print(rgbcolors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
timmya = turtle_module.Turtle()
timmya.penup()
color_list = [(253, 251, 249), (253, 250, 253), (249, 250, 252), (236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234), (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166), (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98), (98, 96, 186)]
timmya.setheading(225)
timmya.forward(300)
timmya.setheading(0)

num_of_dots = 100

for dots in range(1 , num_of_dots + 1):
    timmya.dot(20, random.choice(color_list))
    timmya.forward(50)
    if dots % 10 == 0:
        timmya.setheading(90)
        timmya.forward(50)
        timmya.setheading(180)
        timmya.forward(500)
        timmya.setheading(0)

timmya.hideturtle()

screen = turtle_module.Screen()
screen.exitonclick()