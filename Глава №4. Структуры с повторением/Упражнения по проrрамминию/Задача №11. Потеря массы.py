MASS = 1.5
MONTHS = 6
def Mass_loss():
   initial_mass = float(input('Исходная масса: '))
   mass = initial_mass
   print('Месяц \t\tМасса')
   print('--------------------')
   for month in range(MONTHS): mass -= MASS; print(f'{month + 1} \t\t\t\t{mass}')



if __name__ == '__main__': Mass_loss = Mass_loss()
