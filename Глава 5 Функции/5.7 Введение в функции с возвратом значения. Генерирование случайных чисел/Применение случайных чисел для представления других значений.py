import random as rm


def coin_toss(tos):
    ОРЕЛ = 1
    РЕШКА = 2
    for i in range(tos):
        if rm.randint(ОРЕЛ, РЕШКА) == ОРЕЛ:
            print('ОРЕЛ')
        else:
            print('РЕШКА')


coin_toss(10)
