'''for переменная in строковое_значение:
    инструкция
    инструкция
    . . .
'''
name = 'Вася'
for i in name: print(i)
def main():
    count = 0
    my_string = input('Введите значение: ')
    for i in my_string:
        if i == 'Т' or i == 'т': count += 1
    print(f'Бyквa Т появляется {count}раз(а).')

if __name__ == '__main__': main()