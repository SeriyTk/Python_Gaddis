numbers = [1, 2, 3,4]
squares = {}
for i in numbers: squares[i] = i ** 2
print(squares)
print()
squares = {i: i ** 2 for i in numbers}
print(squares)
print()
phonebook = { 'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
phonebook_copy = {k : v for k, v in phonebook.items()}
print(phonebook_copy)