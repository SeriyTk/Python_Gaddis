import cellphone as CP
def main():
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = float(input('Bвeдитe розничную цену: '))

    phone = CP.CellPhone(man, mod, retail)
    print(phone)

if __name__ == '__main__': main()
