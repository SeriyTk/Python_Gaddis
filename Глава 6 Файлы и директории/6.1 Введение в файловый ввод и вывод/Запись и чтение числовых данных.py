def write_numbers():
    with open(r'J:\Мой диск\GD\numbers.txt', 'w') as n:
        while True:
            print(int(input('Введите число: ')), file=n)
            answer = input('Хотите продолжить введите - д, а иначе - любое значение: ')
            if answer != 'д':
                print('Программа завершена.')
                break


def read_numbers():
    with open(r'J:\Мой диск\GD\numbers.txt') as n:
        line = n.readline()
        total = 0
        while line != '':
            total += int(line)
            print(int(line))
            line = n.readline()
        print(total)

read_numbers()

