def Calories():
    calories_from_fat = float(input('Граммы жиров: ')) * 9
    calories_from_carbs = float(input('Граммы углеводов: ')) * 4
    print(f'Калорий от жиров {calories_from_fat}')
    print(f'Калорий от углеводов {calories_from_carbs}')

if __name__ == '__main__': Calories()