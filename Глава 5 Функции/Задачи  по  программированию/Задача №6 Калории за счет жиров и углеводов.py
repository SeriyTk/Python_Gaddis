def calories(fats, carbohydrates):
    print(f'Калорий от жиров {get_calories_fats(fats)}.')
    print(f'Калорий от углеводов {get_calories_carbohydrates(carbohydrates)}.')


def get_calories_fats(fats):
    return fats * 9


def get_calories_carbohydrates(carbohydrates):
    return carbohydrates * 4

calories(4,  4)
