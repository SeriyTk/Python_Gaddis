# def  имя_функции():
# инструкция
# инструкция

def message():
    print('Я - Вася,')
    print("хороший дядя.")


def main():
    print('У меня для вас известие.')
    message()
    print('Пока!')


def acme_drye():
    startup_message()
    input('Нажмите enter, чтобы увидеть шаг №1:')
    step1()
    input('Нажмите enter, чтобы увидеть шаг №2:')
    step2()
    input('Нажмите enter, чтобы увидеть шаг №3:')
    step3()
    input('Нажмите enter, чтобы увидеть шаг №4:')
    step4()


def startup_message():
    print('Программ за 4 шага объяснит каждому тупому, как разбирать сушилку.')


def step1():
    print('Отключить сушилку и отодвинуть ее от стены.')


def step2():
    print('Удалить шесть винтов с задней стороны сушилки.')


def step3():
    print('Удалить заднюю панель сушилки.')


def step4():
    print('Вынуть верхний блок сушилки.')


acme_drye()