def main():
    tel_num = input('Введите номер телефона: ')
    for i in tel_num:
        if i == 'A' or i == 'B' or i == 'C': print(i.replace(i, '2'),end='')
        elif i == 'D' or i == 'E' or i == 'F': print(i.replace(i, '3'), end='')
        elif i == 'G' or i == 'H' or i == 'I': print(i.replace(i, '4'), end='')
        elif i == 'J' or i == 'K' or i == 'L': print(i.replace(i, '5'), end='')
        elif i == 'M' or i == 'N' or i == 'O': print(i.replace(i, '6'), end='')
        elif i == 'P' or i == 'Q' or i == 'R' or i == 'S': print(i.replace(i, '7'), end='')
        elif i == 'T' or i == 'U' or i == 'V': print(i.replace(i, '8'), end='')
        elif i == 'W' or i == 'X' or i == 'Y' or 'Z' == i: print(i.replace(i, '9'), end='')
        else: print(i, end='')



main()
