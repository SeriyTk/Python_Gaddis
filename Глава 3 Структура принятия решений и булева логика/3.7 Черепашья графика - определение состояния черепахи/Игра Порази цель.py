import turtle as t


def hit_the_target():
    t.setup(600, 600)
    t.hideturtle()
    t.speed(0)
    TARGET_X = 100
    TARGET_Y = 250
    TARGET_WIDTH = 25
    FORCE = 30
    ANIME_SPEED = 1
    t.penup()
    get_target(TARGET_X, TARGET_Y, TARGET_WIDTH)  # Нарисовать цель
    t.penup()
    get_initial_position(ANIME_SPEED)  # Центрировать черепаху
    angle = float(input('Введите угол: '))
    force = float(input('Введите дальность: '))
    distance = force * FORCE
    t.setheading(angle)

    t.pendown()
    t.forward(distance)
    get_shell_hit(TARGET_X, TARGET_Y, TARGET_WIDTH)


def get_target(TARGET_X, TARGET_Y, TARGET_WIDTH):
    t.goto(TARGET_X, TARGET_Y)
    t.pendown()
    for i in range(4):
        t.forward(TARGET_WIDTH)
        t.left(90)


def get_initial_position(ANIME_SPEED):
    t.goto(0, 0)
    t.showturtle()
    t.speed(ANIME_SPEED)


def get_shell_hit(TARGET_X, TARGET_Y, TARGET_WIDTH):
    if (TARGET_X <= t.xcor() <= (TARGET_X + TARGET_WIDTH) and
            TARGET_Y <= t.ycor() <= (TARGET_Y + TARGET_WIDTH)):
        print('Цель поражена.')
    else:
        print("Цель не поражена.")


hit_the_target()
t.done()
