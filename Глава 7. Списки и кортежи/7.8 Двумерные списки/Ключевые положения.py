import random

'''
Двумерный список -
 это список, который в качестве своих элементов содержит другие списки.
'''
students =[['Джо', 'Ким'], ['Сэм', 'Сью'], ['Келли', 'Крис']]
print(students)
print(students[0])
print(students[1])
print(students[2])
print()

ROWS = 3
COLS = 4
def main():
    '''
    values = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)
    '''
    values = [[random.randint(1, 100) for c in range(COLS)] for r in range(ROWS)]
    print(values)

main()