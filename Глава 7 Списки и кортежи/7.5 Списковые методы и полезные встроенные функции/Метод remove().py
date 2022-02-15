def remove_item():
    food = ['Пицца', 'Бургеры', 'Чипсы']
    print('Boт значения списка продуктов питания:')
    print(food)
    item = input('Что следует удалить? ')
    try:
        food.remove(item)
        print('Новый список.')
        print(food)
    except ValueError:
        print('Такого в списке нет.')


remove_item()