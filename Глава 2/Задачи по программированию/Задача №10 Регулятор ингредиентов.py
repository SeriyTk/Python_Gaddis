def ingredient_regulator():
    SUGAR = 1.5
    BUTTER = 1
    FLOUR = 2.75
    BUNS = 48
    number_buns = int(input('Сколько булочек хотите приготовить? '))
    print(f'''
    Для приготовления {number_buns} булочек необходимо:
    {(SUGAR / BUNS) * number_buns} стакана сахара,
    {(BUTTER / BUNS) * number_buns} стакана масла,
   {(FLOUR / BUNS) * number_buns} стакана муки.
''')


ingredient_regulator()
