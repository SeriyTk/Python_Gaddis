TIPS = 0.18
SALES_TAX = 0.07
def Total_amount():
    cost_of_food = float(input('Введите стоимость еды: '))
    tips = cost_of_food * TIPS
    sales = cost_of_food * SALES_TAX
    total = cost_of_food + tips + sales
    print(f'''
Стоимость еды - {cost_of_food}
чаевые - {tips:.2f}
налог с продаж - {sales:.2f}
итоговая сумма - {total:.2f}
''')


if __name__ == '__main__': Total_amount = Total_amount()
