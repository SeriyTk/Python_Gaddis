import  turtle as t
t.hideturtle()
t.speed(10)

def square(x, y, width, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for count in range(4): t.forward(width); t.left(90)
    t.end_fill()

def cirle(x,y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
