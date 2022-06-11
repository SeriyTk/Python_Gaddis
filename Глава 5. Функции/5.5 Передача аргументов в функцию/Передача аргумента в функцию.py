def main():
    intro()
    cups_needed = int(input('Количество чашек: '))
    cups_to_ounces(cups_needed)


def intro():
    print('Этa программа конвертирует замеры в чашках в жидкие унции.')
    print('Дпя справки приводим формулу: 1 чашка = 8 жидких унций')
    print()

def cups_to_ounces(par): print(f'Это конвертируется в {par * 8} унции.')

main()
