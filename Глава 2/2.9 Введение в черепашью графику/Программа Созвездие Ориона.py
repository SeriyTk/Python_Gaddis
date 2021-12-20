import turtle as t

t.setup(500, 600)
t.hideturtle()
t.speed(0)
t.penup()
LEFT_SHOULDER_X = -70
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

t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
t.write('Бетельгейзе')
t.dot()
t.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_Y)
t.write('Хатиса')
t.dot()
t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
t.write('Альнитак')
t.dot()
t.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
t.write('Альнилам')
t.dot()
t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
t.write('Минтака')
t.dot()
t.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y)
t.write('Саиф')
t.dot()
t.goto(RIGHT_КNЕЕ_Х, RIGHT_КNЕЕ_Y)
t.write('Ригель')
t.dot()

t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
t.pendown()
t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
t.penup()
t.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_Y)
t.pendown()
t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
t.penup()
t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
t.pendown()
t.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
t.penup()
t.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
t.pendown()
t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
t.penup()
t.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
t.pendown()
t.goto(RIGHT_КNЕЕ_Х, RIGHT_КNЕЕ_Y)
t.penup()
t.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
t.pendown()
t.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y)
t.done()
