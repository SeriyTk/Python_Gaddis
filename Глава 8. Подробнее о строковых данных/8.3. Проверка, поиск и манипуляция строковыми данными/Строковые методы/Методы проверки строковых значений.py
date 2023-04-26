string1 = '1200'
if string1.isdigit(): print(f'{string1} содержит только цифры.')
else: print(f'{string1} содержит символы, отличные от цифр.')
print()
string2 = '12Заbс'
if string2.isdigit(): print(f'{string2} содержит только цифры.')
else: print(f'{string2} содержит символы, отличные от цифр.')
def main():
    user_string = input('Введите строковое значение: ')
    if user_string.isalnum(): print( 'Эта строка содержит буквы или цифры.')
    if user_string.isdigit(): print('Эта строка содержит только цифры.')
    if user_string.isalpha(): print('Эта строка содержит только буквы алфавита.')
    if user_string.isspace(): print('Эта строка содержит только пробельные символы.')
    if user_string.islower(): print('Все буквы в строке находятся в нижнем регистре.')
    if user_string.isupper(): print('Bce буквы в строке находятся в верхнем регистре.')

if __name__ == '__main__': main()