n = int(input('Количество строк: '))
star = int(input('Количество знаков: '))
for i in range(n):
    print('*' * star, end='')
    print()
print('-----------------------------------------')
for i in range(n):
    for j in range(star):
        print('#', end='')
    print()
print('-----------------------------------------')
for i in range(n):
    for j in range(i + 1):
        print('$', end=' ')
    print()

