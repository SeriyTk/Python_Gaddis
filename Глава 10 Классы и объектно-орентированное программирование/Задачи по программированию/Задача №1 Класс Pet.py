class Pet:
    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.___age = age

    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.___age

    def __str__(self):
        return (f'''
Имя животного: {self.__name}
Тип животного: {self.__animal_type}
Возвраст животного: {self.___age}
''')
    print()

pet1 = Pet(input('Имя: '), input('Тип: '), input("Возвраст: "))
pet2 = Pet(input('Имя: '), input('Тип: '), input("Возвраст: "))
print(pet1)
print(pet2)

