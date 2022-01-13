import turtle as t

t.hideturtle()
t.speed(0)
RADIUS = 10
STEP = 10
CIRCLES = 50
for i in range(CIRCLES):
    t.circle(RADIUS)
    x = t.xcor()
    y = t.ycor() - STEP
    RADIUS = RADIUS + STEP
    t.penup()
    t.goto(x, y)
    t.pendown()
t.done()
