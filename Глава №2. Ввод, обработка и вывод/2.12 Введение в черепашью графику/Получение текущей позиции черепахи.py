import turtle as t
def main():
    t.hideturtle()
    t.goto(0, 100)
    print(t.xcor())
    print(t.ycor())
    t.goto(-100, 0)
    print(t.pos())
    t.goto(0, 0)
    print(t.pos())
    t.done()

if __name__ == '__main__': main()
