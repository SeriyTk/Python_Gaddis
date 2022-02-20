string1 = '1200'
if string1.isdigit():
    print(string1, 'содержит только цифры.')
else:
    print(string1, 'содержит символы, отличные от цифр.')

string2 = '12ЗаЬс'
if string2.isdigit():
    print (string2, 'содержит только цифры.')
else:
    print(string2, 'содержит символы, отличные от цифр.')

def stгiпg_test(par):
    if par.isalnum():
        print('Эта строка содержит буквы или цифры.')
    if par.isdigit():
        print('Эта строка содержит только цифры.')
    if par.isalpha():
        print('Эта строка содержит только буквы алфавита.')
    if par.isspace():
        print('Эта строка содержит только пробельные символы.')
    if par.islower():
        print('Bce буквы в строке находятся в нижнем регистре.')
    if par.isupper():
        print('Bce буквы в строке находятся в верхнем регистре.')
        
stгiпg_test(input('Введите строковые значения: '))

