def main():
    while is_invalid(int(input('Номер модели: '))):
        print('Допустимыми номерами моделей являются 100, 200 и 300.')

def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300: status = True
    else: status = False
    return status

main()
