import random
import turtle as t

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
pointer = t.Turtle()
pointer.speed("fastest")
pointer.penup()
pointer.hideturtle()
pointer.setheading(225)
pointer.forward(300)
pointer.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    pointer.dot(20, random.choice(color_list))
    pointer.forward(50)

    if dot_count % 10 == 0:
        pointer.setheading(90)
        pointer.forward(50)
        pointer.setheading(180)
        pointer.forward(500)
        pointer.setheading(0)


screen = t.Screen()
screen.exitonclick()
