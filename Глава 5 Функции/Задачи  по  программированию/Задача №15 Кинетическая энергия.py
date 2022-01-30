def Kinetic_energy(m, v):
    return 1 / 2 * m * v

mass = int(input('Масса тела: '))
speed = int(input('Скорость тела: '))


print(Kinetic_energy(mass, speed))