'''Функция с возвратом значения имеет инструкцию return, которая возвращает значение
в ту часть программы, которая ее вызвала
def имя_функции():
    инструкция
    инструкция
    . . .
    return выражение
'''
def sum(num1, num2):
    return num1 + num2

if __name__ == '__main__': print(sum(2,3))
print()
def total_ages():
    first_age = int(input('Bвeдитe свой возраст: '))
    second_age = int(input("Bвeдитe возраст своего лучшего друга: "))
    total = sum(first_age, second_age)
    print(f'Bмecтe вам {total} лет.')

def sum(num1, num2): return num1 + num2

if __name__ == '__main__': total_ages()
