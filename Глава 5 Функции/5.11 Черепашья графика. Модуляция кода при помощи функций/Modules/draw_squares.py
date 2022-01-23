import turtle as t


def squares(x, y, width, color):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()

