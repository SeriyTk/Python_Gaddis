def Phone_number_translator():
    enter = input('Введите номер телефона: ')
    for i in enter:
        if i == 'A' or i == 'B' or i == 'C':
            i = i.replace(i, '2')
        if i == 'D' or i == 'E' or i == 'F':
            i = i.replace(i, '3')
        if i == 'G' or i == 'H' or i == 'I':
            i = i.replace(i, '4')
        if i == 'J' or i == 'K' or i == 'L':
            i = i.replace(i, '5')
        if i == 'M' or i == 'N' or i == 'O':
            i = i.replace(i, '6')
        if i == 'P' or i == 'Q' or i == 'R' or i == 'S':
            i = i.replace(i, '7')
        if i == 'T' or i == 'U' or i == 'V':
            i = i.replace(i, '8')
        if i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
            i = i.replace(i, '9')
        print(i, end='')


Phone_number_translator()
