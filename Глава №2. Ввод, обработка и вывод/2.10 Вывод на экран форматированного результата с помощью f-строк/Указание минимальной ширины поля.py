number = 99
print(f'Чиcлo равняется {number:10}')
print()
number = 12345.6789
print(f'Чиcлo равняется{number:12,.2f}')
print(f'Чиcлo равняется{number:12.2f}')
print()
def columns():
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999

    print(f'{num1:10.2f}{num2:10.2f}')
    print(f'{num3:12.2f}{num4:11.2f}')
    print(f'{num5:12.2f}{num6:10.2f}')

if __name__ == '__main__': columns()
