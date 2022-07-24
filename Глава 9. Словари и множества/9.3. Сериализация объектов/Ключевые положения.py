import pickle_objects as p_o

'''
Сериализация объекта - это процесс преобразования объекта в поток байтов, которые
могут быть сохранены в файле для последующего извлечения. В Python сериализация
объекта называется консервацией.
import pickle
phonebook = {'Крис': '555-1111', 'Кэти' : '555-2222', 'Джоанна' : '555-3333'}
with open('phonebook.dat', 'wb') as output_file: pickle.dump(phonebook, output_file)
with open('phonebook.dat', 'rb') as input_file: print(pickle.load(input_file))
'''
def main():
    with open('info.dat', 'wb') as output_file:
        while True:
            again = input('Желаете ввести еще данные?(д): ')
            if again == '': print('Данные сохранены.'); break
            elif again.lower() == 'д': p_o.save_data(output_file)


    with open('info.dat', 'rb') as input_file:
        end_of_file = False
        while not end_of_file:
            try: p_o.display_data(input_file)
            except EOFError: end_of_file = True



main()