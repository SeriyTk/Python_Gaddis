def Ingredient_Regulator():
    SUGAR = 1.5
    BUTTER = 1
    FLOUR = 2.75
    BUNS = 48
    s1 = 1.5 / 48
    but1 = 1 / 48
    flo1 = 2.75 / 48
    buns = int(input('Количество булочек: '))
    print(f'''
Для выпечки {buns} булочек нужно:
сахара {s1 * buns}
масла {but1 * buns}
муки {flo1 * buns}
''')

Ingredient_Regulator()