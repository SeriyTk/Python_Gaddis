import turtle as t
t.hideturtle()
t.speed(0)
t.setheading(45)
t.fillcolor('grey')
t.begin_fill()
for i in range(4):
    t.forward(150)
    t.right(90)
t.end_fill()
t.setheading(135)
t.fillcolor('grey')
t.begin_fill()
for i in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()
t.done()