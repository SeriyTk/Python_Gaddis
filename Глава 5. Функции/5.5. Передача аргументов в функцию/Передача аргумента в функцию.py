def cups_to_ounces():
    intro()
    cups_ounces(int(input('Число чашек: ')))

def intro():
    print('''Эта программа конвертирует замеры в чашках в жидкие унции.
     Для 'справки приводим формулу: 1 чашка= 8 жидких унций''')
    print()
def cups_ounces(cups):
    ounces = cups * 8
    print(f'Этo число конвер тируется в {ounces} унции(й).' )

if __name__ == '__main__': cups_to_ounces()