def Gasoline_consumption():
    kilometers = float(input('Число пройденных километров: '))
    liters = float(input('Расход бензина в литрах: '))
    consumption = liters / kilometers * 100
    print(f"Расход бензина автомобилем составляет {consumption:.2f} литров на 100 километров.")

if __name__ == '__main__': Gasoline_consumption = Gasoline_consumption()
