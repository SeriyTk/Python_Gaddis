import turtle as t

t.hideturtle()
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.goto(50,10)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(40)
t.end_fill()
t.done()
