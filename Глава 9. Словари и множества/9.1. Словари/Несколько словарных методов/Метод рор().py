phonebook = { 'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна':' 555-3333'}
phone_num = phonebook.pop('Крис', "Запись не найдена.")
print(phone_num)
print(phonebook)