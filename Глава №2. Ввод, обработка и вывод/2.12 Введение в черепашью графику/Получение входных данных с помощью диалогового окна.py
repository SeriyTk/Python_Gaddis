import turtle as t
def main():
    radius = t.numinput('Tpeбyютcя данные','Введите радиус окружности')
    t.circle(radius)
    t.done()

    if __name__ == '__main__': main()

def main():
    radius = t.numinput('Tpeбyютcя данные','Введите значение в интервале 1-10',
                        default=5, minval=1, maxval=10)
    t.circle(radius)
    t.done()

if __name__ == '__main__': main()
