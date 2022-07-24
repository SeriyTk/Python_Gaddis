import pickle

def save_data(output_file):
    person = {}
    person['Имя'] = input('Имя: ')
    person['Возраст'] = int(input('Возраст: '))
    person['Масса'] = float(input('Macca: '))

    pickle.dump(person, output_file)

def display_data(input_file):
    person = pickle.load(input_file)
    print('Имя:', person['Имя'])
    print('Возраст:', person['Возраст'])
    print('Масса: ', person['Масса'])
    print()
