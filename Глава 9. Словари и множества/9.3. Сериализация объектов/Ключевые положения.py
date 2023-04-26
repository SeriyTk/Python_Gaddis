import pickle
def main():
    phonebook = {'Крис' : '555-1111', 'Кэти' : '555-2222', 'Джоанна' : '555-3333'}
    with open('phonebook.dat', 'wb') as output_file:
        pickle.dump(phonebook, output_file)
    if __name__ == '__main__': main()

def main():
    with open('phonebook.dat', 'rb') as input_file:
        file = pickle.load(input_file)
    print(file)
    if __name__ == '__main__': main()

def main():
    again = 'д'
    with open('info.dat', 'wb') as out_file:
        while again.lower() == 'д':
            save_data(out_file)
            again = input('Желаете ввести еще данные? (д/н): ')

    end_of_file = False
    with open('info.dat', 'rb') as in_file:
        while not end_of_file:
            try:
                person = pickle.load(in_file)
                display_data(person)
            except EOFError: end_of_file = True

def save_data(file):
    person = {}
    person['имя'] = input('Имя: ')
    person['возраст'] = input('Возраст: ')
    person['масса'] = float(input('Масса: '))
    pickle.dump(person, file)
def display_data(person):
    print(f'''
Имя: {person['имя']}
Возраст: {person['возраст']}
Масса: {person['масса']}
    ''')
    print()
if __name__ == '__main__': main()
