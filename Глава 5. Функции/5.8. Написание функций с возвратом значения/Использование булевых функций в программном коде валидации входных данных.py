model = int(input('Bвeдитe номер модели: '))
while model != 100 and model != 200 and model != 300:
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input('Bвeдитe допустимый номер модели: '))



def is_invalid(model):
    if model != 100 and model != 200 and model != 300: status = False
    else: status = True
    return status

if __name__ == '__main__': print(is_invalid(model))
