# Двумерный список - это список, который в качестве своих элементов содержит другие списки.
import random as rnd
students =[['Джо', 'Ким'], ['Сэм','Сью'], ['Келли', 'Крис']]
print(students)
print(students[0])
print(students[1])
print(students[2])
print()
ROWS = 3
COLS = 4
def random_numbers():
    values = [] # пустой список
    for r in range(ROWS):  # количество строк
        values.append([])   # создаем пустую строку
        for c in range(COLS):   # количество элементов в каждой строке
            values[r].append(rnd.randint(1,100))   # добавляем очередной элемент в строку

    return values

print(random_numbers())