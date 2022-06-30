def main():
    food = ['Пицца', 'Бургеры', 'Чипсы']
    print('Boт значения списка продуктов питания:')
    for i in food: print(i, end=' ')
    print()
    try:
        food.remove(input('Kaкoe значение следует удалить? '))
        print('Вот пересмотренный список:')
        for i in food: print(i, end=' ')
    except ValueError: print('Этo значение в списке не найдено.')



main()
