for col in range(6): print ( '*' , end=' ' )
print()
def rectangular_pattern():
    rows = int(input('Cкoлькo строк? '))
    cols = int(input('Cкoлькo столбцов? '))
    for r in range(rows):
        for с in range(cols):
            print ( '*', end=' ' )
        print()

rectangular_pattern()
print()
def triangle_pattern():
    BASE_SIZE= 8
    for r in range(BASE_SIZE):
        for c in range(r + 1):print('*', end='')
        print()

triangle_pattern()
print()
def stair_step_pattern():
    NUM_STEP = 6
    for r in range(NUM_STEP):
        for c in range(r): print(' ', end='')
        print('#')


stair_step_pattern()
