def write_numbers():
    with open('../Упражнения по программированию/numbers.txt', 'w') as outfile:
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите  еще одно число: '))
        num3 = int(input('Введите  еще одно число: '))

        outfile.write(f'{num1} \n')
        outfile.write(f'{num2} \n')
        outfile.write(f'{num3} \n')

    print('Данные записаны в numbers . txt')

if __name__ == '__main__': write_numbers()
print()
def read_numbers():
    with open('../Упражнения по программированию/numbers.txt') as infile:
        num1 = infile.readline()
        num2 = infile.readline()
        num3 = infile.readline()

        total = int(num1) + int(num2) + int(num3)
        print('Чиcлa :')
        print(f'{num1} {num2}{num3}' )
        print(f'Иx cyммa : {total}')
if __name__ == '__main__': read_numbers()
