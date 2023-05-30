import pickle, cellphone as cpn
FILENAME = 'cellphones.dat'
def main():
    with open(FILENAME, 'wb') as out_file:
        while True:
            enter = input('Введете элемент данных? (д/н): ')
            if enter.lower() == 'д':
                man = input('Введите производителя: ')
                mod = input('Введите номер модели: ')
                retail = float(input('Bвeдитe розничную цену: '))
                phone = cpn.CellPhone(man, mod, retail)
                pickle.dump(phone, out_file)
            elif enter.lower() == 'н': print(f'Дaнныe записаны в {FILENAME}'); break

    if __name__ == '__main__': main()
def main():
    end_file = False
    with open(FILENAME, 'rb') as in_file:
        while not end_file:
            try:
                phone = pickle.load(in_file)
                print(phone)
            except EOFError: end_file = True
if __name__ == '__main__': main()
