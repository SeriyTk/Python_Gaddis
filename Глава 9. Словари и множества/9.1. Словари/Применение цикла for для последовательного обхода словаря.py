'''for переменная in словарь:
    инструкция
    инструкция
    . . .'''
phonebook = {'Крис':'555-1111', 'Кэти' : '555-2222', 'Джоанна': '555-3333'}
for key in phonebook: print(key)
print()
for key in phonebook: print(key, phonebook[key])