SQUARE = 10
OIL = 5
TIME = 8
PRICE = 2000


def main():
    square = int(input('Площадь поверхности: '))
    price_oil = float(input('Цена краски: '))
    print(f'''
Количество требующихся емкостей краски: {amount_oil(square)};
количество требующихся рабочих часов: {amount_times(square)};
стоимость краски: {amount_oil(square) * price_oil};
стоимость работы: {amount_times(square) * PRICE:,.2f};
общая стоимость малярных работ: {amount_oil(square) * price_oil + amount_times(square) * PRICE:,.2f}
''')

def amount_oil(square):
    if (square % SQUARE) == 0: return (square // SQUARE)
    else: return (square // SQUARE + 1)

def amount_times(square):
    times = square / SQUARE * TIME
    return times




main()
