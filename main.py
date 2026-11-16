import turtle
from myfunction import draw_flower

screen=turtle.Screen()
screen.title("Rainbow Dream Flower")

t=turtle.Turtle()
t.speed(0)
t.pensize(3)

draw_flower(t)
t.penup()
t.goto(150,0)
t.pendown()
draw_flower(t)
t.penup()
t.goto(-150,0)
t.pendown()
draw_flower(t)
t.dot(30,"yellow")

t.penup()
t.goto(150,0)
t.pendwon()

draw_flower(t)
t.dot(30,"yellow")

t.penup()
t.goto(-150,0)
t.pendown()

draw_flower(t)
t.dot(30,"yellow")

t.hideturtle(t)
turtle.done()
