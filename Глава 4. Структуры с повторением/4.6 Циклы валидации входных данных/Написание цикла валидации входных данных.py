def retail_with_validation():
    MARK_UP = 2.5
    while True:
        wholesale = input("Bвeдитe оптовую стоимость товара: ")
        if wholesale == '': print('Программа завершена.'); break
        elif float(wholesale) < 0: print('ОШИБКА: стоимость не может быть отрицательной. Bвeдитe правильную оптовую стоимость.')
        else: retail = float(wholesale) * MARK_UP; print(f'Розничная цена:${retail:,.2f}')


retail_with_validation()