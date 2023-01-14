import turtle as t
def concentric_circle():
    NUM_CIRCLES = 20
    STARTING_RADIUS = 20
    OFFSET = 10
    ANIМATION_SPEED = 0
    t.speed(ANIМATION_SPEED)
    t.hideturtle()
    for count in range(NUM_CIRCLES):
        t.circle(STARTING_RADIUS)

        x = t.xcor()
        y = t.ycor() - OFFSET

        STARTING_RADIUS += OFFSET

        t.penup()
        t.goto(x, y)
        t.pendown()


concentric_circle()

t.done()