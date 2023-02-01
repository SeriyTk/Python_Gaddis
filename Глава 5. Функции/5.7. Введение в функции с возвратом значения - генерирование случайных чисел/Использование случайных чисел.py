import random as r
MIN = 1
MAX = 6
def dice():
    while True:
        print('Бросаем кубики ... ')
        print('Значения граней: ')
        print(r.randint(MIN, MAX))
        print(r.randint(MIN, MAX))
        again = input('Бросить кубики? (enter == да): ')
        if again != "": print("Программа завершена."); break

if __name__ == '__main__': dice()