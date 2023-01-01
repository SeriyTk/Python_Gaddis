import turtle as t

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_Х = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
def hit_the_target():
    t.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(TARGET_LLEFT_Y, TARGET_LLEFT_Y)
    t.pendown()
    for i in range(4): t.forward(TARGET_WIDTH); t.left(90)
    t.penup()

    t.goto(0, 0)
    t.setheading(EAST)
    t.showturtle()
    t.speed(PROJECTILE_SPEED)

    angle = float(input('Введите угол: '))
    force = float(input('Введите пусковую силу (1 - 10): '))

    distance = force * FORCE_FACTOR

    t.setheading(angle)

    t.pendown()
    t.forward(distance)

    if (t.xcor() >= TARGET_LLEFT_Y and t.xcor() <= (TARGET_LLEFT_Х + TARGET_WIDTH) and
        t.ycor() >= TARGET_LLEFT_Y and t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)
    ): print('Цель.')
    else: print("Промах")



hit_the_target()

t.done()