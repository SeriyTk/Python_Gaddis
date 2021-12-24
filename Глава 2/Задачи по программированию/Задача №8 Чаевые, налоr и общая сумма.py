def food_cost():
    food = float(input('Введите стоимость еды: '))
    gratuity = food * (18 / 100)
    sales_tax = food * (7/100)
    total_sum = food + gratuity + sales_tax
    print(f'''
Стоимость еды {food},
чаевые {gratuity},
налог с продаж {sales_tax},
общая сумма {total_sum}.
''')

food_cost()
