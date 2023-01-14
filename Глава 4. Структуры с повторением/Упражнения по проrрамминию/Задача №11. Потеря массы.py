def Mass_loss():
    MASS = 1.5
    initial_mass = int(input('Введите исходную массу: '))
    print("Месяц\tМасса")
    for i in range(6): initial_mass -= MASS; print(f'{i + 1}\t\t\t{initial_mass}')

Mass_loss()