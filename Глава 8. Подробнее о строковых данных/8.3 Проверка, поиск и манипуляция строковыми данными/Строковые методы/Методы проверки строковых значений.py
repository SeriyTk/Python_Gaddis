string1 = '1200'
if string1.isdigit(): print(string1, 'содержит только цифры.')
else: print(string1, 'содержит символы отличные от цифр.')
string2 = '123abc'
if string2.isdigit(): print(string2, 'содержит только цифры.')
else: print(string2, 'содержит символы отличные от цифр.')

def main():
    user_string = input('Введите строку: ')
    print('Boт, что обнаружено в отношении введенного значения:')
    if user_string.isalnum(): print ('Эта строка содержит буквы или цифры.')
    if user_string.isdigit(): print ('Эта строка содержит только цифры.')
    if user_string.isalpha(): print ('Эта строка содержит только буквы алфавита.')
    if user_string.isspace(): print ('Эта строка содержит только пробельные символы.')
    if user_string.islower(): print('Bce буквы в строке находятся в нижнем регистре.')
    if user_string.isupper(): print('Bce буквы в строке находятся в верхнем регистре.')

main()