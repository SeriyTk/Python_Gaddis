import turtle as t
t.hideturtle()
t.speed(0)
WIDTH = 10
STEP = 5
for i in range(100):
    for j in range(4):
        t.forward(WIDTH + (i * STEP))
        t.left(90)
t.done()
