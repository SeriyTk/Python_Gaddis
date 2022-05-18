def future_value():
    future_value = float(input('Будущее значение: '))
    rate = float(input('Годовая процентная ставка: '))
    years = int(input('Количество лет: '))
    present_value = future_value / (1.0 + rate) ** years
    print(f'Нужно будет внести {present_value:,.2f}')

future_value()
