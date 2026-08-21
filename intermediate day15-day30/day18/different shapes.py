import turtle as t
import random

tim = t.Turtle()

colors=["blue","pink","red","purple","yellow","green","black"]
def draw_shapes(num_sides):
    angle = 360 / num_sides
    
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)
    
for shape in range(3,10):
    tim.color(random.choice(colors))
    draw_shapes(shape)
        

    
