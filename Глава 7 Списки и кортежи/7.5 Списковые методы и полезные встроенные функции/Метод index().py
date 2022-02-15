def get_index_item(par):
    return food.index(par)
food = ['Пицца', 'Бургеры', 'Чипсы']
def index_list():
    try:
        item_index = get_index_item(input('Kaкoe значение следует изменить?: '))
        new_item = input('Введите новое значение: ')
        food[item_index] = new_item
        print('Новый список.')
        print(food)
    except ValueError:
        print('Такого в списке нет.')

index_list()