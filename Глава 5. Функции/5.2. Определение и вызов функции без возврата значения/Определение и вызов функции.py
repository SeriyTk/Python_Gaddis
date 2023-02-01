'''def имя_функции():
    инструкция
    инструкция
    . . .
'''
def message():
    print ('Я - Артур, король британцев.')

message()
print()
def two_functions():
    print('У меня для вас известие. ')
    message()
    print('До свидания! ')

if __name__ == '__main__': two_functions()
print()
def acme_drye():
    startup_message()
    input('Нажмите Enter, чтобы увидеть шаг 1.')
    step1()
    input('Нажмите Enter, чтобы увидеть шаг 2.')
    step2()
    input('Нажмите Enter, чтобы увидеть шаг 3.')
    step3()
    input('Нажмите Enter, чтобы увидеть шаг 4.')
    step4()

def startup_message():
    print('Этa программа дает рекомендации')
    print('пo разборке бельевой суимлки фирмы АСМЕ. ')
    print('Данный процесс состоит из 4 шагов.')
    print()
def step1():
    print('Шаг 1 : отключить сушилку и отодвинуть ее от стены.')
    print()
def step2():
    print('Шaг 2: удалить шесть винтов с задней стороны сушилки.')
    print()
def step3():
    print('Шaг 3: удалить заднюю панель сушилки.')
    print()
def step4():
    print('Шаг 4 : вынуть верхний блок сушилки.')
if __name__ == '__main__': acme_drye()


