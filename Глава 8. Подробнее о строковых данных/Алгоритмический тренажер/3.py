def main():
    mystring = input('Строка: ')
    total = 0
    for numer in mystring:
        if numer.isdigit(): total += 1

    print(total)


main()
