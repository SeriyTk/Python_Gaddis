letters = 'ЬЭЮЯ'
print(letters, letters.lower())
print()
letters = 'абвг'
print(letters, letters.upper())
print()
again = 'д'
while again.upper() == 'Д':
    print('Привет')
    print('Желаете это увидеть еще раз?')
    again = input('д = да, все остальное = нет: ')