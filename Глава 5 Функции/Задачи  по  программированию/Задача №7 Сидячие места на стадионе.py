A = 20
B = 15
C = 10


def Seats_in_the_stadium():
    menu()
    print(f'Всего билетов было продано на сумму {stepA() + stepB() + stepC()}.')


def menu():
    print('Меню: ')
    print('1. Цена билета класса А - 20.')
    print('2. Цена билета класса B - 15.')
    print('3. Цена билета класса C - 10.')

def stepA():
    num_ticets = int(input("Сколько было куплено билетов класса А: "))
    return num_ticets * A


def stepB():
    num_ticets = int(input("Сколько было куплено билетов класса В: "))
    return num_ticets * B


def stepC():
    num_ticets = int(input("Сколько было куплено билетов класса С: "))
    return num_ticets * C



Seats_in_the_stadium()
