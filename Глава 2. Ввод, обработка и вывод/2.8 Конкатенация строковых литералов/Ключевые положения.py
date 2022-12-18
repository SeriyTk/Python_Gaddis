"""Конкатенация строковых значенийнец другого."""

message = 'Привет, ' + 'Вася'
print(message)

def concatenation():
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    full_name = first_name + ' ' + last_name
    print(f'Полное имя: {full_name}')

concatenation()