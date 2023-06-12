import vehicles
def main():
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)
    print(f'{used_car}Колличество дверей: {used_car.get_doors()}')

    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)
    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('===========================')
    print('Данный легковой автомобиль имеется на складе.')
    print(f'{car}Колличество дверей: {car.get_doors()}')

    print('Данный пикап имеется на складе.')
    print(f'{truck}Tип привода: {truck.get_drive_type()}')

    print('Данный джип имеется на складе.')
    print(f'{suv}Пассажирская вместимость: {suv.get_pass_cap()}')

if __name__ == '__main__': main()
