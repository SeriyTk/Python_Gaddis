SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
BUNS = 48
def Ingredient_Regulator():
    quantity = int(input('Сколько булочек хотите испечь? '))
    sugar = SUGAR / BUNS
    butter = BUTTER / BUNS
    flour = FLOUR / BUNS
    print(f'''
Чтобы испечь {quantity} булочек нужно:
сахара {quantity * sugar:.1f}
масла {quantity * butter:.1f}
муки {quantity * flour:.2f}
''')


if __name__ == '__main__': Ingredient_Regulator = Ingredient_Regulator()
