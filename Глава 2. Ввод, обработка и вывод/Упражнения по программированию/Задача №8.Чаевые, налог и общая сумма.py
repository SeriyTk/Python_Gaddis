def Total_Amount():
    TIPS = 0.18
    SALES_TAX = 0.07
    food_cost = float(input('Стоимость еды: '))
    result = food_cost + (food_cost -TIPS) + (food_cost * SALES_TAX)
    print(f'{result:,.2f}')

Total_Amount()