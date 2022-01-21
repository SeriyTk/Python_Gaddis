def main():
    intro()
    cups_needed = int(input('Количество чашек: '))
    cups_to_uns(cups_needed)


def intro():
    print("Программа конвертирует чашки в унции.")


def cups_to_uns(arg):
    ounces = arg * 8
    print(f'Получилось {ounces} унций.')


main()
