def Gasoline_consumption():
    GASOLINE = 0.04
    dist = int(input('Сколько проехала машина: '))
    consumption = dist * GASOLINE
    print(f'Расход бензина составит {consumption} литра.')

Gasoline_consumption()