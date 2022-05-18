SUGAR = 1.5
OIL = 1
FLOUR = 2.75
TOTAL_BREADS = 48


def Ingredient_Regulator():
    amount_breads = int(input('Сколько булочек хотите приготовить? '))
    print(f'''
Для приготовления {amount_breads} булочек потребуется:
{SUGAR / TOTAL_BREADS * amount_breads:.2f} стакана сахара;
{OIL / TOTAL_BREADS * amount_breads:.2f} стакана масла;
{FLOUR / TOTAL_BREADS * amount_breads:.2f} стакана муки.
''')


Ingredient_Regulator()
