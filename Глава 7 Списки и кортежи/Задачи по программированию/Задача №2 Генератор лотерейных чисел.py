import random as rnd


def Lottery_number_generator(par):
    lottery_number = []
    for i in range(par):
        lottery_number.append(rnd.randint(0, 9))
    for j in lottery_number:
        print(j, end=' ')


Lottery_number_generator(7)
