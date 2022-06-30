def main():
    food = ['Пицца', 'Бургеры', 'Чипсы']
    print('Список продуктов:')
    for i in food: print(i, end=' ')
    try:
        index_item = food.index(input('Что изменить? '))
        food[index_item] = input('Новое значение: ')
        print('Обновленный список:')
        for i in food: print(i, end=' ')
    except ValueError: print('Этo значение в списке не найдено.')

main()
