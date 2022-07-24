phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
name = input('Введите имя: ')
if name in phonebook: print(phonebook[name])
else: print(f'{name} не найдено.')
