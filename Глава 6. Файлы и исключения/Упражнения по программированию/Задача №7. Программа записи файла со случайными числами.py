import random as r
def main():
    rand_num = int(input('Количество случайных чисел: '))
    with open('rand_numbers.txt', 'w') as write_file:
        for i in range(rand_num): write_file.write(f'{str(r.randint(1, 500))}\n')
    print('Запись создана.')

if __name__ == '__main__': main()