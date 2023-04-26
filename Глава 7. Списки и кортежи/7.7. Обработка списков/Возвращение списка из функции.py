def main():
    numbers = get_values()
    print('Чиcлa в списке: ')
    print(numbers)

def get_values():
    values = []
    while True:
        again = input('Желаете добавить число д = да, все остальное = нет: ')
        if again == 'д':
            num = int(input('Введите число: '))
            values.append(num)
        else: return values; break

if __name__ == '__main__': main()