def retail_no_validation():
    MARK_UP = 2.5
    while True:
        wholesale = float(input('Введите оптовую стоимость товара: '))
        if wholesale < 0:
            print('Ошибка! Стоимость товара не может быть отрицательной.')

        else:
            retail = wholesale * MARK_UP
            print(f'Розничная цена товара ${retail:.2f}.')
            another = input('Есть еще один товар? Введите - д: ')
            if another != 'д':
                print('Программа завершена.')
                break


retail_no_validation()
