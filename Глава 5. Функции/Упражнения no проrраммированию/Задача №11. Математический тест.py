import random as r
def Math_Test():
    num_1 = r.randint(1, 300)
    num_2 = r.randint(1, 300)
    print('', num_1)
    print('+', num_2)
    answer = int(input("Ответ: "))
    if answer == num_1 + num_2: print('Правильно.')
    else: print("Не правильно. Правильно будет", num_1 + num_2)


if __name__ == '__main__': Math_Test()