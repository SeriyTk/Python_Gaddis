import random as rnd
students =[['Джо', 'Ким'], ['Сэм', 'Сью'], ['Келли', 'Крис']]
print(students)
print(students[0])
print(students[1])
print(students[2])
print()
def main():
    values = [[1, 2,3], [10, 20, 30], [100, 200, 300]]
    for row in values:
        for element in row: print(element)

if __name__ == '__main__': main()
print()

ROWS = 3
COLS = 4
def main():
    values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for r in range(ROWS):
        for c in range(COLS): values[r][c] = rnd.randint(1, 100)
    print(values)

if __name__ == '__main__': main()