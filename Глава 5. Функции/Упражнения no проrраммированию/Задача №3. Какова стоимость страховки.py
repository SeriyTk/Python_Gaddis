MIN = 0.80
def Insurance_cost():
    price = float(input('Стоимость строения: '))
    print(f'Минимальная страховая сумма {price * MIN}')

if __name__ == '__main__': Insurance_cost()