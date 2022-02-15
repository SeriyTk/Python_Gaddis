СТРОКА = 5
СТОЛБЕЦ = 3
for i in range(СТРОКА):
    print(f'Строка №{i+1}',end=': ')
    for j in range(СТОЛБЕЦ):
        print(j,end=' ')
    print()