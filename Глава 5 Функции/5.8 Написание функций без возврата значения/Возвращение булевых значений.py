def is_even(number):
    if number % 2 == 0:
        status = True
    else:
        status = False
    return status


if is_even(int(input('Введите число: '))):
    print('Число четное.')
else:
    print("Число не четное.")


def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300:
        status = True
    else:
        status = False
    return status


model = int(input('Введите номер модели 100,200 или 300: '))
while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input('Введите номер модели 100,200 или 300: '))
