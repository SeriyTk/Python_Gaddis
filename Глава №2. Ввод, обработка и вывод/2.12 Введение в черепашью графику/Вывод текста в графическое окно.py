import turtle as t
def main():
    t.setup(400, 300)
    t.penup()
    t.hideturtle()
    t.goto(-120, 120)
    t.write('Cлeвa вверху')
    t.goto(70, -120)
    t.write('Cпpaвa внизу')
    t.done()

if __name__ == '__main__': main()
