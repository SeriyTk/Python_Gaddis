def Gasoline_consumption():
    gas_cons = int(input('Расход бензина: '))
    kilo = int(input('Пройденые километры: '))
    total_gas = kilo / gas_cons
    print(f'{total_gas:.2f}')

Gasoline_consumption()