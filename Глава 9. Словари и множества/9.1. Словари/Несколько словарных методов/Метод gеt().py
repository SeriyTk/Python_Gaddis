phonebook = { 'Крис': '555-1111', 'Кэти': '555-2222'}
value = phonebook.get('Вася', "Запись не найдена")
print(value)
print()
value = phonebook.get('Крис', "Запись не найдена")
print(value)