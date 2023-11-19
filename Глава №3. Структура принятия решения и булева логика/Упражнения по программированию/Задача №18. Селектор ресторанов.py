def Restaurant_selector():
    vegetarian = input('Будет ли на ужине вегетарианец? ')
    vegan = input('Будет ли на ужине веганец? ')
    gluten_free = input('Будет ли на ужине приверженец безглютеновой диеты? ')
    print()
    print('Вот ваши варианты ресторанов:')
    print()

    if vegetarian.lower() == 'да':
        print()
        print('Центральная пиццерия')
        print('Кафе за углом')
        print('Кухня шеф-повара')

    if vegan.lower() == 'да':
        print()
        print('Кафе за углом')
        print('Кухня шеф-повара')

    if gluten_free.lower() == 'да':
        print()
        print('Центральная пиццерия')
        print('Кафе за углом')
        print('Кухня шеф-повара')

    else: print("Изысканные гамбургеры от Джо")


if __name__ == '__main__': Restaurant_selector = Restaurant_selector()
