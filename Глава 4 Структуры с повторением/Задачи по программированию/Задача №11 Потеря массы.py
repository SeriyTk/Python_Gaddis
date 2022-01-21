def Mass_loss(initial_mass, months):
    print('Месяц\tМасса')
    for month in range(months):
        mass = initial_mass - 1.5 * (month + 1)
        print(f'{month + 1}  \t\t  {mass}')
        
        
Mass_loss(85, 6)
