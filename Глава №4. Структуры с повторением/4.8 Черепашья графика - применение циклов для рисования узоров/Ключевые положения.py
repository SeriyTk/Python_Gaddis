import turtle as t
NUM_CIRCLES = 36
STARTING_RADIUS = 20
OFFSET = 10
RADIUS = 100
ANGLE = 170
START_Х = -200
START_Y = 0
NUM_LINES = 36
LINE_LENGTH = 400
ANIМATION_SPEED = 0
def concentric_circles():
    t.speed(ANIМATION_SPEED)
    t.hideturtle()
    radius = STARTING_RADIUS

    for count in range(NUM_CIRCLES):
        t.circle(radius)
        x = t.xcor()
        y = t.ycor() - OFFSET

        radius += OFFSET

        t.penup()
        t.goto(x, y)
        t.pendown()

    t.done()


    if __name__ == '__main__': concentric_circles = concentric_circles()

def spiral_circles():
    t.speed(ANIМATION_SPEED)
    for x in range(NUM_CIRCLES):
        t.circle(RADIUS)
        t.left(ANGLE)

    t.done()

    if __name__ == '__main__': spiral_circles = spiral_circles()

def spiral_line():
    t.hideturtle()
    t.penup()
    t.goto(START_Х, START_Y)
    t.pendown()
    t.speed(ANIМATION_SPEED)
    for x in range(NUM_LINES):
        t.forward(LINE_LENGTH)
        t.left(ANGLE)

    t.done()

if __name__ == '__main__': spiral_line = spiral_line()
