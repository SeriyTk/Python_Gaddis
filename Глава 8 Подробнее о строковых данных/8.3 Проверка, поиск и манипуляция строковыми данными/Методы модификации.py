letters = 'ЬЭЮЯ'
print(letters, letters.lower())
letters = 'абвг'
print(letters, letters.upper())

again = 'д'
while again.lower() == 'д':
    print ('Привет')
    print ('Желаете это увидеть еще раз?')
    again = input('д =да, все остальное= нет: ')

again = 'д'
while again.upper() == 'д':
    print ('Привет')
    print ('Желаете это увидеть еще раз?')
    again = input('д =да, все остальное= нет: ')