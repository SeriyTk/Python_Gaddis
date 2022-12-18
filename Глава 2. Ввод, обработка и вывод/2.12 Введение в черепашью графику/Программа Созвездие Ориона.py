import turtle as tlt

def orion():
    tlt.setup(500, 600)
    tlt.speed(1)
    tlt.penup()
    tlt.hideturtle()

    LEFT_SHOULDER_Х = -70
    LEFT_SHOULDER_Y = 200

    RIGHT_SHOULDER_X = 80
    RIGHT_SHOULDER_Y = 180

    LEFT_BELTSTAR_X = -40
    LEFT_BELTSTAR_Y = -20

    MIDDLE_BELTSTAR_X = 0
    MIDDLE_BELTSTAR_Y = 0

    RIGHT_BELTSTAR_X = 40
    RIGHT_BELTSTAR_Y = 20

    LEFT_КNЕЕ_X = -90
    LEFT_КNЕЕ_Y = -180

    RIGHT_КNЕЕ_X = 120
    RIGHT_КNЕЕ_Y = -140

    tlt.goto(LEFT_SHOULDER_Х, LEFT_SHOULDER_Y)
    tlt.dot()
    tlt.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    tlt.dot()
    tlt.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    tlt.dot()
    tlt.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    tlt.dot()
    tlt.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    tlt.dot()
    tlt.goto(LEFT_КNЕЕ_X, LEFT_КNЕЕ_Y)
    tlt.dot()
    tlt.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y)
    tlt.dot()

    tlt.goto(LEFT_SHOULDER_Х, LEFT_SHOULDER_Y)
    tlt.write('Бетельгейзе')
    tlt.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    tlt.write('Хатиса')
    tlt.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    tlt.write('Альнитак')
    tlt.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    tlt.write('Альнилам')
    tlt.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    tlt.write('Минтака')
    tlt.goto(LEFT_КNЕЕ_X, LEFT_КNЕЕ_Y)
    tlt.write('Саиф')
    tlt.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y)
    tlt.write('Ригель')

    tlt.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    tlt.pendown()
    tlt.goto(LEFT_SHOULDER_Х, LEFT_SHOULDER_Y)
    tlt.penup()

    tlt.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    tlt.pendown()
    tlt.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    tlt.penup()

    tlt.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    tlt.pendown()
    tlt.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    tlt.penup()

    tlt.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    tlt.pendown()
    tlt.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    tlt.penup()

    tlt.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    tlt.pendown()
    tlt.goto(LEFT_КNЕЕ_X, LEFT_КNЕЕ_Y)
    tlt.penup()

    tlt.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    tlt.pendown()
    tlt.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y)
    tlt.penup()

orion()
tlt.done()


