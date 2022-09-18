import pet

def main():
    name = input('Кличка животного: ')
    animal_type = input('Тип живонтного: ')
    age = input('Возрасть животного: ')
    animal = pet.Pet(name, animal_type, age)
    print('----------------------------------------------')
    print(f'''
Кличка: {animal.get_name()}
Тип: {animal.get_type()}
Возраст: {animal.get_age()}
''')

if __name__ == '__main__': main()
