def main():
    food = ['Пицца', 'Бургеры', 'Чипсы']
    print(food)
    item = input('Kaкoe значение следует изменить ? ')
    try:
        item_index = food.index(item)
        new_item = input('Введите новое значение: ')
        food[item_index] = new_item
        print('Вот пересмотренный список: ')
        print(food)
    except ValueError: print('Этo значение в списке не найдено.')


if __name__ == '__main__': main()