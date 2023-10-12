import turtle as t
def main():
    t.setup(500, 600)
    t.hideturtle()
    LEFT_SHOULDER_Х = -70
    LEFT_SHOULDER_Y = 200
    RIGHT_SHOULDER_Х = 80
    RIGHT_SHOULDER_Y = 180
    LEFT_BELTSTAR_Х = -40
    LEFT_BELTSTAR_Y = -20
    MIDDLE_BELTSTAR_Х = 0
    MIDDLE_BELTSTAR_Y = 0
    RIGHT_BELTSTAR_Х = 40
    RIGHT_BELTSTAR_Y = 20
    LEFT_КNЕЕ_Х = -90
    LEFT_КNЕЕ_Y = -180
    RIGHT_КNЕЕ_Х = 120
    RIGHT_КNЕЕ_Y = -140

    t.penup()
    t.goto(LEFT_SHOULDER_Х, LEFT_SHOULDER_Y)
    t.dot()
    t.write('Бeтeльгeйзe')
    t.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_Y)
    t.dot()
    t.write('Хатиса')
    t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
    t.dot()
    t.write('Альнитак')
    t.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
    t.dot()
    t.write('Aльнилaм')
    t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
    t.dot()
    t.write('Минтака')
    t.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y)
    t.dot()
    t.write('Саиф')
    t.goto(RIGHT_КNЕЕ_Х, RIGHT_КNЕЕ_Y)
    t.dot()
    t.write('Pигeль')

    # Нанести линию из левого плеча в левую звезду пояса
    t.goto(LEFT_SHOULDER_Х, LEFT_SHOULDER_Y)
    t.pendown()
    t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
    t.penup()
    # Нанести линию из правого плеча в правую звезду пояса
    t.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_Y)
    t.pendown()
    t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
    t.penup()
    # Нанести линию из левой звезды пояса в среднюю звезду пояса
    t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
    t.pendown()
    t.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
    t.penup()
    # Нанести линию из средней звезды пояса в правую звезду пояса
    t.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
    t.pendown()
    t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
    t.penup()
    # Нанести линию из левой звезды пояса в левое колено
    t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
    t.pendown()
    t.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y)
    t.penup()
    # Нанести линию из правой звезды пояса в правое колено
    t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
    t.pendown()
    t.goto(RIGHT_КNЕЕ_Х, RIGHT_КNЕЕ_Y)



    t.done()


if __name__ == '__main__': main()
