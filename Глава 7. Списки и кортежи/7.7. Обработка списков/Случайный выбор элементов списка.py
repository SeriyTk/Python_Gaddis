import random as r
names = [ 'Дженни', 'Келли', 'Хлоя', 'Обои']
winner = r.choice(names)
print(winner)
print()
numbers = [i for i in range(1, 11)]
print(numbers)
selected = r.choices(numbers, k = 3)
print(selected)