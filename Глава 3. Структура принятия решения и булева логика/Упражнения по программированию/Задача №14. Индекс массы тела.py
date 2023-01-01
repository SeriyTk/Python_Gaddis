def Body_mass_index():
    mass = float(input('Введите массу тела: '))
    growth = float(input("Введите рост в метрах: "))
    body_mass_index = mass / growth ** 2
    if body_mass_index < 18.5: print('Ниже нормы.')
    elif body_mass_index > 25: print('Больше нормы.')
    else: print('Норма.')


Body_mass_index()