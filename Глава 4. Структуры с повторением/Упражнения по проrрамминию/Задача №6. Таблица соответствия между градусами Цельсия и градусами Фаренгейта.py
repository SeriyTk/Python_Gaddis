def Celsius_Fahrenheit():
    END = 20
    print('Цельсий\tФаренгейт')
    for i in range(END + 1): print(f'{i}  \t\t\t  {(9 / 5 * i + 32):.1f}')

Celsius_Fahrenheit()