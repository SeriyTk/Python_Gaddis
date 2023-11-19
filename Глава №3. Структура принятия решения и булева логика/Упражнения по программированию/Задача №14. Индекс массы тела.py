def Body_mass_index():
    mass = float(input('Масса тела: '))
    height = float(input('Рост: '))
    mass_index = mass / height ** 2
    if mass_index < 18.5: print(f'Индекс массы тела = {mass_index:.2f}. Недостаточно.')
    elif mass_index > 25: print(f'Индекс массы тела = {mass_index:.2f}. Избыточно.')
    else: print(f'Индекс массы тела = {mass_index:.2f}. Оптимально.')



if __name__ == '__main__': Body_mass_index = Body_mass_index()
