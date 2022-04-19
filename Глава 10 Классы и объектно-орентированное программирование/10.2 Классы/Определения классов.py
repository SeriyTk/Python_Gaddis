import random

# Класс Coin имитирует монету, которую можно подбрасывать

class Coin:
    # создаем атрибуты класса со значением 'Орел'
    sideup = 'Орел'
        # Метод toss генерирует случайное число в диапазоне от 0 до 1.
        # Если это число равно 0, то sideup получает значение 'Орел'.
        # В противном случае sideup получет значение 'Решка'.
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'
        # Метод get_sideup возвращает значение, на которое ссылается sideup
    def get_sideup(self):
        return self.sideup

# Главная функция.
def coin_toss():
    # Создать объект (экземпляр) класса Coin
    my_coin = Coin()
    print(f'Монета лежит вверх {my_coin.get_sideup()}')
    # Подбросить монету.
    print('Подкидываем монету...')
    my_coin.toss()
    print(f'Выпало {my_coin.get_sideup()}')

coin_toss()