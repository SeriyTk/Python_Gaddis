class Mammal:
    def __init__(self, species): self.__species = species
    def show_species(self): print(f'Я - {self.__species}')
    def make_sound(self): print('Гpppppp')

class Dog(Mammal):
    def __init__(self): Mammal.__init__(self, 'собака')
    def make_sound(self): print('Гав-гав!')

class Cat(Mammal):
    def __init__(self): Mammal.__init__(self, 'кот')
    def make_sound(self): print('Mяy!')
