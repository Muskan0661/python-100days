import random
import turtle as t

t.colormode(255)

tim = t.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (255, 99, 71),
    (255, 165, 0),
    (255, 215, 0),
    (50, 205, 50),
    (64, 224, 208),
    (30, 144, 255),
    (138, 43, 226),
    (255, 105, 180),
    (220, 20, 60),
    (255, 127, 80),
    (75, 0, 130),
    (0, 191, 255),
    (154, 205, 50),
    (255, 20, 147),
    (255, 192, 203),
    (46, 139, 87)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for row in range(10):

    for column in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

t.done()
