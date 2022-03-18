# Сериализация объекта - это процесс преобразования объекта в поток байтов, которые
# могут быть сохранены в файле для последующего извлечения.
# В Python сериализация объекта называется консервацией.
import pickle

def save_data(output_file):
    person = {}
    person['имя'] = input('Имя: ')
    person['Возвраст'] = int(input('Возвраст: '))
    person['Масса'] = float(input('Масса: '))
    pickle.dump(person,output_file)
def pickle_objects():
    with open('info.dat','wb') as output_file:
        while True:
            save_data(output_file)
            again = input('Желаете ввести еще данные?(д / н):')
            if again.lower() != 'д':
                print('Файл сохранен.')
                break

def unpickle_objects():
    with open('info.dat','rb') as input_file:
        end_of_file = False
        while not end_of_file:
            try:
                person = pickle.load(input_file)
                display_data(person)
            except EOFError:
                end_of_file = True

def display_data(person):
    print(f'Имя: {person["имя"]}.')
    print(f'Возвраст: {person["Возвраст"]}.')
    print(f'Масса: {person["Масса"]}.')

unpickle_objects()