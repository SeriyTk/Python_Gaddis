for col in range(8): print('*', end=' ')
print()
for row in range(8):
    for col in range(6): print('*', end=' ')
    print()

print()

def rectangular_pattern():
    rows = int(input('Строк: '))
    cols = int(input('Столбцов: '))
    for row in range(rows):
        for col in range(cols): print('&', end=' ')
        print()


rectangular_pattern()


