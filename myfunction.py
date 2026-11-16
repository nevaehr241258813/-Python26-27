
import turtle

def draw_petal(t,size,color):
    t.color(color)
    t.pensize(3)
    t.begin_fill()

    t.fillcolor(color)

    for i in range(2):
        t.circle(size,60)
        t.left(120)

    t.end_fill()

def draw_flower(t):
    colors=["pink","pink","pink","pink","pink","pink","pink","pink"]

    for color in colors:
        draw_petal(t,100,color)
        t.left(45)
