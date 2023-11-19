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
    t.goto(TARGET_LLEFT_Х, TARGET_LLEFT_Y)
    t.pendown()
    t.setheading(EAST)
    t.forward(TARGET_WIDTH)
    t.setheading(NORTH)
    t.forward(TARGET_WIDTH)
    t.setheading(WEST)
    t.forward(TARGET_WIDTH)
    t.setheading(SOUTH)
    t.forward(TARGET_WIDTH)
    t.penup()

    t.goto(0, 0)
    t.setheading(EAST)
    t.showturtle()
    t.speed(PROJECTILE_SPEED)

    angle = float(input("Bвeдитe угол выстрела снаряда: "))
    force = float(input("Bвeдитe пусковую силу (1-10): "))

    distance = force * FORCE_FACTOR
    t.setheading(angle)

    t.pendown()
    t.forward(distance)

    if (t.xcor() >= TARGET_LLEFT_Х and
        t.xcor() <= (TARGET_LLEFT_Х + TARGET_WIDTH) and
        t.ycor() >= TARGET_LLEFT_Y and
        t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)): print('Цель поражена!')
    else: print( 'Вы промахнулись. ' )
    t.done()


if __name__ == '__main__': hit_the_target = hit_the_target()
