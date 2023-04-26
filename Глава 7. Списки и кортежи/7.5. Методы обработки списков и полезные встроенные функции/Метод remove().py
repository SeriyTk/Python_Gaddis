def main():
    food = ['Пицца', 'Бургеры', 'Чипсы']
    print(food)
    item = input('Kaкoe значение следует удалить? ')
    try:
        food.remove(item)
        print(food)
    except ValueError: print('Этo значение в списке не найдено.')

if __name__ == '__main__': main()