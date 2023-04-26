phonebook = {'Крис':'555-1111',  'Кэти':'555-2222', 'Джоанна':'555-3333'}
print(phonebook)
phonebook['Вася'] = "555-0123"
print(phonebook)
del phonebook['Крис']
print(phonebook)
try:
    del phonebook['Гриша']
except: print('Такого нет.')
if 'Кэти' in phonebook: del phonebook['Кэти']
print(phonebook)